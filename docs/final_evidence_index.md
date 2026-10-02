# Final Evidence Index

**Version:** 2026-10-02

## Purpose

Single navigation page for the first complete research cycle.

---

# 1. Start here

## Executive report
`docs/final_executive_report.md`

## Executive synthesis
`docs/executive_synthesis.md`

Use:
- final boardroom conclusions;
- management discussion;
- storyline for future presentation.

---

# 2. Market layer

## Cross-country snapshot
`docs/cross_country_market_snapshot.md`

## Long-form source data
`data/market_landscape.csv`

## Market infrastructure
`docs/market_infrastructure.md`
`data/market_infrastructure.csv`

## SME definitions
`docs/country_sme_definitions.md`
`data/country_sme_definitions.csv`

## Source inventory
`docs/market_source_inventory.md`
`data/market_source_inventory.csv`

## Remaining gaps / stop rules
`docs/remaining_evidence_gaps.md`

---

# 3. Segmentation / universe

## Borrower × need × product
`docs/borrower_product_segmentation.md`
`data/borrower_product_segments.csv`

## Player universe
`docs/player_universe_schema.md`
`data/player_universe.csv`

## Deep-dive shortlist
`docs/deep_dive_shortlist.md`

---

# 4. Company evidence book

## Brazil
- `companies/brazil/nubank.md`
- `companies/brazil/stone.md`
- `companies/brazil/itau.md`

## United States
- `companies/us/american_express_bloc.md`
- `companies/us/square_loans.md`

## United Kingdom
- `companies/uk/funding_circle.md`
- `companies/uk/allica.md`
- `companies/uk/bibby_financial_services.md`

## Germany
- `companies/germany/iwoca.md`
- `companies/germany/commerzbank.md`

## India
- `companies/india/sbi.md`
- `companies/india/ugro.md`

## Netherlands
- `companies/netherlands/rabobank.md`
- `companies/netherlands/floryn.md`

## Australia
- `companies/australia/commbank.md`
- `companies/australia/judo.md`

## Mexico
- `companies/mexico/konfio.md`
- `companies/mexico/mercado_pago.md`

---

# 5. Cross-company synthesis

## Batch 1 — mechanism
`docs/batch1_mechanism_synthesis.md`

## Batch 2 — economics/risk
`docs/batch2_economics_risk_synthesis.md`

## Batch 3 — operating models
`docs/batch3_operating_models_synthesis.md`

---

# 6. Customer journey / screens

## Visual Atlas
`docs/visual_customer_journey_atlas.md`

## Screen evidence audit / acquisition backlog
`docs/screen_evidence_audit.md`

## Normalized journey data
`data/journey_comparison.csv`

Important:
- only official/first-party screens are treated as screen evidence;
- missing evidence is explicitly marked.

---

# 7. Products / features

## Mechanism-based comparison
`docs/product_feature_comparison.md`

## Matrix
`data/product_feature_matrix.csv`

---

# 8. Risk / economics

## Benchmark
`docs/risk_economics_benchmark.md`

## Data
`data/risk_economics_benchmark.csv`

Rule:
never compare rows without checking `scope` and `comparison_status`.

---

# 9. Hypotheses / patterns / transferability

## Hypothesis scorecard
`docs/hypothesis_scorecard.md`

## Pattern library
`docs/pattern_library.md`

## Transferability matrix
`data/transferability_matrix.csv`

---

# 10. Methodology

## Research plan
`docs/research_plan.md`

## Consulting quality standard
`docs/consulting_quality_standard.md`

## Metric dictionary
`docs/metric_dictionary.md`
`data/metric_dictionary.csv`

## Company template
`templates/company-teardown.md`

---

# 11. Evidence-status summary

## High-confidence operating-model conclusions
- multiple credit factories;
- pre-underwriting existing customers;
- data substitution;
- bounded automation;
- human decision-rights value;
- funding architecture by product;
- guarantee-backed distinct economics.

## Medium-confidence / still under-quantified
- repeat-loan economic uplift;
- existing-vs-new risk difference;
- automated-vs-manual cost advantage;
- comparable RAROC;
- guarantee capital-adjusted uplift.

## Intentionally not produced
- country SME “ranking”;
- company “best lender” ranking;
- synthetic NPL ranking;
- synthetic approval ranking;
- synthetic interest-rate ranking.

Reason:
definitions are not sufficiently comparable.

---

# 12. Recommended reading order

For executive reader:
1. `docs/final_executive_report.md`
2. `docs/visual_customer_journey_atlas.md`
3. `docs/risk_economics_benchmark.md`

For strategy/product:
1. `docs/executive_synthesis.md`
2. `docs/product_feature_comparison.md`
3. `docs/pattern_library.md`
4. `data/transferability_matrix.csv`

For CRO:
1. `docs/risk_economics_benchmark.md`
2. company teardowns
3. `docs/hypothesis_scorecard.md`

For research/audit:
1. Metric Dictionary
2. Market Source Inventory
3. long-form CSVs
4. company primary-source sections.
