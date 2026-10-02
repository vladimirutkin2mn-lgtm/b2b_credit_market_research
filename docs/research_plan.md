# Research Plan — B2B / SME Lending Market

Дата версии: 2026-10-02.

## 1. Главный вопрос исследования

Как устроен рынок кредитования юридических лиц / SME, какие бизнес-модели и продуктовые модели работают лучше в разных сегментах, за счет чего игроки зарабатывают, как они управляют риском и какие продуктовые/процессные решения создают лучший клиентский опыт?

Исследование должно привести не к каталогу банков, а к пониманию:

1. **Где находится экономически привлекательный рынок?**
2. **Какие сегменты заемщиков и кредитные продукты наиболее важны?**
3. **Какие типы игроков выигрывают в каждом сегменте и почему?**
4. **Как устроена экономика SME lending: yield, funding, credit loss, OPEX, capital?**
5. **Какие underwriting/data capabilities позволяют выдавать быстро без неприемлемого риска?**
6. **Как выглядит лучший доступный клиентский путь?**
7. **Какие product/features действительно дифференцируют игроков?**
8. **Какие практики переносимы между странами и бизнес-моделями, а какие завязаны на локальную инфраструктуру/регуляцию?**

---

# 2. Принцип построения исследования

Исследование идет сверху вниз:

**Definitions → Market → Segments → Player universe → Deep dives → Product/features → Journey → Underwriting/risk → Economics → Synthesis**

Почему именно так:

- нельзя корректно сравнить игроков, пока не выровнены определения;
- нельзя выбрать правильные компании для deep dive, пока нет universe;
- нельзя оценить привлекательность продукта только по UX — нужна экономика и риск;
- нельзя назвать практику transferable, не понимая local enablers: bureau, open banking, guarantees, funding, regulation.

---

# 3. Единица анализа

Мы сознательно не используем “SME lending” как один однородный рынок.

Каждое наблюдение должно быть привязано минимум к четырем координатам:

**Market × Borrower segment × Product × Lender archetype**

## Market
Страна / регуляторный рынок.

## Borrower segment
Рабочая сегментация:

- self-employed / sole proprietor — отдельно, если рынок включает;
- micro business;
- small business;
- medium business;
- upper-SME / lower-middle-market — при необходимости.

При наличии данных используем одновременно:
- annual revenue;
- employees;
- legal form;
- firm age;
- existing/new-to-bank.

## Product
Минимальный набор:

- unsecured term loan;
- secured term loan;
- revolving line / overdraft;
- business credit card;
- invoice finance / factoring;
- merchant / revenue-based finance;
- equipment / asset finance;
- commercial real-estate secured lending;
- government-guaranteed lending;
- embedded credit.

## Lender archetype

- universal bank;
- SME-focused/specialist bank;
- digital bank / neobank;
- fintech balance-sheet lender;
- marketplace/originator;
- embedded lender;
- factoring / asset-finance specialist;
- payment/acquiring player lending on proprietary transaction data.

---

# 4. Фаза 0 — Definitions & Research Operating System

## Цель

Сделать будущие цифры и сравнения сопоставимыми.

## Вопросы

- Что в каждой стране означает SME?
- Какие продукты входят в “business lending”?
- Что считается outstanding stock, new lending, origination, approval, default, NPL?
- Как будем сравнивать IFRS 9 и CECL reporting?
- Как нормализуем валюту, период и inflation?
- Какие показатели берем как primary, а какие только как proxy?

## Deliverables

### 0.1 Metric dictionary
Для каждой метрики:
- canonical name;
- formula;
- denominator;
- allowed aliases;
- запрещенные смешения;
- preferred source.

### 0.2 Country definition table
Для каждого рынка:
- statutory SME definition;
- statistical definition;
- bank/reporting definition;
- расхождения.

### 0.3 Evidence standard
Уже заложен в:
- `skills/deep-research/SKILL.md`
- `docs/source_registry.md`

## Exit criteria

Можно однозначно объяснить, почему две цифры можно или нельзя сравнивать.

---

# 5. Фаза 1 — Global Market Map

## Цель

Понять структуру рынка до выбора компаний для deep dive.

Важно: не пытаться получить один “глобальный TAM SME lending”, если источники несопоставимы.

## Для каждого выбранного рынка собираем

