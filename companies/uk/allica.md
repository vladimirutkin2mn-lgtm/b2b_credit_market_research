# Company / Lender Teardown — Allica Bank

**Status:** Batch 3 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** United Kingdom  
**Primary segments:** S4/S5 — established SME / growth / asset & property finance  
**Primary question:** how can a specialist SME bank combine human underwriting with digital origination and still create scalable economics?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**Allica's model is best understood as “technology-enabled relationship banking”, not a digital-lending substitute for human underwriting.** The bank digitizes pre-qualification, application and broker workflow, but deliberately keeps underwriters and relationship managers in the decision chain for established SME credit. That model has already scaled to £3.7bn of lending and £5.7bn of deposits while producing £43.7m underlying PBT in 2025.

### Quantified proof points

2025:
- total lending: **£3.7bn**, +23%;
- customer deposits: **£5.7bn**, +29%;
- gross revenue: **£371.3m**, +27%;
- gross profit after risk: **£145.3m**, +32%;
- underlying PBT: **£43.7m**, +34%;
- active Business Rewards Account customers: **14,000+**, +133%;
- >**£1.3bn** new lending during 2025;
- Business Loan: **£25,001–£150,000**, 1–5 years, 9.90%–13.75%;
- Growth Finance: **£1m–£15m**, typically ≥£5m turnover / ≥£500k EBITDA.

### Mechanism

Digital eligibility / data capture
→ fast decision in principle
→ full financial package
→ human underwriter
→ tailored approval
→ relationship manager for larger/complex cases.

### Strategic implication

For medium SME, the design target should not be “remove the underwriter.” It should be **remove administrative friction around the underwriter** while giving decision-makers better data and live workflow.

### Transferability

**High for established-SME banks.**

### Counter-evidence

Allica's model depends on larger tickets, richer financial information and higher relationship value. It is not a template for very small-ticket SME credit.

---

## 1. Position and target customer

Allica focuses on established UK SMEs rather than microbusiness mass-market lending.

Public Growth Finance criteria:
- UK limited company;
- B2B model;
- trading ≥24 months;
- annual turnover >£5m;
- EBITDA >£500k;
- facility £1m–£15m.

Other products extend down-market:
- Business Loan £25,001–£150,000;
- Asset Finance £25k–£2.5m;
- Commercial Mortgages £150k–£15m.

Sources:
- https://www.allica.bank/business-loans
- https://www.allica.bank/growth-finance
- https://www.allica.bank/asset-finance
- https://www.allica.bank/commercial-mortgages

---

## 2. Business Loan journey

Public workflow:

1. **Decision in principle**
   - company name;
   - amount;
   - term;
   - fee structure;
   - indicative eligibility/rate.

2. **Full application**
   - bank statements;
   - company accounts;
   - management accounts;
   - all other debt;
   - personal credit consent for directors/beneficial owners.

3. **Underwriter review**
   - human review;
   - requests for additional information if needed.

4. **Approval and drawdown**
   - formalities;
   - funds released.

This is a useful middle ground between:
- fully automated micro-SME credit;
- traditional branch-heavy underwriting.

---

## 3. Visual customer journey

The official Business Loans page contains first-party step illustrations for:
- decision in principle;
- complete application;
- underwriter review;
- approval/drawdown.

Stable direct image assets were not captured in this research pass.

**Screen evidence status:** official visual workflow observed, actual authenticated forms/screens **missing**.

Broker journey is also digitized:
- online applications;
- real-time status updates;
- direct access to BDM / credit ops / underwriters.

Source:
https://www.allica.bank/introducers

---

### Official first-party screens — enriched second pass

#### Eligibility / decision in principle

