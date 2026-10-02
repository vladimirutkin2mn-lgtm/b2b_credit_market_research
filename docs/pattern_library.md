# SME Lending Pattern Library

**Version:** 2026-10-02

This library captures observed mechanisms, not generic “best practices.”

Each pattern includes:
- problem;
- mechanism;
- evidence;
- prerequisite;
- economic channel;
- risk;
- transferability.

---

# P1 — Continuous pre-underwriting

## Problem
Customer has to start every borrowing event from zero.

## Mechanism
Refresh eligibility continuously using relationship/activity data and surface credit only when the model supports it.

## Evidence
Nubank, Stone, Square, Mercado Pago, CommBank, Amex, SBI.

## Economics channel
- lower CAC;
- lower application-processing cost;
- higher conversion;
- faster repeat lending.

## Risk
Opaque offer-selection can create selection bias; model drift/vintage risk remains.

## Transferability
**High with rich existing customer data.**

---

# P2 — Machine-readable data substitution

## Problem
SME financial documentation creates customer and underwriting friction.

## Mechanism
Replace or supplement documents with:
- Open Banking;
- transactions;
- tax/e-invoice;
- accounting;
- acquiring.

## Evidence
Rabobank, Floryn, iwoca, Konfío, SBI, Stone, Square.

## Economics channel
- lower underwriting OPEX;
- lower abandonment;
- shorter decision time;
- more scalable monitoring.

## Risk
Machine-readable data can be incomplete or manipulated and may not capture structural business changes.

## Transferability
**High, but infrastructure-specific.**

---

# P3 — Explicit automation perimeter

## Problem
One STP policy cannot safely cover every SME exposure.

## Mechanism
Set clear breakpoints by:
- ticket;
- tenor;
- data history;
- industry;
- collateral;
- legal form.

## Evidence
iwoca, Rabobank, Floryn, SBI, Commerzbank, CommBank.

## Economics channel
Allocate underwriting cost to exposure.

## Risk
Bad thresholds can create cliff effects / adverse selection around limits.

## Transferability
**Very high.**

---

# P4 — Human-underwriting fast lane

## Problem
Complex SME cases are slow because decisions pass through too many organizational layers.

## Mechanism
Digitize intake and give qualified RM/underwriter authority close to customer.

## Evidence
Commerzbank, Allica, Judo.

## Economics channel
- fewer handoffs;
- higher banker productivity;
- better conversion;
- premium pricing for service.

## Risk
Key-person inconsistency; concentration; judgment error.

## Transferability
**High for larger SME.**

---

# P5 — Repeat-lending dynamic limit

## Problem
Repeat borrower repeats the same origination process.

## Mechanism
Maintain/update limit based on observed repayment and business behavior.

## Evidence
Amex BLOC, Square, Nubank, SBI, Funding Circle, Mercado Pago.

## Economics channel
- lower CAC;
- lower underwriting cost;
- higher lifetime value;
- better cross-sell.

## Risk
Limit creep in a deteriorating borrower; requires monitoring.

## Transferability
**High.**

---

# P6 — Embedded merchant repayment

## Problem
Collections and cash-flow mismatch create friction/default risk.

## Mechanism
Repay automatically from merchant sales or wallet/account flows.

## Evidence
Stone, Square, Mercado Pago.

## Economics channel
- lower servicing cost;
- smoother borrower cash flow;
- better visibility.

## Risk
Sales decline directly slows repayment; platform concentration.

## Transferability
**Context-specific to acquiring/platform lenders.**

---

# P7 — Digitized government-guarantee lane

## Problem
Collateral/risk constraints exclude otherwise viable SME borrowers.

## Mechanism
Embed guarantee eligibility, tax/revenue checks and contracting into digital origination.

## Evidence
Itaú, Stone, SBI.

## Economics channel
- lower expected loss;
- potentially lower capital/provisioning;
- broader approval.

## Risk
program rules / government dependency; moral hazard; operational eligibility errors.

## Transferability
**Medium/High where schemes exist.**

---

# P8 — Product-specific funding architecture

## Problem
Holding every SME asset on one balance sheet can be inefficient.

## Mechanism
Match funding to product:
- deposits;
- institutional forward flow;
- investor sale;
- securitisation;
- receivables facilities.

## Evidence
Funding Circle, Square, Floryn, Bibby, Judo/Allica/banks.

## Economics channel
- lower funding cost;
- capital recycling;
- liquidity matching.

## Risk
market funding can disappear in stress.

## Transferability
**High for treasury-capable institutions.**

---

# P9 — Receivables-first lending factory

## Problem
B2B seller needs working capital before invoices are paid.

## Mechanism
Underwrite receivable/debtor pool rather than unsecured borrower cash flow.

## Evidence
Bibby.

## Economics channel
- self-liquidating asset;
- fee + financing revenue;
- collections service revenue.

## Risk
invoice fraud;
- dilution;
- debtor concentration;
- disputes.

## Transferability
**High for B2B invoice-heavy sectors, but requires specialized infrastructure.**

---

# P10 — Shared platform, multiple credit factories

## Problem
SME segments have incompatible underwriting/economics.

## Mechanism
Share:
- data;
- identity;
- decision infrastructure;
- servicing;

while running separate:
- risk policy;
- product;
- decision authority;
- funding;
- economics.

## Evidence
SBI, Itaú, Allica, Rabobank, Funding Circle.

## Economics channel
Platform reuse without forcing one product economics model.

## Risk
organizational complexity.

## Transferability
**Very high for scaled banks.**
