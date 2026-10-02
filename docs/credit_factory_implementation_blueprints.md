# Credit Factory Implementation Blueprints

**Version:** 2026-10-02  
**Purpose:** translate the target operating model into implementable building blocks.

The guiding rule is:

> **Build shared capabilities once; configure credit-specific policy and journey by factory.**

---

# 1. Shared platform — capabilities that should not be rebuilt per product

## 1.1 Customer identity / KYB service

### Responsibilities
- legal-entity lookup;
- owners / UBOs;
- directors / signers;
- sanctions / AML;
- KYC/KYB status;
- document validity;
- consent status;
- relationship tenure.

### Outputs
- customer identity object;
- KYB status;
- authorized signer;
- missing/expired checks.

### Required properties
- reusable across products;
- timestamped;
- auditable;
- refreshable without customer re-entry.

---

## 1.2 Data acquisition service

### Connectors
- own-account transactions;
- Open Banking;
- bureau;
- tax / e-invoice;
- accounting;
- acquiring;
- invoices;
- collateral/registry;
- guarantee-program data.

### Responsibilities
- consent;
- source authentication;
- ingestion;
- normalization;
- freshness;
- quality flags.

### Output
One normalized evidence layer with:
- source;
- timestamp;
- coverage period;
- confidence;
- errors.

---

## 1.3 Financial feature service

Reusable derived signals:
- turnover;
- inflow stability;
- volatility;
- seasonality;
- liquidity buffer;
- customer concentration;
- supplier concentration;
- payroll/tax regularity;
- debt-service burden;
- utilization;
- returns/chargebacks;
- invoice aging;
- prior repayment behavior.

### Critical requirement
Feature definitions must be versioned.

---

## 1.4 Decision service

Configurable modules:
- eligibility;
- fraud;
- score;
- affordability;
- limit;
- tenor;
- pricing;
- guarantee;
- collateral;
- escalation;
- authority.

### Output
- approve;
- decline;
- refer;
- conditions;
- limit;
- term;
- price;
- reason codes;
- next decision owner.

---

## 1.5 Credit orchestration

State machine:

**started  
→ data pending  
→ data complete  
→ credit review  
→ offer  
→ conditions  
→ signed  
→ funded  
→ servicing  
→ closed/defaulted**

Every state should have:
- owner;
- timestamp;
- customer-visible status;
- SLA;
- outstanding actions.

---

## 1.6 Pricing / economics service

At decision time, calculate:
- customer price;
- FTP/funding charge;
- expected loss;
- OPEX estimate;
- capital;
- expected contribution.

Not every product needs real-time RAROC to launch, but economics must be available at portfolio/factory level.

---

## 1.7 Monitoring / limit service

Inputs:
- account behavior;
- repayment;
- bureau;
- tax/accounting refresh;
- alerts.

Outputs:
- limit refresh;
- hold/freeze;
- top-up eligibility;
- collections trigger;
- RM alert.

---

# 2. Factory A — Existing-customer pre-approved credit

## MVP scope

Target:
- existing SME current-account customers;
- simple ownership;
- established relationship;
- bounded ticket/tenor.

### Minimum capabilities

Must-have:
- customer/KYB reuse;
- transaction feature engine;
- bureau refresh;
- limit model;
- proactive offer;
- price/term configuration;
- digital acceptance;
- instant internal account disbursement;
- monitoring;
- reason/eligibility logging.

Nice-to-have:
- acquiring data;
- tax/accounting overlay;
- dynamic repricing;
- proactive top-up.

## Decision logic

### Pre-underwriting cycle
Daily/weekly/monthly:
1. refresh customer status;
2. calculate transaction signals;
3. check negative events;
4. calculate risk;
5. calculate affordability;
6. assign max limit/term;
7. price;
8. publish or suppress offer.

### Draw-time checks
- KYB valid;
- no new delinquency;
- fraud/device;
- account active;
- limit still valid.

## Front-end screens

1. offer card;
2. amount/term;
3. total cost / repayment;
4. consent/declaration;
5. signing/authentication;
6. funding confirmation;
7. servicing/repayment;
8. repeat/top-up.

## Human workflow

Only:
- exceptions;
- fraud/manual validation;
- edge cases.

## Required controls

- offer expiry;
- negative-event suppression;
- limit-change policy;
- adverse-action / reason-code requirements where applicable;
- champion/challenger monitoring.

## MVP success test

- material application-effort reduction;
- high automated completion;
- no unacceptable loss deterioration;
- positive incremental contribution.

---

# 3. Factory B — New-to-bank digital cash-flow credit

## MVP scope

Target:
- established SME;
- machine-readable external cash flow;
- simple ownership;
- unsecured / lightly secured;
- bounded ticket.

## Minimum capabilities

- business identity onboarding;
- Open Banking or tax/accounting connector;
- bureau;
- transaction normalization;
- cash-flow affordability;
- eligibility/score;
- exception routing;
- digital offer;
- funding;
- fallback document workflow.

## Customer screens

1. eligibility;
2. business identity;
3. connect data source;
4. data connection status;
5. exceptions/documents if needed;
6. personalized offer;
7. contract;
8. funding.

