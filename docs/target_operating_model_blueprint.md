# Target Operating Model Blueprint — SME Lending

**Version:** 2026-10-02  
**Purpose:** convert the market research into a generic design blueprint for a scaled incumbent / transaction bank.

> This is a **default architecture**, not a recommendation for a specific bank.
>
> Priorities should be re-scored using internal data on customer base, current-account penetration, loss curves, approval funnel, OPEX, funding and capital.

---

# Executive answer

The research supports a target model with:

**one common intelligence layer + multiple credit factories + one economics framework**

rather than one universal SME loan process.

The design principle is:

> **Use the richest data available before asking the customer for anything; automate only inside an explicit risk perimeter; keep human judgment where ticket/complexity can pay for it; manage every lane on risk-adjusted contribution.**

A scaled bank should therefore separate at least five factories:

1. **Existing-customer pre-approved credit**
2. **New-to-bank digital cash-flow credit**
3. **Guarantee-backed credit**
4. **Medium / upper-SME relationship credit**
5. **Receivables / asset-backed credit**

Embedded merchant lending can be a sixth factory where the bank owns or partners for acquiring / marketplace data.

---

# 1. Common intelligence layer

The factories should share common capabilities rather than recreate them.

## 1.1 Customer / identity layer

Core:
- business identity / KYB;
- owners / UBOs;
- directors / authorized signers;
- KYC;
- legal structure;
- registry;
- sanctions / AML;
- fraud/device identity;
- consent.

### Design principle

**Identity is collected once and reused.**

Repeat borrowing should not trigger redundant KYB unless:
- data expired;
- ownership changed;
- policy requires refresh.

---

## 1.2 Financial data layer

Potential sources:
- own-account transactions;
- Open Banking;
- accounting feeds;
- tax / e-invoice;
- acquiring / merchant sales;
- card/payments;
- bureau;
- existing deposits;
- existing lending / repayment;
- invoices / receivables;
- collateral / registry;
- guarantee-program data.

### Design principle

Use a hierarchy:

**owned machine-readable data  
→ consented external machine-readable data  
→ structured documents  
→ manual borrower input**

The borrower should not re-enter data already available reliably.

---

## 1.3 Feature / signal layer

Reusable signals:
- inflow stability;
- average balance;
- cash-flow volatility;
- seasonality;
- concentration;
- payment returns;
- tax-sales consistency;
- invoice aging;
- bureau behavior;
- prior internal repayment;
- days past due;
- limit utilization;
- merchant/refund/chargeback behavior;
- liquidity buffer.

### Design principle

The same raw data can feed different policies by factory.

A €30k cash-flow line and a €3m relationship loan should not use identical weights/cutoffs merely because they share a data lake.

---

## 1.4 Decisioning layer

Shared capabilities:
- eligibility rules;
- scorecards / ML;
- affordability;
- fraud;
- pricing;
- limit assignment;
- collateral / guarantee logic;
- decision explanations;
- exception routing;
- credit authority.

### Decision architecture

Cases should be explicitly routed to:

1. **straight-through approval**
2. **automated + analyst exception**
3. **underwriter / RM decision**
4. **specialist / committee**

The routing policy is part of the product.

---

## 1.5 Credit orchestration layer

One workflow should coordinate:
- application state;
- outstanding data;
- underwriting;
- exception requests;
- offer;
- conditions precedent;
- guarantee;
- collateral;
- documents;
- signing;
- funding;
- servicing.

### Design principle

A digital front end should never feed an invisible manual queue.

The customer should see:
- what is complete;
- what remains;
- who owns the case;
- expected next step.

---

# 2. Factory A — Existing-customer pre-approved credit

## Target customer

- existing SME current-account customer;
- sufficient transaction history;
- simple ownership;
- small / medium working-capital need;
- no complex collateral.

## Reference mechanisms

Nubank, CommBank, Amex BLOC, SBI PABL, Stone, Square, Mercado Pago.

## Customer journey

**continuous monitoring  
→ eligibility / dynamic limit  
→ proactive offer  
→ amount / term selection  
→ price disclosure  
→ acceptance  
→ instant / near-instant funding  
→ continuous monitoring  
→ repeat offer**

