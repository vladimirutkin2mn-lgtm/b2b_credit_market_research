# Company / Lender Teardown — Floryn

**Status:** Batch 3 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Netherlands  
**Primary segment:** S2 — digital cash-flow SME lending  
**Primary question:** how far can PSD2 / bank-transaction underwriting replace financial statements?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**Floryn is one of the purest examples of cash-flow underwriting replacing traditional annual accounts — but only up to a defined €250k boundary.** Six months of bank transactions can be sufficient below that point; above it, recent accounts and receivables/payables lists return. The model is financed through wholesale/private-securitisation capacity rather than deposits.

### Quantified proof points

- loans / credit: **€10k–€2.5m**;
- up to **€250k**: no annual accounts required;
- required history: **6 months bank statements** / PSD2 connection;
- minimum company age: **6 months**;
- minimum annual turnover: **€100k**;
- application: about **2 minutes**;
- account manager contact: within **2 hours**;
- decision/first payout: within **24 hours** if data complete;
- 2025 NatWest private securitisation facility: **€150m**;
- earlier NatWest funding: €65m; earlier NIBC facility: €50m.

### Mechanism

PSD2 / bank transactions
→ real-time cash-flow view
→ no annual accounts below €250k
→ automated analysis + human account-manager overlay
→ fast facility.

Above €250k:
→ annual accounts + debtor/creditor lists
→ richer underwriting.

### Strategic implication

The strongest data-substitution design may use **current cash flow as the default evidence** and financial statements only as an escalation input.

### Transferability

**High where PSD2/open-banking data quality is strong.**

### Counter-evidence

Floryn is privately held and does not disclose comparable NPL, credit cost, yield or profitability. The model's risk-adjusted economics are therefore not independently testable from public data.

---

## 1. Product architecture

### Business loan
- €10k–€2.5m;
- fixed weekly repayment;
- automatic debit;
- early repayment without penalty.

### Revolving business credit
- reusable limit;
- pay interest only on drawn amount;
- direct dashboard drawdowns;
- no annual accounts up to €250k.

### Eligibility
- ≥6 months operating;
- KVK registration;
- ≥€100k annual turnover;
- active business bank account.

Source:
https://www.floryn.com/zakelijke-lening
https://www.floryn.com/zakelijk-krediet

---

## 2. Underwriting / data

Up to €250k:
- six months bank transactions;
- PSD2 connection or PDF statements;
- current turnover/cash flow;
- tax-payment behavior mentioned in pricing/assessment materials.

Above €250k:
- recent annual accounts;
- current debtor/creditor lists.

For BV borrowers, public pages describe a standard personal guarantee around 25% of financing (minimum €25k), with case-specific variation.

---

## 3. Customer journey

1. 2-minute quick application.
2. Upload six months statements or connect bank by PSD2.
3. Automated analysis.
4. Account manager contacts within 2 hours.
5. Offer/decision within 24 hours.
6. Digital approval.
7. Personal dashboard.
8. Draw funds; requests before 13:00 can arrive same day.
9. Repay / redraw for revolving product.

This is a hybrid:
**automation for information extraction + human relationship for confirmation/service.**

---

## 4. Visual evidence

Official pages include product visuals and calculator/quickscan interfaces, but no stable authenticated-screen assets were captured.

**Screen evidence:** partial / marketing-flow only.

Missing:
- PSD2 consent;
- analysis result;
- offer;
- contract;
- dashboard;
- drawdown.

---

## 5. Funding economics

Floryn is not deposit funded.

Official company timeline:
- 2019 NIBC: €50m;
- 2023 NatWest: €65m;
- 2025 NatWest private securitisation: **€150m**.

The 2025 facility expands lending capacity through private securitisation.

Sources:
- https://www.floryn.com/over-ons
- https://www.floryn.com/blog/floryn-haalt-150-miljoen-financiering-op-bij-natwest-via-private-securitisatie

### Implication

Floryn must earn enough asset yield to cover:
- wholesale/securitisation funding;
- losses;
- OPEX;
- equity return.

No public data allow a complete bridge.

---

## 6. Risk

Public process evidence:
- transaction analysis;
- guarantee;
- larger-ticket document escalation.

Not public:
- NPL;
- 30/90+ DPD;
- cost of risk;
- charge-offs;
- vintage losses;
- approval rate.

---

## 7. Hypothesis tests

### H2 — speed is segmentation: very strongly supported
€250k is the explicit document breakpoint.

### H4 — data substitution: very strongly supported
Bank transactions replace annual statements below threshold.

### H3 — funding advantage: unresolved but strategically relevant
Floryn uses private securitisation/wholesale funding, making funding cost more critical than at deposit banks.

### H5 — SME is several businesses: strongly supported
Data and process change above €250k.

---

## 8. Strategic implication

Floryn suggests a powerful underwriting hierarchy:

**real-time transactional evidence first → accounting evidence only when exposure requires it.**

This reverses the traditional bank order.

---

## 9. Evidence gaps

1. Loan book/AUM.
2. Originations.
3. Funding cost.
4. Portfolio yield.
5. Credit losses.
6. ROA/profitability.
7. Approval rate.
8. Full screens.

---

## Sources

- https://www.floryn.com/zakelijke-lening
- https://www.floryn.com/zakelijk-krediet
- https://www.floryn.com/zakelijke-lening-zonder-jaarcijfers
- https://www.floryn.com/bedrijfsfinanciering
- https://www.floryn.com/over-ons
- https://www.floryn.com/blog/floryn-haalt-150-miljoen-financiering-op-bij-natwest-via-private-securitisatie