### Scale
- number of SMEs;
- number / share of borrowing SMEs;
- SME loan stock;
- annual new lending/originations;
- SME share of total business lending;
- bank vs nonbank share where available.

### Growth
- 3–5 year growth of stock;
- 3–5 year growth of new lending;
- structural breaks;
- nominal vs real growth.

### Pricing
- average SME borrowing rate;
- spread vs policy/risk-free/reference rate;
- fee evidence where available.

### Credit quality
- NPL/default/delinquency;
- cost of risk / write-offs where system-level data exists.

### Demand and access
- application rate;
- approval / partial approval;
- rejection;
- discouraged borrowers;
- financing gap;
- reasons for borrowing.

### Market infrastructure
- credit bureaus;
- open banking / open finance;
- digital identity;
- company registry quality;
- tax/accounting data access;
- guarantee programs;
- securitization / alternative funding.

## Deliverable

`market_landscape` — одна comparable country table + country notes.

## Exit criteria

Мы можем ответить:
- какие рынки большие;
- какие быстро растут;
- где есть credit access gap;
- где digital underwriting легче/сложнее;
- какие рынки стоит изучать глубже.

---

# 6. Фаза 2 — Borrower & Product Segmentation

## Цель

Понять, какие сегменты принципиально отличаются по risk/economics/journey.

## Основные разрезы

### Borrower
- revenue band;
- firm age;
- industry;
- legal form;
- owner concentration;
- existing vs new-to-lender.

### Credit need
- short-term working capital;
- seasonal cash gap;
- growth investment;
- equipment;
- receivables financing;
- emergency liquidity;
- property/capex.

### Ticket size
Создаем общие bands после просмотра реальных распределений, а не заранее навязываем универсальные пороги.

### Risk model
- cash-flow based;
- collateral based;
- relationship based;
- transaction-data based;
- invoice/asset based;
- guarantee-backed.

## Deliverable

**Segment map:** borrower × need × product × typical underwriting model.

## Exit criteria

Понятно, какие продукты действительно конкурируют друг с другом за одну и ту же потребность.

---

# 7. Фаза 3 — Player Universe

## Цель

Сначала построить достаточно широкий universe, затем выбрать репрезентативные deep dives.

## Universe fields

Для каждого игрока:

- country;
- lender archetype;
- target SME segment;
- product families;
- approximate business customer base;
- approximate SME loan book;
- originations if available;
- funding model;
- secured/unsecured focus;
- digital/self-service level;
- distribution model;
- notable proprietary data advantage;
- profitability / scale evidence;
- source quality;
- research priority.

## Размер universe

Ориентир: **40–60 игроков**, если доступность данных позволяет.

Это не значит 40–60 deep dives. Universe нужен, чтобы не выбирать победителей заранее.

## Shortlist для deep dive

Ориентир: **12–18 компаний**.

Выбирать не только по размеру, а по архетипам:

- scaled traditional leader;
- strong digital incumbent;
- digital bank;
- SME specialist;
- high-growth fintech;
- embedded lender;
- transaction-data lender;
- invoice/asset specialist;
- интересный emerging-market case;
- игрок с сильным public disclosure по risk/economics.

## Правило отбора

В shortlist должны попасть компании, которые помогают проверить разные гипотезы, а не только самые известные бренды.

## Deliverable

`player_universe` + documented shortlist rationale.

---

# 8. Фаза 4 — Company Deep Dives

Для shortlist используем единый:
`templates/company-teardown.md`

## На каждого игрока собираем девять блоков

1. **Scale**
2. **Business model**
3. **Products**
4. **Features**
5. **Customer journey**
6. **Underwriting**
7. **Portfolio risk**
8. **Lending economics**
9. **Strategic moat / structural advantages**

## Главное правило

Deep dive должен объяснять механизм.

Недостаточно:
> “Компания быстро одобряет кредиты.”

Нужно:
> “Компания использует X data source, Y borrower population, Z decision architecture; заявленный SLA — N; evidence реального SLA — ...; портфельный risk outcome — ...; поэтому скорость, вероятно, поддерживается следующими structural enablers ...”

Последняя причинная часть при отсутствии прямого evidence маркируется как hypothesis.

---

# 9. Фаза 5 — Product & Feature Benchmark

## Цель