## Data

Primary:
- own-account transactions;
- prior repayment;
- deposits;
- acquiring / payments if available;
- bureau;
- customer history.

Secondary:
- tax/accounting if exposure requires.

## Decision model

Mostly:
- continuous pre-underwriting;
- final fraud / policy checks at draw.

## Human role

Exception only.

## Economics thesis

Potentially:
- lowest CAC;
- lowest visible underwriting cost;
- highest repeat potential;
- highest cross-sell value.

## Key risks

- stale limits;
- model drift;
- limit creep;
- deteriorating customer behavior;
- selection bias in comparing with open-market lending.

## Core KPI tree

- eligible customer penetration;
- offer rate;
- offer → accept;
- draw utilization;
- decision time;
- funding time;
- manual-review rate;
- vintage loss;
- repeat draw rate;
- risk-adjusted contribution per relationship.

## Best evidence

CommBank existing-vs-new journey; Amex dynamic line; Nubank recurring eligibility; Stone/Square/Mercado Pago transaction-led offers.

---

# 3. Factory B — New-to-bank digital cash-flow credit

## Target customer

- established small business;
- no rich prior bank relationship;
- unsecured / lightly secured;
- working-capital need;
- machine-readable cash-flow data available.

## Reference mechanisms

iwoca, Floryn, Funding Circle, Konfío, Rabobank external-account route.

## Customer journey

**eligibility  
→ connect bank/tax/accounting data  
→ automated analysis  
→ documents only if required  
→ personalized offer  
→ acceptance  
→ funding**

## Data

Country-dependent:
- Open Banking;
- tax / e-invoice;
- accounting;
- bureau;
- registry.

## Decision model

- STP inside defined perimeter;
- analyst exceptions;
- richer file above ticket threshold.

## Explicit perimeter

Policy should define:
- max ticket;
- max tenor;
- minimum history;
- legal form;
- industry exclusions;
- volatility/concentration thresholds;
- collateral triggers.

## Human role

Exceptions + higher-ticket escalation.

## Economics thesis

Customer acquisition cost is structurally higher than Factory A.

Value must come from:
- scalable digital acquisition;
- document substitution;
- low underwriting OPEX;
- risk pricing.

## Core KPI tree

- acquisition CAC;
- eligibility conversion;
- data-connection completion;
- document-request rate;
- STP rate;
- exception rate;
- decision time;
- booked conversion;
- cost per booked loan;
- first-payment default;
- 30/90+ delinquency;
- risk-adjusted contribution.

---

# 4. Factory C — Guarantee-backed SME credit

## Target customer

- economically viable business;
- ordinary bank underwriting passes;
- collateral / uncovered-risk constraints matter;
- program eligibility exists.

## Reference mechanisms

Itaú FGI/Pronampe/ProCred, SBI guarantee programs, Stone government-backed lines, UK GGS.

## Customer journey

**program eligibility / revenue authorization  
→ bank eligibility  
→ guarantee check  
→ amount / term simulation  
→ credit decision  
→ guarantee registration  
→ contract  
→ funding**

## Data

- bank relationship;
- tax / revenue;
- government eligibility;
- bureau;
- ordinary underwriting inputs.

## Decision model

Bank decision and guarantee decision should be operationally integrated where possible.

## Economics thesis

Guarantee may:
- broaden approval;
- reduce uncovered expected loss;
- reduce collateral need;
- alter provisioning / capital.

## Core KPI tree

- eligible base;
- approval with guarantee;
- incremental approval vs ordinary policy;
- guarantee coverage;
- guarantee fee;
- claim success;
- uncovered loss;
- RWA / capital effect;
- risk-adjusted contribution.

## Critical principle

Do not compare guaranteed and ordinary unsecured products as one book.

---

# 5. Factory D — Medium / upper-SME relationship credit

## Target customer

- larger ticket;
- established business;
- multiple needs;
- collateral / structure / covenant complexity;
- economic relationship sufficient to support banker time.

## Reference mechanisms

Judo, Allica, Commerzbank, SBI larger-SME lane, Rabobank larger cases.

