# BB-05: очередь подробных профилей

Дата: 2026-10-07 (Europe/Moscow). Источник статусов: shortlist.csv; 14 выбранных кейсов в 7 странах. BB-04 дал Qonto/Allica; BB-05 сейчас in_progress и завершил Tide / Mercury / Ramp / Square / Toast. Всего 7 done / 7 todo. Следующий отдельный разбор — iwoca Germany.

| Компания | Рынок | Статус | Материал |
|---|---|---|---|
| Qonto | France | done | [Профиль](../../companies/b2b_banking/france/qonto.md) |
| Tide | United Kingdom | done | [Профиль](../../companies/b2b_banking/united_kingdom/tide.md) |
| Mercury | United States | done | [Профиль](../../companies/b2b_banking/united_states/mercury.md) |
| Allica Bank | United Kingdom | done | [Профиль](../../companies/b2b_banking/united_kingdom/allica.md) |
| Ramp | United States | done | [Профиль](../../companies/b2b_banking/united_states/ramp.md) |
| Square | United States | done | [Профиль](../../companies/b2b_banking/united_states/square.md) |
| Toast | United States | done | [Профиль](../../companies/b2b_banking/united_states/toast.md) |
| iwoca | Germany | todo | Ещё не сохранён |
| YouLend | United Kingdom | todo | Ещё не сохранён |
| Stone | Brazil | todo | Ещё не сохранён |
| RazorpayX | India | todo | Ещё не сохранён |
| Airwallex | Australia | todo | Ещё не сохранён |
| Wise Business | United Kingdom | todo | Ещё не сохранён |
| Funding Circle | United Kingdom | todo | Ещё не сохранён |

## Принятый результат Tide

[Профиль](../../companies/b2b_banking/united_kingdom/tide.md) охватывает подключение, регулярные задачи, банковские/кредитные договорные роли, Credit Flex и внешний подбор. Добавлены 26 source records, 31 claims, 25 metric observations, 7 definitions, 7 features, 15 journey steps, 2 missing-screen records и 4 contradictions. Целевые разделы договорных PDF прочитаны; годовые financial PDF не прочитаны. BB-G24–26, BB-X0004–0007 — в соответствующих реестрах.

Эффект на активность, удержание и кредитную прибыль не доказан. done — ограниченный принятый публичный профиль; полный юридический аудит, реальные закрытые экраны и когортная экономика не подразумеваются. BB-06–12 ещё не выполнены. Не менять BB-05 на done до приёмки всех оставшихся 7.

## Принятый результат Mercury

[Профиль](../../companies/b2b_banking/united_states/mercury.md): account/workflow→IO, IO-only и Working Capital до открытия счёта; VC debt отдельно. 20 sources, 32 claims, 20 metrics, 10 definitions, 9 features, 16 journey steps, 4 missing-screen records, 4 contradictions. OCC PDF прочитан по целевым секциям; текущий собственный банк не установлен. Command June2026, Spend August2026, Books September2026 — публичная доступность, не измеренный эффект.

BB-G27–29 и BB-X0008–0011 сохранены. Аудированный P&L/кохорты/индивидуальный риск и реальный UI не получены. Всего 98 sources / 146 claims / 75 metrics / 84 definitions / 24 features / 49 steps / 9 screen records (0 visually verified) / 11 contradictions. BB-05 in_progress: 2 из 12, вместе с BB-04 — 4 из 14; следующий Ramp US.

## Принятый результат Ramp

[Профиль](../../companies/b2b_banking/united_states/ramp.md): external-bank/card entry, AP-only через бухгалтера, optional Checking fee incentives; daily-card/Reserve cash-backed отдельно. Stack June2026 и Accounts Receivable September2026 подтверждены по релизам; adoption/эффект неизвестны. Исторический Flex не принят как текущая новая выдача.

Добавлены 28 sources (включая неудачные проверки), 29 claims, 22 metrics, 10 definitions, 11 features, 17 journey steps, 5 missing-screen records, 5 contradictions. BB-G30–32 и BB-X0012–0016 сохранены. Юридические JS shell/HTTP403 не выданы за прочитанные договоры.

**Текущий итог: 126 sources / 175 claims / 97 metrics / 94 definitions / 35 features / 66 steps / 14 screen records (0 visually verified) / 16 contradictions. BB-05 in_progress: 3 из 12; вместе с BB-04 — 5 из 14 done, 9 todo; следующий Square US.** Ранее приведённые числа — исторические итоги соответствующего профиля. PDF впереди.

## Принятый результат Square

[Профиль](../../companies/b2b_banking/united_states/square.md): payments/data→credit с внешним банком; optional Checking, Savings, card/AP, Managerbot и Homegrown pilot раздельно. Три официальные иллюстрации скачаны и визуально проверены; это не реальный клиентский путь. Q2 commercial stock/flows и глобальный Square segment не выданы за US cohort P&L. BB-G33–35; BB-X0017–0022.

Текущий итог: 160 sources / 208 claims / 136 metrics / 133 metric_definitions / 46 features / 86 journey_steps / 20 screens / 22 contradictions; 3 visually verified illustrations. BB-05 in_progress: 4 из 12; всего 6 из 14 done / 8 todo; следующий Toast US. Исторические итоги выше сохранены. Финальный PDF впереди.

## Принятый результат Toast — 2026-10-07

[Профиль](../../companies/b2b_banking/united_states/toast.md): restaurant operations/payments→credit, limited Welcome before POS migration approval and Conditional Approval draw later, optional Thread Checking, read-only cash-flow beta, bank/Jar BillPay. WebBank originator, Toast servicing/guarantee/performing HFI разделены. October6 Team/Grow release и прошлые результаты не смешаны. Три official illustrations визуально проверены, example numbers excluded; не actual client journey. BB-G36–38, BB-X0023–0028.

Добавлено: 33 sources, 32 claims, 40 metrics, 34 metric_definitions, 11 features, 26 journey_steps, 6 screens, 6 contradictions. Итог: 193 sources, 240 claims, 176 metrics, 167 metric_definitions, 57 features, 112 journey_steps, 26 screens, 28 contradictions. 6 verified illustrations. **7 из14 done /7 todo; BB-05 in_progress5 из12; следующий iwoca Germany.** BB-06–12 и PDF впереди.
