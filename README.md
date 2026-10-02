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

**Wave 1 — Foundation: завершён**

- Metric dictionary — `docs/metric_dictionary.md` + `data/metric_dictionary.csv`
- Geography shortlist — `docs/geography_shortlist.md`
- Country/SME definitions — `docs/country_sme_definitions.md` + `data/country_sme_definitions.csv`
- Market source inventory — `docs/market_source_inventory.md` + `data/market_source_inventory.csv`
- Player universe schema — `docs/player_universe_schema.md` + `data/player_universe.csv`

Первая географическая волна:
- **Wave A:** US, UK, Brazil, Germany, India
- **Wave B:** Netherlands, Australia, Mexico

**Сейчас: Wave 2 — Market Landscape & Segmentation**

Следующая работа:
1. собрать comparable market metrics по Wave A;
2. построить borrower/product segmentation;
3. начать заполнять universe игроков.

Список найденных и оцененных публичных agent skills: `docs/skill_scout.md`.
