"""Structural checks and contact sheets; visual review remains mandatory."""
import json,re,hashlib,subprocess,os,csv,sys
from pathlib import Path
import pdfplumber
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'reports/b2b_banking/b2b_banking_external_growth_ru.pdf'
QA=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'.tmp/b2b_report_qa';QA.mkdir(parents=True,exist_ok=True)
reader=PdfReader(str(PDF));bad=[];sparse=[];texts=[];annotations=0
with pdfplumber.open(PDF) as pdf:
 for n,p in enumerate(pdf.pages,1):
  txt=p.extract_text() or '';texts.append(txt)
  for ch in p.chars:
   if ch['x0']<-0.1 or ch['x1']>p.width+.1 or ch['top']<-0.1 or ch['bottom']>p.height+.1:bad.append((n,ch['text']))
  bodychars=[c for c in p.chars if 42<c['top']<790]
  overflow=[c for c in bodychars if c['x0']<43 or c['x1']>p.width-43]
  if overflow:bad.append((n,'text outside horizontal body margins'))
  if len(txt.split())<90:sparse.append(n)
assert not bad,bad
assert all((QA/f'page-{i:02d}.png').exists() for i in range(1,len(reader.pages)+1))
pdf_urls=set()
for page in reader.pages:
 for a in page.get('/Annots',[]):
  a=a.get_object()
  if a.get('/Subtype')=='/Link':
   annotations+=1
   act=a.get('/A')
   if act and act.get('/S')=='/URI':
    uri=str(act.get('/URI'));assert uri.startswith(('https://','http://'));pdf_urls.add(uri)
sources={x['source_id']:x['url'] for x in csv.DictReader((ROOT/'data/b2b_banking/sources.csv').open())}
md=(ROOT/'reports/b2b_banking/report_ru.md').read_text()
bib=re.findall(r'<!-- SOURCE (BB-S[0-9]{4}) -->',md)
assert len(bib)==216
for sid in bib:assert sources[sid] in pdf_urls,(sid,'URL missing or altered')
alltext='\n'.join(texts)
assert '10.10.2026' not in alltext
assert '5b584f5adf20b2c421e404f4e1e92486eee2cc41' in alltext
assert 'Внешний B2B-бизнес' in alltext and 'Управленческий ответ' in alltext
assert '\ufffd' not in alltext
for name in ['Qonto','Allica','Tide','Mercury','Ramp','Square','Toast','iwoca','YouLend','Stone','RazorpayX','Airwallex','Wise','Funding Circle']:assert name in alltext
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
imgs=sorted(QA.glob('page-*.png'))[:len(reader.pages)]
contacts=[]
for batch in range(0,len(imgs),4):
 sheet=Image.new('RGB',(1680,2420),'#dde5e9');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(imgs[batch:batch+4]):
  try:im=Image.open(p).convert('RGB')
  except OSError:
   number=str(int(p.stem.split('-')[1]))
   subprocess.run(['pdftoppm','-f',number,'-l',number,'-r','100','-png',str(PDF),str(QA/'page')],check=True)
   im=Image.open(p).convert('RGB')
  im.thumbnail((806,1140))
  x=20+(j%2)*830;y=40+(j//2)*1200
  sheet.paste(im,(x,y));d.text((x,y-27),'Страница '+str(batch+j+1),font=font,fill='#142e45')
 out=QA/f'contact-{batch//4+1:02d}.jpg';sheet.save(out,quality=92);contacts.append(str(out))
result={'structural_result':'PASS','pages':len(reader.pages),'links':annotations,'bibliography_urls_verified':len(bib),'out_of_bounds':bad,'sparse_pages_for_visual_review':sparse,'contact_sheets':contacts,'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'visual_review':'pending'}
(QA/'structural_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
os.sync()
print(json.dumps({k:v for k,v in result.items() if k!='contact_sheets'},ensure_ascii=False))
