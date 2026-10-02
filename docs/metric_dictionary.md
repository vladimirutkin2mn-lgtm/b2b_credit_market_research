# Metric Dictionary — SME / B2B Lending

Version date: 2026-10-02.

## Purpose

This dictionary is the canonical measurement layer for the project.

Every quantitative claim should map to one canonical metric below and preserve the **source's original definition** alongside the normalized metric name.

The dictionary is designed to prevent false comparisons across:
- countries;
- banks vs fintechs;
- products;
- accounting frameworks;
- borrower segments;
- periods;
- stock vs flow metrics.

## Core rule

For every datapoint store at minimum:

- `metric_id`
- `value`
- `unit`
- `period_start`
- `period_end`
- `geography`
- `borrower_segment`
- `product`
- `source_title`
- `source_url`
- `publication_date`
- `source_definition`
- `denominator`
- `evidence_type`
- `confidence`
- `notes`

A normalized metric never replaces the original source definition.

---

# 1. Market scale and lending volume

## MKT_SME_BUSINESS_COUNT — Number of SMEs / small businesses

Number of enterprises in the source-defined SME or small-business population.

**Unit:** count.

Always retain:
- source definition;
- employer vs nonemployer coverage;
- active/registered/statistical population;
- reference date.

**Do not mix**
registered MSMEs, active tax entities, survey populations and economically active businesses as if they were identical.

---

## MKT_REGISTERED_SME_COUNT — Registered/formalised SME count

Number of businesses registered in a formal SME/MSME registry or administrative programme.

Useful in markets such as India, but it is **not automatically the total economic SME population**.

---

## MKT_LENDER_ARCHETYPE_SHARE_NEW_LENDING — Lender-archetype share of new lending

**Formula**

`new lending from specified lender archetype / total relevant new lending`

Examples:
- challenger/specialist banks;
- large incumbent banks;
- non-bank lenders.

The denominator and lender population must be explicit.

---

## FUNNEL_EXTERNAL_FINANCE_USAGE_RATE — External-finance usage rate

Share of source-defined SMEs currently using or having used an external finance product in the specified reference period.

Do not substitute for:
- application rate;
- financing-need rate;
- debt usage rate.

---

## MKT_LOAN_STOCK_SME — SME outstanding loan stock

**Canonical definition**  
Gross outstanding balance of loans to SMEs at a point in time.

**Formula**  
Direct source value. If derived:

`SME loan stock = total business loan stock × SME share of stock`

**Unit**  
Currency.

**Period type**  
Point-in-time / end-of-period stock.

**Preferred denominator**  
None.

**Common aliases**
- SME loans outstanding
- SME loan book
- outstanding business loans, SMEs
- SME credit stock

**Do not mix with**
- new lending/originations;
- average loan book;
- approved limits;
- committed but undrawn facilities.

**Preferred sources**  
Central banks, regulators, OECD SME Financing Scoreboard, audited lender disclosures.

**Comparability note**  
Check whether overdrafts, credit cards, leasing, factoring, securitised loans and non-performing exposures are included.

---

## MKT_LOAN_STOCK_BUSINESS_TOTAL — Total business loan stock

Gross outstanding loans to non-financial enterprises at a point in time.

**Unit:** Currency.  
**Period type:** Stock.

Use as denominator for SME share only when coverage matches the SME numerator.

---

## MKT_SME_SHARE_STOCK — SME share of business loan stock

**Formula**

`SME outstanding loans / total business outstanding loans`

**Unit:** %.

**Do not mix with**
- share of new lending;
- share of borrower count.

---

## MKT_NEW_LENDING_SME — New SME lending

**Canonical definition**  
Loans to SMEs originated/disbursed during an accounting period.

**Formula**  
Direct source value preferred.

**Unit:** Currency.  
**Period type:** Flow.

**Common aliases**
- new business lending, SMEs
- SME originations
- SME disbursements

**Critical note**  
Sources may define “new lending” as:
- signed contracts;
- newly granted loans;
- amounts actually disbursed;
- new business excluding renewals;
- new business including refinancings.

Retain the source definition.

---

## MKT_NEW_LENDING_BUSINESS_TOTAL — Total new business lending

New business lending to all non-financial enterprises during the period.

**Unit:** Currency.  
**Period type:** Flow.

---

## MKT_SME_SHARE_NEW_LENDING — SME share of new business lending

**Formula**

`new SME lending / total new business lending`

**Unit:** %.

---

## MKT_AVG_LOAN_BOOK — Average loan book

