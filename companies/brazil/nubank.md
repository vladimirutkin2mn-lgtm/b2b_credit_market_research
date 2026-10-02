# Company / Lender Teardown — Nubank / Nu Empresas

**Status:** Batch 1 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Brazil  
**Primary segment:** micro / small business  
**Primary journey:** existing Nu Empresas customer → pre-approved working-capital offer

---

## Executive synthesis — answer first

**Nubank's SME credit advantage is primarily an account-and-data advantage, not merely a faster digital form.** Nu Empresas embeds credit into an existing 6-million-customer business-account relationship, continuously re-evaluates eligibility in the background, and only exposes the visible borrowing flow after an offer exists. The result is a short customer journey because part of underwriting has already happened before the customer starts applying.

### Quantified proof points
- **6 million** Nu Empresas customers by May 2026.
- Group deposits of **US$45.3bn** support a deposit-funded balance-sheet context, although this is not SME-specific.
- Capital de Giro funds are deposited **immediately after approval**.
- FGI-PEAC publicly advertises decisioning up to **24 hours** and rates from **1.75% per month**.

### Mechanism
Business-account relationship
→ transaction/relationship signals
→ recurring automated eligibility analysis
→ proactive in-app offer
→ reduced visible data-entry burden
→ digital contracting
→ immediate in-account funding.

### Strategic implication
For another lender, the transferable lesson is not “copy Nubank's screens.” The prerequisite is a sufficiently rich ongoing customer relationship or equivalent data feed that allows underwriting to move upstream of the visible application.

### Transferability
**Transferable with prerequisites.**

Required:
- existing transactional relationship or equivalent consented data;
- digital identity and contracting;
- strong pre-offer decisioning;
- servicing inside the same account/app.

### Counter-evidence / limitation
Public information does **not** disclose Nu Empresas-specific loan book, approval rate, NPL, cost of risk or unit economics. Therefore we can conclude that the journey mechanism is strong; we cannot yet conclude that the SME credit portfolio has superior risk-adjusted economics.

---

## 0. Scope and comparability

This teardown distinguishes three evidence levels:

1. **Nu Empresas-specific** — corporate-customer product, journey and customer-base evidence.
2. **Nu Holdings / Brazil-wide** — group financial/risk/funding metrics that are useful context but are **not SME-specific**.
3. **Hypothesis** — mechanism inferred from evidence but not directly disclosed.

Do not attribute Nu Holdings' group NPL, NIM or credit portfolio directly to Nu Empresas.

---

## 1. Executive fact sheet

| Metric | Value | Period | Scope | Evidence |
|---|---:|---|---|---|
| Nu Empresas customers | 6 million | May 2026 | SME/corporate customers | Nu newsroom |
| Nu global customers | 139 million | Q2 2026 | group | Nu Q2 results |
| Brazil customers | almost 118 million | Q2 2026 | Brazil total | Nu Q2 results |
| Group total credit portfolio | US$39.4bn | Q2 2026 | group, all credit | Nu Q2 results |
| Group deposits | US$45.3bn | Q2 2026 | group | Nu Q2 results |
| Brazil deposits | US$36.4bn | Q2 2026 | Brazil total | Nu Q2 results |
| Group NPL 15–90 | 4.8% | Q2 2026 | group | Nu Q2 results |
| Group NPL 90+ | 6.9% | Q2 2026 | group | Nu Q2 results |
| Group NIM | 22.9% | Q2 2026 | group | Nu Q2 results |
| Group risk-adjusted NIM | 12.4% | Q2 2026 | group | Nu Q2 results |
| Group credit cost | US$1.7bn | Q2 2026 | group | Nu Q2 results |
| Group net income | US$1.1bn | Q2 2026 | group | Nu Q2 results |
| Group ROE | 33% | Q2 2026 | group | Nu Q2 results |
| SME loan book | **Unknown** | — | Nu Empresas | screen evidence missing / disclosure gap |
| SME NPL / CoR | **Unknown** | — | Nu Empresas | disclosure gap |

