# Market Source Inventory — First Geography Set

Version date: 2026-10-02.

## Purpose

This inventory tells us **where to pull each market metric before starting country landscape collection**.

Priority:
- P1 = primary recurring source, use first;
- P2 = complementary primary source;
- P3 = supporting/context source.

The inventory is not exhaustive. It is the minimum source map needed to start Wave 2 without re-discovering sources country by country.

---

# United States

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | Small Business Credit Survey | Federal Reserve Banks | financing need, application, approval, lender choice, satisfaction, debt | Annual | Convenience sample; weighted but not probability sample |
| P1 | Small Business Lending Survey / FR 2028D | Federal Reserve | loan terms, standards, demand, application volume/quality | Quarterly | Bank survey, supply-side |
| P1 | Call Reports / bank regulatory filings | FFIEC / regulators | bank loan books, NPL, charge-offs, capital | Quarterly | SME-specific cuts limited depending on schedule |
| P2 | Small Business Lending Survey | FDIC | underwriting, automation, approval authority/time, product mix | Periodic | Survey waves, not continuous |
| P2 | SBA size standards / program data | SBA | program lending, borrower definition | Program-specific | Definition varies by NAICS |

Links:
- https://www.fedsmallbusiness.org/reports/survey
- https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_2028D
- https://www.fdic.gov/publications/2024-report-small-business-lending-survey
- https://www.sba.gov/document/support-table-size-standards

### Coverage status
Demand: **strong**  
Supply: **strong**  
Risk: **strong at bank level; SME normalization required**  
Pricing: **good**  
Journey: **company-level research required**

---

# United Kingdom

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | Small Business Finance Markets | British Business Bank | gross lending, provider structure, product use, demand, access | Annual | “Smaller business” definition must be retained |
| P1 | Money and Credit | Bank of England | SME net borrowing, loan growth, effective interest rates | Monthly | Bank lending only; net flows differ from gross originations |
| P1 | Business Finance Survey | British Business Bank / Ipsos | financing need, use, application experience | Annual | Survey population/weighting |
| P2 | Business Population Estimates | UK Government | company counts by employment size | Annual | Employment definition differs from other SME rules |
| P2 | Procurement SME guidance | UK Government | definition | As updated | Not a lending-specific population |

Links:
- https://www.british-business-bank.co.uk/about/research-and-publications/small-business-finance-markets-report-2026
- https://www.bankofengland.co.uk/statistics/money-and-credit
- https://www.gov.uk/government/statistics/business-population-estimates-2025/business-population-estimates-for-the-uk-and-regions-2025-statistical-release

### Coverage status
Demand: **strong**  
Supply: **strong**  
Risk: **company/regulatory disclosures needed**  
Pricing: **strong**  
Journey: **strong candidate for screen-based lender research**

---

# Brazil

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | SGS 27701 — credit balance by company size | Banco Central do Brasil | SME/MPME loan stock | Monthly | BCB credit-size definition |
| P1 | SGS 27703 — delinquency by company size | Banco Central do Brasil | 90+ DPD delinquency | Monthly | 90+ DPD is not automatically regulatory default |
| P1 | SCR.data | Banco Central do Brasil | active portfolio, delinquency, problematic assets by product/industry/size/geography | Monthly | Can differ from other BCB publications due to source granularity |
| P1 | Credit concessions by company size (e.g. SGS 26200 family) | Banco Central do Brasil | new lending / concessions | Quarterly / series-specific | Series differ by borrower size and product |
| P2 | Borrower-count series by company size | Banco Central do Brasil | number of business borrowers | Quarterly | Definition tied to SCR size |
| P2 | Open Finance Brasil | Open Finance governance / BCB ecosystem | participants and data-sharing infrastructure | Current | Infrastructure evidence, not lending-volume data |
| P2 | Receita / CGSN rules | Receita Federal | legal/tax size definitions | As updated | ME/EPP definition differs from BCB medium definition |

Links:
- https://dadosabertos.bcb.gov.br/dataset/27701-saldo-das-operacoes-de-credito-por-porte-da-empresa---micro-pequena-e-media-mpme
- https://dadosabertos.bcb.gov.br/en/dataset/27703-inadimplencia-da-carteira-de-credito-por-porte-da-empresa-micro-pequena-e-media-mpme
- https://www.bcb.gov.br/estabilidadefinanceira/scrdata
- https://openfinancebrasil.org.br/quem-participa/

### Coverage status
Demand: **medium; supplement with surveys/industry sources**  
Supply: **very strong**  
Risk: **very strong**  
Pricing: **strong BCB series, source mapping required**  
Journey: **high-priority company research**

