# SME Lending Business Case Framework

**Purpose:** quantify value-at-stake for the target operating model once internal bank data are available.

---

# 1. Total value bridge

For each proposed change:

**Incremental revenue**
+ **funding / capital benefit**
+ **OPEX savings**
+ **credit-loss benefit**
+ **relationship / repeat value**
− **incremental losses**
− **incremental funding**
− **incremental capital**
− **build / run cost**
= **net economic value**

Do not count the same benefit twice.

---

# 2. Existing-customer pre-approved lane

## Revenue uplift

Potential channels:
- more eligible customers reached;
- higher offer conversion;
- higher utilization;
- higher repeat.

### Formula

`incremental booked volume = eligible base × incremental offer penetration × offer acceptance × average utilization`

`incremental net revenue = incremental average balance × net revenue margin`

## OPEX benefit

`applications shifted to STP × manual underwriting cost avoided`

## Risk effect

Compare existing vs new and automated vs manual cohorts **after controlling for risk/ticket**.

## Relationship effect

Optional:
- deposit retention;
- payments/acquiring;
- card usage;
- cross-sell.

Do not attribute all customer relationship revenue to credit.

---

# 3. Machine-readable data substitution

## OPEX

`documented cases avoided × document-processing cost`

plus:

`manual-review reduction × underwriter cost per review`

## Conversion

`applications × completion uplift × approval × acceptance × contribution per booked loan`

## Risk

Measure:
- incremental predictive lift;
- decline/approve reclassification;
- loss by score band.

---

# 4. Automation perimeter

Optimize ticket threshold by comparing:

For each ticket band:

`manual underwriting cost`

versus

`expected incremental loss from automation + model/fraud cost`

Automation is valuable where:

**cost saved + conversion benefit > incremental credit loss + implementation/run cost**

---

# 5. Repeat dynamic limit

## CAC / underwriting benefit

`repeat bookings × (first-loan acquisition+underwriting cost − repeat cost)`

## Revenue

`incremental repeat utilization × contribution margin`

## Risk

Track:
- repeat vintage loss;
- limit growth;
- performance after limit increases.

---

# 6. Relationship workflow redesign

## Productivity

`incremental decisions per underwriter × contribution per decision`

or

`FTE capacity released × fully loaded cost`

## Conversion / revenue

Shorter cycle may increase:
- borrower acceptance;
- win rate;
- share of wallet.

Measure with:
- pre/post;
- pilot/control;
- cohort comparisons.

---

# 7. Guarantee-backed lane

## Incremental approval

`eligible declined/limited borrowers × incremental approval with guarantee × booked contribution`

## Risk benefit

`gross loss − guarantee recovery − guarantee fees − claim friction`

## Capital

Apply actual regulatory/economic capital treatment.

Do not assume guarantee coverage equals capital benefit.

---

# 8. Product-specific funding / distribution

## Funding benefit

`asset balance × (internal FTP − external/distribution all-in cost)`

Adjust for:
- sale discount/premium;
- servicing retained;
- credit retention;
- liquidity;
- hedging;
- capital.

## Capital benefit

`capital released × cost of capital`

---

# 9. Receivables finance

## Revenue

- financing spread;
- service/collection fees;
- bad-debt protection fee.

## Cost

- funding;
- debtor credit;
- fraud;
- operations;
- collections.

## Value

Compare against ordinary unsecured working capital for eligible B2B customers.

---

# 10. Business-case confidence levels

## High
Direct internal historical evidence.

## Medium
Internal analog / pilot evidence.

## Low
External benchmark transferred with assumptions.

Every benefit line should carry:
- source;
- assumption;
- confidence;
- sensitivity.

---

# 11. Sensitivity set

At minimum test:
- conversion uplift;
- STP rate;
- loss delta;
- funding cost;
- CAC/OPEX saving;
- utilization;
- capital charge.

Avoid a single “base case” without downside/upside.

---

# 12. Recommended decision metric

Primary:
**risk-adjusted incremental value**

Supporting:
- payback;
- NPV;
- capital consumption;
- loss volatility;
- strategic/customer value.

Avoid optimizing purely for:
- approval;
- speed;
- originations.
