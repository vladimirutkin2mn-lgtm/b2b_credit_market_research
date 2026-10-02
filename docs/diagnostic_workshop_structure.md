# SME Lending Diagnostic Workshop Structure

**Purpose:** convert the market benchmark into a bank-specific fact base and prioritized pilot list.

---

# Session 0 — Pre-work

Collect:
- current SME segmentation;
- product list;
- credit policy thresholds;
- journey maps;
- application / approval / booking funnel;
- decision/funding SLA;
- manual-touch/document counts;
- risk vintages;
- product P&L / FTP / capital where available.

Participants independently complete:
- `data/sme_lending_diagnostic_scorecard.csv`

No consensus scoring before evidence is shown.

---

# Session 1 — Where is the current model structurally wrong?

## 90–120 minutes

### 1. Segment / factory map
Map current products into:
- existing-customer preapproved;
- new-to-bank digital;
- guarantee-backed;
- relationship;
- receivables/asset;
- embedded merchant if relevant.

Question:
**Which materially different credit problems are currently forced through the same process?**

### 2. Journey friction
Compare:
- customer-entered data;
- documents;
- handoffs;
- decision time;
- funding time;
- repeat journey.

### 3. Data map
Identify:
- data already owned;
- data available but unused;
- documents that duplicate machine-readable data.

### Output
3–5 structural gaps.

---

# Session 2 — Where is the economic value?

## 90–120 minutes

For each structural gap:

1. current volume;
2. conversion loss;
3. OPEX burden;
4. risk impact;
5. capital/funding impact;
6. repeat/cross-sell impact.

Use:
- `docs/business_case_framework.md`
- `data/target_kpi_tree.csv`

### Output
Short list of opportunities with:
- value hypothesis;
- data required;
- confidence;
- test design.

---

# Session 3 — Risk and policy redesign

## 90 minutes

Focus on:
- STP perimeter;
- escalation triggers;
- ticket thresholds;
- existing-vs-new policy;
- repeat limits;
- guarantees;
- human authority.

Question:
**What can safely move left—from manual decision to machine, or from committee to empowered underwriter?**

### Output
Candidate policy changes / experiments.

---

# Session 4 — Target operating model

## 90 minutes

Agree:
- common data layer;
- decision services;
- orchestration;
- factory ownership;
- Product/Risk/Finance governance;
- KPI tree.

### Output
Target architecture and dependency map.

---

# Session 5 — Pilot portfolio

Do not create a 50-item transformation roadmap.

Select 2–4 pilots.

Recommended pilot archetypes:

## Pilot A — Existing-customer preapproved
Test:
- dynamic eligibility;
- proactive offer;
- simplified acceptance.

## Pilot B — Data-substitution
Test:
- Open Banking/tax/accounting connection;
- reduced document pack.

## Pilot C — Relationship fast lane
Test:
- single owner;
- delegated authority;
- digitized credit pack.

## Pilot D — Repeat dynamic limit
Test:
- top-up/redraw;
- behavioral refresh.

Each pilot must define:
- customer perimeter;
- control group if feasible;
- conversion KPI;
- process KPI;
- loss guardrail;
- economics metric;
- stop rule.

---

# Decision discipline

Do not prioritize on:
- competitor excitement;
- UX aesthetics;
- originations alone.

Prioritize on:

**customer value × risk-adjusted economics × feasibility × strategic fit**

with explicit confidence and dependencies.