## Exception rules

Examples:
- insufficient history;
- revenue inconsistency;
- high concentration;
- bank/tax mismatch;
- bureau conflict;
- unusual volatility;
- ownership complexity.

## Human role

Analyst reviews:
- exception reason;
- machine evidence;
- limited supplementary documents.

The analyst should not rebuild the full case from scratch.

## Required controls

- data-source freshness;
- connection quality;
- fraud;
- document fallback;
- decision reason;
- threshold monitoring.

---

# 4. Factory C — Guarantee-backed credit

## MVP scope

Choose one scheme and one borrower perimeter.

Do not launch multiple guarantee schemes at once.

## Minimum capabilities

- ordinary bank underwriting;
- program eligibility rules;
- revenue/size validation;
- guarantee coverage calculation;
- guarantee registration;
- fee calculation;
- claim metadata;
- separate portfolio/economics tag.

## Orchestration

**bank eligibility  
→ guarantee eligibility  
→ guarantee reservation/registration  
→ offer  
→ contract  
→ funding  
→ monitoring  
→ claim if required**

## Customer screens

Keep external-program complexity minimal:
- eligibility confirmation;
- amount/term;
- guarantee-related declarations;
- offer;
- contract.

## Human role

Only where:
- scheme requires review;
- policy exception;
- collateral/legal complexity.

## Required controls

- claim eligibility;
- evidence retention;
- guarantee expiry;
- guarantee amount;
- scheme-specific covenants.

---

# 5. Factory D — Medium / upper-SME relationship credit

## MVP scope

Do not attempt “full automation.”

Target:
- one product family;
- one ticket range;
- one delegated authority model.

## Minimum capabilities

- digital credit request;
- named case owner;
- document/data checklist;
- financial spreading;
- bank transaction summary;
- collateral data;
- covenant template;
- credit memo generation;
- workflow;
- delegated authority;
- conditions tracking;
- digital signing.

## Human workflow

### RM
- customer context;
- financing need;
- structure;
- relationship economics.

### Underwriter
- risk analysis;
- stress;
- structure;
- covenants;
- recommendation.

### Approver
- delegated decision.

### Operations/legal
- conditions;
- security;
- documentation.

## Critical design principle

Every manual action should answer:

**Is this judgment or administration?**

Administration should be automated first.

## Customer-visible screens

- request received;
- required items;
- progress;
- outstanding conditions;
- offer;
- signing/funding.

---

# 6. Factory E — Receivables / asset-backed

## MVP scope

Choose either:
- factoring/invoice finance;
- asset finance;
- collateral-backed SME loan.

Do not combine them initially.

## Invoice-finance minimum capabilities

- invoice ingestion;
- debtor master;
- eligibility;
- concentration;
- advance-rate calculation;
- availability;
- drawdown;
- collections;
- reconciliation;
- dilution/fraud monitoring.

## Customer screens

1. facility availability;
2. invoices;
3. eligible/ineligible items;
4. debtor limits;
5. draw;
6. collections;
7. remaining balance.

## Human role

- debtor risk;
- disputes;
- fraud;
- unusual concentrations.

---

# 7. Factory F — Embedded merchant credit

## Prerequisite

Do not build unless the bank/platform has:
- acquiring data;
- embedded merchant surface;
- sufficient transaction frequency.

## Minimum capabilities

- merchant activity features;
- automated eligibility;
- pre-approved offer API;
- embedded offer component;
- instant funding;
- sales-linked repayment / account sweep;
- merchant monitoring.

## Distribution model

The loan should appear:
- where the merchant already operates;
- not in a separate credit portal.

---

# 8. Shared capability dependency sequence

## Foundation
1. reusable KYB/customer object;
2. data acquisition;
3. feature layer;
4. policy/decision service;
5. orchestration / case state.

## Factory-specific build
6. product policy;
7. offer UI;
8. fulfillment;
9. servicing;
10. monitoring.

## Economics layer
11. FTP / expected loss / OPEX / capital;
12. factory contribution reporting.

## Optimization
13. experimentation;
14. dynamic limits;
15. funding optimization.

---

# 9. What should be configurable vs hard-coded

## Configure
- ticket limits;
- tenor;
- eligibility;
- score cutoffs;
- escalation;
- data requirements;
- pricing;
- guarantee rules;
- authority;
- document rules.

## Avoid hard-coding in front end
- policy logic;
- decision rules;
- product-specific compliance logic.

Reason:
policy changes faster than channel software.

---

# 10. Auditability / model risk requirements

Every decision should preserve:
- raw evidence references;
- feature version;
- model version;
- policy version;
- reason codes;
- override;
- approver;
- timestamp;
- price/limit shown;
- offer accepted.

This is required for:
- risk monitoring;
- disputes;
- regulatory review;
- pilot evaluation;
- policy optimization.

---

# 11. MVP definition of “done”

A factory is not done when the front end launches.

Minimum definition:

- end-to-end journey works;
- decision is auditable;
- exception routing works;
- servicing exists;
- portfolio tagging exists;
- risk outcomes are measurable;
- economics can be attributed;
- control/monitoring is defined.

Without these, it is a channel feature, not a credit factory.
