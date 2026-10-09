"""Validate identity, references, local visual evidence and synthesis citations."""
import csv, re, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/b2b_banking'
T={p.stem:list(csv.DictReader(p.open())) for p in DATA.glob('*.csv')}
spec={'sources':('source_id','BB-S'), 'claims':('claim_id','BB-C'),
      'metrics':('metric_observation_id','BB-M'), 'features':('feature_id','BB-F'),
      'screens':('screen_id','BB-V'), 'journey_steps':('journey_step_id','BB-J'),
      'contradictions':('contradiction_id','BB-X'), 'opportunities':('opportunity_id','BB-O')}
ids={};errors=[]
for name,(field,prefix) in spec.items():
    values=[r[field] for r in T[name]]
    if len(values)!=len(set(values)):errors.append(name+': duplicate IDs')
    ids[prefix]=set(values)
defs=[r['metric_id'] for r in T['metric_definitions']]
if len(defs)!=len(set(defs)):errors.append('Duplicate metric definitions')
for name,rows in T.items():
    for row in rows:
        for key,value in row.items():
            if key.endswith('_ids') or key=='refs':
                for code in re.findall(r'BB-[SCMFVJXO]\d{2,4}',value):
                    if code not in ids[code[:4]]:errors.append(f'{name}/{key}: {code}')
        if name=='metrics' and row['metric_id'] not in defs:errors.append('Metric without definition')
        if name=='screens' and row['local_path'] and not (ROOT/row['local_path']).is_file():errors.append('Missing visual '+row['local_path'])
for p in list((ROOT/'docs/b2b_banking').glob('*.md'))+list((ROOT/'companies/b2b_banking').glob('*/*.md')):
    if p.name=='evidence_protocol.md':
        continue  # Schema examples are intentionally not observations.
    for code in re.findall(r'BB-[SCMFVJXO]\d{2,4}',p.read_text()):
        if code not in ids[code[:4]]:errors.append(str(p.relative_to(ROOT))+': '+code)
assert not errors, '\n'.join(errors)
assert len(T['shortlist'])==14 and all(r['profile_status']=='done' for r in T['shortlist'])
print(json.dumps({'result':'PASS','tables':{k:len(v) for k,v in T.items()},'checks':['unique IDs','reference integrity','metric definitions','local images','document citations','14 accepted profiles']},ensure_ascii=False))
