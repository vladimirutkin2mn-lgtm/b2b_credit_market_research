# Source Registry

Дата проверки: 2026-10-02.

Этот файл задает source hierarchy для исследования SME / B2B lending.

## Tier 1 — первичные / регуляторные источники

### Europe

**EBA — Guidelines on loan origination and monitoring**  
https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/credit-risk/guidelines-loan-origination-and-monitoring

Использовать для:
- governance credit granting;
- borrower information;
- creditworthiness assessment;
- collateral / guarantees;
- monitoring throughout loan lifecycle;
- различий между micro/small и medium/large enterprises.

**Basel Committee / BIS — Basel Framework, Credit Risk**  
https://www.bis.org/basel_framework/

Использовать для:
- regulatory exposure classes;
- corporate / SME treatment;
- credit risk mitigation;
- capital / RWA context;
- определения, когда сравниваем capital intensity игроков.

### United States

**OCC — Lending and Loan Portfolio Risk Management, June 2026**  
https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/lending-loan-portfolio-risk-management/index-lending-loan-portfolio.html

Использовать для:
- lending lifecycle;
- underwriting;
- portfolio management;
- concentrations;
- problem credit and risk governance.

**OCC — Underwriting**  
https://www.occ.treas.gov/topics/supervision-and-examination/credit/commercial-credit/underwriting.html

Полезная рамка: terms and conditions кредита включают financial/collateral requirements, repayment, maturity, pricing и covenants.

**Federal Reserve Banks — Small Business Credit Survey**  
https://www.fedsmallbusiness.org/reports/survey

Использовать для:
- borrower demand;
- application behavior;
- approval outcomes;
- lender choice;
- satisfaction / financing experience;
- сегментации по размеру, возрасту, отрасли и другим характеристикам.

Важно: survey uses a convenience sample; ограничения выборки должны сохраняться в выводах.

**Federal Reserve — Small Business Lending Survey / FR 2028D**  
https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_2028D

Использовать для:
- availability and cost of bank credit;
- loan amounts, rates and terms;
- bank standards;
- application volume / quality;
- demand.

**FDIC — 2024 Small Business Lending Survey**  
https://www.fdic.gov/publications/2024-report-small-business-lending-survey

Использовать для:
- product mix;
- underwriting practices;
- approval authority;
- approval time;
- automation;
- fintech adoption;
- bank-size differences;
- competitive markets.

## Tier 1/2 — международные benchmark sources

**OECD — Financing SMEs and Entrepreneurs 2026: An OECD Scoreboard**  
https://www.oecd.org/en/publications/financing-smes-and-entrepreneurs-2026_075d8058-en/full-report.html

Использовать для country-level benchmarking:
- outstanding SME loans;
- new lending;
- SME share of business loans;
- interest rates / spreads;
- rejection;
- non-performing loans where available;
- government guarantees and alternative finance.

Обязательно проверять country notes: определения SME и статистические series различаются по странам.

## Tier 1 — company-specific

Для каждого банка/финтеха приоритет:
1. annual report / 10-K / 20-F;
2. Pillar 3 / regulatory disclosures;
3. investor presentations / earnings materials;
4. official product pages;
5. terms, tariff PDFs, lending agreements;
6. help center / FAQ / developer docs;
7. official app-store listing and release notes.

## Tier 2 — reliable external evidence

Использовать для проверки и context, но не вместо primary source:
- центральные банки и статистические ведомства;
- reputable rating agencies;
- reputable industry associations;
- audited databases / exchange filings;
- high-quality academic research.

## Tier 3 — user-experience evidence

Подходит для customer journey и friction:
- App Store / Google Play reviews;
- Trustpilot и аналогичные review platforms;
- Reddit / профильные форумы;
- support/community threads;
- видео walkthroughs;
- интервью и публикации клиентов.

Ограничение: anecdotal evidence не превращается в prevalence claim без количественной поддержки.

## Source scoring

Каждому источнику присваивать:

- **Authority (0–3)**: primary/regulator > reputable secondary > anecdotal.
- **Directness (0–3)**: измеряет именно нужную метрику или является proxy.
- **Recency (0–2)**: соответствует нужному периоду.
- **Definition fit (0–2)**: совпадают SME/product/geography definitions.

Итого 0–10. Score не заменяет judgment, но помогает заметить слабые основания.

## Evidence record

Для важного claim хранить:

- Claim
- Source title
- URL
- Publication date
- Data period
- Geography
- Definition / denominator
- Exact metric
- Extract / table reference
- Fact / calculation / estimate / hypothesis
- Confidence
- Conflicts / caveats

## Правило против ложной сопоставимости

Нельзя напрямую сравнивать:
- origination flow с outstanding stock;
- application approval rate с booked-loan conversion;
- delinquency с default/NPL;
- gross yield с NIM;
- provision expense с lifetime credit loss;
- SME definitions разных стран без normalization;
- bank-only market data с total credit market including nonbanks.

Сначала нормализовать определения, затем сравнивать.
