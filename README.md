# B2B SME Credit Market Research

Репозиторий для системного исследования рынка кредитования юридических лиц / SME.

## Цель

Построить доказательный market research, который одновременно отвечает на пять групп вопросов:

1. **Рынок** — размер, динамика, сегменты, страны, типы игроков и источники фондирования.
2. **Финансы** — объемы выдач и портфеля, доходность, стоимость фондирования, cost of risk, OPEX, прибыльность и risk-adjusted economics.
3. **Риск и андеррайтинг** — eligibility, данные, скоринг, правила принятия решения, collateral/guarantees, мониторинг, просрочка, NPL/default, provisioning.
4. **Продукты и функциональности** — виды кредитов, лимиты, сроки, pricing, repayment, pre-approval, integrations, servicing, refinancing/top-up и др.
5. **Клиентские пути** — discovery → eligibility → application → data/documents → underwriting → offer → signing → disbursement → servicing → repeat borrowing.

## Research plan

Основной план исследования: **`docs/research_plan.md`**.

Логика проекта:

**Definitions → Market → Segments → Player universe → Deep dives → Product/features → Journey → Underwriting/risk → Economics → Synthesis**

Работа разбита на пять waves и также заведена в GitHub Issues как исполнимый backlog.

## Quality bar

Целевой стандарт — **boardroom-grade strategy research**, сопоставимый по строгости и executive usefulness с сильной работой top-tier strategy consulting teams, без копирования их proprietary материалов.

Стандарт зафиксирован в:
- `docs/consulting_quality_standard.md`

Ключевые требования:
- answer-first;
- hypothesis-driven;
- quantified;
- mechanism-based;
- UX × risk × economics together;
- counter-evidence;
- explicit `So what?`;
- transferability with prerequisites.

## Принцип исследования

Никаких “одна цифра — один источник” и никаких догадок, замаскированных под факт.

Каждый существенный вывод должен иметь:
- географию и период;
- определение SME / продукта / метрики;
- источник и дату источника;
- статус: **fact / calculation / estimate / hypothesis**;
- уровень уверенности;
- при возможности — независимую проверку вторым методом или источником.

Для спорных или высокозначимых выводов используется source triangulation и adversarial review.

## Исследовательские skills

- `skills/deep-research/SKILL.md` — доказательный ресерч, source hierarchy, triangulation, contradiction handling.
- `skills/market-sizing/SKILL.md` — TAM/SAM/SOM и фактический размер кредитного рынка; stock/flow, top-down + bottom-up.
- `skills/competitor-benchmark/SKILL.md` — сравнение банков/финтехов по продуктам, pricing, процессам и позиционированию.
- `skills/lending-economics/SKILL.md` — P&L и unit economics SME-кредитования.
- `skills/credit-risk-underwriting/SKILL.md` — риск, андеррайтинг, monitoring и portfolio quality.
- `skills/product-feature-taxonomy/SKILL.md` — единая таксономия продуктов и функциональностей.
- `skills/customer-journey-reconstruction/SKILL.md` — восстановление реального клиентского пути только по наблюдаемым evidence.
- `templates/company-teardown.md` — стандартный шаблон deep dive по одному игроку.

## Базовые источники методологии

Приоритет у первичных и регуляторных источников:
- EBA — Guidelines on loan origination and monitoring.
- Basel Committee / BIS — Basel Framework, credit risk.
- OCC — Lending and Loan Portfolio Risk Management; underwriting handbooks.
- OECD — Financing SMEs and Entrepreneurs Scoreboard.
- Federal Reserve / Federal Reserve Banks — Small Business Credit Survey и Small Business Lending Survey.
- FDIC — Small Business Lending Survey.
- IFRS / локальные стандарты — impairment / expected credit loss, когда применимо.
- годовые отчеты, Pillar 3, investor presentations и официальные product/help/legal pages исследуемых банков.

## Текущий этап

**Waves 1–5: first research cycle complete**

### Foundation
- Metric Dictionary
- Geography Shortlist
- Country/SME Definitions
- Market Source Inventory
- Player Universe Schema

### Market landscape
- `data/market_landscape.csv`
- `docs/cross_country_market_snapshot.md`
- `docs/market_infrastructure.md`
- `docs/borrower_product_segmentation.md`
- `docs/remaining_evidence_gaps.md`

### Competitive universe
- **43 players** across 8 markets
- **18 deep dives**

### Company research
All 18 first-pass consulting-grade teardowns complete under `companies/`.

### Cross-company synthesis
- `docs/batch1_mechanism_synthesis.md`
- `docs/batch2_economics_risk_synthesis.md`
- `docs/batch3_operating_models_synthesis.md`
- **`docs/executive_synthesis.md`**
- `docs/hypothesis_scorecard.md`
- `docs/pattern_library.md`
- `data/transferability_matrix.csv`

## Current headline

The evidence does not support one universal “best SME lender.”

The emerging architecture is:

**customer/need × risk object × observable data × decision model × funding/capital model**

with multiple credit factories sharing a common data/risk platform.

## Final decision artifacts

Completed:
- **Final Executive Report** — `docs/final_executive_report.md`
- **Visual Customer Journey Atlas** — `docs/visual_customer_journey_atlas.md`
- **Product / Feature Comparison** — `docs/product_feature_comparison.md`
- **Risk / Economics Benchmark** — `docs/risk_economics_benchmark.md`
- **Final Evidence Index** — `docs/final_evidence_index.md`

Machine-readable supporting datasets:
- `data/journey_comparison.csv`
- `data/product_feature_matrix.csv`
- `data/risk_economics_benchmark.csv`
- `data/transferability_matrix.csv`

**First complete research cycle: finished.**

The highest-value next enrichment is **first-party customer-screen coverage** for journeys that are currently documented mainly through official text/workflow illustrations. Broad market-data filling should remain deprioritized unless a specific decision exhibit requires it.



## Design synthesis

The research has now been translated into a generic incumbent-bank design blueprint:

- **Target Operating Model Blueprint** — `docs/target_operating_model_blueprint.md`
- **Opportunity Map** — `data/opportunity_map.csv`
- **Target KPI Tree** — `data/target_kpi_tree.csv`

The default architecture is:

**one reusable customer/data/decision layer + multiple risk-specific credit factories + one risk-adjusted economics framework.**

The sequencing is intentionally generic and must be re-scored with internal bank data before becoming a bank-specific implementation plan.


## Implementation toolkit

The project now also contains a complete generic path from target model to execution:

- `docs/credit_factory_implementation_blueprints.md`
- `data/capability_dependency_map.csv`
- `docs/implementation_backlog.md`
- `data/implementation_backlog.csv`
- `docs/credit_factory_routing_logic.md`
- `data/factory_routing_rules.csv`
- `docs/governance_decision_rights.md`
- `data/governance_raci.csv`
- `docs/lender_archetype_playbooks.md`

Together with the diagnostic, business-case and pilot toolkit, this makes the external-research layer effectively complete. The next bank-specific step is parameterization with internal data rather than more generic market collection.
