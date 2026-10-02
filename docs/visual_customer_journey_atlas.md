# Visual Customer Journey Atlas — SME Lending

**Version:** 2026-10-02  
**Scope:** 18 deep dives / 5 normalized journey scenarios  
**Purpose:** compare customer-visible credit journeys while preserving the underwriting, data and economics behind them.

> Screens are evidence, not decoration.
>
> Only first-party / official visuals are treated as visual evidence. Missing screens are explicitly marked `screen evidence missing`.

---

# Executive answer

The 18-company evidence does **not** support one universal “best SME loan journey.”

There are five materially different journeys:

1. **Existing-customer pre-approved credit**
2. **New-to-lender digital unsecured credit**
3. **Medium-SME relationship credit**
4. **Embedded merchant credit**
5. **Guarantee-backed credit**

The shortest journeys are not necessarily those with the fewest screens. They are those where the lender has already completed more of the information and risk work **before the customer reaches the screen**.

The central customer-experience metric is therefore:

> **How much new information must the borrower produce after expressing credit intent?**

---

# Normalized journey stages

To compare unlike lenders, every flow is mapped to the same stages:

| Stage | Question |
|---|---|
| 0. Pre-underwriting | What does lender know before customer acts? |
| 1. Discovery / offer | Does customer search, or does offer appear proactively? |
| 2. Eligibility | Is eligibility checked visibly or already known? |
| 3. Amount / need | How does customer specify amount/purpose? |
| 4. Data / documents | What must customer supply or connect? |
| 5. Decision | Automated, analyst, RM, committee? |
| 6. Price / offer | When are rate/fee/repayment disclosed? |
| 7. Contract / authentication | How is acceptance executed? |
| 8. Funding | How quickly and where does cash arrive? |
| 9. Servicing / repayment | Self-service, automatic debit, sales-linked? |
| 10. Repeat / distress | Is next loan easier? How are problems handled? |

---

# Journey A — Existing-customer pre-approved credit

## Core insight

**The fastest journey begins before the visible application.**

The lender continuously observes an existing account/payment relationship and only presents credit when a risk model has already identified an eligible offer.

### Exemplars
- Nubank / Nu Empresas
- Stone
- CommBank
- American Express BLOC
- SBI PABL/PAsBL

---

## A1. Nubank — account-led pre-approved working capital

### Flow

**Nu Empresas relationship**  
→ recurring automated eligibility analysis  
→ Capital de Giro appears in app  
→ choose amount / installments / first due date  
→ see total payable  
→ confirm responsible person  
→ contract  
→ 4-digit PIN  
→ final approval  
→ immediate credit to Nu Empresas account  
→ automatic debit / in-app servicing.

### What the customer does NOT visibly do

In the published flow, the borrower does not begin by:
- uploading annual accounts;
- uploading bank statements;
- visiting a branch;
- requesting an RM review.

That does not mean those data do not matter. It means the underwriting information is largely acquired elsewhere.

### Official visual