### Sources
- https://nu.com/en/newsroom/company/nu-empresas-reaches-6-million-customers-and-becomes-the-largest-financial-institution-in-brazil-in-number-of-cnpjs
- https://international.nubank.com.br/en/newsroom/company/nu-holdings-ltd-reports-second-quarter-2026-financial-results

---

## 2. Business model

Nu Empresas is an **account-led SME banking model** rather than a standalone loan-originator model.

The core credit mechanism visible in public materials is:

**business account relationship → continuous automated credit analysis → offer appears inside app → customer simulates/accepts → loan funded into Nu Empresas account → automated servicing**

This matters because acquisition, underwriting and servicing can reuse the same account relationship.

### Scale

Nu Empresas reached **6 million SME customers** in May 2026.

This is customer-base scale, not borrower count.

No reliable public figure found yet for:
- active SME borrowers;
- SME working-capital loan book;
- SME originations;
- SME credit revenue.

---

## 3. Product portfolio

### 3.1 Capital de Giro

**Use case:** cash-flow / working capital.

**Eligibility**
- must be a Nu Empresas customer;
- Capital de Giro functionality must appear in app;
- final credit approval required.

**Pricing**
- personalized in simulation;
- exact public rate range not found;
- general Nu Empresas loan terms state **no origination fee**.

**Repayment**
- installments;
- standard method is automatic debit from Nu Empresas account;
- borrower can request same-day boleto through support;
- early installment payment generates proportional interest discount;
- repayment date/installment structure is chosen in app.

**Funding SLA**
If approved after contracting, the requested amount is deposited into the Nu Empresas account **immediately**.

Sources:
- https://nubank.com.br/empresas/emprestimos
- https://nubank.com.br/contratos/termos-e-condicoes-geral-de-emprestimo-nu-empresas

### 3.2 Capital de Giro FGI-PEAC

Launched May 2026.

Publicly disclosed terms:
- BNDES FGI-PEAC guarantee;
- 6–82 month repayment term;
- grace period up to 2 years;
- rate from **1.75% per month**, subject to approval;
- approval stated as up to **24 hours**;
- funds credited in-app/account at approval.

Source:
https://nu.com/en/newsroom/company/nubank-expands-its-credit-portfolio-with-solutions-for-sme-customers

### 3.3 Receivables Anticipation

Launched May 2026.

Public mechanism:
- advance issued boleto receivables before due date;
- no invoice required;
- performed directly in app in a few clicks.

Source:
https://nu.com/en/newsroom/company/nubank-expands-its-credit-portfolio-with-solutions-for-sme-customers

### 3.4 Other credit capabilities

Nu Empresas also publicly references:
- corporate credit card;
- Pix on Credit;
- Boleto on Credit;
- Nu Limite Garantido.

These expand business-credit usage beyond one term-loan product.

---

## 4. Underwriting and risk architecture

### 4.1 What is directly evidenced

Nubank states that Capital de Giro availability is determined by **frequent and automatic credit analysis**.

Inputs publicly described include:

**Internal**
- product/account usage;
- Nu Empresas account movement;
- payment behavior;
- concentration of financial activity with Nu PJ/PF.

**External**
- publicly available financial-profile data.

Nubank explicitly says:
- customer service cannot manually release/approve a loan offer;
- analysis is recurring and automatic;
- using the account and remaining current can improve the information available for analysis.

Source:
https://nubank.com.br/empresas/emprestimos

### 4.2 Group-wide technology context

Nu states that its financial-behavior foundation model **NuFormer** powers underwriting, customer service and growth decisions across the company.

This is useful context but **not direct evidence that a particular Nu Empresas Capital de Giro decision is made by NuFormer**.

Source:
https://international.nubank.com.br/en/newsroom/company/nu-holdings-ltd-reports-second-quarter-2026-financial-results

### 4.3 What is unknown

No public evidence found yet for Nu Empresas-specific:
- score variables/weights;
- cutoffs;
- approval rate;
- manual-exception process;
- SME PD/LGD;
- vintage curves;
- SME NPL;
- SME cost of risk.

**Confidence:** High on observed public mechanism; Low/Unknown on proprietary credit-model details.