**Preferred formula**

`(opening gross loan balance + closing gross loan balance) / 2`

Use more granular averages if disclosed.

**Use for**
- yield;
- cost of risk;
- charge-off rate;
- ROA-style ratios.

**Do not substitute closing balance when average balance is materially different without labeling approximation.**

---

## MKT_BORROWING_FIRMS — Number of borrowing SMEs

Number of unique SME firms with outstanding borrowing or borrowing during the defined period.

Always distinguish:
- active borrowers at period end;
- borrowers during period;
- approved borrowers;
- applicants.

---

## MKT_AVG_OUTSTANDING_PER_BORROWER

**Formula**

`SME outstanding loan stock / active SME borrowers`

Derived metric. Use only when numerator and borrower count cover the same population and date.

---

## MKT_AVG_ORIGINATION_SIZE

**Formula**

`new lending amount / number of booked loans`

Prefer median if source provides loan-level distributions.

**Do not mix with**
- approved limit;
- requested amount;
- outstanding balance.

---

# 2. Borrower demand and credit funnel

## FUNNEL_FINANCING_NEED_RATE

Share of SMEs reporting a need for external finance during the period.

**Denominator:** relevant SME survey population.

Keep survey population and weighting methodology.

---

## FUNNEL_APPLICATION_RATE

**Formula**

`SMEs applying for credit / relevant SME population`

Possible denominators:
- all surveyed SMEs;
- SMEs needing finance;
- existing bank customers.

Never compare rates with different denominators without normalization.

---

## FUNNEL_APPLICATIONS_COUNT

Number of submitted credit applications during the period.

Track whether one borrower can submit multiple applications.

---

## FUNNEL_REQUESTED_AMOUNT

Total amount requested by applicants.

Do not equate with approved or disbursed amount.

---

## FUNNEL_APPROVAL_RATE

**Canonical formula**

`approved applications / completed credit applications`

But preserve the source's definition.

Variants that must remain distinct:
- fully approved;
- fully + partially approved;
- conditional approval;
- approved by application count;
- approved by requested value.

---

## FUNNEL_FULL_APPROVAL_RATE

`fully approved applications / completed applications`

Keep separate from partial approvals.

---

## FUNNEL_PARTIAL_APPROVAL_RATE

`partially approved applications / completed applications`

---

## FUNNEL_REJECTION_RATE

Preferred demand-side formula:

`rejected applications / completed applications`

If OECD/source defines via requested vs authorised loans, retain that exact definition.

**Do not infer rejection rate as `1 - approval rate` unless categories are exhaustive.**

---

## FUNNEL_WITHDRAWAL_RATE

Applications withdrawn by borrower before final decision / submitted applications.

Useful for detecting process friction.

---

## FUNNEL_BOOKED_CONVERSION

**Formula**

`booked/disbursed loans / submitted applications`

This is not the same as approval rate.

---

## FUNNEL_APPROVAL_TO_BOOK

`booked loans / approved applications`

Captures offer acceptance, documentation and fulfillment leakage.

---

## FUNNEL_DISCOURAGED_BORROWER_RATE

Share of firms needing finance that did not apply because they expected rejection or found conditions unsuitable, according to source survey.

Do not combine different reasons unless source does.

---

## FUNNEL_CREDIT_CONSTRAINT_RATE

Share of credit-seeking / credit-interested firms reporting restrictive lender behavior, difficulty obtaining credit, or another explicitly defined credit constraint.

**Denominator must be preserved.**

Examples of non-equivalent denominators:
- all SMEs;
- SMEs interested in bank credit;
- firms that entered credit negotiations;
- loan applicants.

Do not interpret this as rejection rate unless the source explicitly defines it that way.

---

# 3. Pricing and revenue

## PRICE_BORROWER_NOMINAL_RATE

Contractual nominal interest rate charged to borrower.

**Do not mix with**
- APR/effective annual rate;
- portfolio yield;
- NIM.

---

## PRICE_APR_EFFECTIVE_RATE

Annualized effective cost to borrower including fees when methodology supports it.

Preserve local regulatory methodology.

---

## PRICE_AVG_OUTSTANDING_LOAN_RATE

Average interest rate on the outstanding loan stock for the defined borrower/product population.

Store:
- borrower-size definition;
- product coverage;
- whether the rate includes fixed and variable loans;
- whether fees are excluded/included.

**Do not mix with**
- rate on new lending;
- APR/effective annual borrower cost;
- portfolio yield calculated from accounting interest income.

---

