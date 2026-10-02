---
name: market-sizing
description: Size SME/B2B credit markets with defensible definitions, top-down and bottom-up methods, stock/flow separation, segmentation and sensitivity analysis.
---

# SME Credit Market Sizing

## Objective

Estimate the market without producing a false-precision “single TAM number”.

Primary outputs:
- outstanding credit stock;
- annual new originations / disbursements;
- number of borrowing firms;
- product and segment mix;
- lender/channel mix;
- financing gap or unmet demand, when evidence supports it.

## Step 1 — Define the market boundary

Always specify:
- geography;
- period;
- borrower definition: micro / small / medium / legal entities / sole proprietors;
- size threshold used by the source;
- product types included;
- bank vs nonbank coverage;
- secured vs unsecured;
- on-balance-sheet lending vs guarantees / factoring / leasing;
- nominal vs real currency values.

If sources use different SME definitions, keep them separate until normalization is possible.

## Step 2 — Separate stock and flow

Never mix:
- **stock** = outstanding balance at a point in time;
- **flow** = new lending/originations during a period.

Report both when possible.

Useful relationships:

`Approximate stock ≈ prior stock + new disbursements - repayments - charge-offs +/- FX/reclassifications`

This is a diagnostic identity, not a substitute for source data.

## Step 3 — Top-down method

Start from official/regulatory aggregates:
- total business lending;
- SME share;
- product/borrower filters;
- geography filters.

Show every filter explicitly.

Example:
`SME loan stock = total business loan stock × SME share`

Do not apply a percentage from one country/year to another without labeling it as a proxy.

## Step 4 — Bottom-up method

Build from units:

`Borrowing firms × average outstanding balance`

or

`Eligible firms × borrowing incidence × average loan size`

For annual flow:

`Borrowers per year × applications per borrower × booked conversion × average disbursement`

Each input must be evidence or a labeled assumption.

## Step 5 — Demand-side cross-check

Where available, use borrower surveys:
- share seeking financing;
- product requested;
- average amount requested;
- approval / partial approval / denial;
- discouraged borrowers;
- reason for financing.

Demand-side data can reveal unmet demand that bank balance-sheet data cannot.

## Step 6 — Supply-side cross-check

Use:
- central bank / regulator statistics;
- bank disclosures;
- lending surveys;
- government guarantee programs;
- nonbank lender disclosures.

Check whether the market is measured by lender type or total system.

## Step 7 — Reconcile methods

Create a reconciliation table:

| Method | Estimate | Period | Definition | Coverage | Key assumptions |
|---|---:|---|---|---|---|

If methods differ:
- inspect SME definition;
- stock vs flow;
- gross vs net;
- bank vs nonbank;
- legal entities vs sole proprietors;
- currency/FX;
- survey bias;
- missing small lenders.

Do not average until differences are conceptually reconciled.

## Step 8 — Segment the market

Minimum useful cuts:
- micro / small / medium;
- loan size bands;
- term loan / line of credit / overdraft / cards / factoring / leasing / asset-backed;
- secured / unsecured;
- bank / fintech / other nonbank;
- industry;
- firm age;
- existing bank customer vs new-to-bank;
- digital/self-serve vs relationship-led.

## Step 9 — Growth and inflation

For multi-year comparisons:
- state whether values are nominal or real;
- normalize FX when comparing countries;
- separate balance growth caused by new lending from interest, FX or acquisitions where relevant;
- use CAGR only over comparable series.

## Step 10 — Sensitivity

For uncertain bottom-up inputs provide at least:
- conservative;
- base;
- high case.

Show which input drives the variance.

## Preferred source order

1. OECD SME Financing Scoreboard / central banks / regulators.
2. Official bank statistics and bank disclosures.
3. Federal Reserve / FDIC surveys where relevant.
4. Government program data.
5. Reputable industry datasets.
6. Estimates from press/research only as secondary checks.

## Output

1. Market definition.
2. Key source definitions.
3. Stock estimate.
4. Flow estimate.
5. Borrower count estimate.
6. Segment split.
7. Top-down calculation.
8. Bottom-up calculation.
9. Reconciliation.
10. Sensitivity.
11. Known exclusions.
12. Confidence and data gaps.

## Hard rules

- “SME market” is not a universal denominator.
- Never quote TAM/SAM/SOM without showing calculation.
- Do not treat financing gap as the same thing as profitable addressable demand.
- Do not use total corporate lending as SME lending without an explicit filter.
