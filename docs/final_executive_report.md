# Executive Report — SME Lending: What Actually Creates Advantage

**Version:** 2026-10-02  
**Scope:** 8 markets, 43-player universe, 18 deep dives  
**Quality standard:** `docs/consulting_quality_standard.md`

---

# Executive summary

The research does not identify one universal “best SME lender.”

It identifies a more useful answer:

> **Advantage in SME lending comes from matching the risk object, data, decision model, funding and customer journey to a specific segment.**

The strongest lenders in the sample do not all look alike.

Some win through:
- proprietary transaction data;
- deposit funding;
- institutional asset distribution;
- tax/e-invoice data;
- empowered relationship bankers;
- guarantees;
- receivables infrastructure.

The common pattern is **fit**, not one technology.

## Five implications for an incumbent lender

1. **Separate existing-customer and new-to-bank credit factories.**
2. **Automate only inside explicit risk/data perimeters.**
3. **Replace documents with machine-readable data before redesigning UI.**
4. **Preserve human judgment where ticket/complexity can economically support it.**
5. **Manage every credit factory on risk-adjusted contribution, not volume or speed alone.**

---

# Exhibit 1 — “SME lending” is at least seven different businesses

## Headline

**One generic SME credit process is structurally wrong: risk, economics and journey change by need and ticket.**

### Evidence

The research identifies seven operating-model segments:

1. transaction-visible micro liquidity;
2. digital unsecured small-business credit;
3. guarantee-backed lending;
4. capex / asset finance;
5. medium/upper-SME relationship lending;
6. receivables/trade finance;
7. embedded merchant credit.

Examples:
- Square/Stone merchant credit;
- iwoca/Floryn digital working capital;
- Itaú/SBI guarantee-backed;
- Judo/Allica relationship credit;
- Bibby factoring.

### Mechanism

Different risk objects
→ different data
→ different decision model
→ different funding/capital
→ different customer journey.

### Implication

Design a **common data/risk platform with multiple credit factories**.

### Watch-out

Do not interpret “multiple factories” as separate organizations. Infrastructure can be shared.

Evidence:
- `docs/borrower_product_segmentation.md`
- `docs/batch3_operating_models_synthesis.md`

---

# Exhibit 2 — The fastest loan journey often begins before the borrower applies

## Headline

**Pre-underwriting turns the application from a data-collection process into an offer-configuration process.**

### Evidence

Observed existing-data models:
- Nubank — recurring eligibility;
- Stone — proactive pre-approved merchant offer;
- Square — daily seller eligibility review;
- Mercado Pago — seller/payment activity creates offers;
- CommBank — eligible existing customers receive conditional approval;
- Amex — select customers can see line/price before full application;
- SBI — PABL/PAsBL use existing transaction behavior.

### Mechanism

Ongoing relationship data
→ continuous underwriting
→ proactive eligibility
→ fewer visible steps
→ faster conversion/funding.

### Implication

For existing customers, the target journey should move toward:

**offer → configure → accept → fund**

rather than:

**application → documents → wait → offer**.

### Watch-out

Sparse/new customers do not get this advantage.

Evidence:
- `docs/visual_customer_journey_atlas.md`
- `docs/batch1_mechanism_synthesis.md`

---

# Exhibit 3 — Data substitution creates more UX value than form redesign

## Headline

**The best digital lenders remove borrower work by retrieving evidence, not by making the same questions prettier.**

### Evidence

Observed substitutions:
- iwoca — Open Banking;
- Floryn — six months bank data, no annual accounts ≤€250k;
- Rabobank — 13 months transaction data inside bounded lane;
- Konfío — SAT/CIEC tax/invoice data;
- SBI — GST/UPI/banking/ITR;
- Stone/Square — acquiring data;
- CommBank/Nubank — existing account data.

### Mechanism

Machine-readable data
→ fewer uploads/manual fields
→ lower underwriting OPEX
→ faster decision
→ better ongoing monitoring.

### Implication

Prioritize:
1. data connections;
2. policy redesign;
3. decision integration;
4. UI.

Not the reverse.

### Watch-out

