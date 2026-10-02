# Deep-Dive Shortlist — 18 Lenders

Version date: 2026-10-02.

## Purpose

Select a compact set of lenders that maximizes **mechanism coverage**, not brand recognition.

The shortlist is locked provisionally after building a 43-player universe across 8 markets.

Selection dimensions:
- operating-model segment;
- country/infrastructure diversity;
- incumbent vs specialist vs fintech vs embedded;
- availability of risk/economics evidence;
- ability to reconstruct customer journey with real screens;
- value for testing project hypotheses.

Machine-readable source:
`data/player_universe.csv`

---

# Shortlist

| Country | Player | Archetype | Primary segments | Why selected | Main hypotheses | Screen potential |
|---|---|---|---|---|---|---|
| US | American Express Business Line of Credit | Bank / digital line | S1/S2 | Linked-bank + existing Amex relationship data, explicit digital line mechanics | H1, H4 | High |
| US | Square Loans | Acquiring / embedded | S7 | Proprietary merchant acquiring data + sales-linked repayment | H1, H6 | High |
| UK | Funding Circle | Digital SME specialist | S2 | Scaled pure SME digital lender with strong public disclosure | H2, H3, H4 | High |
| UK | Allica Bank | SME specialist bank | S4/S5 | Digital intake + human underwriter/RM model for larger SME tickets | H2, H5 | High |
| UK | Bibby Financial Services | Invoice/factoring specialist | S6 | Receivables/debtor risk instead of ordinary borrower-only risk | H5 | Medium |
| Brazil | Nubank / Nu Empresas | Digital bank | S1/S2 | Existing-account digital-bank model and pre-approved credit | H1, H4, H6 | High |
| Brazil | Stone | Acquiring / embedded | S1/S3/S7 | Acquiring data, in-app offers, sales-linked repayment, guarantee products | H1, H4, H6 | High |
| Brazil | Itaú Empresas | Universal bank | S2/S3/S5 | Incumbent benchmark + digital working capital + Pronampe/FGI | H1, H3, H5 | High |
| Germany | iwoca | Digital SME lender | S1/S2 | Explicit process breakpoint: automation/open banking at smaller tickets, more docs at larger tickets | H2, H4, H5 | High |
| Germany | Commerzbank | Universal / Mittelstand bank | S4/S5 | Relationship-banking counterpoint with digital intake and adviser-led underwriting | H2, H5 | Medium |
| India | State Bank of India | Universal bank | S1/S3/S5 | Huge MSME franchise; automated BRE + transaction-based preapproved loans + RM infrastructure | H1, H3, H5 | Medium |
| India | UGRO Capital | MSME NBFC / fintech | S2/S7 | Publicly disclosed specialist economics + proprietary sector/scoring + embedded partnerships | H3, H4 | Medium |
| Netherlands | Rabobank | Universal/cooperative bank | S2/S4/S5 | Explicit replacement of annual accounts with 13 months transaction data up to defined ticket/term | H1, H4, H5 | High |
| Netherlands | Floryn | Digital SME lender | S2 | Six months bank/PSD2 data can replace annual accounts up to €250k | H2, H4 | High |
| Australia | CommBank | Universal bank | S1/S2/S5 | Existing-customer information used for conditional approval and instant-decision pathways | H1, H4 | High |
| Australia | Judo Bank | SME specialist relationship bank | S4/S5 | Pure SME bank with strong public economics and deliberately human/judgement-led model | H3, H5 | Low |
| Mexico | Konfío | Fintech SME lender | S2 | SAT/CIEC/invoice data + proprietary scoring; strong data-substitution case | H2, H4 | High |
| Mexico | Mercado Pago / Mercado Crédito | Marketplace/acquiring lender | S1/S7 | Proprietary seller/payment history, pre-approved app offer, immediate funding and automated repayment | H1, H6 | High |

---

# Coverage by operating-model segment

## S1 — Transaction-visible micro / very small liquidity
Covered by:
- American Express
- Nubank
- Stone
- SBI
- CommBank
- Mercado Pago

## S2 — Digital unsecured small business
Covered by:
- American Express
- Funding Circle
- Nubank
- iwoca
- UGRO
- Rabobank
- Floryn
- Konfío

## S3 — Guarantee-backed lending
Covered by:
- Itaú
- Stone
- SBI

This segment will also use market/program evidence outside individual company teardowns.

## S4 — Capex / equipment / asset-backed
Covered by:
- Allica
- Rabobank
- Judo

## S5 — Medium / upper-SME relationship lending
Covered by:
- Allica
- Itaú
- Commerzbank
- SBI
- Rabobank
- Judo

## S6 — Receivables / trade / supply-chain finance
Covered by:
- Bibby Financial Services

Additional product evidence may be taken from NAB/HSBC/Lloyds without full deep dive.

## S7 — Embedded / acquiring / marketplace merchant credit
Covered by:
- Square
- Stone
- UGRO / partner ecosystems
- Mercado Pago

