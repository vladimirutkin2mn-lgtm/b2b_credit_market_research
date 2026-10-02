# Company / Lender Teardown — Square Loans

**Status:** Batch 3 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** United States  
**Primary segment:** S7 — acquiring / embedded merchant credit  
**Primary question:** how far can real-time merchant data extend credit access while keeping losses investable/distributable?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**Square Loans combines one of the most automated SME journeys in the study with a largely originate-and-distribute funding model.** Daily payment data determine whether a merchant sees an offer; repayment is automatically tied to sales; and the majority of Square Loans are sold to third-party investors, limiting the amount retained on Block's own balance sheet.

In 2026 Square expanded models to reach smaller and even very new sellers, showing how better underwriting can widen the eligible perimeter rather than just accelerate the same applicants.

### Quantified proof points

- offer size: **$100–$500k**;
- >**$32bn** small-business loans originated since 2014;
- average historical loan size: nearly **$10k**;
- 2026 model changes extended offers to **50%+ more sellers**;
- nearly half of new-model borrowers had never received a prior Square Loan offer;
- 66% of new offers went to sellers with **< $25k annual GPV**; 95% to < $125k;
- traditional Square Loan repayment averages about **10 months**;
- Jun-2026 Block commercial loans held for investment: **$488.9m gross**, allowance **$32.3m**;
- commercial loans held for sale: **$676.8m**;
- Block says majority of Square Loans are sold to third-party investors;
- commercial-loan delinquent/nonperforming amount was immaterial at Jun-2026.

### Mechanism

Square payment processing
→ real-time revenue/frequency/customer-mix data
→ daily automated eligibility
→ invitation/pre-approved offer
→ amount slider changes fee/repayment rate
→ fixed share of daily sales automatically repays
→ majority of originated loans can be sold to investors.

### Strategic implication

Square combines **data moat + embedded distribution + repayment control + capital recycling**. This is a stronger model than embedded credit alone.

### Transferability

**High for acquiring/payment ecosystems; low for lenders without merchant-flow data.**

### Counter-evidence

Square Loans remain invitation-only and offer amounts are model-controlled. The fastest journey is available only after the platform has observed sufficient data. Block's consolidated credit-loss accounting includes many consumer products, so only commercial-loan disclosures should be used for Square lending.

---

## 1. Customer/product model

Public current product:
- $100–$500k;
- invitation-only;
- no ongoing interest;
- one fixed loan fee;
- automated repayment as a percentage of daily card sales;
- offer shown in Square Dashboard/email.

Eligibility factors include:
- processing volume;
- frequency;
- account history;
- customer mix;
- payment disputes/chargebacks and other health indicators.

Accounts are automatically reviewed **daily**.

Sources:
- https://squareup.com/us/en/banking/loans
- https://squareup.com/help/us/en/article/8544-review-loan-eligibility-requirements

---

## 2. 2026 underwriting expansion

Square's March 2026 disclosure says improved machine-learning models now:
- assess more varied/seasonal revenue patterns;
- assess some new-to-Square businesses within their first **5 days** of processing;
- create smaller/shorter-duration offers for newer/smaller sellers;
- extend offers to >50% more sellers.

This is important: model innovation changes the **risk perimeter**, not only processing speed.

Source:
https://squareup.com/us/en/press/expanding-access-to-square-loans

---

## 3. Customer journey

1. Square continuously reviews seller.
2. Offer appears in Dashboard/email.
3. Seller opens Banking → Loans.
4. Slider selects amount.
5. Fee and hold/repayment rate update dynamically.
6. Seller enters identity/ownership information.
7. Application review generally 1–2 business days; extra info may be requested.
8. Approved funds:
   - Square Checking: instant;
   - linked bank: 1–3 business days.
9. Fixed percentage of daily sales repays automatically.
10. Dashboard shows balance/minimum payments.
11. After payoff, eligibility is re-evaluated.

Source:
https://squareup.com/help/us/en/article/8543-apply-for-a-loan
https://squareup.com/help/us/en/article/8546-repay-your-loan

---

## 4. Visual evidence

