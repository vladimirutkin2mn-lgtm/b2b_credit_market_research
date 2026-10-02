# Batch 3 Synthesis — Credit Operating Models Beyond “Bank vs Fintech”

**Companies:** Allica Bank, Commerzbank, Floryn, Konfío, Square Loans, Bibby Financial Services  
**Version:** 2026-10-02  
**Purpose:** complete the operating-model map across relationship lending, cash-flow fintech, tax-data underwriting, payments lending and receivables finance.

---

## Executive answer

**“Bank vs fintech” is not a useful primary segmentation for SME lending. The more predictive distinction is: what is the lender actually underwriting, what data makes that risk observable, and how is the decision operationally produced?**

Batch 3 adds five distinct mechanisms:

1. **Digital workflow around human judgment** — Allica.
2. **Fast routing to empowered decision-maker** — Commerzbank.
3. **Cash-flow underwriting from PSD2 transactions** — Floryn.
4. **Tax / e-invoice underwriting** — Konfío.
5. **Merchant transaction underwriting + asset distribution** — Square.
6. **Receivables/debtor underwriting** — Bibby.

These models may all serve an “SME,” but their economics, data, journey and risk are fundamentally different.

---

# 1. Cross-case mechanism matrix

| Player | Primary risk object | Core data | How speed is created | Human role | Funding architecture |
|---|---|---|---|---|---|
| Allica | business cash flow + assets/collateral | accounts, management accounts, bank statements, bureau | digital DIP + workflow | explicit underwriter / RM | deposits |
| Commerzbank | borrower / account liquidity | company data, financials, relationship | 2-min intake + ≤€100k in-adviser decision authority | central to decision | universal-bank funding |
| Floryn | recent business cash flow | 6m bank transactions / PSD2 | documents removed ≤€250k | account manager overlay | wholesale/private securitisation |
| Konfío | tax/invoiced business cash flow | SAT CIEC / invoices | tax-data pull + proprietary score | limited/exception | private/non-bank |
| Square | merchant sales / payment behavior | real-time acquiring | daily pre-underwriting + embedded offer | mostly exception | majority loan sale to investors |
| Bibby | receivable / debtor quality | invoice ledger, debtor behavior | facility established once, then invoices fund quickly | relationship/credit-control | receivables-backed institutional facilities |

---

# 2. Finding 1 — The risk object determines the operating model

## Borrower cash-flow risk
Examples:
- Allica business loan;
- Floryn;
- Konfío.

Primary question:
**Can this business generate enough cash to repay?**

## Merchant transaction risk
Example:
- Square.

Primary question:
**What does high-frequency sales behavior imply about near-term ability to repay?**

## Receivables / debtor risk
Example:
- Bibby.

Primary question:
**Are these invoices real, collectible and diversified, and can the debtor pool repay the advance?**

## Collateral / property risk
Example:
- Allica mortgage/asset products.

Primary question:
**What is the recovery value and debt-service coverage?**

## Relationship / judgment risk
Example:
- Commerzbank / Allica higher-ticket.

Primary question:
**Can an experienced decision-maker integrate financials, business context and structure better than a standardized model?**

### So what?

A useful SME credit taxonomy should begin with **risk object**, not marketing product name.

---

# 3. Finding 2 — There are four distinct ways to make credit “fast”

## A. Underwrite before application
Examples:
- Square;
- Batch 1: Nubank, Stone, Mercado Pago, CommBank existing customers.

Customer starts at the offer.

## B. Replace documents with machine-readable data
Examples:
- Floryn: PSD2/bank statements;
- Konfío: tax/e-invoice data.

Customer applies, but manual evidence disappears.

## C. Empower the human decision-maker
Examples:
- Commerzbank ≤€100k direct adviser decision;
- Allica explicit underwriter workflow.

The process stays human but organizational handoffs shrink.

## D. Establish a reusable facility
Example:
- Bibby invoice finance.

Initial onboarding may be non-trivial, but individual funding events become operationally fast.

### So what?

“Decision time” should be decomposed into **which speed mechanism is being used**. Two lenders can both say “24 hours” while operating completely different factories.

---

# 4. Finding 3 — Human underwriting can be a feature, not a failure

## Evidence

### Allica
Business Loan journey explicitly presents “underwriter review” as a normal product stage.

### Commerzbank
Up to €100k can be decided directly in adviser consultation.

### Judo from Batch 2
Relationship banker + credit executive is the product architecture for multi-million-dollar relationships.

### Mechanism

