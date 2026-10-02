# Company / Lender Teardown — Rabobank Netherlands

**Status:** Batch 1 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Netherlands  
**Primary segments:** S2/S4/S5 — digital small-business + capex + relationship SME  
**Primary scenario:** existing/new Rabobank SME seeking up to €250k business finance

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**Rabobank demonstrates how a large relationship bank can create a fintech-like SME journey by substituting transaction data for annual accounts — but only inside a clearly bounded risk envelope.** For qualifying loans/credit up to €250k and five years, 13 months of transaction data can support automated assessment without annual accounts; beyond that envelope, the broader journey reintroduces annual figures, adviser contact, security and case-specific underwriting.

### Quantified proof points

- Transaction-data route: **€5k–€250k**, maximum term **5 years**.
- Requires at least **13 months of transaction data**.
- Requires more than **€80k account inflows in the prior 12 months**.
- Public journey: indicative pricing in **30 seconds**, personalized offer in about **15 minutes**.
- “Without annual accounts” route communicates clarity within **1 business day** and funding often within **2 business days** after signing.
- Public annual rate on that specialist route: roughly **6.5%–14%**, plus a 0.5% surcharge disclosed on the route.
- Rabobank group 2025 net result: **€4.957bn**; CET1 **20.3%**.

### Mechanism

Open-banking / bank transaction history
→ automated affordability/cash-flow assessment
→ annual accounts removed for bounded exposures
→ rapid personalized offer
→ adviser/check only where needed
→ bank-funded fulfillment.

### Strategic implication

A deposit-funded incumbent does not need to imitate a fintech institutionally. It can create a fintech-like **product lane** inside the bank, with an explicit exposure/data boundary and a controlled transition back to relationship underwriting.

### Transferability

**Highly transferable for banks with transaction access.**

Prerequisites:
- account/Open Banking history;
- standardized small-ticket product;
- rules for minimum turnover/history;
- exclusions for unsuitable sectors/structures;
- digital pricing/offer engine;
- clean adviser handoff.

### Counter-evidence / limitation

The fast route is **not universal SME lending**. It excludes certain sectors and structures, requires sufficient transaction history and turnover, and stops at €250k/5 years. The conventional bank route remains more document- and adviser-intensive.

---

## 0. Scope and comparability

Rabobank combines:
- mass-market digital SME finance;
- relationship banking;
- larger corporate/agri finance.

Group financial metrics are not SME-specific.

---

## 1. Product architecture

### Standard business loan

Rabobank's business-finance pages support:
- business loans;
- revolving business credit;
- real-estate finance;
- leasing/asset finance;
- guarantee-backed / promotional financing;
- specialist sector finance.

For standard online lending, Rabobank publicly describes:
1. calculate indicative rate/monthly cost;
2. provide financing purpose/plans and recent figures;
3. connect transaction data / supply financial data;
4. receive personalized indicative offer;
5. adviser review/contact;
6. sign;
7. funds often within two business days.

### Special route — finance without annual accounts

Publicly stated conditions include:
- amount up to **€250k**;
- maximum five-year term;
- at least **13 months transaction data**;
- account at Rabobank or supported banks such as ING/ABN/Knab/ASN;
- >€80k inflows over prior 12 months;
- legal/ownership/age restrictions;
- sector exclusions.

This is the core evidence for data substitution.

---

## 2. Underwriting / decision architecture

### Standard route

Inputs can include:
- annual accounts / recent business figures;
- transaction data;
- sector;
- investment purpose;
- future outlook;
- security/collateral.

### No-annual-accounts route

Inputs shift toward:
- transaction history;
- turnover/inflows;
- sector;
- business structure;
- entrepreneur age;
- product amount/term.

Rabobank describes an **automatic assessment** using transaction data for this route.

### Risk controls visible in product design

The route is constrained by:
- ticket ceiling;
- term ceiling;
- minimum inflows;
- supported account data;
- sector exclusions;
- in some cases maximum credit as a percentage of annual revenue.

This is a classic example of UX simplification achieved through **tight product/risk perimeter design**.

---

## 3. Customer journey

### Scenario A — qualifying €100k borrower using transaction-data route

| Stage | Customer action | Public timing/evidence |
|---|---|---|
| Explore | Calculate indicative rate/payment | ~30 seconds |
| Apply | Enter business/finance information | ~5 minutes on specialist route |
| Data | Share 13 months bank transactions | Required |
| Assessment | Automated transaction-data analysis | Backstage |
| Offer | Personalized financing proposal | ~15 minutes / clarity within 1 business day depending route |
| Review | Possible adviser follow-up | if required |
| Sign | Digital documentation | documented |
| Funding | Money after signed agreement | often within 2 business days |

### Scenario B — conventional/larger case

Adds:
- annual financial figures;
- potentially additional information;
- adviser/video call;
- security/collateral;
- longer/more bespoke underwriting.

---

## 4. Visual customer journey

Rabobank's source pages contain an interactive financing calculator and application flow, but a stable first-party image asset for the actual credit screens was not recovered in this research pass.

### Screen evidence status

| Stage | Status |
|---|---|
| Calculator | official interactive UI observed; static asset not captured |
| Application | screen evidence missing |
| Transaction-data consent | screen evidence missing |
| Personalized offer | screen evidence missing |
| Adviser handoff | screen evidence missing |
| Contract | screen evidence missing |
| Funding confirmation | screen evidence missing |
| Servicing | screen evidence missing |

**Screen coverage: Low/Partial.**

We do not substitute generic Rabobank marketing images for actual credit-flow evidence.