## PRICE_EFFECTIVE_NEW_LENDING_RATE

Average/effective interest rate on newly originated lending as reported by a central bank or lender portfolio.

Store:
- whether weighted by balances or contracts;
- product/borrower population;
- fixed/floating treatment;
- whether fees are included.

**Do not call this APR unless the source explicitly uses APR/effective annual cost methodology.**

---

## PRICE_SPREAD_TO_REFERENCE

**Formula**

`borrower rate - reference rate`

Possible reference:
- policy rate;
- risk-free rate;
- interbank benchmark;
- bank funding benchmark.

Always store the chosen reference.

---

## PRICE_ORIGINATION_FEE_RATE

`origination fee / original principal`

Store one-off vs recurring distinction.

---

## REV_INTEREST_INCOME

Interest income attributable to the relevant loan portfolio/segment.

Do not allocate group-wide interest income to SME lending without evidence.

---

## REV_FEE_INCOME_LENDING

Fees attributable to lending:
- origination;
- servicing;
- commitment;
- late fees;
- draw fees;
- other credit-related fees.

Document accounting treatment.

---

## ECON_GROSS_LOAN_YIELD

**Preferred formula**

`annualized interest income on loan portfolio / average gross loan balance`

If lender reports yield directly, preserve reported method.

**Do not mix with**
- borrower advertised rate;
- NIM;
- risk-adjusted yield.

---

## ECON_NET_INTEREST_INCOME

**Formula**

`interest income - interest expense`

At company/segment level as reported.

---

## ECON_NIM

**Canonical banking formula**

`annualized net interest income / average earning assets`

For bank-level NIM, denominator is average earning assets, not SME loan book.

**Do not use bank-wide NIM as SME-loan spread without explicit caveat.**

---

# 4. Funding economics

## FUND_INTEREST_EXPENSE

Interest expense associated with funding.

May include:
- deposits;
- wholesale funding;
- warehouse lines;
- securitization liabilities.

Scope must be explicit.

---

## FUND_AVG_COST

**Formula**

`annualized funding interest expense / average interest-bearing funding`

Do not mix company-wide funding cost with marginal cost of funding.

---

## FUND_MARGINAL_COST

Current cost of incremental funding available to support new originations.

Often not directly disclosed. If estimated, mark as estimate.

---

## FUND_GROSS_SPREAD

Approximation:

`portfolio gross yield - funding cost`

Only valid when numerator/denominator scope and period are reasonably aligned.

---

## FUND_DEPOSIT_SHARE

`deposit funding / total funding relevant to lender`

Useful for business-model comparison but not a direct measure of funding cost.

---

# 5. Credit quality and risk

## RISK_DPD_1_PLUS

Share of relevant gross exposure with any contractual amount past due.

Source-specific materiality rules must be stored.

---

## RISK_DPD_30_PLUS

**Preferred formula**

`gross exposure ≥30 days past due / gross loan exposure`

Store whether threshold means:
- 30+;
- >30;
- 31–90 bucket;
- obligor-level vs facility-level.

---

## RISK_DPD_60_PLUS

Same logic for ≥60 days past due.

---

## RISK_DPD_90_PLUS

**Preferred formula**

`gross exposure ≥90 days past due / gross loan exposure`

**Critical:** 90+ DPD is not automatically identical to regulatory default or NPL/NPE.

---

## RISK_DEFAULT_RATE_OBLIGOR

**Preferred formula**

`number of obligors entering default during period / performing obligors at start or average eligible population`

Use only when source is borrower/obligor-based.

Basel-style default can include either:
- unlikeliness to pay; or
- material credit obligation past due more than 90 days.

Always retain lender/regulatory definition.

---

## RISK_DEFAULT_RATE_EXPOSURE

Exposure-weighted default incidence.

**Formula depends on source.**

Do not compare directly with obligor-count default rate.

---

## RISK_PD

Probability of default over a specified horizon.

Store:
- horizon;
- through-the-cycle vs point-in-time;
- model vs realized;
- obligor vs facility basis.

---

## RISK_NPL_RATIO

**Preferred formula**

`non-performing loans / gross loans`

But source definition of non-performing must be retained.

**Do not assume**
NPL = 90+ DPD.

Non-performing classification can include “unlikely to pay” even without >90 DPD.

---

## RISK_NPE_RATIO

`non-performing exposures / gross exposures`

Use NPE when source includes exposures beyond loans.

Do not silently map NPE to NPL.

---

## RISK_STAGE2_RATIO

IFRS 9 Stage 2 gross carrying amount / relevant gross carrying amount.

