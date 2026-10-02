# Company / Lender Teardown — Funding Circle UK

**Status:** Batch 2 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** United Kingdom  
**Primary segments:** S2 digital unsecured SME + revolving SME credit  
**Primary question:** can a non-bank digital lender overcome a funding disadvantage through capital-light origination, data, automation and scale?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**Funding Circle shows that “fintech lending economics” are not one model. Its mature Term Loans business is a capital-light origination-and-servicing platform funded predominantly by institutional investors and already produces high margins; its newer FlexiPay/Card products carry more balance-sheet/funding/ECL intensity and are still moving toward profitability.**

This is one of the clearest public examples in the project of product architecture determining economics.

### Quantified proof points

H1 2026:
- credit extended: **£1.690bn**, +52% YoY;
- revenue: **£138.2m**, +50%;
- PBT: **£24.1m**, 17.4% margin;
- Term Loan originations: **£1.050bn**, +43%;
- Term Loan AUM: **£2.953bn**;
- Term Loan PBT: **£28.6m**, **26.4% margin**;
- FlexiPay/Card transactions: **£640m**, +71%;
- FlexiPay/Card AUM: **£300m**;
- FlexiPay/Card loss before tax: **£4.5m**;
- institutional forward-flow commitments: **£2.4bn**;
- **73% of applicants** receive an instant decision.

### Mechanism

**Term Loans**
proprietary underwriting + digital distribution
→ loan originated
→ institutional capital funds/owns much of credit exposure
→ Funding Circle earns transaction + servicing economics
→ low capital intensity at platform level
→ mature operating leverage.

**FlexiPay/Card**
Funding Circle provides revolving/on-balance-sheet style credit capacity
→ interest income grows
→ warehouse funding + ECL + product build costs matter directly
→ lower near-term profitability despite strong growth.

### Strategic implication

A lender should not ask only whether SME credit is “asset-light” or “balance-sheet.” The product-by-product decision determines:
- revenue model;
- funding cost;
- ECL burden;
- capital requirement;
- operating leverage.

### Transferability

**Capital-light term-loan model: transferable with strong institutional-funding demand.**  
**Revolving model: requires funding and credit-loss capability.**

### Counter-evidence

Funding Circle's established Term Loans economics are strong, but newer revolving/card products show that cross-sell can initially dilute consolidated margin. Faster customer growth does not automatically mean better near-term profitability.

---

## 1. Business model and scale

Funding Circle positions itself as a UK SME finance platform rather than a bank.

Current public scale:
- >**£18bn** credit extended since 2010;
- >**135,000** UK businesses financed;
- about **£3.3bn AUM** at H1 2026.

The group now offers:
- Term Loans;
- short-term loans;
- FlexiPay revolving line;
- business credit card;
- Growth Guarantee Scheme;
- asset finance via specialist partners.

Source:
https://corporate.fundingcircle.com/media/newsroom/half-year-2026-results
https://corporate.fundingcircle.com/

---

## 2. Product / customer journey

### Business Loan

Public current terms:
- **£10k–£750k**;
- 6 months–6 years;
- rates from **6.9% p.a.**;
- online application around **7 minutes**;
- decision in as little as **5 minutes**;
- funds typically within **48 hours**;
- no full early-settlement fee.

Current borrower perimeter:
- limited companies / LLPs;
- at least one year trading.

Funding Circle stopped accepting new sole-trader/partnership applications from **23 February 2026**, explicitly saying that automated/open-banking finance was incompatible with the manual legacy assessments needed for those structures.

That is unusually direct evidence that operating-model simplification can influence **which customer segments a lender chooses to serve**.

Sources:
- https://www.fundingcircle.com/uk/small-business-loans/
- https://www.fundingcircle.com/uk/support/business-loans/non-limited-loans/

### Short-term loans

For loan amounts up to £250k, Funding Circle says decisions can be instant for qualifying applications.

### FlexiPay

- line from **£1k–£250k**;
- eligibility check without affecting company credit score;
- credit limit can be returned immediately;
- fee from **1.99% per transaction** for a 1-month term.

---

## 3. Underwriting architecture

Public underwriting factors include:
- business credit score;
- bank transactions;
- trading history;
- open-banking / financial data;
- proprietary SME lending history.

Funding Circle states its platform uses:
- 15+ years of SME lending data;
- AI-powered risk models;
- human Credit Assessment support for cases that need it.

### Automation perimeter

