# Company / Lender Teardown — Stone

**Status:** Batch 1 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Brazil  
**Primary segments:** micro / small / medium merchants  
**Primary journey:** existing Stone merchant/account customer → pre-approved working-capital offer

---

## 0. Why Stone is important

Stone is a particularly valuable research case because public evidence connects all four layers:

**customer transaction data → pre-approved product journey → credit operating model → portfolio risk/economics**

Unlike many lenders, Stone also publishes multiple official client-facing screens for the working-capital journey.

---

## 1. Executive fact sheet

| Metric | Value | Period | Scope | Source |
|---|---:|---|---|---|
| Stone partners | 4m+ | 2026 product page | broader merchant base, not borrowers | Stone |
| Total credit portfolio | R$3.752bn | Q2 2026 | Stone consolidated credit portfolio | StoneCo |
| Government-backed loans | R$334.2m | Q2 2026 | within credit portfolio | StoneCo |
| Credit revenue | R$348.5m | Q2 2026 | credit products | StoneCo |
| Credit revenue YoY | +153% | Q2 2026 | credit products | StoneCo |
| Provision expense | R$187.6m | Q2 2026 | consolidated credit | StoneCo |
| Cost of risk | 21.5% | Q2 2026 | consolidated credit | StoneCo |
| NPL 15–90 | 6.00% | Q2 2026 | consolidated credit | StoneCo |
| NPL >90 | 8.60% | Q2 2026 | consolidated credit | StoneCo |
| Coverage ratio | 203.6% | Q2 2026 | consolidated credit | StoneCo |
| Group adjusted net income | R$582.7m | Q2 2026 | continuing operations | StoneCo |
| Group adjusted ROE | 21.6% | Q2 2026 | group | StoneCo |

Sources:
- https://www.stone.com.br/capital-de-giro
- https://www.sec.gov/Archives/edgar/data/1745431/000207097926000275/stoneco_earningsrelease2q2.htm

---

## 2. Business model

Stone's SME/MSMB franchise combines:
- acquiring/payment acceptance;
- digital business account;
- credit;
- other financial services.

This creates a structural data advantage for merchants whose **daily sales flow through Stone**.

The lending architecture visible in disclosures has at least two credit lanes:

1. **Automated desk** — scalable, data-driven merchant lending.
2. **Dedicated desk** — larger/more bespoke tickets with more human involvement.

This distinction is critical because Q2 2026 risk performance differed between these lanes.

---

## 3. Product portfolio

### 3.1 Capital de Giro Stone

Current product page states:
- rates **from 1.75% per month**;
- 100% digital contracting or support from a Stone specialist;
- repayments dynamically linked to merchant sales;
- daily sales retention automatically pays daily interest and reduces principal;
- more sales can accelerate amortization and reduce total interest cost;
- all contract terms displayed before acceptance.

Source:
https://www.stone.com.br/capital-de-giro

### 3.2 How repayment works

Stone describes a distinctive revenue-linked mechanism:

- a portion of daily sales is automatically retained;
- lower-sales days lead to lower repayment;
- stronger-sales days lead to faster repayment;
- faster amortization reduces total interest.

This is economically different from a fixed monthly installment loan and should be compared separately.

### 3.3 Other credit products

Stone publicly offers:
- business credit card;
- account limit / credit line;
- Pix on Credit;
- Boleto on Credit;
- incentive/government-backed facilities.

Government-backed lending had already reached **R$334.2m** of Stone's Q2 2026 credit portfolio.

---

## 4. Underwriting architecture

### 4.1 Pre-approved automated offer

Stone's help center states that credit analysis is applied automatically.

Factors include:
- relationship with Stone;
- monthly revenue;
- market/business history;
- external factors such as the macroeconomic environment.

When analysis is positive:
- a pre-approved offer is pushed to the app;
- customer can simulate different amounts within the approved limit;
- simulation displays interest, installments and automatic-retention percentage.

Source:
https://ajuda.stone.com.br/pt_BR/capital-de-giro/capital-de-giro-stone

### 4.2 Proprietary-data advantage

Management explicitly notes that Stone lends to clients whose **daily sales flow through its platform**.

This supports the mechanism:
- high-frequency revenue observability;
- ongoing monitoring;
- automatic repayment from sales;
- potentially lower servicing/collections friction.

### 4.3 Automated vs dedicated desk

Q2 2026 management disclosures distinguish:
- automated desk;
- dedicated desk.

The dedicated desk includes larger tickets; management described average dedicated-desk ticket around R$700k in earnings-call commentary and noted some stressed exposures above R$10m.

Primary earnings release confirms that delinquency pressure differed by desk, even if detailed ticket commentary comes from the call.

---

## 5. Customer journey — Capital de Giro

### Scenario

Existing Stone merchant/account user with a pre-approved credit offer.

