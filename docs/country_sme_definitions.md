# Country SME Definitions — First Geography Set

Version date: 2026-10-02.

## Purpose

There is no globally consistent SME definition.

For this project, **source-native definitions are preserved** and mapped to normalized borrower bands only after the original threshold is recorded.

Do not overwrite a source’s population with a generic “SME” label.

---

# Summary table

| Country | Primary policy/statistical definition | Credit/research-specific definition to watch | Main comparability issue |
|---|---|---|---|
| United States | SBA size standards vary by NAICS; usually employees or average annual receipts | Fed SBCS: firms with <500 employees | No universal SME cutoff |
| United Kingdom | Procurement SME: <250 staff and ≤£44m turnover OR ≤£38m balance sheet | Business Population Estimates: 0–249 employees | Procurement/statistical/lender definitions differ |
| Brazil | ME ≤R$360k revenue; EPP >R$360k to ≤R$4.8m | BCB SCR: micro, small, medium to R$300m revenue with asset condition | Tax/legal “small” ≠ BCB credit MPME |
| Germany | EU SME: <250 employees and ≤€50m turnover OR ≤€43m balance sheet | KfW SME Panel: annual turnover ≤€500m | “Mittelstand” is much broader than EU SME |
| India | Current MSME limits combine investment + turnover | Same definition used for Udyam/PSL classification | Threshold change effective 2025-04-01 |
| Netherlands | EU SME definition used for SME policy/subsidies | KVK filing thresholds differ; lender/DNB series require source check | EU SME vs accounting/reporting categories |
| Australia | ABS: micro 0–4, small 5–19, medium 20–199 employees | Tax/policy and lender definitions can be turnover-based or source-specific | No single definition across use cases |
| Mexico | Official MIPYME stratification combines workers + sales, sector-specific | ENAFIN uses employment strata; micro sample is 6–10 employees | Survey scope differs from legal MIPYME universe |

---

# United States

## Primary official approach — SBA

The U.S. Small Business Administration does **not** use one universal threshold.

A size standard represents the largest size a business can have and still be considered small for relevant SBA/federal programs. Standards vary by NAICS industry and are generally expressed as:
- average annual receipts; or
- average number of employees.

Affiliates are relevant to size determination.

Current SBA size-standard resources:
https://www.sba.gov/document/support-table-size-standards
https://data.sba.gov/dataset/small-business-size-standards

## Important research definition — Federal Reserve SBCS

The Federal Reserve Banks’ Small Business Credit Survey defines its small-business survey population as firms with **fewer than 500 employees**.

Source:
https://www.fedsmallbusiness.org/reports/survey

## Project rule

For US data:
- preserve NAICS/SBA threshold for program/lending data when applicable;
- preserve <500 employees for SBCS;
- create normalized employee/revenue bands only as a second layer.

**Never write “US SME = <500 employees” as a universal statutory definition.**

---

# United Kingdom

## Procurement Act SME definition

Current UK procurement guidance states an enterprise qualifies as an SME when it has:
- fewer than 250 staff; and
- annual turnover ≤ **£44 million** **OR** balance-sheet total ≤ **£38 million**,

subject to ownership/group rules.

Source:
https://www.gov.uk/government/publications/procurement-act-2023-short-guides/supplementary-information-small-and-medium-sized-enterprises-definition-html

## Statistical definition

UK Business Population Estimates use employment bands:
- small business: **0–49 employees**;
- medium-sized: **50–249 employees**;
- SME: **0–249 employees**;
- large: 250+.

Source:
https://www.gov.uk/government/statistics/business-population-estimates-2025/business-population-estimates-for-the-uk-and-regions-2025-statistical-release

## Project rule

Tag UK data as:
- `UK_PROCUREMENT_SME`;
- `UK_BPE_EMPLOYMENT_SME`;
- lender-specific definition if different.

Do not assume British Business Bank, Companies House, HMRC and procurement thresholds are identical.

---

# Brazil

Brazil requires two definitions to be kept separately.

## Legal/tax ME and EPP

For Simples Nacional / Complementary Law framework:

- **Microempresa (ME):** annual gross revenue ≤ **R$360,000**.
- **Empresa de Pequeno Porte (EPP):** annual gross revenue > R$360,000 and ≤ **R$4.8 million**.

Source:
https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278

## Banco Central do Brasil — SCR borrower size

For credit-risk reporting in SCR, BCB instructs institutions to classify legal entities as:

- **Porte 1 — Micro:** annual gross revenue ≤ **R$360,000**.
- **Porte 2 — Small:** > R$360,000 and ≤ **R$4.8 million**.
- **Porte 3 — Medium:** > R$4.8 million and ≤ **R$300 million**, provided total assets are not above **R$240 million**.
- **Porte 4 — Large:** annual gross revenue > **R$300 million** **or** total assets > **R$240 million**.

Source:
Banco Central do Brasil, SCR Documento 3040 — Instruções de Preenchimento:
https://aprendervalor.bcb.gov.br/content/estabilidadefinanceira/Leiaute_de_documentos/scrdoc3040/SCR_InstrucoesDePreenchimento_Doc3040.pdf

## Project rule

For BCB lending/risk series use **BCB SCR size bands**, not the tax definition.

This is a major comparability point: the BCB “MPME” credit population includes firms far larger than legal/tax EPP.

---

# Germany

## EU SME definition

Germany uses the EU SME framework for many policy/support contexts:

### Micro
- <10 employees; and
- turnover ≤ €2m **OR** balance sheet ≤ €2m.

### Small
- <50 employees; and
- turnover ≤ €10m **OR** balance sheet ≤ €10m.

### Medium
- <250 employees; and
- turnover ≤ €50m **OR** balance sheet ≤ €43m.

Group/linked-enterprise rules apply.

EU source:
https://single-market-economy.ec.europa.eu/smes/sme-fundamentals/sme-definition_en

## KfW SME Panel definition

KfW’s flagship Mittelstand Panel includes private-sector enterprises with annual turnover up to **€500 million**.

Source:
https://www.kfw.de/About-KfW/KfW-Research/KfW-Mittelstandspanel.html

## Additional KfW definition caveat

Other KfW indicators can use different thresholds. For example, the KfW-ifo SME indicator generally uses ≤500 employees and ≤€50m annual turnover, with narrower sector-specific limits.

## Project rule

Never merge:
- `EU_SME`
- `KFW_PANEL_MITTELSTAND_500M`
- `KFW_IFO_SME`

without explicit re-bucketing.

---

# India

## Current MSME classification

Effective **1 April 2025**, the classification thresholds are:

### Micro
- investment in plant/machinery or equipment ≤ **₹2.5 crore**; and
- annual turnover ≤ **₹10 crore**.

### Small
- investment ≤ **₹25 crore**; and
- turnover ≤ **₹100 crore**.

### Medium
- investment ≤ **₹125 crore**; and
- turnover ≤ **₹500 crore**.

Government source:
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2209712

The 2025 revision increased investment limits 2.5x and turnover limits 2x versus the prior definition.

## Banking treatment

RBI directs regulated lenders to follow the Ministry of MSME / Udyam classification for MSME classification and priority-sector purposes.

RBI lending direction:
https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11060

## Project rule

For time series spanning April 2025:
- mark the definition break;
- do not interpret a jump in MSME stock/accounts as organic growth without testing reclassification effects.

---

# Netherlands

## EU SME definition

The Netherlands’ government business portal states that the EU definition is used for SME/MKB support contexts:

- employees: **<250**; and
- turnover ≤ **€50m** **OR**
- balance-sheet assets ≤ **€43m**.

Source:
https://business.gov.nl/starting-your-business/first-steps/what-is-an-sme/

Micro/small/medium EU sub-bands follow the European Commission thresholds:
- micro <10 / ≤€2m;
- small <50 / ≤€10m;
- medium <250 / ≤€50m turnover or ≤€43m balance sheet.

## Accounting/reporting caveat

Dutch Chamber of Commerce financial-reporting categories use separate thresholds. A company may satisfy the EU SME definition but fall into a different KVK reporting category.