Represents exposures with significant increase in credit risk under IFRS 9, not default.

Do not compare as if equivalent to 30+ DPD.

---

## RISK_STAGE3_RATIO

IFRS 9 Stage 3 gross carrying amount / relevant gross carrying amount.

Credit-impaired accounting classification.

Do not assume identical to regulatory NPL/NPE or default.

---

## RISK_ECL_ALLOWANCE

Balance-sheet allowance for expected credit losses.

Track accounting framework:
- IFRS 9;
- CECL;
- other.

Do not mix allowance stock with impairment expense flow.

---

## RISK_ALLOWANCE_RATIO

`ECL/credit-loss allowance / gross loan exposure`

Denominator must match portfolio scope.

---

## RISK_NPL_COVERAGE

Common formula:

`credit-loss allowance attributable to relevant portfolio / non-performing loans`

Only compare where numerator and denominator scope match.

---

## RISK_PROVISION_EXPENSE

P&L impairment/provision expense during period.

This is a **flow**.

Do not call it realized credit loss.

---

## RISK_COST_OF_RISK

**Preferred formula**

`annualized credit impairment/provision charge / average gross loans`

Possible lender variants:
- provisions / average loans;
- net credit losses / average loans;
- impairment / risk-weighted assets.

Always store reported formula.

**Do not compare CoR until numerator definition is aligned.**

---

## RISK_GROSS_CHARGEOFF

Principal balance written off during period before recoveries.

---

## RISK_RECOVERIES

Cash/accounting recoveries on previously charged-off loans.

---

## RISK_NET_CHARGEOFF

**Formula**

`gross charge-offs - recoveries`

Some reporting systems include adjustments; retain source definition.

---

## RISK_NET_CHARGEOFF_RATE

**Preferred formula**

`annualized net charge-offs / average gross loans`

Do not mix with provision-based cost of risk.

---

## RISK_VINTAGE_CUM_LOSS

Cumulative credit loss for an origination cohort divided by original cohort principal or relevant exposure base.

Always store:
- vintage month/quarter/year;
- months-on-book;
- loss definition;
- recoveries treatment.

---

## RISK_LGD

Loss given default.

`economic/accounting loss after recoveries and collateral / exposure at default`

Store whether modeled or realized.

---

## RISK_EAD

Exposure at default.

For revolving facilities, may include expected future drawings.

---

## RISK_EXPECTED_LOSS

Model concept:

`PD × LGD × EAD`

Over a specified horizon and modeling basis.

Do not equate directly with accounting ECL unless definitions align.

---

# 6. Collateral and guarantees

## COLLATERAL_REQUIRED_RATE

Share of relevant borrowers/loans required to provide collateral.

Store whether measured by borrower survey, applications, or booked loans.

---

## COLLATERAL_LTV

`loan exposure / eligible collateral value`

Store valuation basis and haircut policy where available.

---

## GUARANTEE_COVERAGE_RATE

`guaranteed amount / covered exposure`

For government or third-party guarantees.

---

## GUARANTEED_LOAN_STOCK

Outstanding amount of loans covered by guarantees.

Keep separate from the amount of guarantees outstanding.

---

# 7. Operating model and customer journey

## OPS_TIME_TO_DECISION

Elapsed time from a clearly defined application-complete event to credit decision.

Store:
- start event;
- end event;
- clock vs business time;
- median/mean/pXX;
- advertised vs observed.

**Advertised “decision in X minutes” is not an observed SLA.**

---

## OPS_TIME_TO_CASH

Elapsed time from defined application or approval event to funds available to borrower.

Store exact start point.

Do not equate with time-to-decision.

---

## OPS_STP_RATE

Straight-through-processing rate.

**Preferred formula**

`applications decided without manual credit intervention / eligible applications`

Source definitions often vary.

---

## OPS_MANUAL_REVIEW_RATE

`applications requiring manual credit review / eligible applications`

Not necessarily `1 - STP` if other paths exist.

---

## OPS_ADDITIONAL_INFO_RATE

`applications with at least one additional-information request / submitted applications`

Useful friction/underwriting metric.

---

## UX_STEPS_COUNT

Number of customer-visible steps/screens in a normalized journey scenario.

Must be tied to:
- borrower scenario;
- product;
- channel;
- date observed.

---

## UX_REQUIRED_FIELDS_COUNT

Number of mandatory user-entered fields in the application journey.

Autofilled fields should be tracked separately.

---

## UX_DOCUMENTS_REQUIRED_COUNT