Ответить не “у кого больше фич”, а какие capabilities меняют conversion, speed, risk selection или cost-to-serve.

Используем:
`skills/product-feature-taxonomy/SKILL.md`

## Feature groups

### Discovery
- calculators;
- transparent eligibility;
- indicative pricing;
- pre-qualification.

### Application
- registry autofill;
- saved application;
- open banking;
- accounting connection;
- document OCR;
- multi-owner handling.

### Decision
- instant/automated decision;
- conditional approval;
- real-time status;
- additional-info loop.

### Offer
- amount/term configuration;
- pricing transparency;
- multiple offers;
- collateral/guarantee disclosure.

### Fulfillment
- e-sign;
- same-day disbursement;
- direct-to-account;
- supplier payment.

### Servicing
- dashboard;
- drawdown;
- payoff;
- extra payment;
- renewal;
- top-up;
- limit increase;
- covenant/document refresh.

### Risk/collections UX
- early warning;
- payment support;
- restructuring/self-service;
- collections communications.

## Deliverable

Feature matrix with:
- Yes / No / Partial / Unknown;
- evidence;
- relevant segment;
- observed value hypothesis.

Не создаем общий субъективный score.

---

# 10. Фаза 6 — Customer Journey Benchmark

## Цель

Восстановить реальные flows, а не маркетинговые обещания.

Используем:
`skills/customer-journey-reconstruction/SKILL.md`

## Нормализованные test scenarios

Чтобы сравнивать игроков, создаем несколько стандартных заемщиков.

### Scenario A — Existing micro/small business customer
- established company;
- transactional history exists;
- modest working-capital need.

### Scenario B — New-to-bank small business
- established company;
- no existing relationship;
- unsecured working-capital need.

### Scenario C — Medium SME
- larger ticket;
- financial statements available;
- may require RM/manual underwriting.

### Scenario D — Transaction-rich merchant
- payment/acquiring data exists;
- short-term funding need.

Конкретные параметры задаются после market segmentation.

## Для каждого flow измеряем

Customer journey должен быть не только текстовым. Для ключевых customer-visible шагов мы стремимся собирать **клиентские экраны / screenshots / screenflows** и использовать их как самостоятельный тип evidence.

Приоритет визуального evidence:
1. собственный observed walkthrough;
2. официальные application/product screens;
3. официальные app screenshots;
4. официальные demos / videos / help-center visuals;
5. user-posted screenshots — только как дополнительный evidence.

Для каждого ключевого этапа, где это возможно, сохраняем:
- screenshot / screen sequence;
- screen source;
- evidence type: observed / official / reported;
- date captured;
- relevant borrower scenario;
- annotations: что именно экран доказывает;
- status `screen evidence missing`, если визуального подтверждения нет.

Особенно интересны экраны:
- landing / product discovery;
- eligibility / pre-check;
- application start;
- business / owner data entry;
- data-source connection;
- document upload;
- application status;
- additional-information request;
- approval / decline;
- offer with amount / term / pricing / fees;
- guarantee / collateral disclosure;
- e-sign / contract;
- disbursement confirmation;
- loan servicing dashboard;
- repayment / payoff;
- renewal / top-up / limit increase.

Визуальный evidence нужен не для иллюстрации, а для проверки фактического UX: количества шагов, disclosure условий, autofill, document burden, status transparency и post-disbursement servicing.

### Flow metrics

- number of steps/screens;
- mandatory fields;
- docs;
- integrations;
- redirects;
- handoffs;
- waiting;
- additional-info loops;
- decision SLA;
- cash SLA;
- support availability;
- pricing transparency;
- post-disbursement servicing.

## Deliverable

1. Journey per lender/scenario.
2. **Screenflow / screenshot sequence** по ключевым customer-visible этапам, где evidence доступен.
3. Annotated screens с пояснением, что именно подтверждает каждый экран.
4. Comparative friction matrix.
5. Best observed patterns by stage.
6. Screen-evidence gaps и остальные evidence gaps.

Итоговый артефакт — не только journey map, но и **visual Customer Journey Atlas**.

---

# 11. Фаза 7 — Underwriting & Risk Benchmark

## Цель

Понять, как скорость и доступность связаны с risk selection.

Используем:
`skills/credit-risk-underwriting/SKILL.md`

## Research questions

