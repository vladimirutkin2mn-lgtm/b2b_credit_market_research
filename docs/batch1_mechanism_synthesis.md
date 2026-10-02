# Batch 1 Synthesis — How Data Changes SME Lending

**Companies:** Nubank, Stone, iwoca, Rabobank, CommBank, Mercado Pago  
**Version:** 2026-10-02  
**Purpose:** test H1, H2, H4 and H6 before scaling deep dives.

---

## Executive answer

**The strongest cross-company pattern is that leading fast SME journeys do not primarily eliminate underwriting — they move underwriting upstream, automate data collection, or constrain the product until the risk problem becomes standardized.**

Across the six cases, the shortest visible journeys occur when the lender already has high-frequency customer data:
- business-account activity;
- acquiring/payment data;
- marketplace sales;
- transaction feeds via Open Banking.

Where that data becomes insufficient — because the ticket grows, collateral enters, the customer is new-to-bank, or the business becomes more complex — financial documents and human judgment return.

### The strategic implication

The useful design question is therefore not:

> “How do we make the SME application shorter?”

It is:

> **“What information can we know before the customer applies, and where does that information stop being sufficient for the exposure?”**

That reframes digital SME lending from a UX project into a **data + risk-segmentation + operating-model project**.

---

# 1. Cross-case evidence matrix

| Player | Core proprietary / machine-readable data | Visible application starts after pre-underwriting? | Public process breakpoint | Human layer | Strong portfolio-risk evidence | Screen evidence |
|---|---|---|---|---|---|---|
| Nubank | Nu Empresas account / relationship signals | **Yes** | Offer availability itself | unclear / exceptions not public | Group only, not SME-specific | Partial |
| Stone | acquiring / daily sales / relationship | **Yes** | Automated desk vs dedicated desk / larger tickets | Dedicated desk | **Yes** | Strong |
| iwoca | Open Banking / transactions / bureau | Partly | **€50k** document breakpoint | increases above breakpoint | Germany-specific weak | Strong |
| Rabobank | own/external transaction data | Partly | **€250k / 5y** no-annual-accounts perimeter | Adviser / complex cases | SME-lane weak | Low/partial |
| CommBank | existing bank/customer information | **Yes for eligible existing customers** | existing vs new customer; secured/larger cases | Specialist | Business-bank strong | Partial |
| Mercado Pago | marketplace / payment / seller behavior | **Yes** | Offer eligibility / product type | largely hidden/not public | Group/regional only | Low |

---

# 2. Finding 1 — The best journey often begins before the customer sees it

## Answer

Nubank, Stone, CommBank and Mercado Pago all show a version of **pre-application underwriting**.

The lender first observes the customer, then decides whether to expose credit.

### Nubank
Capital de Giro appears only after recurring automated analysis of internal and external signals.

### Stone
A pre-approved offer is pushed into the app based on relationship, revenue and other credit signals.

### CommBank
Eligible existing customers can see conditional/pre-approved business-finance offers based on information the bank already holds.

### Mercado Pago
Merchant behavior on the platform produces eligibility; the visible flow starts from a pre-approved offer.

## Mechanism

Ongoing customer activity
→ underwriting data accumulates before credit need
→ eligibility can be refreshed continuously
→ customer enters at offer/configuration stage
→ visible application becomes shorter.

## So what?

Banks should separate two products:

1. **Existing-data credit** — underwriting can happen continuously.
2. **New-to-bank credit** — data must be acquired during application.

Treating them as one journey wastes the incumbent's information advantage.

---

# 3. Finding 2 — “Instant” is usually a bounded risk lane

## Answer

Public evidence does not support the idea that these lenders automate all SME credit equally.

Instead, they define a perimeter.

### iwoca
- up to €50k: transaction data can carry much of the process;
- above €50k: BWA/SuSa enter.

### Rabobank
Annual accounts can be removed only inside a defined perimeter:
- up to €250k;
- max five-year term;
- sufficient transaction history/inflows;
- eligible sectors/structures.

### CommBank
Instant digital experience is strongest for eligible existing customers; new customers and secured/more complex requests involve a specialist.

### Stone
The company explicitly separates automated and dedicated desks, and risk outcomes differ between them.

## Mechanism

Lower complexity / better data / smaller exposure
→ standardized policy
→ automated decision.

Larger exposure / weaker data / bespoke structure
→ more information
→ human judgment
→ longer process.

## So what?

The target architecture should be a **credit ladder**, not a universal straight-through process.

---

# 4. Finding 3 — Data substitution matters more than form simplification

## Answer

The meaningful UX innovation is not fewer form fields by itself.

It is replacing borrower-entered evidence with machine-readable evidence.

### Observed substitutions

| Traditional input | Machine-readable substitute / supplement |
|---|---|
| Bank statements uploaded manually | Open Banking / bank transaction feed |
| Annual accounts for small tickets | cash-flow history |
| Revenue declaration | acquiring / marketplace sales |
| Existing relationship questions | bank/account history already held |
| Repeat-borrower documents | repayment + transaction behavior |

## Examples

- iwoca: Open Banking below its public ticket breakpoint.
- Rabobank: 13 months transactions can replace annual accounts within the defined lane.
- Stone: acquiring sales are embedded into the customer relationship.
- Mercado Pago: platform sales/history create the initial credit file.
- CommBank: existing-customer information is reused.
- Nubank: account usage informs recurring eligibility.

## So what?

A lender seeking better SME UX should prioritize **data integrations and pre-underwriting architecture before front-end redesign**.

A beautiful application that still asks the borrower to recreate data the lender could fetch is not a structurally better model.

---

# 5. Finding 4 — Embedded data improves observability, not immunity from losses

## Answer

