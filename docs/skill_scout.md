# Skill Scout: что нашли и что берем в работу

Дата отбора: 2026-10-02.

Цель — не установить максимальное количество чужих skills, а собрать надежную исследовательскую систему для SME / B2B lending.

## 1. Сильные публичные skills

### OpenAI — Market Sizing
Источник: https://github.com/openai/role-specific-plugins/blob/main/plugins/data-analytics/skills/market-sizing/SKILL.md

Что полезно:
- явное разделение evidence и assumptions;
- выбор между top-down, bottom-up и value-based подходами;
- sensitivity analysis;
- фиксация того, какие данные сильнее всего улучшат уверенность оценки.

Берем в наш `market-sizing`: прозрачные расчетные цепочки, uncertainty, sensitivity и обязательный audit trail.

### OpenAI — UX Research
Источник: https://github.com/openai/plugins/blob/main/plugins/product-design/skills/research/SKILL.md

Что полезно:
- фокус на реальных проблемах и friction;
- исследование onboarding, self-serve flows, help/docs и workflow;
- требование свежих evidence.

Берем в `customer-journey-reconstruction`: evidence-first анализ реального опыта, а не фантазирование journey map.

### NVIDIA Skill2Env — Deep Research
Источник: https://github.com/NVlabs/Skill2Env/blob/main/SkillHub/skills/research/deep-research/SKILL.md

Что полезно:
- triangulation;
- falsifiable hypotheses;
- adversarial review;
- отдельное хранение evidence и утверждений;
- поиск disconfirming evidence.

Берем в `deep-research`: тезисы должны быть проверяемыми, противоречия нельзя скрывать, важные claims проходят red-team pass.

### Browserbase / Firecrawl — Competitor Analysis
Источники:
- https://github.com/browserbase/skills/blob/main/skills/competitor-analysis/SKILL.md
- https://github.com/firecrawl/web-agent/blob/main/agent-core/src/skills/definitions/competitor-analysis/SKILL.md

Что полезно:
- нормализованная feature/pricing matrix;
- одинаковые research lanes для каждого конкурента;
- отделение официального product surface от external signals;
- chronological feed изменений.

Берем в `competitor-benchmark`: одна и та же схема сбора по каждому банку; продуктовые страницы сами по себе недостаточны.

### Product-on-Purpose — Customer Journey
Источник: https://github.com/product-on-purpose/pm-skills/blob/main/skills/discover-journey-map/SKILL.md

Особенно сильный принцип: journey map — это synthesis artifact, а не brainstorm. Эмоции, pain points и действия нельзя придумывать без evidence.

Берем почти как design principle: если данных нет, отмечаем `unknown` или `hypothesis`, а не заполняем красивую таблицу домыслами.

### PM Skills — Customer Journey Map
Источник: https://github.com/phuryn/pm-skills/blob/main/pm-market-research/skills/customer-journey-map/SKILL.md

Полезная структура:
persona/JTBD → stages → touchpoints → actions → pain points → opportunities.

Используем как каркас, но дополняем lending-specific полями: документы, external data pulls, decision SLA, offer, signing, disbursement, servicing.

### Market sizing frameworks / research-ops
Источники:
- https://github.com/slgoodrich/agents/blob/main/plugins/ai-pm-copilot/skills/market-sizing-frameworks/SKILL.md
- https://github.com/borghei/Claude-Skills/blob/main/research-ops/market-research/SKILL.md

Полезно:
- независимые методы sizing;
- reconciliation между оценками;
- sensitivity;
- сегментация вместо одного “рынка SME”.

Берем метод, но не переносим без проверки эвристические диапазоны или generic venture benchmarks.

## 2. Что намеренно НЕ копируем

Публичные skills часто содержат:
- неподтвержденные “typical benchmarks”;
- жесткие числовые thresholds без отраслевого обоснования;
- рекомендации, заточенные под SaaS/VC, а не банковский кредит;
- автоматическое ранжирование конкурентов по субъективным score;
- шаблоны, где модель обязана заполнить поле даже при отсутствии данных.

В нашем исследовании неизвестное остается неизвестным.

## 3. Банковские skills строим сами

Качественных публичных agent skills по SME credit underwriting, portfolio risk и lending P&L почти нет. Поэтому эти блоки строятся из первичных источников:

- EBA Guidelines on loan origination and monitoring;
- Basel Framework;
- OCC lending / underwriting / portfolio risk handbooks;
- OECD Financing SMEs and Entrepreneurs;
- Federal Reserve Small Business Credit Survey;
- FDIC Small Business Lending Survey;
- отчетность и Pillar 3 конкретных банков.

Это надежнее, чем использовать generic “financial analyst” skill, который не знает специфики lending book.

## 4. Итоговый skill stack проекта

| Skill | Главный вопрос |
|---|---|
| deep-research | Можно ли доказать этот вывод? |
| market-sizing | Насколько велик рынок и как мы это посчитали? |
| competitor-benchmark | Чем реально отличаются игроки? |
| lending-economics | Где и почему зарабатывает/теряет деньги кредитный бизнес? |
| credit-risk-underwriting | Как отбирается риск и как портфель ведет себя после выдачи? |
| product-feature-taxonomy | Что именно продается клиенту и какие capabilities есть? |
| customer-journey-reconstruction | Что реально проходит клиент от потребности до погашения? |

## 5. Правило использования чужих skills

Чужой skill — источник идеи процесса, не источник фактов о рынке.

Все факты о банках, продуктах, риске, размерах рынка и финансовых показателях проверяются отдельно по первичным или высококачественным отраслевым источникам.