Country infrastructure determines what data are realistically available.

Evidence:
- `docs/market_infrastructure.md`
- `docs/product_feature_comparison.md`

---

# Exhibit 4 — “Instant” credit is a risk perimeter, not a universal capability

## Headline

**Every credible fast lender has a boundary where richer evidence or human review returns.**

### Evidence

- iwoca: >€50k adds BWA/SuSa.
- Rabobank: no-annual-accounts lane capped at €250k / 5 years plus eligibility rules.
- Floryn: >€250k adds annual accounts and AR/AP.
- SBI: digital product limits redirect larger needs to branch/centralized processes.
- Commerzbank: ≤€100k can be decided in adviser conversation.
- Stone: automated vs dedicated desks.
- CommBank: best instant flow for eligible existing customers.

### Mechanism

Exposure / complexity / weak data rises
→ uncertainty rises
→ value of additional evidence/human judgment rises.

### Implication

Publish and manage explicit:
- ticket thresholds;
- tenor thresholds;
- data-history minimums;
- collateral triggers;
- industry exclusions;
- manual-review triggers.

### Watch-out

Hard thresholds can create adverse-selection “cliffs” and should be monitored.

Evidence:
- `docs/hypothesis_scorecard.md`
- `docs/pattern_library.md`

---

# Exhibit 5 — Human underwriting can be a competitive feature

## Headline

**For larger SME, speed may come from decision rights rather than automation.**

### Evidence

Judo:
- A$14.7bn lending;
- 4,822 lending customers;
- deliberately relationship-led.

Allica:
- digital DIP → underwriter → approval;
- £3.7bn lending;
- profitable growth.

Commerzbank:
- ~2-minute online intake;
- adviser within 48h;
- ≤€100k decision possible directly in consultation.

### Mechanism

Digital preparation
+ experienced decision-maker
+ delegated authority
→ fewer organizational handoffs
→ faster complex decisions.

### Implication

Automate:
- data gathering;
- spreading;
- checks;
- workflow.

Do not automatically remove:
- credit judgment;
- structuring;
- relationship advice.

### Watch-out

Judgment does not eliminate concentration losses; Judo's FY26 impairments rose.

Evidence:
- `docs/risk_economics_benchmark.md`
- company teardowns.

---

# Exhibit 6 — Better data does not guarantee better credit losses

## Headline

**Embedded data can improve observability and collections while underwriting policy can still produce bad vintages.**

### Evidence

Stone Q2 2026:
- credit portfolio R$3.752bn;
- NPL >90: 8.6%;
- cost of risk: 21.5%;
- management cited weaker vintages and dedicated-desk cases.

Stone simultaneously has:
- merchant sales data;
- proactive offers;
- sales-linked repayment.

### Mechanism

Data reduces information latency.

It does not eliminate:
- wrong cutoff;
- rapid growth;
- macro shocks;
- segment concentration;
- large-ticket idiosyncratic risk.

### Implication

Measure digital lending by:
**vintage risk-adjusted contribution**, not speed or approval alone.

### Watch-out

Different NPL/CoR definitions cannot be compared naively across companies.

Evidence:
- `companies/brazil/stone.md`
- `docs/risk_economics_benchmark.md`

---

# Exhibit 7 — Funding is a strategic design choice, not just a treasury input

## Headline

**Non-banks can substitute for deposits through asset distribution and securitisation — if product cash flows are investable.**

### Evidence

- Funding Circle Term Loans — institutional forward flow; 26.4% H1-26 PBT margin.
- Square — majority of Square Loans sold to investors.
- Floryn — €150m private securitisation facility.
- Bibby — >£1.1bn funding capacity with receivables-backed facilities.
- Judo/Allica/large banks — deposit-funded models.
- UGRO — 10.16% borrowing cost shows wholesale-funding constraint.

### Mechanism

Product cash-flow structure
→ determines funding options
→ funding/capital structure
→ affects required customer yield and economics.

### Implication

Choose funding **by product engine**.

### Watch-out

Institutional/market funding can become less available in stress.

Evidence:
- `docs/batch2_economics_risk_synthesis.md`
- `docs/risk_economics_benchmark.md`