## Customer journey

**digital preparation  
→ financial / transaction package  
→ named banker / underwriter  
→ structured discussion  
→ credit decision  
→ conditions / collateral / legal  
→ signing / funding  
→ ongoing relationship**

## Data

- financial statements;
- management accounts;
- transaction history;
- collateral;
- bureau;
- sector;
- projections;
- group structure.

## Decision model

Human judgment is explicit.

The key design variables are:
- delegated authority;
- number of handoffs;
- information quality;
- turnaround;
- accountability.

## Economics thesis

Larger ticket and relationship margin can justify higher underwriting OPEX.

## Core KPI tree

- time to complete credit package;
- handoffs per case;
- underwriter / RM touches;
- time to decision;
- approval;
- margin / fee;
- banker productivity;
- loss / specific impairment;
- RAROC;
- relationship revenue.

## Critical principle

Automation target:
**administration, spreading, checks, workflow**

not necessarily:
**the final judgment**.

---

# 6. Factory E — Receivables / asset-backed credit

## Target customer

- B2B invoicing;
- working-capital gap;
- verifiable receivables or identifiable assets.

## Reference mechanisms

Bibby invoice finance; specialist asset finance products at Allica and banks.

## Customer journey

For factoring:
**facility setup  
→ invoice / ledger ingestion  
→ availability calculation  
→ draw / advance  
→ debtor collection  
→ reconciliation  
→ repeat**

## Data

- invoice ledger;
- debtor;
- dilution;
- concentration;
- disputes;
- aging;
- payment history;
- asset values where applicable.

## Decision model

Specialist credit factory.

## Economics thesis

Revenue can combine:
- financing spread;
- service fees;
- collections / credit-control fees;
- bad-debt protection.

## Core KPI tree

- onboarding time;
- invoice auto-ingestion;
- advance rate;
- utilization;
- dilution;
- debtor concentration;
- fraud;
- time from invoice to cash;
- cost per financed invoice;
- debtor loss;
- client retention.

---

# 7. Optional Factory F — Embedded merchant credit

## When it is relevant

Only if bank/platform has:
- acquiring;
- merchant POS;
- marketplace;
- embedded software distribution;
- high-frequency merchant sales.

## Reference mechanisms

Stone, Square, Mercado Pago, UGRO.

## Customer journey

**merchant activity  
→ prequalification  
→ offer in operating platform  
→ configure  
→ accept  
→ fund  
→ repay from sales / account**

## Key advantage

The same transaction stream can support:
- underwriting;
- monitoring;
- repayment.

## Key limitation

Without high-frequency merchant data, this model is not simply replicable by copying the UI.

---

# 8. Opportunity map for a generic incumbent bank

This is a **default sequencing**, assuming:
- meaningful SME current-account base;
- conventional bank balance sheet;
- existing RM / underwriting organization;
- no evidence yet on internal economics.

| Opportunity | Strategic impact | Typical feasibility | Evidence confidence | Default sequence |
|---|---|---|---|---|
| Existing-customer continuous pre-underwriting | High | High/Medium | High | **1** |
| Machine-readable transaction / tax / accounting data | High | Medium | High | **1** |
| Explicit automation / escalation perimeter | High | High | High | **1** |
| Repeat dynamic-limit / top-up loop | High | Medium | Medium/High | **2** |
| Digital status / case orchestration | Medium/High | High | High | **2** |
| Empowered RM/underwriter fast lane | High for larger SME | Medium | High | **2** |
| Digitized guarantee-backed lane | Medium/High | Medium | Medium/High | **3** |
| Product-specific funding / asset distribution | High where relevant | Low/Medium | High | **3** |
| Receivables specialist factory | Segment-specific High | Low/Medium | High | **4** |
| Embedded merchant credit | High only with payments data | Context-specific | High | **4 / conditional** |

---

# 9. Why the default sequence starts with existing customers

The research repeatedly shows that incumbents already own data that fintechs must acquire.

The highest-value early question is therefore:

> **How much of SME underwriting can happen before an existing customer asks for credit?**