---

# Germany

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | KfW SME Panel | KfW Research | financing structure, credit negotiations, investment, profitability, firm structure | Annual | Population up to €500m turnover |
| P1 | KfW-ifo Credit Constraint | KfW / ifo | credit access / lender reluctance | Quarterly | Uses a different SME definition from KfW Panel |
| P1 | SAFE | ECB | financing need, applications, outcomes, rates/conditions, collateral | Quarterly / half-yearly series | EU/SAFE firm-size population |
| P2 | Bundesbank / ECB banking statistics | Bundesbank / ECB | corporate loan stocks/rates/new business | Monthly | SME split may require loan-size proxies or SAFE/KfW |
| P2 | EU SME definition | European Commission | policy definition | As updated | Narrower than KfW Mittelstand |

Links:
- https://www.kfw.de/About-KfW/KfW-Research/KfW-Mittelstandspanel.html
- https://www.kfw.de/About-KfW/Service/Download-Center/Konzernthemen/Research/Indikatoren/KfW-ifo-Kredith%C3%BCrde/
- https://www.ecb.europa.eu/stats/ecb_surveys/safe/html/index.en.html
- https://data.ecb.europa.eu/data/datasets/SAFE

### Coverage status
Demand: **very strong**  
Supply: **strong**  
Risk: **company-level disclosures plus banking stats**  
Pricing: **strong**  
Journey: **requires lender-by-lender research**

---

# India

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | RBI Annual Report — Bank Credit to MSMEs | Reserve Bank of India | accounts and outstanding by micro/small/medium | Annual | Classification break from Apr 2025 |
| P1 | Sectoral Deployment of Bank Credit | RBI | credit growth / outstanding by sectors incl. MSE/medium | Monthly | Select banks cover most non-food credit |
| P1 | Annual BSR-1 Credit by Scheduled Commercial Banks | RBI | detailed bank-credit distribution | Annual | Classification/source-table mapping required |
| P1 | Priority Sector Lending returns | RBI | MSME exposure and policy treatment | Annual/periodic | Policy classification tied to Udyam |
| P2 | Udyam / Ministry of MSME | Government of India | registered MSME counts and size distribution | Current / periodic | Registered/formal population |
| P2 | Account Aggregator Framework | Department of Financial Services / RBI ecosystem | digital-data infrastructure | Current | Infrastructure, not direct credit metric |

Links:
- https://www.rbi.org.in/scripts/AnnualReportPublications.aspx
- https://www.rbi.org.in/Scripts/Pr_DataRelease.aspx?DateFilter=Year&SectionID=376
- https://www.financialservices.gov.in/account-aggregator-framework
- https://www.msme.gov.in/

### Coverage status
Demand: **medium**  
Supply: **very strong**  
Risk: **medium/strong depending source granularity**  
Pricing: **medium**  
Journey: **high-value for digital/data-underwriting research**

---

# Netherlands

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | SME corporate lending statistics | De Nederlandsche Bank | SME loan stock/share, interest rates | Monthly/series-specific | Newer SME-specific presentation; methodology must be retained |
| P1 | Financieringsmonitor | CBS / Ministry of Economic Affairs | need, orientation, application, approval/outcome, finance types | Annual | Survey population is MKB in business economy |
| P1 | SAFE | ECB | financing demand/conditions/outcomes | Quarterly | Useful cross-EU comparable demand data |
| P2 | CBS business statistics | CBS | firm counts/size/industry | Annual / series-specific | Statistical size categories |
| P2 | Business.gov.nl SME definition | KVK/RVO | EU policy definition | Current | KVK filing thresholds differ |

Links:
- https://www.dnb.nl/en/general-news/statistical-news/2026/almost-half-of-corporate-lending-goes-to-smes-interest-rates-slightly-higher/
- https://www.cbs.nl/nl-nl/longread/aanvullende-statistische-diensten/2026/financieringsmonitor-2025
- https://www.ecb.europa.eu/stats/ecb_surveys/safe/html/index.en.html

### Coverage status
Demand: **very strong**  
Supply: **strong**  
Risk: **company-level/regulatory work needed**  
Pricing: **strong**  
Journey: **strong EU digital-banking test market**

---