---

# Exhibit 8 — High rates do not mean attractive economics

## Headline

**A high-yield SME book can still produce modest returns after funding, loss and OPEX.**

### Evidence

UGRO FY26:
- portfolio yield 17.50%;
- cost of borrowings 10.16%;
- GNPA 2.50%;
- material credit cost/OPEX;
- ROA 2.1%.

Funding Circle:
- Term Loan engine profitable;
- FlexiPay/Card still loss-making in H1-26 despite strong growth.

### Economic bridge

**yield/fees  
− funding  
− credit loss  
− OPEX  
− capital  
+ relationship value  
= risk-adjusted contribution**

### Implication

Competitor benchmarking should never use advertised rates/yields as a profitability proxy.

### Watch-out

Public capital/OPEX allocation is incomplete for many players.

Evidence:
- `docs/risk_economics_benchmark.md`

---

# Exhibit 9 — Existing-customer advantage can become a lifetime-value flywheel

## Headline

**The same data that shortens first credit can make repeat lending structurally cheaper and easier.**

### Evidence

- Amex — reusable line, dynamic review.
- Square — eligibility re-evaluated continuously.
- Nubank — recurring offer eligibility.
- SBI — top-up / preapproved transaction-based products.
- Funding Circle — top-up/multi-product.
- Mercado Pago — renewed offers based on new behavior.

### Mechanism

First loan
→ repayment behavior observed
→ more data / less uncertainty
→ lower re-underwriting burden
→ faster/larger repeat credit
→ higher customer LTV.

### Implication

Build a **repeat credit product**, not merely a repeat application.

Metrics should include:
- repeat share;
- repeat time-to-cash;
- repeat loss;
- repeat contribution;
- limit growth.

### Watch-out

Public repeat-vs-first cohort economics remain a major evidence gap.

Evidence:
- `docs/hypothesis_scorecard.md`
- `docs/remaining_evidence_gaps.md`

---

# Exhibit 10 — Guarantees shift the feasible approval frontier

## Headline

**A digitized government guarantee can improve both access and lender risk economics.**

### Evidence

Itaú:
- government-sponsored SME originations +47.3% QoQ in 2Q26;
- rapid digital FGI channel adoption.

Stone:
- government-backed lines described as lower-risk and requiring lower provision coverage.

SBI:
- public guarantee programs are embedded in MSME architecture.

### Mechanism

Guarantee
→ lower uncovered loss
→ lower collateral constraint
→ different approval threshold / capital economics.

### Implication

Create a distinct guarantee-backed factory:
- automated eligibility;
- tax/revenue pull;
- guarantee validation;
- separate risk/economics tracking.

### Watch-out

Guarantee economics depend on:
- coverage;
- claim process;
- fees;
- capital treatment;
- program stability.

Evidence:
- `docs/pattern_library.md`
- `docs/market_infrastructure.md`

---

# Exhibit 11 — Country infrastructure determines which “best practice” is portable

## Headline

**There is no globally universal alternative-data stack.**

### Evidence

- UK / Netherlands — Open Banking / PSD2.
- Brazil — Open Finance + payments/acquiring.
- India — Account Aggregator + GST + Udyam + UPI.
- Mexico — SAT/e-invoice data.
- Australia — CDR + business authorization.
- US — commercial data-sharing remains more fragmented; private/account/ecosystem data is more important.

### Implication

Before copying a competitor journey, check:
1. data rail;
2. identity rail;
3. guarantee rail;
4. funding rail;
5. legal/consent framework.

### Watch-out

A visual journey can be copied; the data infrastructure behind it often cannot.

Evidence:
- `docs/market_infrastructure.md`
- `data/transferability_matrix.csv`

---

# Exhibit 12 — “Bank vs fintech” is the wrong competitor map

## Headline

**Factories explain competitive behavior better than institution labels.**

### Better taxonomy

## Risk object
- borrower cash flow;
- merchant sales;
- receivables;
- collateral;
- guaranteed exposure.

## Data
- transactions;
- tax/e-invoice;
- acquiring;
- accounting;
- financial statements.

