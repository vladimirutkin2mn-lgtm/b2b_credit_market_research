# Internal Bank Data Request — SME Lending

**Purpose:** convert the market-derived target operating model into a bank-specific opportunity sizing and business case.

This request is intentionally structured around **credit factories**, not organizational departments.

---

# 1. Minimum viable extract

If only one extract can be produced, provide loan/application-level records with:

## Customer
- anonymized customer_id
- legal form
- industry
- geography
- annual revenue band
- employee band if available
- business age
- existing-vs-new-to-bank at application
- current-account tenure
- acquiring relationship flag
- accounting/tax data connection flags

## Application
- application_id
- application date/time
- product
- requested amount
- requested tenor
- purpose
- channel
- guarantee-program flag
- collateral flag/type
- pre-approved flag
- approval / decline
- decline reason
- approved amount
- offered rate / fee
- acceptance
- booking date/time
- funding date/time

## Process
- STP flag
- manual review flag
- number of manual touches
- number of document requests
- documents requested
- underwriter / RM touch flags
- exception reason
- decision timestamp
- contract timestamp
- funding timestamp

## Risk outcome
- origination cohort
- PD / risk grade
- 30 DPD date
- 60 DPD date
- 90 DPD date
- default date / definition
- charge-off
- recovery
- ECL / provision
- guarantee recovery if applicable

## Economics
- average balance / utilization
- interest income
- fee income
- FTP / funding charge
- credit loss / provision charge
- acquisition cost if available
- underwriting / operations cost allocation
- servicing / collections cost
- RWA / capital allocation
- cross-sell / deposit contribution if available

## Repeat
- prior loan count
- prior repayment behavior
- subsequent loan/draw date
- repeat amount
- limit changes

---

# 2. Additional customer-account data

For existing-customer pre-underwriting:

Monthly or daily:
- inflows;
- outflows;
- average balance;
- low balance days;
- returned payments;
- overdraft usage;
- number/value of incoming counterparties;
- customer concentration;
- seasonality;
- acquiring sales;
- refund/chargeback rate;
- payroll/tax payments;
- existing debt service.

Prefer raw or reusable derived features, subject to privacy/governance constraints.

---

# 3. Funnel dataset

Monthly by factory/product/channel:

- visitors / leads;
- eligibility checks;
- started applications;
- completed applications;
- data connection completed;
- document request;
- credit decision;
- approved;
- accepted;
- booked;
- funded;
- repeat.

Also provide:
- median / p75 / p90 time between each stage.

This separates:
**conversion problem** from **process-time problem**.

---

# 4. Operations dataset

By product/month:

- applications per credit FTE;
- booked loans per credit FTE;
- underwriting minutes/hours per case;
- operations minutes/hours;
- KYB time;
- document-processing time;
- exception rate;
- rework rate;
- support contacts;
- collections contacts.

If task-level time is unavailable:
- FTE;
- workload;
- applications;
- bookings

can be used for top-down cost estimates.

---

# 5. Risk dataset

At minimum:

**product × cohort × existing/new × decision model × ticket band**

Provide:
- origination;
- exposure;
- approval;
- FPD;
- 30/60/90 DPD;
- default;
- charge-off;
- recovery;
- ECL;
- realized loss.

Optional/high value:
- model score;
- override;
- underwriter decision;
- collateral;
- guarantee;
- cure.

This is needed to test whether automation or relationship data improve risk **after controlling for selection**.

---

# 6. Economics dataset

By product/factory and month/quarter:

## Revenue
- interest income;
- fee income;
- unused line fee;
- interchange / payments revenue attributed to relationship if applicable.

## Funding
- FTP;
- liquidity premium;
- hedge cost if relevant.

## Risk
- expected loss;
- provision;
- realized loss;
- recovery.

## OPEX
- acquisition;
- underwriting;
- KYB;
- operations;
- servicing;
- collections.

## Capital
- RWA;
- regulatory capital;
- economic capital;
- capital charge methodology.

---

# 7. Guarantee dataset

For guaranteed loans:

- scheme;
- guarantee percentage;
- guaranteed amount;
- fee;
- registration date;
- claim conditions;
- claim submission;
- claim approved/rejected;
- recovery amount;
- claim TAT;
- RWA/capital treatment.

Need a comparable non-guaranteed control group.

---

# 8. Data-availability inventory

For each source:

| Data source | Available? | Historical depth | Refresh | Consent needed | Usable in decision? | Current products |
|---|---|---|---|---|---|
| own transactions | | | | | | |
| Open Banking | | | | | | |
| acquiring | | | | | | |
| bureau | | | | | | |
| tax | | | | | | |
| accounting | | | | | | |
| invoices | | | | | | |
| registry | | | | | | |
| collateral | | | | | | |

---

# 9. Required definition sheet

For every extract state:

- default definition;
- NPL/DPD definition;
- write-off rule;
- ECL basis;
- customer segment definition;
- product definition;
- origination vs booking date;
- approval denominator;
- cost allocation method;
- FTP method;
- capital method.

No analysis should begin until definitions are explicit.

---

# 10. Privacy / security

The research does **not** require names, tax IDs, account numbers, phone numbers or addresses.

Use:
- anonymized customer IDs;
- masked product identifiers where needed;
- secure internal environment for raw transaction data.

The minimum principle is:
**use only data required to answer the economic/risk question.**

---

# 11. Preferred history

Ideal:
- 36 months applications / originations;
- 24+ months mature risk outcomes.

Minimum useful:
- 18–24 months for funnel/process;
- enough seasoning for risk cohorts.

Where product changed:
preserve version / policy dates.

---

# 12. Output enabled by this data

With this dataset we can build:

1. existing vs new customer economics;
2. automated vs manual cost/risk comparison;
3. ticket-breakpoint optimization;
4. repeat-loan LTV;
5. guarantee-adjusted RAROC;
6. data-connection value;
7. RM / underwriter productivity;
8. opportunity sizing by credit factory;
9. prioritized roadmap;
10. bank-specific target KPI levels.
