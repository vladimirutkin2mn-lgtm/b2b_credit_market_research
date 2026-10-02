# Company / Lender Teardown — State Bank of India SME

**Status:** Batch 2 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** India  
**Primary segments:** S1/S3/S5  
**Primary question:** can one universal bank run both instant cash-flow SME lending and large relationship/centralized credit at scale?

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**SBI is perhaps the strongest evidence so far that SME lending should be designed as multiple factories inside one institution.** It runs instant transaction-history-based micro/small-business credit, end-to-end digital cash-flow products up to ₹50 lakh, automated decision engines into crore-sized exposures, and a separate branch/CPC relationship infrastructure for larger and more complex SME credit. At the same time, its MSME asset quality improved while the book grew rapidly.

### Quantified proof points — FY2026

- >**23 lakh SME customers**.
- SME portfolio: about **₹6.12 trillion (₹612,222 crore)**, +20.99% YoY.
- SME portfolio = **14.60% of domestic advances**.
- disclosed SME segment yield: **9.16%**.
- narrower MSME portfolio: **₹450,683 crore**, +29.81% YoY.
- MSME GNPA: **1.18%**, down from 1.25%.
- PABL: **1.11 lakh loans**, ₹5,513 crore sanctioned/disbursed in FY26.
- PABL limit: up to **₹20 lakh**, instant sanction based on transaction history.
- Digi Sugam: up to **₹50 lakh**, cash-flow/GST/account based.
- broader fast-tracked digital SME lending: up to **₹5 crore**.

### Mechanism

Existing CASA / transaction / UPI / GST data
→ pre-approved cash-flow underwriting
→ instant/digital lower-ticket sanction.

As ticket/complexity rises:
→ more financial data
→ BRE / centralized processing
→ branch/CPC/relationship architecture.

### Strategic implication

A universal bank should not force a single underwriting operating model across SME. SBI's architecture is closer to a **portfolio of factories** linked by common data and risk infrastructure.

### Transferability

**High where a bank has current accounts + national digital tax/payment data.**

### Counter-evidence / limitation

Indian policy infrastructure (GST, Udyam, priority-sector rules, guarantee schemes, UPI) is unusually enabling. The model cannot be transplanted unchanged to markets with weaker formal data.

---

## 1. Definitions — important comparability warning

SBI public materials use both:
- **SME portfolio** — broader internal segment: ~₹6.12tn;
- **MSME portfolio** — policy/classification subset: ₹450,683 crore.

These are **not interchangeable**.

The MSME definition also changed effective 1 April 2025, so historical growth must be interpreted with care.

---

## 2. Digital credit stack

### PABL — Pre-Approved Business Loan

- existing-customer / transaction-history-based;
- instant sanctions up to **₹20 lakh**;
- FY26: 1.11 lakh loans / ₹5,513 crore.

This is a classic S1 pre-underwriting model.

### PAsBL — Pre-Approved Small Business Loan

Launched 1 Jan 2026:
- cash-flow based;
- existing CASA customers;
- targets informal micro enterprises;
- uses UPI settlement data.

FY26:
- 3.55 lakh leads;
- ₹11,913 crore potential;
- 11,214 conversions;
- ₹372.05 crore business.

### SME Digi Sugam

Public product:
- ₹1–50 lakh;
- min 2 years vintage;
- GST data >=2 years;
- account statements pulled from SBI/CBS or uploaded/fetched;
- two years ITR;
- dropline OD;
- top-up after 12 months subject to clean behavior;
- CMR / bureau requirements.

An important policy breakpoint:
- if enhancement pushes above ₹50 lakh, it is redirected to **branch channel** or capped at ₹50 lakh.

This is direct H2 evidence.

### Larger automated lending

SBI reports fast-tracked digital lending up to **₹5 crore** and BRE-based processing for SME credit.

---

## 3. Customer journey — transaction-visible existing customer

### PABL/PAsBL archetype

1. Existing current/CASA account produces transaction/UPI history.
2. SBI analytics generates lead / pre-approved limit.
3. Customer sees/receives offer in digital banking journey.
4. Minimal additional verification/consent.
5. Instant sanction.
6. Digital documentation/disbursement.

### Digi Sugam archetype

1. YONO Business.
2. Udyam/PAN/GST identification.
3. GST data + account statements.
4. ITR and bureau.
5. digital assessment.
6. sanction.
7. digital top-up/renewal under conditions.

### Visual evidence

SBI product pages contain product imagery but a reliable complete first-party credit screenflow was not captured.

**Screen evidence:** Low/partial; flow strongly documented, UI screens missing.

---

## 4. Risk architecture

Observed controls:
- transaction/cash-flow history;
- GST turnover;
- ITR;
- bureau/CMR;
- account credit summation;
- delinquency/SMA conditions for top-up;
- branch escalation above digital limits;
- dedicated SME processing centers for high value.

### Asset quality

FY26 MSME:
- NPA amount: **₹6,515 crore**;
- GNPA: **1.18%**, vs 1.25% at Mar-2025.

This is meaningful because the book expanded materially while the ratio improved.

Caveat: the 2025 definition revision can affect portfolio composition.

---

## 5. Economics

Public SME segment evidence:
- portfolio: ~₹6.12tn;
- segment yield: **9.16%**.

This is unusually useful product-segment economics relative to many banks.

Missing:
- funding cost allocated to SME;
- SME cost of risk;
- SME OPEX;
- SME RWA / RAROC.

Group bank economics should not be used to back-solve those without disclosure.

---

## 6. Operating model — digital + relationship

SBI maintains a large specialist physical/processing infrastructure alongside digital:
- SME-intensive branches;
- centralized credit/processing centers;
- high-value proposal handling.

This supports the thesis that automation **does not replace** the relationship factory; it segments it.

---

## 7. Hypothesis tests

### H1 — existing-customer advantage: very strongly supported
PABL/PAsBL explicitly use existing account/transaction data.

### H2 — speed is segmentation: very strongly supported
Digi Sugam has a hard ₹50 lakh digital route and redirects higher enhancement to branch.

### H4 — data substitution: strongly supported
GST, UPI, account and bureau data are machine-readable underwriting inputs.

### H5 — SME is several businesses: strongly supported
The bank visibly runs micro pre-approved, digital structured and high-value centralized/RM lanes.

### H6 — repeat economics: supported operationally
Top-up is permitted after 12 months based on observed clean behavior; direct repeat-cohort economics are not public.

---

## 8. Strategic implication

SBI suggests an architecture for universal banks:

**Lane 1 — continuous pre-approved micro credit**  
transaction + UPI behavior.

**Lane 2 — digital cash-flow SME**  
GST + bank statements + bureau + ITR.

**Lane 3 — larger/complex SME**  
centralized credit + branch/RM + richer analysis.

The benefit is not simply faster lending; it is **allocating underwriting cost to economic exposure**.

---

## 9. Evidence gaps

1. Approval rates by digital product.
2. PABL/PAsBL NPL vs traditional SME.
3. Digital-vs-branch cost-to-serve.
4. SME cost of risk.
5. RWA / economic capital.
6. Full customer screens.
7. Time-to-cash, not only sanction.
8. Repeat borrower cohort economics.

---

## Sources

- SBI FY2025-26 Annual Report: https://nsearchives.nseindia.com/annual_reports/AR_29279_SBIN_2025_2026_A_22551017_26052026223038.pdf
- https://sbi.co.in/web/business/sme-digi-sugam
- SBI SME / business product pages and annual-report disclosures
