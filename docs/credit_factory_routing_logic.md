# Credit Factory Routing Logic

**Version:** 2026-10-02  
**Purpose:** define how SME credit requests should be routed into different underwriting factories.

> This is a generic routing blueprint. Numeric thresholds must be calibrated to internal portfolio economics and risk appetite.

---

# Executive answer

Routing should be based on **what makes the risk observable and what level of decision effort is economically justified**.

The primary routing dimensions are:

1. existing relationship;
2. data depth;
3. ticket / tenor;
4. collateral / structure complexity;
5. receivables / asset basis;
6. guarantee eligibility;
7. merchant / acquiring visibility;
8. legal / ownership complexity.

The routing logic should produce one of:

- **A — Existing-customer pre-approved**
- **B — New-to-bank digital cash-flow**
- **C — Guarantee-backed**
- **D — Medium / upper-SME relationship**
- **E — Receivables / asset-backed**
- **F — Embedded merchant**
- **Manual specialist review / decline**

---

# 1. Top-level routing tree

## Step 1 — Is the requested financing fundamentally receivables / asset based?

### Yes
Route to **E — Receivables / asset-backed** if:
- valid B2B receivables exist; or
- identifiable financeable asset / collateral is the primary risk object.

Do not force these cases through generic unsecured cash-flow credit.

### No
Proceed.

---

## Step 2 — Is the customer visible through high-frequency merchant/acquiring/platform data?

### Yes
If:
- merchant sales are sufficiently observable;
- use case is short/medium working capital;
- product can be embedded in operating surface;

consider **F — Embedded merchant**.

If ticket/complexity exceeds merchant-credit perimeter:
route to D or E.

### No
Proceed.

---

## Step 3 — Is this an existing customer with sufficient behavioral history?

### Yes
Test eligibility for **A — Existing-customer pre-approved**.

Required:
- minimum relationship history;
- stable transaction evidence;
- current KYB;
- no recent adverse events;
- simple enough ownership/structure;
- ticket inside automated perimeter.

If outside perimeter:
- guaranteed case → C;
- larger/complex → D;
- new asset-specific need → E.

### No
Proceed.

---

## Step 4 — Is machine-readable external cash-flow data sufficient?

Examples:
- Open Banking;
- tax/e-invoice;
- accounting;
- bureau/registry.

### Yes
If:
- ticket within digital perimeter;
- simple legal/ownership structure;
- unsecured / lightly secured;
- data history sufficient;

route to **B — New-to-bank digital cash-flow**.

If data are incomplete:
- request fallback documents; or
- refer to D.

### No
Proceed.

---

## Step 5 — Is the borrower eligible for a guarantee scheme that materially changes feasibility?

### Yes
Route to **C — Guarantee-backed** if:
- ordinary bank policy is otherwise viable;
- guarantee addresses collateral/uncovered-risk constraint;
- scheme economics remain attractive.

### No
Proceed.

---

## Step 6 — Is the exposure large / complex enough to economically justify human judgment?

Signals:
- larger ticket;
- bespoke tenor;
- multiple entities;
- collateral;
- covenants;
- projections;
- acquisition/refinancing;
- complex ownership;
- sector nuance.

### Yes
Route to **D — Medium / upper-SME relationship**.

### No
If neither A/B/C/E/F applies:
- specialist review;
- or decline due to insufficient data / non-standard risk.

---

# 2. Routing logic by dimension

## Relationship

### Strong existing relationship
Potentially A.

### New customer
Potentially B/D/E/C depending risk object and data.

### Existing customer with weak activity
Do not treat as A automatically.

Relationship must mean **observable behavior**, not merely account age.

---

# 3. Data sufficiency

## Level 0 — Sparse
- registry only;
- borrower-entered data.

Not enough for automated cash-flow credit.

## Level 1 — Static documents
- financial statements;
- uploaded bank statements.

Suitable for D / manual B.

## Level 2 — Machine-readable periodic
- accounting;
- tax;
- bureau.

Supports B.

## Level 3 — High-frequency relationship
- own-account;
- acquiring;
- marketplace.

Supports A/F.

Routing should respond to **data quality**, not only source existence.

---

# 4. Ticket / complexity routing

Numeric values must be calibrated internally.

Use at least four ticket bands:

## T1 — Micro / low
Preferred:
- A, B, F.

Avoid:
- high manual effort.

## T2 — Small
Preferred:
- A/B;
- C where guarantee relevant.

## T3 — Medium
Preferred:
- B if data/risk still standardized;
- C;
- D where structure grows.

## T4 — Large / bespoke
Preferred:
- D/E.

The key threshold is not only amount.

Use:
**ticket × tenor × uncertainty × collateral × ownership complexity**.

---

# 5. Guarantee routing rule

Guarantee should not be the default for every eligible borrower.

Use it when:

**incremental approval / loss / capital benefit > guarantee fee + operational friction + program constraints**

Possible routes:

### Route C1 — Guarantee enables approval
Ordinary policy would decline / constrain for collateral or uncovered risk.

### Route C2 — Guarantee improves terms
Ordinary policy approves, but guarantee changes:
- amount;
- tenor;
- collateral;
- price.

### Route C3 — No guarantee
If ordinary economics are better without it.

---

# 6. Receivables / asset routing rule

Route to E where repayment/recovery is primarily linked to:

- invoices;
- receivables;
- equipment;
- property;
- other identifiable asset.

Do not evaluate only borrower PD.

Need additional dimensions:
- debtor quality;
- asset value;
- concentration;
- dilution;
- enforceability;
- fraud.

---

# 7. Embedded merchant routing rule

Route to F only if:
- enough sales history;
- data coverage high;
- merchant operates in bank/platform surface;
- repayment integration exists or can be controlled.

If merchant data are partial:
use as supplementary data in A/B rather than create a false embedded-credit lane.

---

# 8. Human referral rules

Referral should be **reason-coded**, not a generic manual queue.

Examples:

- insufficient data history;
- high concentration;
- ownership complexity;
- unusual sector;
- collateral;
- amount above threshold;
- tenor above threshold;
- bureau conflict;
- revenue mismatch;
- model uncertainty;
- guarantee exception;
- fraud review.

Every referral reason should map to:
- owner;
- required evidence;
- SLA;
- next possible state.

---

# 9. Decline rules

Decline should be separate from referral.

Decline only where:
- policy prohibits;
- affordability fails;
- fraud/identity fails;
- risk exceeds appetite;
- business/information cannot become decisionable.

Do not use “manual review” as hidden decline.

---

# 10. Routing examples

## Example 1
Existing current-account customer, 24 months history, stable inflows, modest WC request, no collateral.

→ **A Existing-customer pre-approved**

## Example 2
New borrower, 3 years trading, Open Banking connected, standardized unsecured request.

→ **B New-to-bank digital**

## Example 3
Existing small business has sufficient cash flow but inadequate collateral; government guarantee available.

→ **C Guarantee-backed**

## Example 4
Established manufacturer requests larger capex/refinancing facility with collateral and projections.

→ **D Relationship**

## Example 5
B2B wholesaler has large diversified receivables book and long customer payment terms.

→ **E Receivables**

## Example 6
Merchant processes most sales through bank acquiring and needs short-duration working capital.

→ **F Embedded merchant**

---

# 11. Routing quality KPIs

Track by route:

- share routed;
- approval;
- booked conversion;
- manual referral;
- re-routing;
- decision time;
- loss;
- OPEX;
- economics.

Critical metric:

**re-routing rate**

High re-routing implies:
- poor segmentation;
- wrong thresholds;
- inadequate data;
- unclear factory ownership.

---

# 12. Threshold optimization

Every threshold should be reviewed using:

- conversion just below/above;
- loss just below/above;
- manual cost;
- customer abandonment;
- risk-adjusted contribution.

Good candidates for quasi-experimental analysis:
- ticket threshold;
- tenure threshold;
- data-history threshold.

Avoid permanent legacy thresholds with no economic evidence.

---

# 13. Routing governance

## Product
Defines customer need / journey.

## Risk
Defines eligibility/perimeter.

## Finance
Validates economics.

## Operations
Validates exception capacity.

## Technology/Data
Ensures required signals are available.

No routing rule should be owned solely by front-end product management.

---

# Final principle

A customer should not choose the underwriting factory.

The bank should infer the right factory from:

> **relationship + risk object + data + exposure + structure + guarantee context**

and present the simplest viable journey.