This can unlock value without requiring:
- a new acquisition engine;
- a new funding model;
- a new legal entity.

It does require:
- data engineering;
- risk policy;
- digital offer delivery;
- governance.

---

# 10. 18–24 month generic capability roadmap

## Horizon 0 — Measure before rebuilding

Establish one baseline by lane:
- applications;
- approvals;
- time to decision;
- time to cash;
- document count;
- manual touches;
- cost per decision / booked loan;
- yield;
- credit loss;
- capital;
- repeat rate.

Without this, automation cannot be economically evaluated.

---

## Horizon 1 — Existing-customer fast lane

Build:
- transaction-derived eligibility;
- dynamic pre-approved limit;
- low-friction offer;
- digital contract;
- instant account funding where feasible.

Start with a bounded:
- ticket;
- tenor;
- customer-vintage;
- industry set.

Run champion/challenger risk monitoring.

---

## Horizon 2 — Data-connected new-to-bank lane

Add:
- Open Banking / accounting / tax connections;
- document extraction;
- automated affordability;
- clear exception routing.

Use documents as escalation, not default.

---

## Horizon 3 — Repeat / servicing loop

Add:
- dynamic limit refresh;
- reduced-friction redraw;
- top-up;
- early repayment;
- covenant/behavior monitoring;
- proactive distress support.

---

## Horizon 4 — Relationship workflow redesign

For larger SME:
- prefill/spread data;
- standard credit pack;
- single case owner;
- delegated authority;
- digital conditions tracking;
- customer-visible status.

---

## Horizon 5 — Specialized economics

Where strategic:
- guarantee-backed lane;
- receivables;
- asset finance;
- investor distribution / securitisation.

---

# 11. Governance model

## Product owns
- customer journey;
- conversion;
- offer presentation;
- servicing.

## Risk owns
- policy;
- models;
- limits;
- exceptions;
- monitoring;
- loss appetite.

## Finance / Treasury owns
- funding;
- transfer pricing;
- capital;
- RAROC framework.

## Operations owns
- KYB;
- document exceptions;
- fulfillment;
- servicing operations.

## Data / Technology owns
- reusable data products;
- decision services;
- APIs;
- auditability.

## Critical rule

No team should optimize its metric in isolation.

Examples:
- Product should not optimize approval speed without loss.
- Risk should not optimize NPL without growth/price.
- Treasury should not optimize funding cost while creating product mismatch.

---

# 12. Management KPI architecture

Top-level:

## Growth
- eligible base;
- application;
- approval;
- booking;
- utilization;
- repeat.

## Customer
- completion;
- decision time;
- time to cash;
- manual steps;
- document burden;
- support contacts.

## Risk
- FPD;
- DPD;
- default/NPL;
- ECL;
- vintage loss;
- recoveries.

## Economics
- yield/fees;
- funding;
- credit cost;
- acquisition;
- underwriting OPEX;
- servicing OPEX;
- capital;
- risk-adjusted contribution.

## Operating model
- STP rate;
- exception rate;
- RM/underwriter touches;
- decision authority;
- data-connection rate;
- auto-ingestion rate.

---

# 13. What internal data are required to tailor this blueprint

The next step for a specific bank should request:

1. SME customer counts by revenue / legal form / tenure.
2. Current-account penetration and transaction-history depth.
3. Credit stock / origination by ticket/product.
4. Approval and decline reasons.
5. Funnel conversion by channel.
6. Decision / funding times.
7. Manual touch / document counts.
8. Cost-to-serve / underwriting FTE.
9. Vintage loss by product/channel/customer relationship.
10. Yield / transfer-pricing / capital by product.
11. Repeat borrowing / top-up behavior.
12. Guarantee utilization.
13. Acquiring / tax / accounting data availability.

Only with this can the default sequence be converted into a bank-specific business case.

---

# Final target-state principle

A strong SME bank should feel simple to the customer because the complexity sits backstage.

The target operating model is:

> **one customer identity  
> + one reusable data layer  
> + one decision / orchestration platform  
> + multiple risk-specific credit factories  
> + one risk-adjusted economics framework**

That architecture is the most consistent pattern across the 18 deep dives.
