# Hypothesis Scorecard

**Version:** 2026-10-02  
**Evidence base:** 18 deep dives / 8 markets

---

# H1 — Existing-customer advantage materially improves SME lending

## Original idea

Existing customers should be easier/faster/cheaper to underwrite because the lender already owns relevant behavioral data.

## Evidence supporting

- Nubank — recurring automated eligibility from relationship/account behavior.
- Stone — merchant relationship and monthly revenue feed pre-approved offers.
- CommBank — existing customers can receive conditional approval using bank-held data; new customers route to specialist.
- Amex — existing relationship affects preapproval, line availability and larger initial limits.
- SBI — PABL/PAsBL use existing transaction/UPI behavior.
- Square — merchant processing history generates eligibility.
- Mercado Pago — platform seller/payment activity generates offers.

## Counter-evidence / limitations

- public data rarely isolate existing-vs-new losses;
- selection bias is likely;
- relationship data may be weak for low-activity accounts.

## Current conclusion

**Strongly supported as an operating-model advantage.**

Not yet proven:
- exact reduction in loss;
- exact CAC/underwriting-cost benefit;
- RAROC uplift.

**Confidence: High on mechanism / Medium on quantified economics.**

---

# H2 — Speed is segmentation, not magic

## Evidence

- iwoca: €50k document breakpoint.
- Rabobank: €250k / 5-year fast perimeter.
- SBI: digital-limit / branch escalation.
- Commerzbank: ≤€100k direct-adviser decision threshold.
- Stone: automated vs dedicated desks.
- Funding Circle: automation influenced decision to stop serving new sole traders/partnerships in legacy-manual flow.
- Floryn: €250k annual-account breakpoint.

## Counter-evidence

Some lenders can automate relatively high amounts when data are strong, so “small ticket = automated” is not universal.

## Current conclusion

**Very strongly supported.**

The correct unit is:
ticket × data quality × complexity × security × product.

**Confidence: High.**

---

# H3 — Funding advantage remains a major determinant of economics

## Evidence

Deposit-funded:
- Itaú;
- SBI;
- Judo;
- Allica;
- CommBank;
- Rabobank.

Wholesale/high-cost:
- UGRO cost of borrowing 10.16% vs 17.50% yield.

Asset-light substitutes:
- Funding Circle institutional forward flow.
- Square majority loan sale.
- Floryn private securitisation.
- Bibby receivables-backed facilities.

## Counter-evidence

Deposit funding is not required for strong economics if the lender can distribute assets or use institutional capital.

## Current conclusion

**Supported but refined.**

New hypothesis:
> Attractive SME economics require either low-cost funding or an efficient asset-light risk/funding-transfer mechanism, unless unusually high pricing power compensates.

**Confidence: High.**

---

# H4 — Best customer journeys primarily come from data substitution

## Evidence

- Rabobank — transactions replace annual accounts.
- Floryn — PSD2 replaces annual accounts ≤€250k.
- Konfío — tax/invoice data substitute for manual financial file.
- SBI — GST/UPI/bank data.
- iwoca — Open Banking.
- Stone/Square/Mercado Pago — acquiring/marketplace data.
- CommBank/Nubank — existing-account information.

## Counter-evidence

Allica/Commerzbank/Judo show another valid route:
keep human underwriting but reduce handoffs and administrative friction.

## Current conclusion

**Strongly supported, with an important refinement.**

Best UX comes from either:
1. replacing manual evidence with machine-readable data; or
2. compressing organizational decision latency.

**Confidence: High.**

---

# H5 — SME is several different lending businesses

## Evidence

Observed fundamentally different models:
- micro preapproved;
- unsecured working capital;
- guarantee-backed;
- asset/capex;
- relationship banking;
- receivables finance;
- embedded merchant credit.

Risk objects and funding differ materially.

## Counter-evidence

A single lender can share common infrastructure across these segments, so separate “factories” do not require separate companies.

## Current conclusion

**Very strongly supported.**

Target design:
common data/risk platform + multiple credit factories.

**Confidence: High.**

---

# H6 — Repeat lending can be structurally superior

## Evidence

- Amex dynamic line / repeated draws.
- Square continuous re-evaluation after repayment.
- Nubank recurring eligibility.
- Stone existing merchant relationship.
- Mercado Pago updated platform behavior.
- SBI top-up after clean behavior.
- Funding Circle top-ups / multi-product relationship.

Potential mechanisms:
- lower CAC;
- more observed data;
- less documentation;
- better behavioral risk discrimination;
- higher cross-sell.

## Counter-evidence

Public data generally do not disclose:
- repeat vs first-loan loss;
- repeat contribution;
- repeat approval-rate uplift.

## Current conclusion

**Strongly supported as mechanism; incompletely proven economically.**

**Confidence: Medium/High.**

---

# New hypothesis H7 — Decision rights are a first-class speed lever

## Evidence

- Commerzbank: ≤€100k decision in adviser conversation.
- Allica: underwriter is explicitly embedded in digital process.
- Judo: in-market banker/credit authority.
- SBI: different centralized/branch authorities by product.

## Conclusion

Not every speed gain requires predictive automation.

**Hypothesis status: Supported.**  
**Confidence: Medium/High.**

---

# New hypothesis H8 — Product funding should be optimized at product-engine level

## Evidence

- Funding Circle Term Loans vs FlexiPay have different balance-sheet economics.
- Square distributes much of merchant loans.
- Floryn securitises.
- Bibby uses receivables-backed facilities.
- banks retain loans against deposit base.

## Conclusion

One treasury model for all SME products can be structurally inefficient.

**Hypothesis status: Strongly supported.**  
**Confidence: High.**
