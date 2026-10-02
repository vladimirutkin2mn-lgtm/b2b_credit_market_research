# Implementation Backlog — Generic SME Lending Platform

**Version:** 2026-10-02  
**Purpose:** convert the target operating model into a dependency-aware implementation backlog.

> This is a generic sequence. It is not a dated project plan and should not be used for resourcing before current-state architecture and internal data are known.

---

# Epic 0 — Baseline and instrumentation

## Goal
Make current economics and process observable before changing them.

### Deliverables
- application/loan IDs;
- stage timestamps;
- product/factory tagging;
- existing/new flag;
- STP/manual flag;
- policy/model version;
- decision reasons;
- loss cohort;
- FTP/OPEX/capital fields.

### Exit criterion
Current baseline can be calculated for:
- conversion;
- time;
- manual work;
- loss;
- economics.

---

# Epic 1 — Shared customer and data foundation

### Work
- reusable customer/KYB object;
- consent service;
- own transaction history;
- external data connectors;
- normalized financial data;
- feature definitions/versioning.

### Why first
Every high-value factory depends on this.

### Exit criterion
One application can consume reusable customer/data objects without bespoke manual assembly.

---

# Epic 2 — Decisioning and orchestration

### Work
- eligibility service;
- score/affordability;
- limit;
- pricing;
- refer;
- reason codes;
- case state;
- SLA;
- exception queue.

### Exit criterion
Policy can be changed without front-end code and every case has one auditable state.

---

# Epic 3 — Existing-customer pre-approved MVP

### Work
- eligible base;
- offer generation;
- in-app offer;
- configure amount/term;
- acceptance;
- internal funding;
- monitoring.

### Pilot
Use Pilot A.

### Exit criterion
Controlled cohort can complete end-to-end without traditional application.

---

# Epic 4 — Data-substitution MVP

### Work
- Open Banking/tax/accounting connection;
- machine cash-flow analysis;
- document fallback;
- analyst exception workspace.

### Pilot
Use Pilot B.

### Exit criterion
Treatment cohort has materially fewer documents/manual touches with controlled risk.

---

# Epic 5 — Repeat / servicing

### Work
- reusable limit;
- dynamic refresh;
- top-up;
- servicing state;
- early repayment;
- hold/freeze.

### Pilot
Use Pilot D.

### Exit criterion
Eligible repeat borrower can receive/draw credit without re-originating from zero.

---

# Epic 6 — Relationship fast lane

### Work
- digital credit pack;
- spreading;
- RM/underwriter case owner;
- delegated authority;
- conditions/legal tracking;
- customer-visible state.

### Pilot
Use Pilot C.

### Exit criterion
Cycle time/handoffs reduced for comparable cases without control deterioration.

---

# Epic 7 — Guarantee integration

### Work
- one scheme;
- eligibility;
- data authorization;
- guarantee registration;
- separate economics;
- claims data.

### Exit criterion
Guaranteed loan can be measured separately from ordinary credit end-to-end.

---

# Epic 8 — Specialist factories

Choose based on strategy.

## Receivables
- invoice ingestion;
- debtor risk;
- availability;
- draw;
- collections.

## Embedded merchant
- merchant signals;
- partner/API offer;
- sales-linked repayment.

## Asset finance
- asset eligibility;
- valuation;
- security;
- fulfillment.

### Exit criterion
Each specialist factory has its own risk object and economics, while reusing shared platform capabilities.

---

# Epic 9 — Funding / capital optimization

### Work
- factory FTP;
- capital allocation;
- guarantee-adjusted capital;
- investor sale / securitisation options;
- hold/distribute economics.

### Exit criterion
Factory growth decisions use capital/funding-adjusted contribution.

---

# Epic 10 — Continuous optimization

### Work
- champion/challenger;
- ticket threshold experiments;
- dynamic limits;
- reason-code analysis;
- loss/conversion frontier;
- portfolio allocation.

### Exit criterion
Policy changes are evidence-based and measurable, not annual manual redesigns.

---

# Cross-cutting workstreams

## Risk/model governance
- policy versioning;
- model monitoring;
- overrides;
- adverse-action reasons;
- validation.

## Compliance/legal
- consent;
- KYB;
- privacy;
- contract;
- guarantee evidence.

## Data
- lineage;
- source quality;
- retention;
- feature versioning.

## Operations
- exception queues;
- SLAs;
- workload;
- fallback.

## Finance
- FTP;
- cost allocation;
- capital;
- business-case reporting.

---

# Dependency principle

Do not schedule by what is most visible to the customer.

Schedule by **blocking dependency**.

Example:

A pre-approved offer front end is low value if:
- eligibility is not refreshed;
- limit is stale;
- risk reasons are not auditable;
- funding still requires manual intervention.

Therefore the dependency order is generally:

**identity/data → features → decision → orchestration → offer → fulfillment → monitoring → economics optimization**.