## Decision
- preapproved automated;
- STP + exceptions;
- analyst;
- empowered RM;
- committee.

## Funding
- deposits;
- forward flow;
- investor sale;
- securitisation;
- wholesale.

### Implication

Compare like-for-like **credit factories**, not brands.

Example:
Square may be more comparable with Stone than with another US fintech; Judo may be more comparable with Allica than with an Australian digital lender.

Evidence:
- `docs/batch3_operating_models_synthesis.md`

---

# Exhibit 13 — Target architecture: one platform, multiple credit factories

## Headline

**The strategic end-state is modular, not monolithic.**

### Common platform

- customer identity/KYB;
- transactions;
- bureau;
- tax;
- accounting;
- acquiring;
- invoices;
- collateral;
- consent;
- fraud;
- monitoring.

### Factory A — Existing-customer preapproved
Low visible effort, continuous underwriting.

### Factory B — New-to-bank digital
Machine-readable data + automated exceptions.

### Factory C — Guarantee-backed
Bank underwriting + program risk-sharing.

### Factory D — Medium relationship
Digital prep + empowered RM/underwriter.

### Factory E — Asset/receivables
Specialist collateral/debtor infrastructure.

### Common management framework

Every factory should report:
- approval;
- booked conversion;
- time-to-decision;
- time-to-cash;
- manual-review rate;
- yield;
- funding;
- credit loss;
- OPEX;
- capital;
- repeat value.

---

# Exhibit 14 — Transformation priorities for an incumbent lender

## Headline

**The highest-value transformation sequence starts backstage, not in the UI.**

### Priority 1 — Existing-customer pre-underwriting
Build continuous eligibility from transaction behavior.

### Priority 2 — Data substitution
Integrate:
- bank transactions;
- tax;
- accounting;
- acquiring;
- invoice data.

### Priority 3 — Credit-lane segmentation
Define explicit automated / analyst / RM perimeters.

### Priority 4 — Repeat-credit loop
Dynamic limits and reduced-friction redraw/top-up.

### Priority 5 — Risk-adjusted economics
Measure contribution per factory, not just originations.

### Priority 6 — Guarantee / alternative funding
Use guarantee and asset-distribution structures where economically useful.

---

# Exhibit 15 — What remains genuinely unknown

## Headline

**The biggest remaining gaps are causal economics, not market descriptions.**

Priority unanswered questions:

1. How much cheaper is automated underwriting per booked loan?
2. Are existing-customer loss rates actually lower after controlling for selection?
3. What is repeat-vs-first loan contribution?
4. What is RAROC by automated vs relationship lane?
5. How much does a guarantee improve capital-adjusted return?
6. At what ticket does human underwriting become economically optimal?

These questions cannot be solved by adding more generic competitor features.

They require:
- internal bank data;
- lender cohort disclosures;
- loan-level datasets;
- expert interviews.

---

# Final conclusion

The evidence points to a clear strategic principle:

> **Do not build one SME lending journey. Build a common intelligence layer and multiple credit factories, each optimized for its own risk object, data advantage, ticket, funding and customer economics.**

The customer should experience that complexity as simplicity:

> **Ask only for genuinely new information, make the decision at the lowest economically safe level, and use every repayment event to make the next credit decision better.**

---

# Evidence book

## Market
- `docs/cross_country_market_snapshot.md`
- `docs/market_infrastructure.md`
- `data/market_landscape.csv`

## Company / operating model
- `companies/`
- `docs/batch1_mechanism_synthesis.md`
- `docs/batch2_economics_risk_synthesis.md`
- `docs/batch3_operating_models_synthesis.md`

## Journey
- `docs/visual_customer_journey_atlas.md`
- `data/journey_comparison.csv`

## Product
- `docs/product_feature_comparison.md`
- `data/product_feature_matrix.csv`

## Risk / economics
- `docs/risk_economics_benchmark.md`
- `data/risk_economics_benchmark.csv`

## Transferability
- `docs/hypothesis_scorecard.md`
- `docs/pattern_library.md`
- `data/transferability_matrix.csv`
