# Player Universe Schema

Version date: 2026-10-02.

## Purpose

The player universe is the broad lender map used **before** selecting deep-dive companies.

Target size for Wave 2:
- approximately **40–60 players** across the eight first-wave markets;
- then shortlist **12–18** for full teardown.

The universe is not a ranking.

Its job is to:
- show which lender archetypes actually exist;
- avoid selecting only famous brands;
- capture scale and business-model evidence;
- identify where we have strong public financial/risk data;
- identify where customer journeys and client screens can realistically be reconstructed.

---

# 1. Entity identity

## player_id
Stable project identifier.

Recommended format:
`COUNTRY_COMPANY_SLUG`

Example:
`BR_NUBANK`

## company_name
Public brand / commonly used lender name.

## legal_entity
Relevant lending legal entity where known.

## parent_group
Parent financial group if applicable.

## country
Primary market being analyzed.

A multinational lender appears as a separate country-market record when the product/journey differs materially by geography.

## website
Official country/product URL.

---

# 2. Lender archetype

Controlled values:

- `universal_bank`
- `regional_bank`
- `community_bank`
- `sme_specialist_bank`
- `digital_bank`
- `fintech_balance_sheet_lender`
- `fintech_originator_marketplace`
- `embedded_lender`
- `payments_or_acquiring_lender`
- `invoice_factoring_specialist`
- `asset_equipment_finance`
- `government_development_lender`
- `credit_union_cooperative`
- `other`

Multiple archetypes may be stored in a separate notes field, but one primary archetype is required.

## regulatory_type
Examples:
- bank;
- NBFC/non-bank financial company;
- credit institution;
- payment institution;
- broker/marketplace;
- development bank;
- other.

Do not infer license type from branding.

---

# 3. Target borrower

## target_segment

Controlled multi-value field:
- self_employed;
- micro;
- small;
- medium;
- upper_sme;
- lower_middle_market.

## borrower_definition
Exact lender/source definition if available.

## existing_customer_requirement

Controlled:
- existing_only;
- existing_preferred;
- open_market;
- unknown.

## minimum_business_age
Value + unit.

## revenue_eligibility
Text/raw threshold from source.

## industries_excluded
Text / normalized tags.

---

# 4. Scale

Store current value and period/source separately.

## business_customers
Business customer count.

## sme_borrowers
Active SME borrower count.

## loan_book
Outstanding relevant business/SME credit.

## originations
New lending / disbursements during period.

## geography_scope
Country-only / region / global value.

## scale_confidence
- high
- medium
- low
- unknown

Important:
- company-wide business customers are not automatically SME borrowers;
- total business loan book is not automatically SME loan book.

---

# 5. Product families

Controlled multi-value field:

- unsecured_term_loan
- secured_term_loan
- revolving_line
- overdraft
- business_credit_card
- invoice_finance
- factoring
- merchant_cash_advance
- revenue_based_finance
- asset_equipment_finance
- commercial_real_estate
- trade_finance
- government_guaranteed_loan
- embedded_credit
- other

## min_amount
## max_amount
## min_term
## max_term

Only populate normalized values if product definitions are comparable.

---

# 6. Risk/security profile

## secured_focus
Controlled:
- mostly_unsecured
- mixed
- mostly_secured
- product_dependent
- unknown

## personal_guarantee
- required
- sometimes
- no_public_requirement
- unknown

## government_guarantee_use
- yes
- no
- unknown

## public_risk_metrics_available
- strong
- partial
- weak
- none_known

## disclosed_risk_metrics
Examples:
- NPL
- 30+ DPD
- 90+ DPD
- cost of risk
- charge-offs
- Stage 2/3
- vintage losses

---

# 7. Funding model

Controlled primary value:

- retail_deposits
- business_deposits
- wholesale_funding
- warehouse_facility
- securitization
- bond_market
- equity_balance_sheet
- partner_bank
- originate_to_distribute
- government_funding
- mixed
- unknown

## funding_notes
Free text for material structural details.

This field is important for later lending-economics comparison.

---

# 8. Distribution model

Controlled multi-value:

- branch
- relationship_manager
- web_self_service
- mobile_self_service
- broker
- accountant_partner
- marketplace
- embedded_partner
- payments_ecosystem
- ecommerce_ecosystem
- outbound_sales
- other

## primary_distribution
One main channel.

---

# 9. Underwriting/data advantage

## decision_model

