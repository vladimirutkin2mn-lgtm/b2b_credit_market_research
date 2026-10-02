# Company / Lender Teardown — CommBank Business

**Status:** Batch 1 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Australia  
**Primary segments:** S1/S2/S5  
**Primary scenario:** existing CommBank small-business customer applying for BetterBusiness Loan

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**CommBank provides one of the cleanest natural experiments for the value of an existing transaction relationship: the same bank can give eligible existing customers an online application in ~10 minutes with an instant decision and funds within minutes, while new customers are routed to a specialist appointment.** The difference is not UI alone — CommBank explicitly uses information it already holds about existing customers.

### Quantified proof points

- Business lending: **A$168bn** at Dec-2025, up **12% YoY** from A$150bn.
- Business transaction accounts: **1.4m**, up **7% YoY**.
- Around **90% of business loans are linked to a transaction account**.
- Existing-customer BetterBusiness Loan application: about **10 minutes**; eligible borrowers can receive an **instant decision** and funds within minutes.
- Small-business auto-approvals through BizExpress **doubled over two years**.
- Business Banking 1H26 operating performance: **A$3.342bn**; impairment expense **A$91m**; cash NPAT **A$2.272bn**.
- Management reported business loan losses of about **6 bps** in the half.

### Mechanism

Existing transaction relationship
→ bank already possesses identity/account/cash-flow data
→ conditional/pre-approved eligibility
→ less customer input
→ automated credit decision
→ instant digital fulfillment.

New-to-bank
→ missing relationship data
→ specialist contact / greater information collection
→ slower path.

### Strategic implication

The strongest incumbent-bank advantage may not be cheaper funding alone. It can be **pre-existing information** that allows the bank to remove application steps and make decisions before competitors can finish data collection.

### Transferability

**Highly transferable to banks with active SME current-account relationships.**

Prerequisites:
- high transaction-account penetration;
- usable cash-flow history;
- integrated decision engine;
- digital origination/contracting;
- clear policy for when a specialist takes over.

### Counter-evidence / limitation

Instant decisioning applies only to eligible existing-customer cases. It should not be presented as CommBank's universal SME journey. Larger/secured/new-to-bank cases remain more relationship- and documentation-led.

---

## 0. Scope

Primary product:
**BetterBusiness Loan**

Broader business-banking economics are used to provide context but are not identical to small-business-loan economics.

---

## 1. Product portfolio and customer segmentation

### BetterBusiness Loan — unsecured

Public product evidence:
- online application for eligible existing customers;
- application roughly 10 minutes;
- instant decision if eligible;
- funds within minutes;
- online variable rate publicly shown from **12.84% p.a.** at research date;
- limits up to **A$250k**;
- term up to **7 years**.

### BetterBusiness Loan — secured

Public page:
- variable rate from **7.29% p.a.** at research date;
- amounts from A$10k;
- longer terms possible depending security, potentially up to 30 years;
- specialist involvement.

### Eligibility / risk controls

Public page references:
- recent overdraft/arrears history;
- bankruptcy history;
- recent collections;
- for secured lending, security/deposit/cash-reserve requirements.

Documents may include:
- financial statements;
- personal income information;
- bank statements;
- identification.

---

## 2. Existing-customer vs new-customer journey

### Existing customer

1. Log in to NetBank/app.
2. Access business loan/finance offers.
3. CommBank can use information already held.
4. Eligible customer may be conditionally approved.
5. Online application takes roughly 10 minutes.
6. Instant decision may be available.
7. Funds can arrive within minutes.
8. Loan can be serviced digitally.

### New customer

Public BetterBusiness Loan page instructs a new-to-bank customer to book an appointment / speak with a business specialist.

This creates a useful within-bank control:
**same institution, different data availability, different journey.**

---

## 3. Visual customer journey

An official CommBank product-page visual shows the app navigation into:

**Business loans &… → Your offers → conditional approval**

with text indicating:
> Great news — your business is conditionally approved for finance.

### What it proves

- credit can be surfaced proactively inside the authenticated app;
- some existing customers reach the application with conditional approval already present;
- the journey begins from an existing-data position rather than a blank application.

### Evidence status

The official screen was observed on CommBank's product-site materials, but the research index did not expose a stable direct image-asset URL suitable for embedding in GitHub.

Therefore:
- official customer screen observed: **Yes**
- embedded static screen in repo: **screen evidence missing**
- source page: https://www.commbank.com.au/business/loans-and-finance/betterbusiness-loan.html

### Remaining gaps

- detailed amount-selection screen;
- data-consent screen;
- decision screen;
- e-sign;
- funding confirmation;
- servicing dashboard.

---

### Current official conditional-approval evidence — enriched second pass

CommBank's current BetterBusiness Loan page includes a first-party mobile screen showing:

- **Business loans & finance**
- **Your offers**
- the message **"your business is conditionally approved for finance"**
- available business-finance products.