---

# Coverage by hypothesis

## H1 — Existing-customer advantage
Primary cases:
- American Express
- Square
- Nubank
- Stone
- Itaú
- SBI
- Rabobank
- CommBank
- Mercado Pago

Counterexamples / new-to-lender cases:
- Funding Circle
- iwoca
- Floryn
- Konfío

## H2 — Speed is segmentation, not magic
Primary cases:
- iwoca
- Allica
- Commerzbank
- Rabobank
- Floryn
- Funding Circle

We will explicitly locate process breakpoints:
- ticket;
- data requirements;
- security;
- manual review;
- approval authority.

## H3 — Funding advantage remains important
Primary comparison:
- deposit-funded banks: Itaú, SBI, Rabobank, CommBank, Judo;
- nonbank/specialist funding: Funding Circle, UGRO, iwoca, Floryn;
- platform/partner structures: Square, Mercado Pago.

## H4 — Best UX comes from data substitution
Primary cases:
- American Express — linked bank data;
- Stone — acquiring/transaction data;
- iwoca — Open Banking;
- SBI — bureau/GST/ITR/banking;
- Rabobank — transaction data replacing annual accounts;
- Floryn — PSD2/bank data;
- CommBank — existing-bank information;
- Konfío — fiscal/invoice data;
- Mercado Pago — marketplace/payment history.

## H5 — SME is several businesses
Best contrasts:
- Nubank / Square / Mercado Pago vs Judo / Allica / Commerzbank;
- iwoca small-ticket path vs higher-ticket document path;
- Rabobank digital transaction-data route vs larger adviser route;
- SBI automated BRE vs relationship-management infrastructure.

## H6 — Repeat lending can be structurally better
Primary cases:
- Square
- Nubank
- Stone
- American Express
- Mercado Pago

Look for:
- larger repeat limits;
- faster repeat flow;
- lower document burden;
- observed risk/economics where disclosed.

---

# Coverage by evidence type

## Strong public economics/risk disclosure
High-priority:
- Funding Circle
- Itaú
- SBI
- UGRO
- Rabobank
- CommBank
- Judo

Useful company/group disclosure:
- Nubank
- Stone
- American Express
- Commerzbank

## Strong customer-journey / screen potential
High:
- American Express
- Square
- Funding Circle
- Allica
- Nubank
- Stone
- Itaú
- iwoca
- Rabobank
- Floryn
- CommBank
- Konfío
- Mercado Pago

Medium:
- Bibby
- Commerzbank
- SBI
- UGRO

Low:
- Judo

The visual atlas should therefore not be expected to have equal screen depth for every company. Judo is included mainly for economics/relationship model, not UI richness.

---

# Why some strong candidates are not in the first 18

## Fundbox
Excellent automation/embedded-capital case, but overlaps heavily with other digital US cases. Keep as alternate.

## PayPal Working Capital
Very strong S7 case, but Square + Stone + Mercado Pago already provide cross-country payment-data comparison. Keep as alternate.

## NatWest
Strong incumbent digital journey, but UK already has Funding Circle + Allica + Bibby. Use as benchmark evidence if needed.

## New10 / ABN AMRO
Very strong bank-owned fintech case. Keep as first alternate if the Dutch pair needs a pure digital bank-owned comparator.

## NAB
Excellent accounting-data integration and invoice-finance evidence. Use as product-pattern evidence; upgrade to deep dive if CommBank/Judo leaves a gap.

## Banorte
Strong Mexico incumbent with transaction/tax/document breakpoints. First incumbent alternate if we need Mexico bank-vs-fintech comparison in full depth.

## Lendingkart
Highly screenable Indian digital NBFC journey; alternate if UGRO's customer-facing evidence proves insufficient.

---

# Deep-dive execution order

Do not research all 18 shallowly at once.

## Batch 1 — Mechanism exemplars
1. Nubank
2. Stone
3. iwoca
4. Rabobank
5. CommBank
6. Mercado Pago

Purpose:
- validate screen-capture methodology;
- validate H1/H4;
- identify real process breakpoints.

## Batch 2 — Economics/risk exemplars
7. Funding Circle
8. Itaú
9. SBI
10. UGRO
11. Judo
12. American Express

Purpose:
- connect product/risk/funding to profitability;
- calibrate what public disclosures support.

## Batch 3 — Relationship and specialist products
13. Allica
14. Commerzbank
15. Floryn
16. Konfío
17. Square
18. Bibby Financial Services

Purpose:
- complete relationship, embedded and receivables patterns.

Order may change if screen/source access is weak, but substitutions must preserve operating-model coverage.

---

# Exit criteria for shortlist

The shortlist is ready when:
- 12–18 players are selected;
- every core operating-model segment is represented;
- each player has a documented research purpose;
- cross-country diversity is preserved;
- enough players have strong economics/risk evidence;
- enough players have high screen/journey evidence.

**Status: met with 18 players.**