Number of distinct document types required from borrower.

Separate documents manually uploaded from data retrieved via integrations.

---

## UX_DATA_CONNECTIONS_COUNT

Number of external data connections requested:
- open banking;
- accounting;
- tax;
- acquiring;
- marketplace;
- other.

---

## UX_PRICING_TRANSPARENCY

Categorical research metric, not a financial ratio.

Allowed values:
- full pre-application;
- indicative;
- only after application;
- only in contract/offer;
- unknown.

This is descriptive, not a composite score.

---

## UX_SCREEN_COVERAGE_RATE

**Formula**

`key customer-visible stages with screen evidence / key customer-visible stages in reconstructed journey`

Evidence types:
- observed;
- official;
- reported.

Never use generated/recreated screens as evidence.

---

# 8. Operating cost and unit economics

## COST_ACQUISITION

Customer/borrower acquisition cost attributable to lending.

If allocated, show method.

---

## COST_UNDERWRITING

Direct underwriting/KYB/KYC/data/manual-review cost per application or booked loan.

Often estimated; label accordingly.

---

## COST_SERVICING

Ongoing servicing cost per active borrower/loan.

---

## COST_COLLECTIONS

Collections and recoveries operating cost attributable to delinquent/defaulted accounts.

---

## ECON_COST_TO_INCOME

`operating expenses / operating income`

Usually segment/company level.

Do not treat bank-wide cost-to-income as SME lending cost-to-serve.

---

## ECON_CONTRIBUTION_PRE_CAPITAL

Research metric:

`interest + lending fees - funding cost - credit cost - attributable operating cost`

Only calculate if allocations are defensible.

---

## ECON_RISK_ADJ_CONTRIBUTION

Research metric:

`pre-capital contribution - capital charge`

All assumptions must be shown.

---

## ECON_ROA_LOANS

Approximation:

`annualized lending net contribution / average loan assets`

Do not confuse with company ROA.

---

## ECON_RAROC

General research form:

`risk-adjusted return / allocated economic or regulatory capital`

RAROC implementations vary materially by institution.

Always record:
- numerator;
- capital denominator;
- expected loss treatment;
- tax treatment;
- hurdle rate if used.

Do not compare reported RAROC numbers without methodology alignment.

---

## ECON_CAC_PAYBACK

Time required for cumulative risk-adjusted contribution to recover acquisition/onboarding cost.

Only derive if cohort economics are observable.

---

# 9. Capital and balance-sheet intensity

## CAP_RWA

Risk-weighted assets attributable to relevant portfolio/segment.

---

## CAP_RWA_DENSITY

`RWA / exposure measure`

Specify exposure denominator:
- gross loans;
- EAD;
- assets.

---

## CAP_CET1_ALLOCATED

CET1 or economic capital allocated to the lending segment.

Often unavailable publicly.

---

## CAP_RETURN_ON_ALLOCATED_CAPITAL

`segment earnings / allocated capital`

Do not label RAROC unless risk-adjustment methodology supports it.

---

# 10. Portfolio mix

## MIX_SECURED_SHARE

`secured loan exposure / total relevant loan exposure`

---

## MIX_UNSECURED_SHARE

`unsecured loan exposure / total relevant loan exposure`

---

## MIX_REVOLVING_SHARE

`revolving exposure / total relevant exposure`

---

## MIX_SHORT_TERM_SHARE

Preferred OECD-style concept:
share of SME loans with original maturity ≤1 year.

Store whether measure is stock or new lending.

---

## MIX_EXISTING_CUSTOMER_SHARE

Share of originations/booked loans to existing relationship customers.

Define “existing” threshold if disclosed.

---

## MIX_REPEAT_BORROWER_SHARE

Share of booked loans/borrowers with prior borrowing history at lender.

Not necessarily equal to existing current-account customer.

---

# 11. Growth metrics

## GROWTH_YOY_STOCK

`current period-end stock / prior-year comparable stock - 1`

Check acquisitions, FX and reclassifications.

---

## GROWTH_YOY_ORIGINATIONS

`current-period new lending / prior comparable period new lending - 1`

---

## GROWTH_CAGR

`(ending value / beginning value)^(1/years) - 1`

Use only comparable series.

---

## GROWTH_REAL

Nominal growth adjusted for relevant inflation index.

State chosen deflator.

---

# 12. Borrower and product context fields

These are dimensions, not metrics, but are mandatory for normalization where available.

## DIM_BORROWER_REVENUE
Annual revenue/turnover band.

