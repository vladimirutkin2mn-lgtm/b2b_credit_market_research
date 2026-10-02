# Product / Feature Comparison — Mechanism-Based

**Version:** 2026-10-02  
**Scope:** 18 deep-dive lenders

## Executive answer

A generic feature checklist is misleading in SME lending.

The valuable question is not whether a lender has a feature, but:

> **Which part of the credit economics or customer journey does the feature change?**

This matrix therefore groups features into six mechanisms:

1. **Acquisition / pre-underwriting**
2. **Data collection**
3. **Decision architecture**
4. **Offer / fulfillment**
5. **Servicing / repeat**
6. **Risk / funding structure**

---

# 1. Acquisition / pre-underwriting

## Pattern

The strongest acquisition advantage appears when credit is distributed through an existing operating relationship rather than a standalone loan funnel.

| Player | Existing relationship central? | Pre-approved / proactive offer | Main distribution advantage |
|---|---|---|---|
| Nubank | Yes | Yes | business account/app |
| Stone | Yes | Yes | acquiring + business account |
| Square | Yes | Yes | merchant payments |
| Mercado Pago | Yes | Yes | marketplace/payments |
| CommBank | Strong for best lane | Yes/conditional | business transaction account |
| Amex BLOC | Helpful / sometimes decisive | Yes for select users | Card + Blueprint + Checking |
| SBI | Yes for PABL/PAsBL | Yes | CASA/UPI/current relationship |
| Itaú | Strong for digital route | Yes on eligible products | business bank app |
| Funding Circle | No | Generally application-led | direct digital/broker |
| iwoca | No | Not core | direct digital |
| Floryn | No | Partial | direct digital |
| Konfío | No | Offer after tax-data evaluation | digital direct |
| Rabobank | No, but own-account helps | Partial | bank relationship + external data |
| Allica | No | No | broker/direct/RM |
| Commerzbank | Relationship helps | Not core | digital-to-adviser |
| Judo | No | No | banker/broker |
| Bibby | No | No | broker/relationship |
| UGRO | Partner/merchant context important | Yes in embedded channel | fintech/payment partners |

### Strategic implication

If a bank has an SME current-account franchise, its first product-design question should be:
**why is the customer entering a generic application at all?**

---

# 2. Data collection / document substitution

## Feature groups

### Transaction / Open Banking
Strongly observed:
- iwoca
- Floryn
- Rabobank
- CommBank
- Amex
- SBI
- Stone
- Nubank

### Tax / fiscal / e-invoice
Strongly observed:
- Konfío
- SBI
- Itaú
- UGRO

### Acquiring / marketplace
Strongly observed:
- Square
- Stone
- Mercado Pago
- UGRO embedded channel

### Traditional financial package remains central
- Allica
- Commerzbank
- Judo
- Bibby (plus invoice ledger)

### Receivables-specific data
- Bibby

## Strategic interpretation

Machine-readable data do not merely make the form shorter.

They can alter:
- approval policy;
- monitoring frequency;
- manual-review share;
- fraud controls;
- repeat limits.

---

# 3. Decision architecture

| Decision architecture | Exemplars | When it works |
|---|---|---|
| Continuous pre-underwriting | Nubank, Stone, Square, Mercado Pago | existing recurring data |
| Automated + exceptions | iwoca, Floryn, Funding Circle, Konfío, UGRO | standardized small-business cash flow |
| Existing-customer auto/conditional | CommBank, Amex, SBI | account/relationship history |
| Digital + explicit underwriter | Allica | established SME / larger ticket |
| Digital-to-empowered adviser | Commerzbank | relationship SME |
| Relationship-led | Judo | large complex exposure |
| Specialist receivables underwriting | Bibby | invoice/debtor risk |
| Product-dependent multi-factory | Itaú, Rabobank, SBI | universal-bank portfolio |

## Core finding

The strongest architecture is **not maximal automation**.

It is an explicit allocation of cases between:
- machine;
- exception analyst;
- empowered RM;
- specialist factory.

---

# 4. Offer / price / fulfillment

## Fastest fulfillment patterns

### Immediate / minutes after approval
- Nubank Capital de Giro
- CommBank eligible digital route
- Mercado Pago wallet/account
- Square to Square Checking
- Amex to eligible Business Checking

### Same day / ~24h
- Floryn
- some SBI digital products
- UGRO embedded finance

### 24–48h
- iwoca
- Funding Circle
- some digital/bank flows

### Case-specific
- Allica
- Commerzbank
- Judo
- Bibby initial facility

## What explains the difference

Funding speed is often driven by:
- where the account/wallet sits;
- whether legal/security documents are required;
- whether an external bank transfer is needed;
- whether the facility is already established.

Therefore **time-to-cash must not be treated as the same thing as credit decision time.**

---

# 5. Servicing / repayment / repeat

## Automatic or embedded repayment

### Sales-linked
- Stone
- Square
- some Mercado Pago products

### Account debit
- Nubank
- bank products generally
- Floryn / iwoca depending contract

### Debtor-settlement linked
- Bibby factoring

