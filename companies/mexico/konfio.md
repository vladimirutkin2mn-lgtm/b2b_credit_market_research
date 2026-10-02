# Company / Lender Teardown — Konfío

**Status:** Batch 3 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Mexico  
**Primary segment:** S2 — digital unsecured SME credit  
**Primary question:** can tax/invoice data substitute for collateral and traditional SME financial packages?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**Konfío's core innovation is not simply online lending; it is using Mexican tax-system data as the primary underwriting spine.** The borrower can begin with RFC + SAT CIEC, allowing Konfío to analyze invoicing and fiscal activity, generate a personalized offer, and avoid mortgage collateral. Repeat offers then update as company inflows/outflows and repayment behavior evolve.

### Quantified proof points

Current public product:
- credit up to **MXN10m**;
- advertised funding within **48 hours**;
- no mortgage collateral;
- fixed rate;
- public flow says approval can occur in minutes;
- money typically 24–72 hours depending validation.
- current site marketing says **8 in 10** customers report Konfío was their first credit — treat as company marketing/survey claim, not population statistic.

### Mechanism

SAT CIEC / invoice-tax history
→ observed business revenue and fiscal behavior
→ AI / proprietary scoring
→ personalized amount/term
→ no real-estate collateral
→ digital contract
→ repeat offers as new behavior accumulates.

### Strategic implication

In markets with strong tax e-invoicing, **tax infrastructure can play the role Open Banking plays elsewhere**.

### Transferability

**High only where tax/e-invoice data are digital, accessible and reliable.**

### Counter-evidence

Konfío is private and public risk/economic disclosure is limited. Faster access and inclusion cannot be assumed to imply superior portfolio quality or profitability.

---

## 1. Product

Current public page:
- up to MXN10m;
- no mortgage guarantee;
- fixed rate;
- prepayment allowed;
- online simulation/application.

Source:
https://konfio.mx/credito/

Older/currently updated help/blog material describes:
- RFC;
- SAT CIEC;
- personalized offer;
- amount/term selection;
- document verification;
- FIEL contract signature;
- funding to bank account;
- repeat offers during/after the first credit.

---

## 2. Underwriting/data architecture

### Directly evidenced inputs

- SAT CIEC;
- monthly invoicing/fiscal data;
- company inflows/outflows;
- bureau / credit history in broader risk materials;
- KYC/documentation.

Konfío says CIEC is read-only access and supports analysis of tax/invoicing information.

### What this replaces

Traditional SME process often requests:
- manually supplied revenue proof;
- years of financial statements;
- collateral.

Konfío instead attempts to infer repayment capacity from machine-readable business tax data.

---

## 3. Customer journey

1. Select tax regime.
2. Enter required amount.
3. Provide RFC/CIEC.
4. Konfío analyzes business invoicing/fiscal activity.
5. Personalized offer appears.
6. Select amount/term.
7. Upload identity/company documents if required.
8. Sign with FIEL/digital process.
9. Funds to bank account.
10. Repeat offers may appear as behavior evolves.

### Visual evidence

The current official product page exposes an interactive simulator with:
- tax regime;
- desired amount.

Stable full application screenflow assets were not captured.

**Screen evidence: Partial.**

---

### Current tax-data underwriting evidence — enriched second pass

Konfío's current official materials reinforce the underwriting sequence:

- customer provides **RFC + SAT password/CIEC**;
- Konfío uses read-only fiscal/invoicing data to personalize financing;
- the system estimates affordable monthly payment and generates a personalized amount/rate/term;
- after validation, the customer can receive recurring/new offers in the Konfío app as business inflows/outflows and repayment behavior evolve.

Current official explanations explicitly say SAT data are used to:
1. personalize financing to business size;
2. calculate affordable monthly payment;
3. set a fixed rate appropriate to the business profile.

**What it proves**
- tax-data access is the underwriting spine, not merely a KYC step;
- the personalized offer is calculated from observed fiscal behavior;
- repeat credit can become increasingly relationship-like even though the original customer was new-to-lender.

**Screen status:** current simulator remains public; authenticated SAT-consent / personalized-offer screen asset not recovered.

Official sources:
- https://konfio.mx/credito/
- https://konfio.mx/blog/soluciones-financieras/credito/ventajas-de-ingresar-tus-datos-del-sat-en-konfio/
- https://konfio.mx/blog/soluciones-financieras/creditos/que-es-konfio-y-como-impulsa-negocios-en-mexico/

---

## 4. Risk

Public risk architecture is clear at a high level:
- alternative tax/invoice data;
- proprietary score;
- no real-estate collateral for the standard product;
- fixed-term repayment.

Missing:
- NPL;
- DPD;
- charge-offs;
- cost of risk;
- vintages;
- approval rates;
- loss by repeat/first borrower.

---

## 5. Economics/funding

Public product pricing is personalized.

Konfío does not currently disclose enough product P&L to build:
- portfolio yield;
- funding cost;
- net spread;
- credit cost;
- ROA/RAROC.

Therefore this case is primarily a **data/journey architecture** case rather than an economics benchmark.

---

## 6. Hypothesis tests

### H4 — data substitution: very strongly supported
SAT data substitutes for much of the traditional financial-file process.

### H2 — speed is segmentation: supported
The shortcut depends on sufficient formal tax/invoice data and eligibility.

### H6 — repeat lending: supported operationally
Public materials describe new offers as behavior/history accumulates.

### H3 — funding advantage: unresolved
No sufficiently detailed public funding-cost economics.

---

## 7. Strategic implication

For SME markets with digital tax invoices, the bank's data roadmap should not stop at:
- bureau;
- Open Banking.

It should include:
- tax;
- invoices;
- receivables;
- e-commerce/payment flows.

Different countries may have different “best” machine-readable proxy for business cash flow.

---

## 8. Evidence gaps

1. Loan book/originations.
2. Approval rate.
3. NPL/charge-offs.
4. Funding model/cost.
5. Yield/ROA.
6. Repeat-customer loss/economics.
7. Full first-party screens.

---

## Sources

- https://konfio.mx/credito/
- https://konfio.mx/producto/credito
- https://konfio.mx/blog/soluciones-financieras/credito/como-solicitar-un-credito-empresarial-y-obtenerlo-el-mismo-dia/
- https://konfio.mx/blog/gestion-del-negocio/que-es-la-contrasena-del-sat-ciec/
- https://konfio.mx/blog/soluciones-financieras/creditos/que-es-konfio-y-como-impulsa-negocios-en-mexico/