- Какие данные реально используются?
- Какие сегменты fully automated?
- Где начинается human review?
- Что происходит с larger tickets?
- Как используются guarantees/collateral?
- Как pricing связан с risk?
- Какие early-warning signals доступны?
- Есть ли evidence better/worse vintages?
- Как различается new-to-bank и existing-customer performance?
- Насколько public risk metrics позволяют сравнение?

## Deliverable

**Risk architecture matrix:**
data → decision → terms → monitoring → loss outcome.

---

# 12. Фаза 8 — Lending Economics

## Цель

Связать продукт и риск с прибылью.

Используем:
`skills/lending-economics/SKILL.md`

## Economics bridge

**Borrower pricing / portfolio yield**
− funding cost
− expected/realized credit loss
− acquisition
− underwriting/KYB
− servicing
− collections
− capital charge
= risk-adjusted contribution

## На уровне компании/сегмента собираем

- portfolio yield;
- funding cost / deposit economics;
- fees;
- NIM/spread;
- provision / cost of risk;
- charge-offs;
- OPEX/cost-to-serve evidence;
- segment profit;
- RWA/capital;
- ROA/RAROC where defensible.

## Ключевой аналитический вопрос

Не только “кто прибыльнее”, а **какая комбинация pricing × risk × funding × automation × cross-sell объясняет прибыльность**.

## Deliverable

Comparable economics bridge + sensitivity where allocation is estimated.

---

# 13. Фаза 9 — Cross-Company Synthesis

## Цель

Перейти от описания компаний к причинным гипотезам и transferable practices.

## Синтезируем по темам

### Market structure
- где банки доминируют;
- где fintechs получили место;
- какие lending niches структурно привлекательны.

### Distribution
- relationship-led;
- self-serve;
- embedded;
- ecosystem cross-sell.

### Data moat
- transaction data;
- accounting;
- acquiring;
- tax;
- bureau;
- proprietary ecosystem signals.

### Underwriting
- где automation дает реальное преимущество;
- где manual underwriting остается экономически оправданным.

### Economics
- low funding cost;
- high pricing power;
- lower losses;
- lower cost-to-serve;
- cross-sell;
- capital efficiency.

### Journey
- какие steps можно убрать;
- какие steps нельзя убрать, но можно автоматизировать/скрыть;
- где transparency важнее raw speed.

## Формат вывода

Для каждой практики:

### Practice
Что делает игрок.

### Evidence
Кто и где это делает.

### Mechanism
Почему это может работать.

### Preconditions
Какие данные / regulation / customer base / funding нужны.

### Economics impact
Revenue / risk / cost / capital.

### Transferability
Где применимо и где нет.

### Confidence
High / Medium / Low.

---

# 14. Исследовательские гипотезы первой волны

Это не выводы, а вопросы, которые будем пытаться опровергнуть.

## H1 — Existing-customer advantage
Банки/экосистемы с транзакционными данными могут давать существенно более короткий путь и лучше контролировать risk для existing customers.

**Что опровергнет:** fintechs без prior relationship дают сопоставимые SLA и loss outcomes.

## H2 — Speed is segmentation, not magic
Самые быстрые lending journeys обычно ограничены ticket size, risk segment или existing-customer population.

**Что опровергнет:** крупные new-to-bank unsecured tickets проходят столь же автоматизированно без ухудшения risk.

## H3 — Funding advantage remains important
У deposit-funded lenders есть структурное преимущество в pricing/economics перед lenders с дорогим wholesale funding, если automation/risk performance сопоставимы.

**Что опровергнет:** nonbank lender стабильно компенсирует funding gap pricing power / lower OPEX / superior risk.

## H4 — Best UX comes from data substitution
Сильный lending UX создается не просто хорошим UI, а заменой ручных документов machine-readable data.

**Что опровергнет:** существенно лучший conversion/speed достигается при аналогичном документном процессе.

## H5 — SME is several businesses
Micro/small automated lending и medium-SME relationship lending имеют настолько разные economics/risk/process, что их нельзя анализировать как один продукт.

**Что опровергнет:** один operating model эффективно обслуживает весь диапазон.

## H6 — Repeat lending can be structurally better
Repeat/existing borrowers могут иметь ниже acquisition/underwriting cost и лучше observable risk, что позволяет улучшить economics и journey.