| Stage | Customer action | Evidence | Status |
|---|---|---|---|
| 1. Offer | Banner appears on Stone app home screen | Official screen | Observed official |
| 2. Entry | Tap available credit offer | Official page | Documented |
| 3. Simulation | Choose amount and simulate | Official page/help | Documented |
| 4. Pricing/repayment | Compare interest, installments and retention % | Official help | Documented |
| 5. Review | Review contract/request data | Official page | Documented |
| 6. Authentication | Enter Stone PIN | Official page | Documented |
| 7. Credit analysis | Request enters analysis | Official screen | Observed official |
| 8. Tracking | App shows request → analysis → approved → funds | Official screen | Observed official |
| 9. Funding | If approved, funds credited to Stone account; public screen says up to 4 business days | Official screen | Observed official |
| 10. Repayment | Daily automatic retention from sales | Official page | Documented |
| 11. Servicing | App displays open amount, installments, payment history/contracts | Official page/screens | Documented + visual |

---

## 6. Visual customer journey / screens

Stone has materially better first-party screen evidence than many peers.

### Screen 1 — Pre-approved offer on account home

Official image:

![Stone — pre-approved credit offer in app](https://martech-web-cdn.stone.com.br/optimized/stone/4271eb33-edc1-4617-a3eb-b42b1e09a759/step-by-step-emprestimo-desktop.png)

Direct asset:
https://martech-web-cdn.stone.com.br/optimized/stone/4271eb33-edc1-4617-a3eb-b42b1e09a759/step-by-step-emprestimo-desktop.png

Source:
https://www.stone.com.br/capital-de-giro

**What it proves**
- proactive offer is surfaced in the app;
- available amount can be communicated before application;
- offer is embedded next to daily account/sales activity.

### Screen 2 — Application status timeline

Official image:

![Stone — loan application status timeline](https://res.cloudinary.com/dunz5zfpt/f_auto%2Cc_limit%2Cw_1080%2Cq_90/stone-cms/prod/capital_de_giro_stone_abra_seu_app_confira_oferta_credito_passo_4_web_159c8abd6c)

Direct asset:
https://res.cloudinary.com/dunz5zfpt/f_auto%2Cc_limit%2Cw_1080%2Cq_90/stone-cms/prod/capital_de_giro_stone_abra_seu_app_confira_oferta_credito_passo_4_web_159c8abd6c

**Visible states**
- request received;
- loan under analysis;
- loan approved;
- funds received in Stone account.

The screen explicitly says that, if approved, funds can reach the account in **up to 4 business days**.

### Screen 3 — Repayment / installment state

Official image:

![Stone — repayment and installment servicing](https://res.cloudinary.com/dunz5zfpt/f_auto%2Cc_limit%2Cw_1080%2Cq_90/stone-cms/prod/capital_de_giro_stone_vendeu_bem_no_mes_valor_da_parcela_diminui_b4c3ad04b5)

Direct asset:
https://res.cloudinary.com/dunz5zfpt/f_auto%2Cc_limit%2Cw_1080%2Cq_90/stone-cms/prod/capital_de_giro_stone_vendeu_bem_no_mes_valor_da_parcela_diminui_b4c3ad04b5

**What it proves**
- paid/future installment state;
- repayment balance;
- displayed interest savings;
- in-app servicing transparency.

### Remaining screen gaps

| Stage | Screen status |
|---|---|
| Offer/banner | available |
| Amount simulation | screen evidence missing |
| Rate/retention comparison | screen evidence missing |
| Contract review | screen evidence missing |
| PIN | screen evidence missing |
| Status tracking | available |
| Funding confirmation | partial via status timeline |
| Repayment/servicing | available |
| Renegotiation/collections | screen evidence missing |

**Visual evidence coverage: Medium/High.**

---

## 7. Credit risk

### Q2 2026

- provision expense: **R$187.6m**;
- cost of risk: **21.5%**;
- NPL 15–90: **6.00%**;
- NPL >90: **8.60%**;
- coverage: **203.6%**.

All are consolidated credit metrics, not exclusively Capital de Giro.

### What management says drove deterioration

The Q2 release attributes higher provisions to:
1. continued credit portfolio expansion;
2. additional delinquency in dedicated desk;
3. flow-through of weaker second-half 2025 and early-2026 vintages.

The over-90 NPL increase reflected:
- migration of weaker automated-desk vintages;
- specific dedicated-desk cases rolling into >90-day delinquency.

### Positive signal

Management says underwriting changes implemented during Q2 were improving first-payment-default performance in the automated desk, with the June cohort showing the best result in the prior 12 months.

This is valuable cohort evidence, but the exact FPD data are not published in the earnings release.

### Government-backed mix effect

Stone states that government-backed lines:
- have lower risk profile;
- require lower provision coverage;
- contributed to a slight sequential decline in cost of risk despite higher provisions.

This directly supports treating guarantee-backed credit as a separate risk/economics model.

Source:
https://www.sec.gov/Archives/edgar/data/1745431/000207097926000275/stoneco_earningsrelease2q2.htm

---

## 8. Lending economics

### Directly observable

Q2 2026:
- credit portfolio: R$3.752bn;
- credit revenue: R$348.5m;
- credit revenue +153% YoY;
- credit revenue +14.1% QoQ;
- provision expense: R$187.6m.

Management states credit-revenue growth reflected:
- portfolio expansion;
- higher average monthly interest rates charged, especially in automated desk.

### Important accounting caveat

Stone began including **credit-card interchange revenue** in total credit revenue and restated prior periods accordingly.

Therefore:
- do not treat credit revenue / loan portfolio as a pure loan yield;
- do not compare directly with bank loan interest income without adjustment.

### Funding / costs

Group financial expenses net were R$1.078bn in Q2 2026, but this is not a clean credit-funding-cost allocation.

A defensible SME loan spread/RAROC cannot yet be calculated from public information alone.

---

## 9. Distinctive operating mechanics

### 1. Credit embedded in acquiring relationship
Credit offer sits inside the same ecosystem that sees merchant sales.

### 2. High-frequency observable cash flow
Daily sales are both an underwriting/monitoring signal and repayment source.

### 3. Revenue-linked repayment
Automatic sales retention changes debt service with business activity.

### 4. Two-desk underwriting architecture
Automated small/standardized credit and dedicated larger-ticket credit behave differently in risk.

### 5. Government guarantee as active portfolio-mix lever
Stone is using guaranteed lines not only for access but to alter risk-adjusted economics.

---

## 10. Hypothesis tests

### H1 — Existing-customer advantage: strong evidence

Observed:
- relationship/revenue are explicit inputs;
- pre-approved offer is pushed in-app;
- sales flow through Stone.

Still missing:
- approval rates vs new-to-Stone borrowers;
- direct loss comparison.

### H2 — Speed is segmentation, not magic: strong evidence

The public operating/risk evidence supports at least two lanes:
- automated;
- dedicated.

Larger-ticket dedicated cases have materially different risk/process characteristics.

### H4 — UX from data substitution: strong evidence

The visible customer flow contains no financial-statement upload before offer. Much of the eligibility work occurs through relationship/sales data before the customer starts contracting.

### H6 — Repeat/relationship advantage: plausible/strong mechanism

Stone's own-client credit share of wallet was described by management as still only mid-single digits, suggesting significant cross-sell headroom into an already-observed merchant base.

This should be tested with repeat/cohort data if available.

---

## 11. Evidence gaps

1. Number of active credit borrowers.
2. Merchant credit portfolio vs card split in all periods.
3. Automated vs dedicated portfolio balances.
4. Average/median automated ticket.
5. Approval rate / pre-approved offer penetration.
6. Exact automated underwriting inputs/model weights.
7. FPD by vintage.
8. Recoveries/charge-offs.
9. Funding cost attributable to credit portfolio.
10. Exact product rate distribution rather than “from 1.75%”.
11. Full screen sequence for simulation and contract.

---

## 12. Current synthesis

### Well evidenced

Stone's credit model is structurally linked to its merchant payments ecosystem: the company can observe sales, generate proactive offers, collect repayment from sales and monitor credit performance at high frequency.

### Key analytical insight

The most important lesson is **not merely that Stone has a fast app**.

The deeper operating model is:

**proprietary transaction data + embedded distribution + automated repayment + risk segmentation by desk**

This is exactly the type of mechanism the project is designed to identify.

### Counter-evidence / caution

Fast/data-rich lending does not eliminate credit risk. Q2 2026 showed:
- materially higher NPLs;
- weaker prior vintages;
- stress in larger-ticket dedicated exposures;
- high cost of risk.

This is useful counter-evidence against simplistic claims that transaction data automatically creates superior portfolio quality.

### Confidence

- Journey/product mechanics: **High**
- Risk performance: **High**
- Automated-vs-dedicated architecture: **High**
- Full credit unit economics: **Medium/Low**
- Screenflow: **Medium/High**

---

## Sources

Primary:
- https://www.stone.com.br/capital-de-giro
- https://www.stone.com.br/credito
- https://ajuda.stone.com.br/pt_BR/capital-de-giro/capital-de-giro-stone
- https://investors.stone.co/
- https://www.sec.gov/Archives/edgar/data/1745431/000207097926000275/stoneco_earningsrelease2q2.htm
- https://www.sec.gov/Archives/edgar/data/1745431/000207097926000274/stoneco_06x2026.htm

Secondary/context only:
- Q2 2026 earnings-call transcripts for additional management commentary should be treated as attributed commentary, not as audited financial data.