# Australia

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | Lenders' Interest Rates — Table F7 | RBA / APRA | outstanding/new rates by small/medium/large business | Monthly | Business-size methodology must be kept with series |
| P1 | Financial Stability Review / RBA research | RBA | credit access, competition, standards, private credit context | Semiannual / ad hoc | Analytical, not always a clean time series |
| P1 | Monthly ADI Statistics | APRA | individual bank balance-sheet data | Monthly | Not always SME-specific |
| P1 | Counts of Australian Businesses | ABS | firm counts, entries/exits, employment size | Annual rolling release | Business count population differs from lending population |
| P2 | Characteristics of Australian Business | ABS | size, digital/innovation/business characteristics | Annual | Survey/statistical scope |
| P2 | Bank annual reports / Pillar disclosures | Individual ADIs | SME/business portfolio, risk and economics | Half-year/annual | Definitions vary by bank |

Links:
- https://www.rba.gov.au/statistics/interest-rates/
- https://www.apra.gov.au/news-and-publications/monthly-authorised-deposit-taking-institution-statistics
- https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/latest-release
- https://www.abs.gov.au/statistics/industry/technology-and-innovation/characteristics-australian-business/2024-25

### Coverage status
Demand: **medium**  
Supply: **strong**  
Risk: **strong at lender level**  
Pricing: **very strong by size**  
Journey: **good bank/nonbank comparison market**

---

# Mexico

| Priority | Source | Owner | Metric families | Frequency | Key caveat |
|---|---|---|---|---|---|
| P1 | ENAFIN 2024 | INEGI / CNBV | financing need, sources, applications, conditions, financial services | Multi-year survey | Micro sample starts at 6 employed persons |
| P1 | Evolución del Financiamiento a las Empresas | Banco de México | finance sources, bank credit usage, new credit, constraints | Quarterly | Survey; size cuts can differ from legal MIPYME |
| P1 | EnBan — bank credit standards | Banco de México | demand, standards, terms by SME/large segment | Quarterly | Bank-side diffusion indices |
| P1 | SIE — Credit to Small and Medium Non-Financial Companies | Banco de México | credit-market conditions and SME series | Quarterly/series-specific | Series definition must be captured |
| P2 | DOF MIPYME stratification | Secretaría de Economía | official size definition | Current reference | Sector + employment + sales + combined score |

Links:
- https://en.www.inegi.org.mx/programas/enafin/2024/
- https://www.banxico.org.mx/publicaciones-y-prensa/evolucion-trimestral-del-financiamiento-a-las-empr/evolucion-del-financiamiento-.html
- https://www.banxico.org.mx/publicaciones-y-prensa/encuesta-sobre-condiciones-generales-y-estandares-/condiciones-en-credito-bancar.html
- https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CF842&locale=es

### Coverage status
Demand: **very strong**  
Supply: **strong survey/central-bank coverage**  
Risk: **requires bank/regulator/company supplements**  
Pricing: **medium/strong**  
Journey: **high-value fintech/bank comparison**

---

# Metric-to-source routing

| Metric family | US | UK | Brazil | Germany | India | Netherlands | Australia | Mexico |
|---|---|---|---|---|---|---|---|---|
| SME/business counts | SBA/Census | BPE | Receita/IBGE | KfW/official stats | Udyam/MSME | CBS | ABS | INEGI |
| Loan stock | Fed/FFIEC | BoE/BBB | BCB/SCR | Bundesbank/ECB/KfW | RBI | DNB | RBA/APRA | Banxico |
| New lending | Fed/bank data | BBB/BoE | BCB concessions | KfW/ECB | RBI | DNB/CBS | RBA/APRA | Banxico |
| Interest rates | Fed/bank data | BoE | BCB | ECB/Bundesbank | RBI | DNB | RBA | Banxico |
| Application/approval | SBCS | BBB survey | supplementary | KfW/SAFE | supplementary | CBS/SAFE | supplementary | ENAFIN/Banxico |
| Credit standards | FR2028D | BoE/BBB | BCB / lender | KfW/SAFE | RBI | SAFE | RBA | EnBan |
| Delinquency/NPL | FFIEC/banks | banks/regulatory | BCB/SCR | banks/regulatory | RBI/banks | banks/DNB | APRA/banks | banks/CNBV/Banxico |
| Journey/screens | lender research | lender research | lender research | lender research | lender research | lender research | lender research | lender research |

---

# Retrieval rules

1. Pull **primary source raw tables/data first**, narrative report second.
2. Save source definition and table/series code with every datapoint.
3. For recurring series, record frequency and last available period.
4. Do not backfill a missing SME split using total corporate data unless explicitly labeled proxy.
5. Survey and administrative data remain separate evidence lanes.
6. Keep lender-level annual reports/Pillar 3 as a separate source family from system-level market data.

---

# Status

The source environment is sufficient to begin Wave 2 for all eight selected markets.

Remaining work is **metric extraction**, not source discovery.