Higher ticket / complexity
→ more value at risk
→ customer can support higher margin / relationship value
→ human credit skill becomes economically affordable.

### So what?

Target automation should be:

**automate administrative work and standardized decisions; preserve human judgment where its expected value exceeds its cost.**

---

# 5. Finding 4 — Data substitution is country-infrastructure dependent

## Netherlands
PSD2 / bank transaction data are strong enough for Floryn to remove annual accounts below €250k.

## Mexico
Konfío can use SAT/CIEC and invoicing data as the core underwriting spine.

## US merchant ecosystem
Square uses payments data.

## Implication

There is no globally universal “best alternative-data stack.”

The right hierarchy depends on the country:

**Open Banking vs tax/e-invoice vs acquiring vs marketplace vs accounting.**

### So what?

A bank entering a new market should first map the **digital data infrastructure**, then design the underwriting journey.

---

# 6. Finding 5 — Asset/funding matching is visible even in non-banks

## Square

The majority of Square Loans are sold to third-party investors.

At Jun-2026:
- commercial HFI gross: $488.9m;
- commercial HFS: $676.8m.

This allows capital recycling.

## Floryn

2025:
- €150m NatWest private securitisation facility.

## Bibby

2026:
- €250m HSBC facility;
- >£1.1bn total funding capacity;
- back-to-back receivables financing.

### So what?

The funding model follows the asset:
- standardized merchant loan → investor sale;
- short SME credit → securitisation/warehouse;
- receivable → receivables-backed facility.

A lender should not default to “hold everything on balance sheet.”

---

# 7. Finding 6 — Square combines data moat with asset-light economics

Square is strategically notable because four loops reinforce each other:

**Payments**
→ transaction data.

**Transaction data**
→ automatic underwriting.

**Embedded offer**
→ low acquisition friction.

**Loan sale**
→ capital recycling.

**Sales-linked repayment**
→ integrated servicing.

This is a stronger structural model than simply “digital application.”

### Risk evidence

At Jun-2026, Block disclosed that commercial loans — primarily Square Loans — had immaterial delinquent/nonperforming balances in the HFI portfolio, though product/vintage comparisons and investor-owned loan performance remain incomplete.

This is positive but should not be overgeneralized.

---

# 8. Finding 7 — Receivables finance is a separate business, not a loan feature

Bibby shows why S6 deserves its own operating-model segment.

The lender must manage:
- invoice validity;
- debtor quality;
- concentration;
- disputes/dilution;
- collections;
- reconciliation;
- fraud.

The product can combine:
- funding;
- credit control;
- bad-debt protection.

### So what?

A bank considering invoice finance needs a dedicated operating stack. Adding a “finance invoice” button to a term-loan platform is insufficient.

---

# 9. Implications for the project taxonomy

The existing S1–S7 framework should now be interpreted through four additional dimensions:

## Risk object
- borrower cash flow;
- transaction stream;
- receivable/debtor;
- collateral/asset;
- guarantee.

## Data source
- relationship transactions;
- Open Banking;
- tax/e-invoice;
- acquiring;
- accounting;
- financial statements.

## Decision mechanism
- pre-approved automated;
- STP/new-to-lender automated;
- rules + analyst;
- empowered RM;
- committee.

## Funding mechanism
- deposits;
- institutional forward flow;
- securitisation/warehouse;
- receivables funding;
- own balance sheet.

This 4D view is more explanatory than lender archetype alone.

---

# 10. What Batch 3 adds to the hypothesis set

## H2 — Speed is segmentation, not magic
**Further strengthened.**
Speed can be generated by different mechanisms, each with a defined risk perimeter.

## H4 — Best UX comes from data substitution
**Strengthened but broadened.**
Data substitution is one of several mechanisms; decision-right simplification can matter equally in larger SME.

## H5 — SME is several businesses
**Very strongly confirmed as an operating-model statement.**
Receivables, merchant credit, micro cash-flow credit and relationship lending should not share one factory.

## H3 — Funding advantage
**Broadened.**
Asset-liability matching / asset distribution can substitute for deposits.

---

# 11. Boardroom takeaway

**The right question is not “bank or fintech?”**

The right questions are:

1. What risk object are we financing?
2. What data make it observable?
3. What decision mechanism is economical at this ticket?
4. What funding source best matches the asset?
5. What customer journey naturally falls out of that architecture?

The strongest SME lenders are not necessarily the most automated. They are the ones whose **data, decision rights, funding and servicing model fit the specific credit problem.**

Confidence: **High on operating-model taxonomy; Medium on comparative RAROC because public product-level capital/loss data remain uneven.**
