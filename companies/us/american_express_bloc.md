# Company / Lender Teardown — American Express Business Line of Credit

**Status:** Batch 2 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** United States  
**Primary segments:** S1/S2  
**Primary question:** how does an existing card/bank relationship change small-business credit underwriting, repeat access and funding speed?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**American Express BLOC combines open-market small-business underwriting with a materially better path for existing Amex customers.** The line decision uses linked bank accounts, bureau data, business revenue/transaction volume and prior Amex/financial-institution history; select Card Members can see price and line size before applying, and borrowers who also use Amex Business Checking can receive drawdown funds within seconds.

This is a strong example of **relationship flywheel economics**: acquisition, underwriting, deposit/account relationship and repeat borrowing reinforce one another.

### Quantified proof points

- line sizes: **$2k–$250k**;
- initial lines >$150k available only to select borrowers with a pre-existing Amex relationship and other criteria;
- minimum published eligibility: ≥**1 year** business, ≥**660 FICO**, ≥**$3k average monthly revenue**;
- installment terms: 6/12/18/24 months;
- monthly loan fee: **0.55%–1.55%** of original principal, depending eligibility;
- Amex Business Checking disbursement: typically **within seconds**;
- ACH: 1–3 business days.
- Jun-2026 American Express “Other loans” net balance: **$11.115bn**; this category includes consumer installment and small-business lines of credit, so it is not BLOC-only.

### Mechanism

Existing Amex relationship
+ linked bank account
+ bureau / prior repayment
→ richer underwriting profile
→ potential preapproval / larger line
→ repeat draws without reapplying
→ optional instant transfer into Amex Business Checking
→ deeper ecosystem relationship.

### Strategic implication

The most powerful repeat-lending product is not simply a revolving line. It is a **continuously re-underwritten relationship limit** connected to the operating account and payments ecosystem.

### Transferability

**High for banks/card issuers with business transaction relationships.**

### Counter-evidence

Public SEC risk disclosures do not isolate BLOC. “Other loans” includes other consumer/small-business products, and Amex's detailed small-business loss rates primarily relate to Card balances, not BLOC. We cannot claim BLOC has the same risk profile.

---

## 1. Product design

### Business Line of Credit

- $2,000–$250,000 line;
- multiple draws without reapplying, subject to ongoing eligibility;
- each draw becomes a separate installment/single-repayment loan;
- 6/12/18/24 month installment terms are public;
- no application, origination, annual or maintenance fee; loan fees apply;
- early full repayment avoids future unposted monthly fees.

### Pricing

Instead of a conventional interest rate, installment loans use a monthly loan fee:
**0.55%–1.55% of original principal per outstanding month**.

Amex also shows a comparable APR in the SMART Box on the loan agreement.

This is important for competitive benchmarking:
monthly fee ≠ nominal APR ≠ portfolio yield.

---

## 2. Eligibility / underwriting

Minimum public eligibility:
- FICO >=660;
- business age >=12 months;
- recent average monthly revenue >=$3,000;
- eligible industry.

Public underwriting factors include:
- business bank accounts;
- linked accounts;
- prior credit;
- repayment history;
- consumer bureau;
- commercial bureau;
- average monthly revenue;
- time in business;
- transaction volume;
- history with American Express and other institutions.

Ongoing account review can increase or reduce line availability.

Source:
https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/applying/index.how-do-you-determine-how-much-funding-i-can-access-and-can-my-business-line-of-credit-change-over-time.html

---

## 3. Existing-customer advantage

Select existing Amex Card Members may see:
- whether they are pre-approved;
- available line size;
- price
**before applying**.

Initial lines above $150k are only available to select borrowers with a pre-existing Amex relationship plus other criteria.

This is strong direct H1 evidence.

---

## 4. Customer journey

### Initial approval

1. Check pre-approval / start application.
2. Provide EIN/SSN, industry, revenue.
3. Link/maintain business bank accounts.
4. Amex uses bank/credit/relationship data.
5. Receive line decision.
6. Line becomes available in Business Blueprint.

### Repeat draw

1. “Take a loan” / “Fund my account.”
2. Select draw amount.
3. Select available term.
4. Review monthly fee / APR / repayment.
5. Choose deposit account or eligible payee.
6. Sign loan agreement.
7. Funds delivered.

### Fulfillment

