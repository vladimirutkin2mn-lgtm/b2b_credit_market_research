# Governance & Decision Rights — SME Lending Factories

**Version:** 2026-10-02  
**Purpose:** define ownership and decision rights for a multi-factory SME lending model.

---

# Executive answer

The operating model should avoid two failure modes:

1. **Product-led speed without risk/economics ownership**
2. **Risk-led control without customer/economic accountability**

Each credit factory needs one accountable business owner, but decisions are jointly governed by:

- Product / Business
- Risk / Credit
- Finance / Treasury
- Operations
- Data / Technology
- Legal / Compliance

The key rule is:

> **No factory should have split accountability for end-to-end economics.**

---

# 1. Factory owner

Each factory should have one accountable owner for:

- growth;
- customer journey;
- operating performance;
- economics;
- coordination across functions.

The owner does **not** unilaterally own:
- credit policy;
- model validation;
- capital rules;
- compliance.

But the owner is accountable for the combined outcome.

---

# 2. Decision-right hierarchy

## Level 1 — Automated policy decision

Used when:
- case inside explicit perimeter;
- required data complete;
- no exception.

Decision:
- approve/decline/refer;
- amount;
- tenor;
- price.

Owner:
Risk-approved decision service.

---

## Level 2 — Analyst exception

Used when:
- machine result is incomplete/ambiguous;
- limited additional evidence can resolve uncertainty.

Decision:
- approve within delegated threshold;
- return for more data;
- escalate.

Owner:
Credit analyst.

---

## Level 3 — Underwriter / RM authority

Used when:
- larger ticket;
- context matters;
- structure/collateral/covenants.

Decision:
- approve within delegated authority;
- structure;
- covenants;
- pricing recommendation.

Owner:
Named underwriter / credit executive, with RM input.

---

## Level 4 — Specialist / committee

Used only when:
- exposure;
- complexity;
- exception;
- policy override

justify additional governance.

Committee should not be the default queue for ordinary medium-SME cases.

---

# 3. Product / Business responsibilities

Accountable for:
- customer proposition;
- channel;
- funnel;
- adoption;
- journey;
- servicing experience;
- product requirements.

Must not independently change:
- risk thresholds;
- model cutoffs;
- policy;
- capital assumptions.

Primary KPIs:
- eligible reach;
- conversion;
- utilization;
- repeat;
- customer effort;
- contribution.

---

# 4. Risk / Credit responsibilities

Accountable for:
- risk appetite;
- eligibility;
- score/model use;
- affordability;
- limits;
- overrides;
- delegated authority;
- monitoring;
- losses.

Must not optimize only:
- NPL;
- approval conservatism.

Primary KPIs:
- risk-adjusted contribution;
- loss by vintage;
- overrides;
- model/policy performance;
- risk frontier.

---

# 5. Finance / Treasury responsibilities

Accountable for:
- FTP;
- liquidity cost;
- capital;
- cost of capital;
- guarantee economics;
- asset-distribution economics;
- business-case methodology.

Primary KPIs:
- contribution;
- ROA/RAROC;
- capital efficiency;
- funding mix.

---

# 6. Operations responsibilities

Accountable for:
- KYB execution;
- exception handling;
- documents;
- fulfillment;
- servicing operations;
- claims / collections operations.

Primary KPIs:
- touch time;
- rework;
- SLA;
- cost per booked case;
- exception aging.

---

# 7. Data / Technology responsibilities

Accountable for:
- reusable customer object;
- data connectors;
- feature services;
- policy/decision services;
- orchestration;
- APIs;
- monitoring infrastructure;
- lineage/versioning.

Primary KPIs:
- service availability;
- data quality;
- decision latency;
- deployment lead time;
- failure/retry rate.

---

# 8. Legal / Compliance responsibilities

Accountable for:
- consent;
- disclosures;
- fair/adverse decision requirements;
- privacy;
- KYB/AML standards;
- contracting;
- guarantee evidence requirements.

Must be integrated into design, not added after journey completion.

---

# 9. Factory-level governance cadence

## Weekly operating review
Focus:
- volume;
- funnel;
- SLA;
- exceptions;
- incidents.

## Monthly risk/economics review
Focus:
- vintage;
- loss;
- overrides;
- contribution;
- funding/capital;
- threshold performance.

## Quarterly policy review
Focus:
- cutoffs;
- segmentation;
- ticket/perimeter;
- data sources;
- guarantee use;
- portfolio mix.

Policy changes should be versioned.

---

# 10. Mandatory joint metrics

Every factory steering pack should show together:

## Growth
- offers;
- approvals;
- bookings;
- utilization.

## Customer
- completion;
- decision time;
- funding time;
- document burden.

## Risk
- FPD;
- DPD/default;
- loss;
- overrides.

## Economics
- yield/fees;
- funding;
- credit loss;
- OPEX;
- capital;
- contribution.

Do not review these in separate meetings only.

---

# 11. Change rights

## Product can change without Risk approval
Examples:
- copy;
- navigation;
- non-credit UX;
- support content.

## Joint Product + Risk
Examples:
- application fields that feed policy;
- document rules;
- offer presentation linked to eligibility;
- retry/resubmission.

## Risk approval required
- score cutoff;
- eligibility;
- limits;
- tenor;
- overrides;
- policy.

## Finance/Treasury approval required
- FTP assumptions;
- funding structure;
- capital methodology;
- profitability hurdle.

---

# 12. Override governance

Every override must record:
- original machine/policy result;
- reason;
- approver;
- resulting terms;
- outcome.

Track:
- override rate;
- loss on overrides;
- conversion benefit;
- economics.

Overrides should be a source of policy learning, not an invisible manual layer.

---

# 13. Factory owner scorecard

The factory owner should be evaluated on:

**risk-adjusted contribution**
plus:
- growth;
- customer effort;
- risk;
- operating efficiency.

No single metric dominates.

---

# Final governance principle

A fast SME credit factory requires:

> **clear case ownership + clear credit authority + shared economics**

Without all three, technology mainly accelerates the handoff into the next queue.