Square Support officially embeds images for:
- loan repayment/minimum-payment status;
- loan-dashboard views.

The current indexed pages identify these as illustrative.

Stable direct asset URLs were not captured.

**Screen evidence:** official illustrative screenshots documented; direct repo embedding missing.

---

### Screen evidence — enriched second pass

#### Loan servicing / repayment dashboard

![Square Loans — repayment dashboard](https://images.ctfassets.net/gc4s9mi2asix/5foEyfENDInLcsDiN1eAcB/ddffd1df3aeecbe950888887e0282514/Healthy_Plan_-_desktop__1_.png)

**What it proves**
- outstanding balance and repayment progress are visible in the same Square Dashboard;
- automatic payments are shown alongside manual payments;
- minimum remaining payment and paid-to-date are transparent;
- servicing is embedded into the seller's operating dashboard.

#### Split payment example

![Square Loans — payment split between balance and ACH](https://images.ctfassets.net/gc4s9mi2asix/23eXZOT1gL32QcSjtbiPRp/59c8b5eb88c0d81559fd98d03547679f/Screenshot_2025-07-23_at_2.18.10%C3%A2__PM.png)

**What it proves**
- repayment can be sourced from stored Square balance and linked bank account;
- the servicing layer reconciles multiple repayment sources.

Official source:
https://squareup.com/help/us/en/article/8548-view-your-loan-reports

---

## 5. Funding / balance-sheet economics

Block 2Q26 filing:

Commercial loans primarily include Square Loans.

At June 30, 2026:
- held-for-investment commercial amortized cost: **$488.860m**;
- allowance: **$32.252m**;
- net HFI: **$456.608m**;
- commercial held-for-sale: **$676.750m**.

Block states:
- Square Financial Services originates Square Loans;
- the **majority are sold to third-party investors**;
- a portion remains on balance sheet.

This is an important asset-light mechanism similar in spirit to Funding Circle, but with a bank-originator/payment-platform stack.

---

## 6. Risk

Block defines:
- Square Loan delinquent: 60+ DPD;
- nonperforming: 90+ DPD;
- generally written off: 120+ DPD.

At June 30, 2026:
- amount of commercial loans identified as delinquent/nonperforming was **immaterial**.
- six-month commercial provisions: **$21.9m**;
- commercial write-offs: **$29.4m**;
- recoveries: **$6.1m**;
- allowance ending balance: **$32.3m**.

Caveat:
commercial category primarily includes Square Loans, but may not be exclusively one product cohort.

Source:
https://www.sec.gov/Archives/edgar/data/1512673/000162828026053368/R15.htm

---

## 7. Hypothesis tests

### H1 — existing-customer advantage: very strongly supported
Eligibility is generated from seller activity.

### H4 — data substitution: very strongly supported
Transaction data replaces traditional financial-file collection.

### H6 — repeat lending: supported
Continuous re-evaluation after repayment creates a repeat-offer loop.

### H3 — funding architecture: strengthened
Majority loan sale to investors reduces retained credit/funding burden.

---

## 8. Strategic implication

Square's model suggests the highest-value embedded-lending architecture is:

**observe → pre-underwrite → offer → auto-repay → sell/recycle asset → observe again.**

That combines:
- lower CAC;
- lower document cost;
- lower servicing friction;
- capital recycling.

---

## 9. Evidence gaps

1. Square-specific originations for 2026.
2. Investor sale economics / gain-on-sale.
3. Product yield / fee APR distribution.
4. Vintage default by new underwriting model.
5. Repeat borrower loss vs first loan.
6. Seller conversion from offer to funded loan.
7. Complete screenflow assets.

---

## Sources

- https://squareup.com/us/en/banking/loans
- https://squareup.com/us/en/press/expanding-access-to-square-loans
- https://squareup.com/help/us/en/article/8544-review-loan-eligibility-requirements
- https://squareup.com/help/us/en/article/8543-apply-for-a-loan
- https://squareup.com/help/us/en/article/8546-repay-your-loan
- https://www.sec.gov/Archives/edgar/data/1512673/000162828026053368/R15.htm