## DIM_EMPLOYEES
Employee-count band.

## DIM_FIRM_AGE
Years since incorporation/trading start.

## DIM_EXISTING_RELATIONSHIP
Existing / new-to-lender.

## DIM_PRODUCT
Canonical product taxonomy.

## DIM_SECURITY
Secured / unsecured / partially secured / guaranteed.

## DIM_TICKET
Requested / approved / originated amount band.

## DIM_TERM
Original contractual term.

## DIM_INDUSTRY
Industry classification.

---

# 13. Metrics that must never be silently substituted

| Metric A | Metric B | Why not interchangeable |
|---|---|---|
| Loan stock | New lending | Stock vs period flow |
| New lending | Approval amount | Approval may never be booked |
| Approval rate | Booked conversion | Approved borrowers may not accept/complete |
| Borrower rate | Portfolio yield | Offer pricing vs realized portfolio economics |
| Portfolio yield | NIM | NIM includes funding and broader earning assets |
| Provision expense | Charge-offs | Expected/accounting loss vs realized write-off |
| Cost of risk | Net charge-off rate | Different numerator definitions |
| 90+ DPD | Default | Default can include unlikely-to-pay |
| Default | NPL/NPE | Regulatory/accounting classifications differ |
| Stage 2 | 30+ DPD | SICR is broader than delinquency |
| Stage 3 | NPL | Often overlaps but definitions/framework differ |
| NPL ratio | Vintage loss | Stock quality vs cohort cumulative loss |
| Time to decision | Time to cash | Credit decision vs fulfillment |
| “Up to” loan amount | Average loan size | Product ceiling vs observed book |
| Existing customer | Repeat borrower | Relationship may exist without prior loan |

---

# 14. Metric acceptance rules

A metric is **comparison-ready** only when:

1. numerator is known;
2. denominator is known;
3. period is known;
4. borrower population is known;
5. product scope is known;
6. geography is known;
7. accounting/regulatory definition is known for risk metrics;
8. stock vs flow is explicit;
9. source definition is stored;
10. material caveats are documented.

If any of 1–4 is missing, default status is **not directly comparable**.

---

# 15. Source hierarchy by metric family

## Market volumes
1. Central bank / regulator
2. OECD
3. Government statistical source
4. Audited lender disclosures
5. Reputable industry datasets

## Demand / application funnel
1. Official borrower surveys
2. Regulator/bank surveys
3. Lender disclosure
4. Reputable third-party research

## Pricing
1. Contract/tariff/product terms
2. Central-bank lending-rate statistics
3. Lender disclosures
4. Borrower surveys

## Risk
1. Regulatory filings / Pillar 3
2. Audited annual report
3. Regulator system statistics
4. Investor materials
5. Management commentary

## Customer journey / operations
1. Direct observed walkthrough + screenshots
2. Official application/help/product screens
3. Official demos/videos
4. Lender-stated SLAs
5. User-reported evidence

---

# 16. Primary methodological anchors

## OECD Financing SMEs and Entrepreneurs 2026
Use for:
- outstanding SME loans as stock;
- new SME lending as flow;
- SME share of business loans;
- short-/long-term loans;
- interest rates;
- collateral;
- NPL indicators;
- demand-side finance indicators.

OECD explicitly notes that national definitions and product coverage differ, so country notes must be preserved.

## Basel Framework
Use as an anchor for default terminology. Basel default includes either:
- unlikeliness to pay in full without realization of security; or
- more than 90 days past due on a material credit obligation.

This is an anchor, not proof that every public lender metric uses Basel default.

## EBA / CRR reporting
Use for European non-performing/past-due concepts and materiality context. A non-performing exposure can arise through >90 days material past due or unlikely-to-pay criteria.

## FDIC / bank reporting
Use for banking profitability concepts such as NIM, which is based on net interest income relative to average earning assets.

## Federal Reserve reporting
Useful for explicit charge-off/recovery definitions and US banking credit metrics.

---

# 17. Working policy for missing metrics

Use one of:

- **Reported**
- **Calculated**
- **Estimated**
- **Proxy**
- **Unknown**

Never convert Unknown to zero.

Never calculate a missing metric if required denominator/scope cannot be reconciled.

---

# 18. Next extension

After the first 3–5 country and lender data pulls, revisit this dictionary and add:

- source-specific mappings;
- country-specific risk definitions;
- IFRS 9 vs CECL mapping notes;
- product-level utilization metrics for revolving lines;
- collections/restructuring metrics;
- fraud-loss metrics if public data proves material.