The same current page states:
- the conditional approval is based on information CommBank already knows about the business;
- the customer can apply online in minutes with no paperwork;
- existing customers apply in NetBank in up to ~10 minutes;
- eligible customers receive an instant decision and funds within minutes;
- new-to-bank customers are routed to a Business Lending Specialist.

**What it proves**
- pre-underwriting is visible to the customer as an offer state;
- the best digital journey is explicitly tied to an existing relationship;
- this is not just prefilled data: the bank is exposing a credit decision state before the full application.

**Asset status:** official screen observed and indexed on the current product page; stable direct image asset URL not recovered, so the page itself remains the source of record.

Official source:
https://www.commbank.com.au/business/loans-and-finance/betterbusiness-loan.html

---

## 4. Underwriting and data architecture

### Directly evidenced

CommBank states that for existing customers it can base conditional approval on information **already held by the bank**.

This is the key H1/H4 evidence.

Broader business-credit inputs can include:
- bank relationship;
- transaction/account behavior;
- financial statements;
- security/collateral;
- business/personal information.

### Automation signal

CBA management says:
- small-business loans auto-approved via **BizExpress doubled over the prior two years**;
- annual loan-maintenance effort fell by **85%**;
- time to credit decision improved by about **two days** versus the prior year.

These are Business Banking operational metrics, not all specifically BetterBusiness Loan.

---

## 5. Business scale and economics

CBA Business Banking — 1H26:
- business lending: **A$168bn**;
- business transaction accounts: **1.4m**;
- net interest income: **A$4.387bn**;
- other operating income: **A$539m**;
- total operating income: **A$4.926bn**;
- operating expenses: **A$1.584bn**;
- operating performance: **A$3.342bn**;
- impairment expense: **A$91m**;
- cash NPAT: **A$2.272bn**.

Management also described roughly **6 bps** of business loan losses in the half.

### Funding context

Group deposit funding ratio at Dec-2025 was about **79%** and customer deposits were about **A$956bn**.

These are group funding metrics; they establish the structural funding environment but not the marginal funding cost of BetterBusiness Loan.

---

## 6. Risk

### Positive evidence
- low reported business-loan loss rate in the period;
- impairment expense down materially YoY;
- large diversified business loan portfolio;
- deep transaction-account penetration.

### What remains unknown
- small-business unsecured NPL/DPD specifically;
- instant-decision vs manually approved loss rate;
- approval rate;
- new-to-bank vs existing-customer losses;
- vintage performance by BizExpress/BetterBusiness Loan.

This missing comparison is exactly what would be needed to prove that better UX preserves risk quality.

---

## 7. Distinctive capabilities

1. **Conditional approval using existing bank information**
2. **Instant decision/funding for eligible existing customers**
3. **90% loan-to-transaction-account linkage**
4. **Scaled digital auto-approval via BizExpress**
5. **Large relationship-bank fallback for more complex cases**
6. **Deposit-funded incumbent economics**

---

## 8. Hypothesis tests

### H1 — Existing-customer advantage: very strongly supported
The existing-vs-new customer journey difference is explicit on the same product.

### H4 — UX comes from data substitution: strongly supported
The bank reduces visible customer data collection because it already knows the customer.

### H2 — Speed is segmentation: supported
Instant approval is an eligibility-limited lane, not the universal process.

### H3 — Funding advantage: structurally plausible
CBA is heavily deposit-funded, but product-level funding spread is not public.

### H5 — SME is several businesses: supported
Unsecured digital small-business credit and secured/larger specialist lending have materially different processes.

---

## 9. Strategic implication

CommBank suggests a high-value priority for incumbent banks:

> **Before building a new loan form, determine how much of the application can disappear for existing current-account customers.**

A bank with rich transaction data should treat “existing SME customer” as a different origination product, not merely the same application with prefilled fields.

---

## 10. Transferability prerequisites

- SME current-account scale;
- transaction history;
- internal consent/data governance;
- integrated risk engine;
- digital offer management;
- instant/near-instant fulfillment;
- human specialist channel for non-standard cases.

**Transferability: High for transaction banks.**

---

## 11. Counter-evidence / watch-outs

- Best journey depends on existing relationship.
- Public small-business auto-approval metrics do not disclose selection criteria.
- No public proof yet that auto-approved cohorts have equal/better risk-adjusted economics.
- Larger/secured cases remain operationally different.

---

## 12. Evidence gaps

1. BetterBusiness Loan approval rate.
2. Share of applications instant-approved.
3. Median decision and funding time.
4. Small-business unsecured default/NPL.
5. Existing-vs-new customer loss comparison.
6. Product yield/funding cost.
7. Product-level RAROC.
8. Full first-party screenflow assets.

---

## 13. Sources

Primary:
- https://www.commbank.com.au/business/loans-and-finance/betterbusiness-loan.html
- https://www.commbank.com.au/business/loans-and-finance/compare-business-loans.html
- https://www.commbank.com.au/business/rates-fees.html
- Commonwealth Bank of Australia 1H26 Profit Announcement / Business Banking presentation
- Commonwealth Bank of Australia 1H26 results transcript / investor materials