---

## 5. Customer journey — Capital de Giro

### Scenario

Existing Nu Empresas customer whose account already has a Capital de Giro offer/function available.

### Flow

| Stage | Customer-visible action | Evidence | Status |
|---|---|---|---|
| 1. Eligibility | Capital de Giro function appears in app after automatic analysis | Official FAQ | Documented |
| 2. Entry | Tap Capital de Giro on PJ home screen | Official FAQ | Documented |
| 3. Product intro | Review explanation of product | Official FAQ | Documented |
| 4. Simulation | Choose amount, number of installments and first due date | Official FAQ | Documented |
| 5. Price disclosure | App shows total amount payable including interest | Official FAQ | Documented |
| 6. Proposal summary | Review simulated structure | Official FAQ | Documented |
| 7. Responsible person | Confirm responsible person's name and CPF | Official FAQ | Documented |
| 8. Contract | Review key contract conditions and tap Contract | Official FAQ | Documented |
| 9. Authentication | Enter 4-digit password/PIN | Official FAQ | Documented |
| 10. Funding | If approved, money enters Nu Empresas account immediately | Official FAQ | Documented |
| 11. Servicing | Track/manage Capital de Giro in app | Official FAQ | Documented |
| 12. Repayment | Automatic debit; early repayment with interest discount | Official FAQ | Documented |
| 13. Distress | Renegotiation via support; different process for current vs overdue loan | Official page | Documented |

Source:
https://nubank.com.br/empresas/emprestimos

### Important journey observation

There are two separate “decision” moments:

1. **Offer eligibility** — recurring automated analysis determines whether the product appears.
2. **Contract/request approval** — the requested proposal remains subject to approval.

This distinction should be preserved in cross-lender comparisons.

---

## 6. Visual customer journey / screen evidence

### Official screen evidence found

#### A. Official Capital de Giro marketing image
Source page:
https://nubank.com.br/empresas/emprestimos

Asset surfaced by official page:

![Nu Empresas Capital de Giro — official visual](https://www.datocms-assets.com/120597/1743107465-nu-empresas-capital-de-giro.jpg?crop=focalpoint&dpr=1&fit=crop&fm=jpg&q=60&w=1200)

Direct asset:
https://www.datocms-assets.com/120597/1743107465-nu-empresas-capital-de-giro.jpg?crop=focalpoint&dpr=1&fit=crop&fm=jpg&q=60&w=2000

**Evidence type:** official marketing image showing the Capital de Giro function on a Nu Empresas phone screen.

**What it proves**
- Capital de Giro is surfaced inside the mobile experience.
- Product is presented as an in-app business-credit capability.

**What it does not prove**
- exact fields/pricing layout;
- full simulation flow;
- contract confirmation;
- servicing dashboard.

### Screenflow gaps

The official page provides detailed textual step-by-step instructions, but we do **not yet have clean first-party screenshots** for every step.

| Stage | Screen evidence |
|---|---|
| Offer/banner | partial official visual |
| Product intro | screen evidence missing |
| Simulation amount | screen evidence missing |
| Installment selection | screen evidence missing |
| First-payment date | screen evidence missing |
| Total-to-pay disclosure | screen evidence missing |
| Proposal summary | screen evidence missing |
| Responsible-person confirmation | screen evidence missing |
| Contract review | screen evidence missing |
| PIN confirmation | screen evidence missing |
| Funding confirmation | screen evidence missing |
| Servicing dashboard | screen evidence missing |
| Early repayment | screen evidence missing |
| Renegotiation | screen evidence missing |

**Screen coverage status: Partial.**

Non-business/personal-loan Nubank screenshots are deliberately excluded from SME evidence.

---

## 7. Lending economics and funding

### What is observable at group level

Q2 2026:
- total credit portfolio: US$39.4bn;
- deposits: US$45.3bn;
- consolidated deposit cost: 88% of interbank rates;
- NIM: 22.9%;
- risk-adjusted NIM: 12.4%;
- credit cost: US$1.7bn;
- credit represented 41% of gross profit contribution.

This supports the structural observation that Nu is a **deposit-funded digital lender at group level**.

### What cannot be concluded

We cannot infer:
- Nu Empresas loan yield;
- Nu Empresas funding spread;
- SME cost of risk;
- SME RAROC;
- SME contribution margin.

Any such calculation using group metrics would be false precision.

---

## 8. Risk context

Group Q2 2026:
- NPL 15–90: 4.8%;
- NPL 90+: 6.9%.

Management says the 90+ increase largely reflected seasonal migration of first-quarter early delinquencies and that the business had deliberately expanded into higher-risk/higher-return segments.

Again: **this is group credit quality, not SME portfolio quality.**

---

## 9. Distinctive capabilities

### Well evidenced

1. **Credit offer embedded in the operating account**
2. **Recurring automated eligibility analysis rather than customer-initiated manual underwriting**
3. **Internal relationship/activity data explicitly used**
4. **End-to-end mobile simulation and contracting**
5. **Immediate disbursement after approval**
6. **In-app servicing and early-payment discount**
7. **Broader SME credit portfolio now includes receivables and government-guaranteed working capital**
8. **6 million SME customers creates a large potential cross-sell base**

---

## 10. Mechanism hypotheses

### H1 — Existing-customer advantage: strongly supported as mechanism

Observed:
- Capital de Giro requires Nu Empresas relationship;
- account use and financial concentration provide more internal information;
- eligibility is automated and recurring.

Hypothesis:
This can reduce acquisition/data-collection cost and allow proactive offers.

**Not yet proven:** superior credit losses or approval conversion versus new-to-bank lenders.

### H4 — UX from data substitution: supported

The core journey does not begin with uploading financial statements. Eligibility occurs in the background, and customer-facing journey starts after an offer exists.

This is evidence that much underwriting friction is shifted **before** the visible loan application.

### H6 — Repeat/relationship economics: plausible

Nubank has a large business-account base and continuously updates credit eligibility, but public evidence does not yet show repeat-loan cohort economics.

---

## 11. Evidence gaps

Highest-value missing evidence:

1. Nu Empresas credit portfolio outstanding.
2. Number/share of 6m SME customers with a credit product.
3. Working-capital originations.
4. Approval rate / offer rate.
5. Typical ticket and term distribution.
6. SME-specific NPL/DPD/charge-off/ECL.
7. SME pricing/yield.
8. Repeat borrower performance.
9. Exact underwriting data beyond generic internal/external categories.
10. Full first-party screenflow.

---

## 12. Current synthesis

### Well evidenced

Nu Empresas is a large account-led SME franchise with 6m customers and a working-capital flow in which **credit eligibility is continuously assessed before the customer begins the visible application journey**.

### Plausible but not proven

Its structural advantage likely comes from:
- existing-account data;
- low-friction distribution;
- high-frequency automated re-underwriting;
- deposit-funded group balance sheet.

### What contradicts an overly simple “instant SME lending” narrative

The product is not universally available on demand. The customer must first receive the functionality/offer through Nubank's automated analysis, and the final proposal remains subject to approval.

### Confidence

- Product/journey mechanism: **High**
- Underwriting input categories: **Medium/High**
- SME-specific risk/economics: **Low / Unknown**
- Visual screenflow completeness: **Low/Partial**

---

## Sources

Primary:
- https://nubank.com.br/empresas/emprestimos
- https://nubank.com.br/empresas
- https://nubank.com.br/contratos/termos-e-condicoes-geral-de-emprestimo-nu-empresas
- https://nu.com/en/newsroom/company/nu-empresas-reaches-6-million-customers-and-becomes-the-largest-financial-institution-in-brazil-in-number-of-cnpjs
- https://nu.com/en/newsroom/company/nubank-expands-its-credit-portfolio-with-solutions-for-sme-customers
- https://international.nubank.com.br/en/newsroom/company/nu-holdings-ltd-reports-second-quarter-2026-financial-results
- https://www.sec.gov/Archives/edgar/data/1691493/000129281426002166/nuform20f_2025.htm
