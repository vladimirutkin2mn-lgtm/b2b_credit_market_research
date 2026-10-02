# Company / Lender Teardown — UGRO Capital

**Status:** Batch 2 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** India  
**Primary segments:** S2/S4/S7  
**Primary question:** how does an MSME NBFC actively reshape product mix to improve risk-adjusted returns?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**UGRO is a useful counterpoint to a bank because management explicitly manages portfolio mix, funding cost, credit cost and operating cost toward a target ROA.** Its strategy is shifting away from lower-priority intermediated businesses toward two higher-yield engines: secured Emerging Market LAP and merchant embedded finance. Public disclosures make the trade-off unusually visible.

### Quantified proof points — FY26

- AUM: **₹15,334 crore**, +28% YoY.
- Embedded Finance AUM: **₹2,280 crore**, +27% QoQ; ~**2.5 lakh active merchants**.
- Emerging Market LAP AUM: **₹3,581 crore**.
- portfolio yield: **17.50%**.
- cost of borrowings: **10.16%**.
- credit cost: **₹209.4 crore**, +21%.
- GNPA: **2.50%**; NNPA 1.60%.
- Embedded Finance GNPA: **1.70%**.
- EM LAP GNPA: **1.20%**.
- PAT: **₹174.8 crore**, +21%.
- reported ROA: **2.1%**.
- target FY29 annuity ROA: **3.0–3.5%**.
- announced annualised cost takeout: **₹200–220 crore**.

### Mechanism

High-yield unsecured embedded merchant finance
+ secured small-ticket LAP
→ higher portfolio yield / scalable origination.

But NBFC funding cost ~10%
+ credit cost
+ operating branch/tech cost
→ ROA constrained.

Management response:
- grow targeted high-yield verticals;
- run down Prime Intermediated book;
- remove operating cost;
- improve funding/capital mix;
- target higher steady-state ROA.

### Strategic implication

UGRO demonstrates that data-driven lending does not remove the need for **portfolio-mix management**. A lender can have strong technology and still destroy economics if the product/funding/cost mix is wrong.

### Transferability

**High as an economics framework; medium as a product model.**

---

## 1. Business model

UGRO is a listed MSME-focused NBFC with:
- >300 Emerging Market branches;
- secured Loan Against Property;
- machinery/equipment finance;
- embedded merchant finance;
- digital/fintech/payment partnerships;
- proprietary GRO Score 3.0.

Current June 2026 homepage:
- **400k+ customers**;
- AUM **₹15,013 crore**;
- 317 EM branches.

Source:
https://www.ugrocapital.com/

---

## 2. Product architecture

### Embedded Finance

Current public page:
- up to **₹50 lakh**;
- up to **24 months**;
- unsecured;
- short/revolving working-capital products;
- platform transaction data auto-captured;
- 6 months bank statements;
- GST where applicable;
- daily/weekly/monthly repayment options.

Flow:
1. merchant pre-qualified from platform transaction data;
2. automated GRO Score / financial-data evaluation;
3. pre-approved offer generated inside partner platform;
4. simple KYC/consent;
5. instant / hours disbursement.

Source:
https://www.ugrocapital.com/embedded-financing

### Emerging Market LAP
Secured small-ticket credit against property.

### Machinery & Equipment Finance
Asset-backed financing for MSME capex.

This provides three very different risk/economic engines under one platform.

---

## 3. Embedded customer journey

This is a true embedded flow: the merchant may not need a separate UGRO application.

| Stage | Evidence |
|---|---|
| Prequalification | platform transaction data |
| Credit evaluation | automated GRO Score + financial data |
| Offer | pre-approved in partner platform |
| KYC/consent | digital |
| Disbursement | instantly / within hours |
| Repayment | daily, weekly or monthly |

### Visual evidence

The official UGRO page visually depicts all five stages, but stable direct image assets were not captured for repo embedding.

**Screen evidence:** official flow visual documented; authenticated partner-app screen missing.

---

## 4. Risk

FY26:
- GNPA: 2.50%;
- NNPA: 1.60%;
- Stage 3: 2.50%;
- collection efficiency: 98%;
- EM LAP GNPA: **1.20%**;
- Embedded Finance GNPA: **1.70%**.

This segment split is highly valuable:
- secured EM LAP has lower observed GNPA;
- embedded unsecured merchant lending has somewhat higher but still below consolidated GNPA.

It supports analyzing risk by product engine rather than company average.

---

## 5. Lending economics

FY26:
- portfolio yield: **17.50%**;
- cost of borrowings: **10.16%**;
- simple gross yield-cost gap: **7.34 percentage points** before fees, credit cost, OPEX and capital;
- finance cost: ₹954.3cr;
- OPEX: ₹613.9cr;
- credit cost: ₹209.4cr;
- PAT: ₹174.8cr;
- ROA: 2.1%.

The 7.34ppt spread is **not NIM/RAROC**; it is only a diagnostic gross spread.

### Strategic mix shift

UGRO stopped Prime Intermediated disbursements from Feb 7, 2026 and is targeting:
- 85% AUM in EM LAP + Embedded Finance by FY29;
- ₹200–220cr cost reduction;
- no incremental equity through FY29;
- ROA 3.0–3.5%.

This is direct evidence that management sees **mix + cost + capital** as the path to better economics.

---

## 6. Funding and capital

FY26:
- CRAR: **21.2%**;
- net worth: ₹2,906cr;
- leverage: 3.7x.

Unlike deposit-funded banks, UGRO pays materially higher wholesale/market funding costs. This makes high-yield product selection and operating efficiency central to sustainability.

---

## 7. Hypothesis tests

### H3 — funding advantage remains important: strongly supported
A 17.5% portfolio yield can coexist with only 2.1% ROA because funding, credit and OPEX absorb substantial economics.

### H4 — data substitution: strongly supported in Embedded Finance
Platform transaction data enables prequalification and embedded offers.

### H5 — SME is several businesses: very strongly supported
Secured LAP and unsecured embedded merchant finance have different risk/yield/operating characteristics.

### H2 — speed is segmentation: supported
Instant flow is concentrated in embedded merchant credit, not all UGRO products.

---

## 8. Strategic implication

A useful SME-credit P&L should be managed at **product-engine level**:

`yield – funding – credit cost – OPEX – capital`

not merely at company level.

UGRO's own strategy effectively follows this logic by shifting AUM toward engines with better expected risk-adjusted contribution.

---

## 9. Counter-evidence / caveats

- FY26 consolidated figures include Profectus Capital from Dec 2025, reducing clean YoY comparability.
- Embedded Finance growth can raise risk/selection exposure as it scales.
- Management FY29 ROA target is a target, not observed performance.
- Public segment yield/cost is still incomplete.

---

## 10. Evidence gaps

1. Yield by EM LAP vs Embedded Finance.
2. Funding cost by product.
3. Credit cost by product.
4. Vintage losses for GROx.
5. Approval / conversion.
6. Cost per loan/merchant.
7. Full partner-app screens.
8. RWA/economic capital by product.

---

## Sources

- https://www.ugrocapital.com/
- https://www.ugrocapital.com/embedded-financing
- https://www.ugrocapital.com/lending-service-provider
- https://nsearchives.nseindia.com/corporate/UGROCAP_20042026220427_PR.pdf