Controlled:
- automated
- automated_plus_manual_exceptions
- rules_plus_analyst
- relationship_led
- credit_committee_led
- product_dependent
- unknown

## underwriting_data

Controlled multi-value:
- financial_statements
- management_accounts
- bank_transactions
- open_banking
- accounting_data
- tax_data
- bureau
- trade_credit
- owner_guarantor_bureau
- acquiring_data
- ecommerce_data
- invoice_data
- payroll_data
- collateral
- relationship_history
- registry_data
- unknown

Only list as evidenced if public evidence exists.

## proprietary_data_advantage
Short text.

Examples:
- acquiring history;
- current-account transactions;
- marketplace GMV;
- payment processing;
- accounting ecosystem.

## data_advantage_confidence
high / medium / low / unknown.

---

# 10. Digital / customer journey

## digital_application
- yes
- partial
- no
- unknown

## preapproved_offer
- yes
- no
- unknown

## stated_decision_sla
Raw lender claim.

## stated_cash_sla
Raw lender claim.

Never convert stated SLA to observed SLA.

## servicing_self_service
- strong
- partial
- weak
- unknown

## journey_researchability

Controlled:
- high
- medium
- low

Factors:
- public application flow;
- app availability;
- help center;
- demos/videos;
- ability to start application without being an existing customer;
- screenshots available.

## screen_evidence_potential

Controlled:
- high
- medium
- low
- unknown.

## screen_evidence_found
- yes
- partial
- no_yet.

This is a universe-level flag only. Full screen catalog belongs in the company teardown.

---

# 11. Economics / disclosure quality

## public_financial_disclosure

Controlled:
- strong_segment_disclosure
- company_level_only
- limited
- private_minimal
- unknown.

## sme_specific_economics_available
yes / partial / no / unknown.

## funding_cost_observable
yes / proxy / no.

## credit_cost_observable
yes / proxy / no.

## capital_observable
yes / proxy / no.

---

# 12. Source quality

## primary_sources_count
Count of relevant primary sources found.

## source_quality

Controlled:
- high
- medium
- low.

High means:
- official product evidence; and
- financial/regulatory source; and
- enough information to distinguish product/segment definitions.

## latest_source_date
Latest meaningful source date.

## key_source_1
## key_source_2
## key_source_3

Prefer primary URLs.

---

# 13. Research selection

## research_priority

Controlled:
- A
- B
- C

Meaning:

### A
High-value candidate for deep dive:
- distinctive archetype or mechanism;
- meaningful scale or strategic relevance;
- sufficient evidence.

### B
Useful comparison / archetype coverage.

### C
Keep in universe but low current evidence or redundant archetype.

This is **research priority**, not lender quality.

## shortlist_status

Controlled:
- universe_only
- candidate
- shortlisted
- deferred
- excluded_from_deep_dive.

## selection_hypothesis

Why this lender helps test the project.

Examples:
- existing-customer data advantage;
- ultra-fast new-to-bank lending;
- deposit-funded digital lending;
- embedded/acquiring underwriting;
- larger-ticket relationship lending;
- transparent public risk economics.

## deep_dive_rationale
Populated when shortlisted.

---

# 14. Evidence status rules

For fields that are not known:

Use:
- `unknown`

Do **not** use:
- empty string when we actually checked and found no evidence;
- `no` when absence has not been verified.

Recommended distinction:

- `unknown` = not established;
- `no_public_evidence` = checked, but no evidence found;
- `no` = reliable evidence that capability is absent.

---

# 15. CSV schema

The machine-readable starter is:
`data/player_universe.csv`

The first collection pass should prioritize:

1. identity;
2. archetype;
3. target segment;
4. products;
5. approximate scale;
6. funding;
7. distribution;
8. data/underwriting advantage;
9. journey researchability / screen potential;
10. disclosure quality;
11. research priority.

Do not attempt full teardown fields inside the universe.

---

# 16. Shortlisting rule

A lender should enter the 12–18 company deep-dive shortlist because it adds **distinct evidence**, not simply because it is large.

The shortlist as a whole should cover:

- incumbents;
- digital banks;
- fintech lenders;
- embedded/payment-led lenders;
- specialists;
- multiple ticket sizes;
- existing-customer and new-to-bank journeys;
- secured and unsecured lending;
- strong and weak public-disclosure environments;
- at least several lenders where screen-based journey reconstruction is feasible.

---

# Status

Schema ready for Wave 2 population.
