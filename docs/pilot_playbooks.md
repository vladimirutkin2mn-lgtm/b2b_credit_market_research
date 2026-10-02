# SME Lending Pilot Playbooks

**Purpose:** convert the research hypotheses into testable bank experiments.

> These playbooks are generic. Final eligibility, sample size, loss guardrails and economics must be set using internal bank data and risk appetite.

---

# Pilot A — Existing-customer pre-approved credit

## Hypothesis

For existing SME customers with sufficient transaction history, continuous pre-underwriting can:
- reduce application effort;
- reduce manual review;
- improve conversion;
- preserve or improve risk-adjusted economics.

## Treatment

Eligible customers receive:
- pre-calculated limit;
- proactive offer;
- minimal data entry;
- digital acceptance;
- instant/near-instant account funding.

## Control

Current existing-customer application process.

## Eligibility

Start with:
- existing current-account customers;
- minimum relationship tenure;
- stable inflows;
- no recent delinquency;
- simple legal structure;
- bounded ticket/tenor;
- excluded high-risk industries.

## Metrics

### Funnel
- offer rate;
- offer acceptance;
- booked conversion;
- utilization.

### Customer
- time-to-fund;
- data fields / documents;
- abandonment;
- support contacts.

### Operations
- manual review rate;
- cost per booked loan.

### Risk
- FPD;
- 30/90+ DPD;
- vintage loss;
- override rate.

### Economics
- risk-adjusted contribution;
- repeat rate;
- deposit/payments retention if measurable.

## Guardrails

Stop or tighten if:
- loss exceeds control by agreed tolerance;
- fraud rises;
- utilization creates liquidity/funding stress;
- limit creep occurs.

## Decision rule

Scale only if:
**conversion + cost benefit + relationship value > incremental loss + capital/funding cost.**

---

# Pilot B — Machine-readable data substitution

## Hypothesis

Replacing default document requests with bank/tax/accounting data can reduce customer effort and underwriting OPEX without increasing losses.

## Treatment

Customer:
- connects Open Banking / accounting / tax data;
- provides manual documents only if exception rules trigger.

## Control

Current standard document pack.

## Eligibility

Choose a homogeneous:
- product;
- ticket band;
- legal form;
- industry set.

Avoid mixing multiple policy changes in first test.

## Metrics

### Customer
- completion rate;
- document count;
- time to complete;
- support contacts.

### Operations
- document-request rate;
- manual extraction time;
- STP rate;
- analyst touches.

### Risk
- approval distribution;
- score discrimination;
- FPD / DPD;
- fraud.

### Economics
- underwriting cost;
- booked conversion;
- contribution per application.

## Guardrails

- data connection failure;
- missing/low-quality data;
- model confidence threshold;
- fallback to documents.

## Key analysis

Compare:
**same customer risk band with and without document substitution**.

Do not infer risk effect from raw treated-vs-control averages if selection differs.

---

# Pilot C — Relationship fast lane

## Hypothesis

Medium-SME speed can improve materially by reducing organizational handoffs and increasing delegated authority, without moving the final decision to full automation.

## Treatment

- one named case owner;
- standardized digital credit pack;
- automated spreading/checks;
- underwriter/RM paired early;
- predefined decision authority;
- digital outstanding-items tracker.

## Control

Current relationship-credit process.

## Eligibility

Use:
- one ticket range;
- one or two product types;
- similar collateral complexity;
- same risk appetite.

## Metrics

### Process
- time to complete file;
- handoffs;
- clarification loops;
- complete-file-to-decision time;
- conditions-to-funding time.

### Productivity
- decisions per credit FTE;
- approved volume per credit FTE;
- RM time.

### Customer
- acceptance;
- drop-off;
- satisfaction / support contacts if available.

### Risk
- approval;
- overrides;
- loss / impairment;
- covenant quality.

### Economics
- contribution;
- cost per case;
- relationship revenue;
- RAROC.

## Guardrails

- no reduction in mandatory risk controls;
- delegated authorities remain explicit;
- complex cases route to normal process.

## Decision rule

Scale if cycle-time/productivity gains occur without deterioration in:
- risk quality;
- control exceptions;
- pricing discipline.

---

# Pilot D — Repeat dynamic limit / top-up

## Hypothesis

Customers with good repayment and ongoing business activity can borrow again with lower CAC and underwriting cost while preserving or improving loss outcomes.

## Treatment

After defined repayment history:
- limit refreshed automatically;
- top-up/redraw offered proactively;
- reduced data/document burden.

## Control

Repeat customer uses ordinary new-loan process.

## Eligibility

- minimum seasoning;
- clean repayment;
- current account / data visibility;
- no negative bureau/internal signals;
- bounded limit growth.

## Metrics

### Repeat
- repeat offer rate;
- acceptance;
- time to repeat;
- limit utilization.

### Customer
- time-to-fund;
- reduced fields/documents.

### Operations
- manual review;
- cost per repeat booking.

### Risk
- repeat-vs-first vintage loss;
- performance after limit increases;
- deterioration flags.

### Economics
- repeat contribution;
- repeat CAC;
- customer LTV.

## Guardrails

- cap limit growth;
- refresh behavior at every draw;
- automatic freeze on risk deterioration.

## Decision rule

Scale if repeat contribution improves after controlling for:
- borrower quality;
- seasoning;
- ticket;
- selection.

---

# Experiment design rules

## 1. Keep treatment narrow

Do not simultaneously change:
- pricing;
- underwriting policy;
- UI;
- documents;
- funding

unless the pilot explicitly tests the bundle.

## 2. Preserve a comparison group

Preferred:
- randomized / controlled where feasible.

Alternative:
- matched cohort;
- phased rollout;
- regression discontinuity around threshold;
- pre/post with strong controls.

## 3. Define outcomes before launch

Primary outcome:
- risk-adjusted contribution.

Supporting:
- conversion;
- time;
- OPEX;
- risk.

## 4. Define loss guardrails before launch

No post-hoc tolerance.

## 5. Measure mature outcomes

Fast conversion results arrive first.
Credit-loss results season later.

Do not declare success based only on first-month conversion.

## 6. Track policy/version

Every loan must carry:
- pilot flag;
- policy version;
- model version;
- treatment/control;
- origination cohort.

---

# Recommended first pilot order for a typical incumbent bank

1. **Existing-customer pre-approved**
2. **Data substitution**
3. **Relationship fast lane**
4. **Repeat dynamic limit**

Reason:
these test the four strongest, most transferable hypotheses from the external research without requiring a fundamentally new balance-sheet model.

This order remains provisional until internal data identify the largest value pool.