- External ACH: 1–3 business days.
- Amex Business Checking: typically seconds, 24/7 when eligible.

---

## 5. Visual customer journey

American Express publishes an official illustrated guide showing:
- Business Blueprint dashboard “Take a loan”;
- BLOC home-screen “Fund my account”;
- Business Checking account selection with “Instant deposits”;
- success screen.

Source:
https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/

The article explicitly labels screens “For illustrative purposes only.”

Stable direct image-asset URLs were not captured, so the repo links the official guide rather than reproducing uncertain assets.

**Screen evidence: Medium/High documented official illustrations.**

---

### Screen evidence — enriched second pass

#### Business Blueprint dashboard

![Amex BLOC — Business Blueprint start](https://www.americanexpress.com/content/dam/amex/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/InstantDeposit_step1a.png)

#### Business Line of Credit home / start draw

![Amex BLOC — Fund my account](https://www.americanexpress.com/content/dam/amex/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/InstantDeposit_step2b.png)

#### Deposit-location selection

![Amex BLOC — deposit location](https://www.americanexpress.com/content/dam/amex/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/Step-2a.png)

#### Successful instant deposit

![Amex BLOC — success](https://www.americanexpress.com/content/dam/amex/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/Step-3.jpg)

**What the official sequence proves**
- repeat draw starts inside Business Blueprint/BLOC rather than a fresh application;
- deposit destination is selected in-flow;
- Amex Business Checking is explicitly integrated as an instant-deposit destination;
- successful completion returns the user toward account access.

Official source:
https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/

---

## 6. Risk context

### BLOC-specific risk disclosure gap

Amex reports “Other loans” as a combined category covering:
- consumer installment loans;
- lines of credit offered to small-business customers.

Jun-2026:
- Other loans net: **$11.115bn**;
- reserve: **$312m**.

The filing reports overall Other-loan aging/write-offs, but not BLOC as a standalone product.

### Small-business Card context — do not mix

Amex separately reports small-business Card balances and net write-off rates.

Those are valuable context for Amex's business-credit underwriting franchise, but they are **not BLOC loss metrics** and are not substituted here.

---

## 7. Economics

Direct BLOC economics publicly observable:
- fee structure;
- revolving/repeat draw design;
- banking ecosystem integration.

Not public:
- BLOC originations;
- average utilization;
- yield;
- funding cost;
- BLOC credit losses;
- unit contribution;
- RAROC.

### Structural economics hypothesis

Existing Amex Card/Checking customers may provide:
- lower acquisition cost;
- richer risk data;
- higher cross-sell revenue;
- faster repeat lending;
- deposits/funding relationship.

These are plausible channels, not publicly quantified BLOC unit economics.

---

## 8. Hypothesis tests

### H1 — existing-customer advantage: very strongly supported
Preapproval, line-size eligibility and >$150k availability explicitly depend partly on pre-existing relationship.

### H4 — data substitution: strongly supported
Linked account/bureau/history data are core underwriting inputs.

### H6 — repeat lending: structurally strong
Borrowers can draw repeatedly without a full reapplication; line is continuously reviewed.

### H3 — funding advantage: plausible
Business Checking adds a deposit relationship, but BLOC marginal funding cost is not public.

---

## 9. Strategic implication

The repeat-lending loop should be treated as a product in its own right:

**observe customer → maintain dynamic limit → preapprove → one-click/reduced-friction draw → observe repayment → update limit.**

This can create much better lifetime economics than re-originating a term loan from zero each time.

---

## 10. Evidence gaps

1. BLOC outstanding balance/originations.
2. Utilization.
3. Approval/preapproval rate.
4. BLOC DPD/NCO/ECL.
5. Repeat draw frequency.
6. BLOC yield/funding cost.
7. Cross-sell uplift from Checking/Card.
8. Stable image assets for official flow.

---

## Sources

- https://www.americanexpress.com/en-us/business/blueprint/business-line-of-credit/
- https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/applying/faq.whats-required-to-apply-for-american-express-business-line-of-credit.html
- https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/applying/index.how-do-you-determine-how-much-funding-i-can-access-and-can-my-business-line-of-credit-change-over-time.html
- https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/
- https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/fees/faq.what-fees-are-charged-for-american-express-business-line-of-credit-loans.html
- https://www.sec.gov/Archives/edgar/data/4962/000000496226000322/axp-20260630.htm