## Project rule

For market/lending data:
- keep the DNB source definition;
- use EU SME only where the source explicitly aligns;
- do not infer DNB size bands from KVK filing categories.

---

# Australia

## ABS statistical business-size bands

Current ABS business-characteristics publications use:

- **Micro:** 0–4 persons employed.
- **Small:** 5–19 persons employed.
- **Medium:** 20–199 persons employed.
- **Large:** 200+.

In some ABS publications the broader phrase **small business** refers to all businesses with fewer than 20 employees, including micro.

Source:
https://www.abs.gov.au/statistics/industry/technology-and-innovation/characteristics-australian-business/2024-25

## Project rule

Use ABS employment bands as the default statistical normalization.

However:
- tax definitions may use turnover;
- bank/RBA lending statistics may use their own business-size classification.

Therefore lender/rate-series source definitions must remain attached.

---

# Mexico

## Official MIPYME stratification

The Secretaría de Economía’s official stratification published in the Diario Oficial de la Federación combines:
- employee count;
- annual sales;
- sector;
- a combined maximum score.

### Micro — all sectors
- employees: up to **10**;
- annual sales: up to **MXN 4 million**;
- maximum combined score: 4.6.

### Small
**Commerce**
- 11–30 employees;
- annual sales MXN 4.01m–100m;
- combined maximum 93.

**Industry and services**
- 11–50 employees;
- annual sales MXN 4.01m–100m;
- combined maximum 95.

### Medium
**Commerce**
- 31–100 employees.

**Services**
- 51–100 employees.

**Industry**
- 51–250 employees.

For medium firms:
- annual sales MXN 100.01m–250m;
- combined maximum 235 for commerce and 250 for industry/services.

Combined score formula:

`employees × 10% + annual sales (MXN million) × 90%`

Source:
https://dof.gob.mx/nota_detalle.php?codigo=5096849&fecha=30/06/2009

## ENAFIN 2024 survey strata

ENAFIN uses employment-size strata and, for its financing survey frame, defines:

- micro: **6–10** employed persons;
- small:
  - industry/services 11–50,
  - commerce 11–30;
- medium:
  - industry 51–250,
  - services 51–100,
  - commerce 31–100.

Source:
https://www.inegi.org.mx/rnm/index.php/catalog/1106

## Project rule

Do not extrapolate ENAFIN results to all legal microenterprises without noting that its micro survey population starts at 6 employed persons.

---

# Normalization policy

## Preserve three layers

For every country datapoint:

### 1. Source definition
Exact population used in the source.

### 2. Country definition tag
Examples:
- `US_SBA_NAICS`
- `US_FED_LT500`
- `UK_PROCUREMENT_SME`
- `BR_BCB_SCR_SIZE`
- `BR_ME_EPP`
- `EU_SME`
- `DE_KFW_PANEL_500M`
- `IN_MSME_2025`
- `AU_ABS_EMPLOYMENT`
- `MX_MIPYME_DOF`
- `MX_ENAFIN_EMPLOYMENT`

### 3. Project-normalized band
Only when enough information exists:
- micro;
- small;
- medium;
- upper-SME / lower-middle-market;
- large;
- unknown.

The normalized band **never replaces layer 1 or 2**.

---

# Comparability implications

## Safe-ish comparisons
Possible when source populations are explicitly aligned:
- EU-definition SME data between Germany and Netherlands;
- ABS employee bands over time in Australia;
- BCB SCR size bands over time in Brazil, subject to methodology changes.

## High-risk comparisons
Require re-bucketing or caveats:
- KfW “Mittelstand” vs EU SME;
- Brazil BCB MPME vs EU SME;
- US Fed <500 vs EU <250;
- India turnover/investment classification vs employee-based definitions;
- Mexico ENAFIN micro vs full legal microenterprise population.

---

# Status

Country definition mapping for the first eight markets is now sufficient to start building the market-source inventory.

It should be revised whenever:
- a source uses a different threshold;
- a country changes its legal classification;
- a lending dataset uses a proprietary size bucket.
