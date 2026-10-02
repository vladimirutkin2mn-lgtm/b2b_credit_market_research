# Remaining Evidence Gaps — Materiality Triage

**Version:** 2026-10-02

## Purpose

Do not chase every missing cell.

Only collect additional evidence if it can:
- change a major conclusion;
- materially improve economic/risk comparability;
- support a final executive exhibit;
- resolve a contradiction.

---

# Priority 1 — Must close before final report if obtainable

## India — current post-Apr-2025 MSME risk

### Gap
Comparable GNPA/credit-quality measure under the new MSME classification.

### Why it matters
India is a core scale/data-infrastructure market and the definition changed materially in Apr-2025.

### Stop rule
If only pre-change figures exist, retain historical risk and explicitly label the break.

---

## US — standardized small-business credit supply/risk anchor

### Gap
A defensible regulatory/bank-system measure for small-business loan stock/risk that does not pretend to be identical to the Fed <500 employee survey population.

### Why it matters
US is central to the player universe, but market-side evidence is currently demand-heavy.

### Stop rule
Use small-loan-size regulatory proxies only if labeled as proxies; do not call them “SME stock.”

---

## Mexico — system credit stock / pricing context

### Gap
Current official SME/MIPYME bank-credit balance or a clean Banxico size-segment series plus pricing if available.

### Why it matters
Mexico currently has strong demand/approval evidence but weaker supply-side scale.

### Stop rule
Do not use total corporate credit as SME stock.

---

# Priority 2 — Valuable, but company-level evidence can substitute

## Netherlands — exact SME bank-stock numeric series
DNB public article says just under half of €340bn corporate lending is SME, but the exact share/value should only be used if the underlying series can be sourced cleanly.

## Australia — SME/business outstanding stock
Useful for market-size exhibit but not essential to the core operating-model conclusions.

## UK — system-level SME credit risk
Company/regulatory disclosures may be more decision-useful than forcing one market NPL.

## Germany — clean SME stock rather than loan-size proxy
KfW/ECB/Bundesbank definitions differ; the exact number is lower priority than the already strong demand/investment evidence.

---

# Priority 3 — Do not spend time unless final exhibit needs it

- fully harmonized business counts across all countries;
- one uniform cross-country interest-rate series;
- one uniform approval-rate series;
- historical guarantee volumes for every market;
- generic country rankings.

These are likely to create more false comparability than insight.

---

# High-value evidence gaps at company level

More valuable than many country gaps:

1. existing-vs-new customer loss rates;
2. repeat vs first-loan economics;
3. automated vs manual cost-to-serve;
4. approval / booked conversion by lane;
5. product-level funding cost;
6. product-level RWA/economic capital;
7. guarantee-backed vs ordinary credit loss/RAROC;
8. authenticated screenflows for current missing journeys.

These directly test the major strategic hypotheses.

---

# Recommended research allocation

## Spend effort
- risk-adjusted economics;
- decision/automation boundaries;
- repeat lending;
- guarantee economics;
- visual journeys;
- data prerequisites.

## Avoid low-value effort
- filling every country cell;
- constructing synthetic rankings from incompatible definitions;
- broad “feature counts.”

---

# Decision rule

A new datapoint should answer:

> **Which strategic conclusion would change if this number were different?**

If there is no clear answer, it is probably not a priority.


---

# Priority-1 research resolution — 2026-10-02

The three Priority-1 gaps were re-checked against current official sources.

## India — current post-Apr-2025 system MSME risk

### Outcome
**Not fully resolved at system level.**

Current public evidence supports:
- strong overall banking asset quality;
- lender-specific post-definition MSME risk, including SBI MSME GNPA of 1.18% at Mar-2026 in the company deep dive.

But a clean, current, all-SCB MSME GNPA series under the new Apr-2025 definition was not established from the official sources reviewed.

### Decision
Do **not** use overall SCB/PSB GNPA as MSME GNPA.

Use:
- current lender-level risk;
- historical system MSME risk with definition warning;
- new system series only if RBI publishes a clearly defined comparable measure.

**Status: methodological stop, not an unresolved blocker.**

---

## United States — small-business supply/risk anchor

### Outcome
A regulatory source exists, but it is a **proxy framework**, not a universal SME borrower definition.

FFIEC Call Reports include Schedule RC-C Part II — Loans to Small Businesses and Small Farms.

The regulatory/reporting concept has historically relied materially on:
- original loan amount;
- separate reporting for loans to businesses with gross annual revenues ≤$1m.

Current FFIEC forms continue to contain the small-business schedule.

Sources:
- https://www.ffiec.gov/resources/reporting-forms/ffiec031
- https://www.fdic.gov/bank-financial-reports/ffiec-reports-condition-and-income-instructions-ffiec-051-report-form-1

### Decision
This is useful for **bank-supply proxy analysis**, but it must not be merged with:
- Fed SBCS <500 employee population;
- SBA NAICS size standards.

A future US exhibit can show:
**borrower survey lane vs regulatory small-loan proxy lane**, explicitly separated.

**Status: source architecture resolved; no synthetic “US SME stock” will be created.**

---

## Mexico — SME system stock/pricing

### Outcome
CNBV publishes detailed regulated-institution credit data and portfolio characteristics, including:
- credit balances;
- originations;
- weighted rates;
- maturity;
- financial-quality indicators.

However, CNBV's own statistical FAQ states that current enterprise-size reporting has data-quality issues and that it is not presently possible to provide a reliable micro/small/medium breakdown in the relevant reporting context.

Sources:
- https://www.gob.mx/cnbv/es/articulos/portafolio-de-informacion-pi
- https://www.gob.mx/cnbv/acciones-y-programas/preguntas-frecuentes-informacion-estadistica
- https://www.gob.mx/cnbv/acciones-y-programas/informacion-estadistica-100861

Banco de México also provides PyME credit-standards survey series, but those are diffusion/conditions indicators rather than a clean SME stock.

### Decision
Do **not** infer a national MIPYME stock from total corporate financing.

Use:
- ENAFIN for borrower-side demand/access;
- Banxico for PyME credit standards/conditions;
- CNBV portfolio data when the size definition is source-clean;
- company data for lender-level risk/economics.

**Status: methodological stop; data-quality limitation documented.**

---

# Final gap-triage conclusion

The market layer is now sufficiently researched for strategic synthesis.

The remaining missing numbers are mostly cases where:
- the public definition is not aligned; or
- forcing a number would reduce analytical quality.

The highest-value next evidence is therefore **company/product-level causal evidence**, not more broad country-cell filling.
