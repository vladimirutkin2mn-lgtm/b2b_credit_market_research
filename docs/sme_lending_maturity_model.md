# SME Lending Maturity Model

**Version:** 2026-10-02  
**Purpose:** diagnose a bank against the operating-model patterns found in the market research.

The model uses five maturity levels:

- **L0 — Fragmented / opaque**
- **L1 — Digitized front end**
- **L2 — Data-connected**
- **L3 — Factory-based**
- **L4 — Continuously optimized**

> This is not a league table. A bank may be L4 in one factory and L1 in another.

---

# 1. Customer segmentation / factory architecture

## L0
One broad SME credit process; segmentation mostly by legal size.

## L1
Different product forms, but common underwriting workflow.

## L2
Basic ticket/product routing and some specialist lanes.

## L3
Distinct factories for:
- existing customer;
- new-to-bank digital;
- relationship;
- guarantee;
- specialist assets.

## L4
Factory economics and policies are dynamically optimized; common platform reused across lanes.

---

# 2. Existing-customer pre-underwriting

## L0
Customer must apply from zero.

## L1
Known fields are prefilled.

## L2
Existing transactions inform underwriting after application.

## L3
Continuous eligibility / pre-approved offers for bounded segments.

## L4
Dynamic limits refresh continuously and feed repeat / top-up decisions with risk-adjusted optimization.

---

# 3. External data substitution

## L0
Manual documents dominate.

## L1
Documents uploaded digitally.

## L2
Open Banking / tax / accounting data used as supplemental evidence.

## L3
Machine-readable data replace documents inside explicit perimeters.

## L4
Multi-source data orchestrated automatically; document requests are exception-driven and measured.

---

# 4. Decisioning / automation perimeter

## L0
Manual decisioning and implicit escalation.

## L1
Rules automate some checks.

## L2
STP exists for selected products but thresholds are mostly product-legacy driven.

## L3
Explicit ticket/data/security/industry perimeters with clear exception routing.

## L4
Perimeters are regularly optimized using conversion, loss, OPEX and capital data.

---

# 5. Human underwriting / relationship model

## L0
Multiple handoffs, unclear ownership.

## L1
Named RM but separate credit chain remains opaque.

## L2
Digital credit package and standard workflow.

## L3
Empowered RM/underwriter with delegated authority and visible case ownership.

## L4
Human effort is deliberately allocated by marginal economic value; productivity and RAROC measured by case type.

---

# 6. Journey orchestration

## L0
Customer cannot see status; repeated requests.

## L1
Digital application front end.

## L2
Basic status and digital document upload.

## L3
Single case state across:
- data;
- underwriting;
- conditions;
- signing;
- funding.

## L4
Proactive next-best action, exception prevention and customer-visible ETA based on live workflow.

---

# 7. Pricing / offer transparency

## L0
Pricing appears late and opaquely.

## L1
Indicative pricing publicly available.

## L2
Personalized price before final commitment.

## L3
Price, fees, repayment and total cost shown at offer/draw stage.

## L4
Dynamic risk/relationship pricing with auditable controls and clear customer explanation.

---

# 8. Repeat lending

## L0
Repeat customer reapplies from zero.

## L1
Some data reused.

## L2
Fast-track repeat application.

## L3
Dynamic reusable limit / top-up based on observed behavior.

## L4
Limit, price and offers update continuously with monitoring and customer-LTV economics.

---

# 9. Guarantee-backed credit

## L0
Program handled manually / outside core workflow.

## L1
Dedicated specialists process guarantee products.

## L2
Some digital eligibility checks.

## L3
Tax/revenue/program eligibility integrated into origination and economics tracked separately.

## L4
Guarantee allocation optimized by incremental approval, uncovered loss and capital-adjusted return.

---

# 10. Specialist receivables / asset credit

## L0
Handled as generic term credit.

## L1
Specialist product exists.

## L2
Dedicated underwriting team.

## L3
Dedicated data/workflow for:
- invoices/assets;
- debtor/collateral;
- monitoring;
- drawdown.

## L4
High automation in recurring asset ingestion plus product-level funding / capital optimization.

---

# 11. Funding / capital architecture

## L0
One internal funding view for all SME credit.

## L1
Basic FTP by product.

## L2
Product-specific funding costs and capital visible.

## L3
Alternative funding / guarantees / securitisation considered by product engine.

## L4
Originate-to-hold vs distribute decisions dynamically reflect funding, capital and investor economics.

---

# 12. Risk measurement

## L0
Portfolio NPL only.

## L1
Risk by product.

## L2
Risk by product and vintage.

## L3
Risk by:
**product × customer relationship × decision model × channel × vintage**.

## L4
Risk-adjusted contribution and policy optimization performed at the same grain.

---

# 13. Economics

## L0
Volume / revenue focus.

## L1
Product P&L.

## L2
Yield − funding − credit cost visible.

## L3
Full contribution:
- acquisition;
- underwriting;
- servicing;
- capital;
- repeat/cross-sell.

## L4
Economic decisioning embedded in product/risk policy and opportunity allocation.

---

# 14. Data / technology platform

## L0
Point systems and manual transfer.

## L1
Digital front end around legacy cores.

## L2
Reusable APIs and selected data services.

## L3
Shared identity/data/decision/orchestration layer across factories.

## L4
Composable decision services with versioning, experimentation, monitoring and auditable lineage.

---

# 15. Governance

## L0
Product, Risk, Ops and Finance optimize separate metrics.

## L1
Periodic steering committee.

## L2
Shared transformation KPIs.

## L3
Factory-level owner with joint Product/Risk/Finance economics.

## L4
Continuous portfolio allocation based on risk-adjusted factory economics.

---

# Scoring guidance

Score each dimension **0–4** only with evidence.

Do not average blindly.

Instead identify:
- **blocking capabilities**;
- **maturity gaps relevant to chosen factories**;
- **capabilities already good enough**.

A bank targeting only medium-SME relationship lending does not need L4 embedded-merchant capability.

---

# Diagnostic output

For each dimension produce:

- current level;
- evidence;
- target level;
- reason target matters;
- gap;
- dependency;
- value channel;
- risk;
- owner.

The resulting roadmap should be **factory-specific**, not a generic “digital transformation” list.