**Что опровергнет:** repeat cohorts не демонстрируют значимого преимущества после учета selection effects.

---

# 15. Data model проекта

Каждый material data point должен иметь:

| Field | Meaning |
|---|---|
| entity | market / lender / product |
| metric | canonical metric name |
| value | raw value |
| unit | currency / % / count |
| period_start | start |
| period_end | end |
| geography | country/market |
| borrower_segment | normalized segment |
| product | normalized product |
| source_title | source |
| source_url | URL |
| publication_date | publication date |
| definition | original definition |
| denominator | denominator |
| evidence_type | fact/calculation/estimate/hypothesis |
| confidence | high/medium/low |
| notes | caveats/conflicts |

Для journey/features дополнительно:
- scenario;
- stage;
- observed/documented/reported/inferred/unknown;
- screenshot/page evidence;
- screenshot source;
- screenshot capture date;
- screen evidence type: observed / official / reported;
- screen annotations / what the screen proves;
- `screen evidence missing` when a key customer-visible step has no visual evidence.

---

# 16. Контроль качества

Перед публикацией каждого major finding:

## Comparability check
Совпадают ли:
- borrower definition;
- product;
- period;
- denominator;
- accounting treatment;
- stock/flow;
- bank/nonbank coverage?

## Source check
Есть ли primary source?

## Triangulation check
Есть ли независимый cross-check для критичного вывода?

## Contradiction check
Искали ли данные, которые опровергают тезис?

## Causality check
Не выдаем ли correlation или marketing narrative за механизм?

## Confidence check
Соответствует ли confidence силе evidence?

---

# 17. Конечные deliverables исследования

## A. Executive market report
Краткий narrative по рынку и главным выводам.

## B. Country market landscape
Размер, динамика, access, pricing, risk, infrastructure.

## C. Player universe
40–60 игроков с normalized metadata.

## D. 12–18 company teardowns
Глубокие профили ключевых архетипов.

## E. Product / feature matrix
Comparable offering and capabilities.

## F. Visual Customer Journey Atlas
Normalized flows по ключевым scenarios **с клиентскими экранами, screenflows и annotated screenshots**, где они доступны. Для отсутствующих ключевых экранов явно фиксируется `screen evidence missing`.

## G. Risk / underwriting benchmark
Data, automation, monitoring, portfolio outcomes.

## H. Lending economics benchmark
Yield, funding, loss, OPEX, capital, profitability.

## I. Pattern library
Доказанные practices и механизмы.

## J. Opportunity / transferability map
Какие решения можно переносить и при каких prerequisites.

---

# 18. Очередность выполнения

## Wave 1 — Foundation
1. Metric dictionary.
2. Geography shortlist.
3. Market-source inventory.
4. Player universe schema.

## Wave 2 — Landscape
5. Country market sizing.
6. Borrower/product segmentation.
7. Initial 40–60 player universe.

## Wave 3 — Shortlist
8. Select 12–18 deep dives by archetype/evidence value.
9. Lock normalized research scenarios.

## Wave 4 — Deep research
10. Company teardowns.
11. Product/features.
12. Customer journeys.
13. Underwriting/risk.
14. Economics.

Эти блоки делаем по возможности параллельно на одного игрока, чтобы одна evidence base переиспользовалась.

## Wave 5 — Synthesis
15. Cross-company comparison.
16. Test hypotheses.
17. Pattern library.
18. Transferability assessment.
19. Executive conclusions.

---

# 19. Что НЕ делаем

- Не начинаем с рейтинга “лучших банков”.
- Не сравниваем компании одним composite score.
- Не считаем наличие feature доказательством ценности feature.
- Не считаем красивый digital flow доказательством хорошей экономики.
- Не считаем низкий NPL доказательством лучшего underwriting без учета mix/vintage.
- Не считаем высокую ставку доказательством высокой прибыльности.
- Не переносим практику из одной страны без проверки local infrastructure.
- Не заполняем Unknown догадками.

---

# 20. Ближайший конкретный шаг

Следующая рабочая итерация:

1. создать **metric dictionary**;
2. выбрать **первый набор стран** для landscape;
3. для них собрать **market-source inventory**;
4. создать пустой **player universe** с единым schema;
5. только после этого начинать массовый сбор компаний.

Это минимальная foundation, после которой исследование начинает масштабироваться без потери сопоставимости.