Stone is the clearest counter-evidence against a simplistic “more transaction data = lower losses” thesis.

Q2 2026:
- NPL >90: 8.6%;
- cost of risk: 21.5%;
- management linked deterioration to weaker vintages and dedicated-desk cases.

This occurred despite high-frequency merchant transaction data and integrated repayment.

## Mechanism

Data can reduce:
- information lag;
- document burden;
- servicing friction;
- monitoring latency.

But it cannot eliminate:
- poor policy thresholds;
- adverse selection;
- macro deterioration;
- rapid growth effects;
- large-ticket concentration;
- vintage mistakes.

## So what?

Digital underwriting should be judged on **risk-adjusted economics by cohort**, not just decision speed or data richness.

---

# 6. Finding 5 — Incumbents may possess the strongest raw data advantage

## Answer

The first six cases weaken the idea that fintechs inherently have better digital-credit data.

CommBank and Rabobank show that incumbent banks can possess:
- primary transaction accounts;
- long history;
- deposits;
- payments;
- existing identity/KYC;
- collateral relationships.

The challenge is often turning that data into a **separate fast credit lane**.

## Examples

### CommBank
~90% of business loans linked to a transaction account; eligible existing customers can receive instant decisions.

### Rabobank
Own or consented external transaction data can support financing without annual accounts inside the €250k lane.

## So what?

For an incumbent bank, the strategic gap may be less about data availability and more about:
- decision architecture;
- systems integration;
- policy segmentation;
- product ownership;
- legacy process.

---

# 7. Finding 6 — Funding and economics remain a separate dimension

## Answer

The six cases have different funding structures:
- deposit-funded banks/digital banks;
- non-bank specialist funding;
- payments/platform ecosystems.

Fast UX alone says little about profitability.

### Evidence quality

Strongest direct economics/risk evidence in Batch 1:
- Stone;
- CommBank.

Useful but not SME-specific:
- Nubank group;
- Rabobank group;
- Mercado Libre group/regional.

Group profitability but weak Germany-specific risk:
- iwoca.

## So what?

The next economics/risk batch is necessary before drawing conclusions about which operating model produces superior returns.

We must compare:
**price/yield − funding − credit loss − operating cost − capital**.

---

# 8. Archetype map emerging from Batch 1

## Archetype A — Pre-approved ecosystem credit
Examples:
- Nubank
- Stone
- Mercado Pago
- CommBank existing-customer lane

Characteristics:
- relationship exists before loan;
- underwriting runs in background;
- offer is pushed/proactively surfaced;
- low visible document burden.

## Archetype B — Data-connected new-to-lender fintech
Example:
- iwoca

Characteristics:
- no pre-existing relationship required;
- fast data connection replaces documents;
- process intensity increases with ticket.

## Archetype C — Incumbent fast lane + relationship fallback
Examples:
- Rabobank
- CommBank

Characteristics:
- low-complexity route automated;
- larger/complex cases return to adviser/relationship model.

These archetypes are more decision-useful than the generic categories “bank vs fintech”.

---

# 9. Implications for a bank designing SME credit

## A. Build separate existing-customer and new-to-bank journeys

Do not merely prefill the same form.

Existing-customer lending should use:
- transaction history;
- prior KYC;
- deposits;
- payment behavior;
- existing products;
- historical credit performance.

Goal:
move underwriting before explicit application.

## B. Define the automation perimeter explicitly

For each product, set:
- ticket ceiling;
- tenor ceiling;
- minimum data history;
- industry exclusions;
- collateral rules;
- manual-review triggers.

## C. Measure document substitution

Track:
- documents removed;
- fields autofilled;
- external data connected;
- share of decisions without manual review.

## D. Connect UX to risk and economics

Core KPI stack should include:
- application completion;
- decision time;
- booked conversion;
- manual-review rate;
- cost per decision;
- vintage loss;
- repeat borrowing;
- risk-adjusted contribution.

## E. Treat repeat lending as a distinct product

The relationship should get better over time:
- fewer steps;
- better limits;
- faster decision;
- lower underwriting cost;
- ideally better risk discrimination.

---

# 10. What Batch 1 does NOT yet prove

We do not yet have sufficient evidence to conclude:

1. automated lenders have lower losses;
2. fintechs have better economics than banks;
3. existing-customer lending always has lower NPL;
4. fastest journeys have highest conversion;
5. proprietary data creates higher RAROC;
6. one ticket breakpoint is universally optimal.

These remain empirical questions for Batch 2/3.

---

# 11. Next hypotheses to test in Batch 2

Batch 2:
- Funding Circle
- Itaú
- SBI
- UGRO
- Judo
- American Express BLOC

## Primary questions

### Economics
Can non-bank digital lenders overcome funding-cost disadvantage through:
- pricing;
- lower OPEX;
- better risk;
- repeat behavior?

### Incumbent scale
Do Itaú/SBI/Amex show stronger economics where:
- deposits are cheap;
- cross-sell exists;
- current-account data are deep?

### Relationship model
Does Judo demonstrate that high-touch SME lending can still create attractive economics at larger tickets?

### Public risk evidence
Can we link automation/data architecture to actual:
- NPL;
- cost of risk;
- vintages;
- provisions;
- capital?

---

# 12. Boardroom takeaway

**Fast SME credit is not primarily a front-end capability. It is the visible outcome of a deeper architecture: pre-existing data, product segmentation, decision automation, and a controlled boundary where human underwriting re-enters.**

The strongest transferable pattern from Batch 1 is therefore:

> **Move information collection upstream, automate only inside an explicit risk perimeter, and design the handoff to human underwriting rather than pretending it will disappear.**

Confidence: **High on the operating-model pattern; Medium/Low on comparative risk-adjusted economics pending Batch 2.**