![Nubank — Nu Empresas Capital de Giro](https://www.datocms-assets.com/120597/1743107465-nu-empresas-capital-de-giro.jpg?crop=focalpoint&dpr=1&fit=crop&fm=jpg&q=60&w=1200)

**What this proves**
- business credit is embedded in the app;
- credit is presented as an available Nu Empresas capability.

**What remains missing**
- amount selection;
- price/term screen;
- contract;
- approval confirmation;
- servicing.

**Screen coverage:** Partial.

Source:
https://nubank.com.br/empresas/emprestimos

---

## A2. CommBank — existing customer vs new customer

### Existing-customer flow

Existing business relationship  
→ bank uses information already held  
→ conditional/pre-approved eligibility  
→ ~10-minute online application  
→ instant decision if eligible  
→ funds within minutes.

### New-to-bank flow

No existing information  
→ book appointment / specialist  
→ collect additional business/financial information  
→ underwriting  
→ offer / funding.

### Why this is analytically valuable

This is almost a natural experiment:
**same lender + same broad product family + different prior information = different customer journey.**

### Screen evidence

Official conditional-approval visual observed on the product page, but a stable direct first-party asset was not recovered.

**Screen evidence missing for repo embedding.**

Source:
https://www.commbank.com.au/business/loans-and-finance/betterbusiness-loan.html

---

## A3. American Express BLOC — dynamic relationship limit

### Flow

Existing relationship / linked bank data  
→ possible preapproval / visible line terms for select customers  
→ Business Blueprint  
→ Take a loan / Fund my account  
→ select amount  
→ select term  
→ review monthly fee/APR  
→ select deposit account  
→ sign  
→ instant to eligible Amex Business Checking or 1–3 days ACH.

### Distinctive element

The repeat draw does not recreate a full origination:
**the credit line is continuously reviewed and reused.**

### Screen evidence

Amex publishes an official illustrated guide showing:
- BLOC dashboard;
- Fund my account;
- Business Checking instant-deposit selection;
- success state.

Direct stable image assets were not recovered.

Official guide:
https://www.americanexpress.com/en-us/business/blueprint/help-center/business-line-of-credit/how-to-instant-deposit/

**Screen coverage:** Medium / official illustrations.

---

# Journey B — New-to-lender digital unsecured credit

## Core insight

For a borrower without a prior relationship, the key UX lever is **data substitution**.

The customer still has to create a credit file, but a strong lender replaces manual financial evidence with machine-readable transaction/tax data.

### Exemplars
- iwoca
- Floryn
- Konfío
- Funding Circle

---

## B1. iwoca — visible ticket breakpoint

### Low-ticket flow

Application  
→ business/account information  
→ Open Banking / 90 days transactions  
→ automated / rapid credit decision  
→ offer  
→ digital contract  
→ funding.

### Higher-ticket flow

Same journey  
+ BWA/SuSa historical/current financial evidence  
→ greater underwriting depth.

### Breakpoint

Publicly documented:
- **€1k–€50k:** transaction data can carry the core evidence;
- **€50,001–€500k:** BWA/SuSa are added.

This is one of the clearest observed examples of a **journey changing with exposure**.

### Official screens

#### Step 1 — application

![iwoca Step 1 — application](https://cdn.prod.website-files.com/62e9302315b6e0c45f706ad7/6787ebf92a960a796f7bbce9_Step%201-min.png)

**Proof:** the flow starts with lightweight digital application.

#### Step 2 — data

![iwoca Step 2 — data](https://cdn.prod.website-files.com/62e9302315b6e0c45f706ad7/6787ebf9869c1caafa0a6bb7_Step%202-min.png)

**Proof:** data/document provision is a distinct stage.

#### Step 3 — offer/completion

![iwoca Step 3 — offer](https://cdn.prod.website-files.com/62e9302315b6e0c45f706ad7/6787ebf9f16c37fd417e3cc6_Step%203-min.png)

**Proof:** lender presents the journey as a compact digital sequence.

### Missing screens
- exact Open Banking consent;
- BWA/SuSa upload;
- pricing/contract detail;
- funding confirmation;
- repeat/top-up dashboard.

Source:
https://www.iwoca.de/kredit-fuer-unternehmen

---

## B2. Floryn — current cash flow first

### ≤€250k flow

2-minute application  
→ connect bank / upload six months statements  
→ automated analysis  
→ account manager within ~2 hours  
→ decision / facility within 24 hours  
→ dashboard drawdown.

### >€250k

Adds:
- annual accounts;
- receivables/payables lists.

### Core UX mechanism

**Current transaction evidence is the default; accounting statements are an escalation input.**

### Screen evidence

Official product calculator/quickscan visuals exist, but authenticated PSD2/offer/dashboard assets were not recovered.

**Screen coverage: Low/Partial.**

Source:
https://www.floryn.com/zakelijk-krediet

---

## B3. Konfío — tax data as the onboarding rail

### Flow

Choose tax regime / amount  
→ RFC + SAT/CIEC  
→ platform reads tax/invoicing activity  
→ personalized offer  
→ select amount/term  
→ identity/company validation  
→ digital signature / FIEL  
→ bank-account funding.

### Core UX mechanism

Instead of asking the SME to reconstruct revenue manually:
**tax and invoice history becomes the machine-readable financial file.**

### Screen evidence

The current official product page has an interactive simulator, but a complete authenticated credit flow was not captured.

**Screen coverage: Partial.**

Source:
https://konfio.mx/credito/

---

# Journey C — Medium-SME relationship lending

## Core insight

At larger tickets, good UX does **not** mean removing the human.

The strongest observed pattern is:

> **digital preparation → empowered underwriter/RM → short approval chain**

### Exemplars
- Allica
- Commerzbank
- Judo
- SBI larger SME lane

---

## C1. Allica — underwriter as an explicit product stage

### Flow

Digital decision in principle  
→ full application  
→ bank statements + accounts + management accounts + debt  
→ underwriter review  
→ clarifications if needed  
→ approval  
→ drawdown.

### What is different from legacy relationship banking

The customer does not disappear into an opaque back office.

The underwriter is a visible, designed part of the journey.

### Screen evidence

Official product page shows step illustrations for:
- decision in principle;
- complete application;
- underwriter review;
- approval/drawdown.

Stable direct assets not recovered.

**Screen coverage: Medium / workflow visual.**

Source:
https://www.allica.bank/business-loans

---

## C2. Commerzbank — reduce organizational latency

### Flow

~2-minute online request  
→ optional financial document upload  
→ adviser contact within max 48 hours  
→ up to €100k can be decided directly in consultation  
→ larger/complex requests proceed to deeper analysis.

### Core UX mechanism

No claim of universal automation.

Instead:
**route quickly to someone who has authority to decide.**

### Screen evidence

Four-step journey documented on official page; actual customer screens unavailable.

**Screen evidence missing.**

Source:
https://www.commerzbank.de/unternehmerkunden/finanzierungen/gewerbekredit/

---

## C3. Judo — relationship is the interface

### Flow

Broker/direct referral  
→ relationship banker  
→ understand business/context  
→ financials / transactions / security  
→ banker + credit executive  
→ tailored terms  
→ legal/security  
→ settlement  
→ ongoing banker relationship.

### Core UX insight

For a multi-million-dollar SME exposure, the customer-experience object is not the number of screens.

It is:
- access to decision-maker;
- response time;
- consistency;
- expertise;
- ability to structure a deal.

### Screen evidence

Public self-service credit screenflow is absent because the journey is relationship-led.

**Screen evidence missing by operating-model design.**

---

# Journey D — Embedded merchant credit

## Core insight

In embedded merchant credit, the credit journey can almost disappear into the merchant's operating environment.

### Exemplars
- Stone
- Square
- Mercado Pago

---

## D1. Stone — best first-party visual evidence in the sample

### Flow

Merchant payment relationship  
→ automated credit analysis  
→ pre-approved offer on home screen  
→ choose amount  
→ review interest/installments/sales-retention %  
→ PIN  
→ analysis/status tracking  
→ funding  
→ automatic repayment from sales  
→ in-app servicing.

### Screen 1 — pre-approved offer

![Stone — pre-approved offer](https://martech-web-cdn.stone.com.br/optimized/stone/4271eb33-edc1-4617-a3eb-b42b1e09a759/step-by-step-emprestimo-desktop.png)

**What it proves**
- credit appears inside the merchant's operating account;
- available amount can be communicated before a traditional application.

### Screen 2 — status tracking

![Stone — application status](https://res.cloudinary.com/dunz5zfpt/f_auto%2Cc_limit%2Cw_1080%2Cq_90/stone-cms/prod/capital_de_giro_stone_abra_seu_app_confira_oferta_credito_passo_4_web_159c8abd6c)

**What it proves**
- request / analysis / approval / funding states are visible;
- customer can see where the loan is in the process.

### Screen 3 — repayment servicing

![Stone — repayment servicing](https://res.cloudinary.com/dunz5zfpt/f_auto%2Cc_limit%2Cw_1080%2Cq_90/stone-cms/prod/capital_de_giro_stone_vendeu_bem_no_mes_valor_da_parcela_diminui_b4c3ad04b5)

**What it proves**
- repayment is integrated into the app;
- the borrower sees installment/payment state and interest savings.

Source:
https://www.stone.com.br/capital-de-giro

---

## D2. Square — continuous seller eligibility

### Flow

Daily automatic merchant review  
→ loan offer appears in Dashboard/email  
→ amount slider  
→ fixed fee + repayment percentage update  
→ ownership/identity confirmation  
→ final review  
→ Square Checking instant or external bank 1–3 days  
→ percentage of daily sales repays loan  
→ eligibility refreshed after payoff.

### Core UX mechanism

The merchant does not build a traditional credit file.

Square's payment relationship **is** much of the credit file.

### Screen evidence

Official Square Help contains illustrative loan-dashboard/repayment screenshots, but stable direct asset URLs were not recovered.

**Screen coverage: Medium / official illustrations.**

Source:
https://squareup.com/us/en/banking/loans

---

## D3. Mercado Pago — marketplace/payment graph

### Flow

Seller activity  
→ automatic eligibility  
→ offer inside Mercado Pago  
→ choose product / amount / term  
→ accept terms  
→ immediate Mercado Pago balance credit  
→ product-specific repayment  
→ future offer based on updated behavior.

### Screen evidence

Credit-specific authenticated screens were not recovered.

**Screen evidence missing.**

Source:
https://www.mercadopago.com.mx/mercado-credito/prestamos-negocio-online

---

# Journey E — Guarantee-backed SME credit

## Core insight

Guarantee-backed journeys add one important backstage layer:

**programme eligibility / risk-sharing approval**

The best implementations hide as much of this complexity as possible inside the lender workflow.

### Exemplars
- Itaú FGI / Pronampe
- Stone incentive lines
- SBI guarantee-supported MSME products

---

## E1. Itaú — guarantee inside incumbent digital banking

### Flow

Existing Itaú Empresas relationship  
→ product/program eligibility  
→ tax/revenue sharing/checks  
→ simulate amount/term  
→ bank credit analysis  
→ government guarantee layer  
→ digital token acceptance  
→ funding.

### Why it matters

The guarantee changes:
- uncovered loss;
- collateral need;
- potentially pricing;
- provisions;
- capital.

Therefore the extra eligibility stage may improve approval economics even if it adds process complexity.

### Screen evidence

Exact app route is documented by official product pages, but stable transaction screens were not captured.

**Screen evidence missing.**

Sources:
https://www.itau.com.br/empresas/emprestimos-financiamentos/fgi
https://www.itau.com.br/empresas/emprestimos-financiamentos/fgo

---

# Cross-journey comparison

| Journey | Customer starts from | New data burden | Human intervention | Speed mechanism | Main economic advantage |
|---|---|---:|---|---|---|
| A Existing pre-approved | offer / conditional approval | Low | Low–exception / product-dependent | underwriting before application | low CAC + low processing cost + repeat/cross-sell |
| B New-to-lender digital | application | Medium | Low–medium | machine-readable data substitution | scalable acquisition + lower underwriting OPEX |
| C Medium relationship | request / adviser | High but economically justified | High | empowered humans / fewer handoffs | premium spread + larger ticket |
| D Embedded merchant | platform offer | Very low | Low | proprietary transaction data + embedded distribution | low CAC + monitoring + repayment control |
| E Guarantee-backed | banking/product offer | Medium | Medium | digital eligibility + risk-sharing | broader approval / lower uncovered risk |

---

# Where the customer actually waits

A useful journey comparison must distinguish **customer time** from **underwriting time**.

## Existing pre-approved / embedded
Much of underwriting occurs before customer action.

Visible wait may be:
- final fraud/KYC/credit confirmation;
- funding rails.

## New-to-lender digital
Wait concentrates in:
- data access;
- exceptions;
- missing documentation;
- final review.

## Relationship
Wait concentrates in:
- analyst/RM availability;
- clarifications;
- collateral/legal;
- decision authority.

## Guarantee-backed
Additional wait can arise from:
- programme eligibility;
- data sharing;
- guarantee confirmation.

---

# What screens do not show

A screenflow alone does not reveal:

- approval policy;
- rejected-customer journey;
- manual-review rate;
- fraud controls;
- PD/LGD;
- vintage performance;
- funding cost;
- capital usage.

This is why the Atlas must be read together with:
- `docs/executive_synthesis.md`;
- company teardowns;
- risk/economics benchmark.

---

# Screen evidence scorecard

| Company | First-party visual status | Best evidenced stages | Main gaps |
|---|---|---|---|
| Stone | **Strong** | offer, status, servicing | simulation, contract |
| iwoca | **Strong/Medium** | application, data, completion | detailed Open Banking, contract, servicing |
| Nubank | Partial | product surfaced in app | most detailed flow screens |
| Amex BLOC | Medium / official illustrations | draw, deposit, success | stable direct assets |
| CommBank | Partial | conditional offer observed | full application sequence |
| Allica | Medium / workflow illustrations | DIP, underwriting stages | authenticated application |
| Square | Medium / official illustrations | loan servicing/repayment | stable direct assets, offer sequence |
| Floryn | Partial | calculator/quickscan | PSD2, offer, dashboard |
| Konfío | Partial | simulator | authenticated flow |
| Rabobank | Low/Partial | calculator/process | transaction consent, offer |
| Mercado Pago | Low | product flow documented | credit screens |
| Itaú | Low | app route documented | credit screens |
| SBI | Low | product flow documented | credit screens |
| Commerzbank | Low | four-step process | actual screens |
| Judo | Low by design | relationship process | self-service screens not central |
| Funding Circle | Low/Partial | journey/calculator | authenticated screens |
| UGRO | Low/Partial | official embedded-flow diagram | partner app screens |
| Bibby | Low | explanatory journey | portal/invoice screens |

---

# Design implications for a target SME credit journey

## 1. Existing customer
Do not ask the borrower to rebuild information already available.

Target:
**offer → configure → accept → fund**

not:
**application → upload → wait → offer**.

## 2. New-to-bank
Ask for data connections before documents where possible.

Target hierarchy:
**transaction/tax/accounting data → exceptions/documents**.

## 3. Larger SME
Make human interaction valuable and visible.

Target:
**digital prep → named decision-maker → clear outstanding items → decision**

not:
**digital form → invisible manual queue**.

## 4. Embedded merchant
Keep credit in the operational context:
- payment dashboard;
- seller account;
- sales-linked repayment.

## 5. Guarantee-backed
Hide programme complexity wherever regulations allow:
- automated eligibility;
- tax/revenue pull;
- integrated guarantee checks.

---

# Atlas conclusion

The best SME journey is not the one with the fewest clicks.

It is the one in which:

> **the customer is asked only for information that is genuinely new, the decision model matches the exposure, and every necessary human step creates value rather than organizational delay.**

This is the customer-facing expression of the broader operating-model thesis:
**data × risk perimeter × decision rights × funding/economics.**