---

### Current live customer journey — enriched second pass

Rabobank's current business-finance pages expose a real interactive journey rather than only explanatory copy:

1. customer selects financing purpose and amount;
2. **30-second price indication** shows estimated rate and monthly payment;
3. selecting **Ga verder** starts personalization;
4. customer supplies business/investment information and connects transaction data from relevant business accounts;
5. a **personalized / indicative offer is shown directly**, including amount, rate, term and product form;
6. customer can still alter term / own contribution before making the application final;
7. after final submission, an adviser contacts the customer within one business day / up to two business days depending product page;
8. after offer signing, funding can often be used within two business days.

For qualifying credit/loans up to **€250k / 5 years**, Rabobank states that annual accounts may not be required; automatic affordability assessment can use at least **13 months of transaction data**, subject to turnover/sector/structure rules.

**What it proves**
- price indication, data connection and personalized offer are customer-visible digital stages;
- the personalized offer exists **before** adviser conversation;
- transaction data are not only collected backstage: they directly determine whether the low-document route is available.

**Visual status:** live first-party calculator/application UI is current and observable, but a stable static transaction-consent / personalized-offer image asset was not recovered.

Official sources:
- https://www.rabobank.nl/bedrijven/zakelijk-financieren
- https://www.rabobank.nl/bedrijven/zakelijk-financieren/bereken-indicatie
- https://www.rabobank.nl/bedrijven/zakelijk-financieren/hoe-vraag-ik-een-financiering-aan
- https://www.rabobank.nl/bedrijven/zakelijk-financieren/hoe-hoog-wordt-mijn-rente

---

## 5. Risk and portfolio quality

### Company-level / group evidence

Rabobank 2025:
- net result: **€4.957bn**;
- loan impairment charges: **€764m** vs €468m in 2024;
- cost/income ratio: **54.5%**;
- ROE: **9.1%**;
- CET1: **20.3%**.

Wholesale & Rural loan portfolio was about **€132bn**, but this is not an SME measure and includes a large Food & Agri share.

Source:
https://www.rabobank.com/about-us/press/articles/011514168/rabobank-posts-a-net-result-of-eur-4-957-million-in-2025

### SME-specific risk gap

Publicly accessible product materials do not provide:
- SME NPL;
- SME cost of risk;
- automated-lane loss rate;
- transaction-data-route vintages.

Therefore we can evaluate architecture more confidently than its specific credit outcome.

---

## 6. Lending economics

### Structural context

Rabobank is a deposit-funded cooperative/universal bank, giving it a fundamentally different funding base from non-bank SME fintechs.

### What is observable
- strong group profitability;
- substantial capital;
- deposit-funded banking model;
- customer/account distribution;
- digital small-ticket pathway layered onto relationship infrastructure.

### What is not observable
- yield on €5k–€250k transaction-data SME loans;
- lane-specific acquisition/underwriting cost;
- lane-specific expected loss;
- SME RAROC.

---

## 7. Distinctive capabilities

1. **Explicit transaction-data substitute for annual accounts**
2. **€250k / 5-year risk perimeter**
3. **15-minute personalized-offer design**
4. **Automatic assessment + relationship/adviser fallback**
5. **Bank funding + broad SME product stack**
6. **Clear sector/turnover eligibility controls**

---

## 8. Hypothesis tests

### H1 — Existing-customer advantage: supported
Rabobank can use own-account data directly, although supported external-bank transaction data means the model is not limited to existing customers.

### H2 — Speed is segmentation: strongly supported
The fast/no-annual-accounts pathway has a defined exposure, term, turnover and sector perimeter.

### H4 — UX comes from data substitution: strongly supported
Annual accounts can disappear when transaction history is sufficient and exposure is bounded.

### H5 — SME is several businesses: supported
Larger/complex cases move back to financial statements, adviser interaction and collateral.

---

## 9. Strategic implication

Rabobank suggests a pragmatic incumbent-bank transformation pattern:

**Do not redesign the whole SME credit factory at once. Create a bounded “fast lane.”**

Fast lane:
- standard product;
- clean transaction data;
- defined ticket;
- high automation.

Escalation lane:
- richer financials;
- adviser;
- security;
- bespoke terms.

This architecture can protect risk discipline while still delivering fintech-like UX to the segment where it is economically justified.

---

## 10. Transferability prerequisites

- Open Banking / bank-account data access;
- digital consent;
- enough transaction history;
- customer/sector eligibility rules;
- pricing engine;
- digital contracts;
- human-credit fallback.

**Transferability: High for incumbent banks.**

---

## 11. Evidence gaps

1. SME-specific stock/originations by product lane.
2. Approval rate for transaction-data route.
3. Automated decision rate.
4. Actual observed decision distribution.
5. DPD/NPL by lane.
6. Credit cost / RAROC by lane.
7. First-party static screenflow assets.
8. Repeat/renewal journey.

---

## 12. Sources

Primary:
- https://www.rabobank.nl/bedrijven/zakelijk-financieren
- https://www.rabobank.nl/bedrijven/zakelijk-financieren/hoe-vraag-ik-een-financiering-aan
- https://www.rabobank.nl/bedrijven/zakelijk-financieren/zakelijke-lening
- https://financieren-zonder-jaarcijfers.rabobank.nl/
- https://financieren-zonder-jaarcijfers.rabobank.nl/zakelijk-krediet/
- https://www.rabobank.com/about-us/press/articles/011514168/rabobank-posts-a-net-result-of-eur-4-957-million-in-2025