## Reusable / repeat credit

Strong patterns:
- Amex BLOC — reusable dynamic line;
- Square — re-evaluation after payoff;
- Nubank — recurring eligibility;
- SBI — top-up / repeat digital eligibility;
- Funding Circle — top-ups/multi-product;
- Mercado Pago — renewed offers;
- revolving products at Rabobank/Floryn.

## Economic implication

Repeat functionality can affect:
- acquisition cost;
- underwriting cost;
- lifetime utilization;
- cross-sell;
- data quality.

This deserves a separate customer-LTV metric rather than being treated as a servicing convenience.

---

# 6. Risk / funding structural features

## Government guarantee embedded in product

Observed:
- Itaú
- Stone
- SBI
- Funding Circle under UK GGS
- other bank products in market universe

Economic channel:
- lower uncovered expected loss;
- potentially different capital/provisions;
- different approval perimeter.

## Asset-light / distributed credit exposure

Observed:
- Funding Circle Term Loans — institutional forward flow;
- Square — majority loan sale to third-party investors.

## Securitisation / warehouse funding

Observed:
- Floryn;
- Bibby;
- Judo as part of funding/capital toolkit;
- UGRO wholesale funding stack.

## Deposit-funded

Observed:
- Itaú;
- SBI;
- Rabobank;
- CommBank;
- Judo;
- Allica;
- bank ecosystem supporting Amex/Nubank at group level.

---

# 7. Mechanism-to-feature map

| Feature / capability | Customer effect | Risk effect | Economics effect | Best evidence |
|---|---|---|---|---|
| Pre-approved offer | removes search/application stages | selection happens backstage | lower CAC / conversion friction | Nubank, Stone, Square |
| Open Banking connection | fewer uploads | current cash-flow visibility | lower underwriting OPEX | iwoca, Floryn, Rabobank |
| Tax/e-invoice pull | fewer revenue proofs | verified sales/fiscal history | faster scalable underwriting | Konfío, SBI |
| Existing-account data | less re-entry | longer behavior history | CAC + cross-sell advantage | CommBank, Nubank, Amex |
| Ticket breakpoint | simpler low-ticket path | limits model risk/exposure | optimizes human cost | iwoca, Floryn, Rabobank |
| Visible underwriter/RM | clearer complex journey | judgment/context | supports larger-ticket economics | Allica, Judo |
| Sales-linked repayment | smoother repayment | high-frequency collection visibility | lower servicing friction | Stone, Square |
| Reusable credit limit | faster repeat borrowing | continuous monitoring required | higher LTV / lower repeat CAC | Amex |
| Government guarantee | potential collateral relief | lowers uncovered loss | may improve approval/capital economics | Itaú |
| Loan sale/forward flow | no direct UX effect | transfers part of asset exposure | capital/funding efficiency | Funding Circle, Square |
| Invoice-ledger integration | faster recurring draws | debtor-level monitoring | working-capital + service economics | Bibby |

---

# 8. Product architecture by operating-model segment

## S1 — Transaction-visible micro

Essential:
- proactive eligibility;
- in-app offer;
- machine-readable transaction data;
- instant/near-instant funding;
- repeat limit.

Examples:
Nubank, SBI PABL, Amex existing-customer lane.

## S2 — Digital unsecured small business

Essential:
- digital KYB;
- Open Banking/tax/accounting data;
- explicit automation threshold;
- exceptions process;
- transparent digital offer.

Examples:
iwoca, Floryn, Konfío, Funding Circle.

## S3 — Guarantee-backed

Essential:
- program eligibility;
- automated revenue/tax validation where possible;
- lender credit decision;
- guarantee workflow;
- integrated contract.

Examples:
Itaú, Stone, SBI.

## S4/S5 — Capex / medium relationship

Essential:
- digital prep;
- document/data room;
- named RM/underwriter;
- delegated approval;
- collateral/legal workflow;
- status transparency.

Examples:
Allica, Judo, Commerzbank.

## S6 — Receivables

Essential:
- invoice ingestion;
- debtor limits;
- availability calculation;
- collections/reconciliation;
- fraud/dispute management.

Example:
Bibby.

## S7 — Embedded merchant

Essential:
- transaction history;
- proactive offer;
- minimal separate application;
- integrated funding;
- sales-linked/embedded servicing.

Examples:
Square, Stone, Mercado Pago.

---

# 9. What should NOT be used as a feature benchmark

Avoid counting:
- number of product pages;
- “AI” claims;
- generic mobile-app availability;
- number of optional channels;
- “fast decision” marketing without start/end definition;
- feature presence without adoption.

The feature is strategically relevant only if it changes:
- conversion/revenue;
- risk;
- cost;
- capital;
- customer effort.

---

# Final product conclusion

The most important “feature” in SME lending is often invisible:

> **the lender already has the data and has already made much of the decision.**

Everything customer-visible should be designed around that reality.

The target product architecture is therefore not a maximal feature set.

It is a **minimal customer-visible workflow supported by a rich backstage data/risk/funding architecture**.