The 2026 sole-trader decision is strategically important:
- limited companies/LLPs fit the increasingly automated workflow;
- sole traders/partnerships required more manual legacy assessment;
- Funding Circle chose to narrow the addressable segment rather than preserve operational complexity.

This is a strong H2/H4 signal.

---

## 4. Customer journey

| Stage | Current public experience |
|---|---|
| Eligibility | ~30 seconds |
| Application | ~7 minutes |
| Data | company/business details; bank transactions/supporting documents if needed |
| Decision | as little as 5 minutes for some loans; instant in some lower-ticket products |
| Offer | personalized rate/terms |
| Contract | digital |
| Funding | typically within 48 hours |
| Servicing | online account |
| Repeat | top-up can be offered without full re-application |

### Visual evidence

Funding Circle's product pages visibly present the 4-step journey and calculator, but stable direct first-party application-screen assets were not captured in this research pass.

**Screen status:** documented visual workflow, actual authenticated application screens **missing**.

---

## 5. Economics — why Term Loans and FlexiPay differ

### H1 2026

| Metric | Term Loans | FlexiPay + Card |
|---|---:|---:|
| Originations / transactions | £1.050bn | £640m |
| AUM | £2.953bn | £300m |
| PBT | £28.6m | **-£4.5m** |
| PBT margin | 26.4% | n/a / loss |

Funding Circle describes Term Loans as:
- highly cash generative;
- capital-light;
- supported by sustainable institutional funding.

Institutional forward-flow capacity stood at **£2.4bn**.

FlexiPay funding included a renewed/up-sized Citi facility of **£320m**, providing around **£400m** lending capacity including Funding Circle equity.

Source:
https://corporate.fundingcircle.com/media/newsroom/half-year-2026-results

### FY2025 ECL evidence

The 2025 Annual Report disclosed for FlexiPay:
- gross drawn lines: **£205.1m**;
- ECL on drawn lines: **£32.2m**;
- ECL on undrawn lines: **£2.5m**.

This is a material balance-sheet credit-risk requirement absent from the same form in the capital-light Term Loan platform.

Source:
https://corporate.fundingcircle.com/media/5pyhlkbj/funding-circle-holdings-plc-annual-report-and-accounts-2025.pdf

---

## 6. Risk

### Term Loans
Funding Circle reports continued institutional-investor demand and returns in line with expectations, but current public H1 material does not provide one simple borrower-loss metric directly comparable with a bank NPL.

### FlexiPay
The ECL stock demonstrates that revolving exposure has a meaningful expected-loss balance-sheet burden.

### What remains unknown
- current vintage default curves by product;
- approval rate by risk band;
- charge-offs by product;
- true economic capital allocation;
- RAROC.

---

## 7. Hypothesis tests

### H2 — Speed is segmentation: strongly supported
Automation influences customer eligibility and even legal-form coverage.

### H3 — Funding advantage: nuanced
Funding Circle avoids needing a bank deposit franchise for most Term Loan credit risk by using institutional capital. For revolving products, funding cost/ECL return as major economic variables.

### H4 — Data substitution: strongly supported
Bank transaction data + digital underwriting enable quick decisions with documents only when needed.

### H6 — repeat relationship: supported
31% of customers had >1 product at H1 2026, and top-ups can be offered without reapplying from scratch.

---

## 8. Strategic implication

**The choice of product balance-sheet architecture matters as much as the underwriting model.**

A bank/fintech can potentially use:
- capital-light originate-and-service for term credit;
- balance sheet for high-frequency revolving products where customer lifetime value justifies funding/ECL intensity.

The two should not be evaluated using the same margin framework.

---

## 9. Evidence gaps

1. Product-level vintage losses.
2. Institutional-investor loan net loss / gross yield.
3. FlexiPay net charge-offs.
4. Product-specific cost-to-serve.
5. Approval/booked conversion.
6. Capital allocated to balance-sheet products.
7. Authenticated customer screens.

---

## Sources

- https://corporate.fundingcircle.com/media/newsroom/half-year-2026-results
- https://corporate.fundingcircle.com/
- https://www.fundingcircle.com/uk/small-business-loans/
- https://www.fundingcircle.com/uk/all-products/
- https://www.fundingcircle.com/uk/support/business-loans/non-limited-loans/
- https://www.fundingcircle.com/uk/support/flexipay/
- https://corporate.fundingcircle.com/media/5pyhlkbj/funding-circle-holdings-plc-annual-report-and-accounts-2025.pdf