![Allica — checking eligibility](https://www.allica.bank/hs-fs/hubfs/get-a-decision-in-principle.png?height=750&name=get-a-decision-in-principle.png&width=1218)

**What it proves**
- the journey begins with an explicit eligibility / decision-in-principle step;
- the customer gets a preliminary outcome before completing the full underwriting file.

#### Connect bank accounts

![Allica — connect bank accounts](https://www.allica.bank/hs-fs/hubfs/complete-your-application.png?height=981&name=complete-your-application.png&width=1624)

**What it proves**
- bank-account connectivity is part of the application workflow;
- the digital layer is used to acquire transaction evidence alongside financial statements.

#### Application submitted / underwriter handoff

![Allica — application submitted](https://www.allica.bank/hs-fs/hubfs/underwriter-review.png?height=620&name=underwriter-review.png&width=1624)

**What it proves**
- submission and human underwriting are deliberately separated into visible stages;
- manual review is a designed part of the experience rather than an invisible queue.

#### Approval / drawdown

![Allica — money added to account](https://www.allica.bank/hs-fs/hubfs/approval-and-drawdown.png?height=966&name=approval-and-drawdown.png&width=1624)

**What it proves**
- funding confirmation is part of the public journey;
- the published illustration explicitly visualizes cash reaching the business account.

Official source:
https://www.allica.bank/business-loans

---

## 4. Underwriting and risk architecture

### £75,000 document breakpoint

Current official Business Loan guidance adds a second underwriting breakpoint inside the £25,001–£150,000 product:

- **up to £75,000:** three months of business bank statements plus 12 months management accounts (less than 60 days old) **or** two years full accounts where sufficiently recent;
- **over £75,000:** six months of business bank statements plus two years accounts, and management accounts if the latest filed accounts are more than six months old;
- applicants may also be asked for an assets / liabilities / income / expenditure statement.

Allica also publishes a minimum **150% debt-service-cover** eligibility requirement for this product.

This is important because the public journey remains digitally simple while the evidence burden increases with exposure.

### Publicly evidenced inputs:
- bank statements;
- statutory/company accounts;
- management accounts;
- existing debt;
- director/beneficial-owner credit searches;
- collateral/security for relevant products;
- DSCR/LTV for property finance.

Human layer:
- underwriter review;
- relationship manager;
- BDM / credit ops for brokers.

### Important design insight

Allica does not hide manual underwriting. It productizes it:
- digital intake;
- visible stage;
- clear escalation;
- specialist ownership.

That is a materially better operating design than a digital front end feeding an opaque manual back office.

---

## 5. Product-risk segmentation

### Business Loan
- £25,001–£150k;
- unsecured / relatively standardized;
- digital application;
- underwriter review.

### Asset Finance
- up to £2.5m;
- asset-backed;
- published pricing bands;
- specialist relationship.

### Commercial Mortgage
- £150k–£15m;
- up to 80% LTV;
- DSCR rules;
- security required;
- human credit decision.

### Growth Finance
- £1m–£15m;
- revolving/term;
- bespoke asset mix;
- relationship manager.

This is direct evidence for H5: one SME lender runs multiple underwriting factories.

---

## 6. Economics

Official 2025 results:
- lending: £3.7bn;
- deposits: £5.7bn;
- NIM: **4.7%**;
- gross revenue: £371.3m;
- gross profit after risk: £145.3m;
- underlying PBT: £43.7m;
- statutory PBT: £36.9m.

The bank invested £30m strategically in new products/go-to-market while remaining profitable.

This supports a model where:
- deposit funding;
- premium SME spread;
- larger ticket;
- operating leverage

can finance relationship-intensive underwriting.

Source:
https://www.allica.bank/press-releases/record-results-as-number-of-smes-choosing-allica-more-than-doubles-putting-the-uks-only-full-service-digital-bank-for-established-smes-on-course-f-1776178083380

---

## 7. Risk

Public headline results disclose “gross profit after risk” but do not provide a clean SME NPL/CoR metric on the current results page.

Product risk controls are more visible than portfolio quality:
- two years accounts for many products;
- DSCR / LTV;
- security;
- personal/company credit searches;
- underwriter review.

**Risk-outcome evidence: Medium/Low.**

---

## 8. Hypothesis tests

### H2 — speed is segmentation: strongly supported
Lower standardized business loans use a digital workflow; larger growth/property finance is explicitly relationship-led.

### H4 — data substitution: partial
Allica digitizes information flow but does not remove financial documents for many products.

### H5 — SME is several businesses: very strongly supported
Product/risk architecture changes materially by ticket and collateral.

### H3 — funding advantage: supported
Deposits exceed loans and the bank reports strong NIM, but product-level RAROC remains undisclosed.

---

## 9. Strategic implication

The Allica pattern is:

> **Digitize workflow around judgment rather than forcing judgment out of the workflow.**

For larger SME lending, this can improve:
- speed;
- transparency;
- banker productivity;
- broker experience;
- customer certainty

without weakening risk analysis.

---

## 10. Evidence gaps

1. Product-level approval rates.
2. Time-to-decision distribution.
3. SME NPL / charge-off / CoR.
4. Underwriter productivity.
5. Digital vs broker acquisition cost.
6. Business Loan vintage performance.
7. Full client-screen assets.

---

## Sources

- https://www.allica.bank/press-releases/record-results-as-number-of-smes-choosing-allica-more-than-doubles-putting-the-uks-only-full-service-digital-bank-for-established-smes-on-course-f-1776178083380
- https://www.allica.bank/business-loans
- https://www.allica.bank/growth-finance
- https://www.allica.bank/asset-finance
- https://www.allica.bank/commercial-mortgages
- https://www.allica.bank/introducers
