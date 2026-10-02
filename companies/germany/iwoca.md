# Company / Lender Teardown — iwoca Germany

**Status:** Batch 1 first-pass teardown  
**Research date:** 2026-10-02  
**Geography:** Germany  
**Primary segments:** S1/S2 — transaction-visible micro / digital unsecured small business  
**Primary scenario:** new-to-lender small business seeking unsecured working-capital credit

> Quality standard: `docs/consulting_quality_standard.md`

---

## Executive synthesis — answer first

**iwoca's strongest lesson is that “fast SME lending” is not one underwriting model: the process is deliberately segmented by ticket size and data burden.** At the low end, bank-transaction data can substitute for traditional financial documents; above the disclosed threshold, iwoca adds BWA/SuSa and more financial evidence. The customer journey remains digital, but the underwriting stack becomes progressively richer as exposure rises.

### Quantified proof points

- Product range: **€1,000–€500,000**.
- Published eligibility: trading for at least **2 months** and annual revenue above **€22,000**.
- **€1k–€50k:** last 90 days of business-account transactions can be provided via Open Banking or statements.
- **€50,001–€500k:** transaction data plus historical/current BWA and SuSa are required.
- Some smaller applications can be decided immediately; broader public SLA is **within 24–48 hours / up to 48 hours**.
- iwoca group reported **£366m revenue**, **£85.1m profit** and **£1.5bn of SME funding in 2025** across the UK and Germany.

### Mechanism

Low ticket
→ bank-transaction visibility
→ limited document burden
→ automated/rapid decisioning.

Higher ticket
→ more financial evidence
→ greater underwriting depth
→ still-digital journey, but more manual/analytical work.

### Strategic implication

The transferable design principle is not “make every SME loan instant.” It is to create **explicit credit-process breakpoints**: use machine-readable cash-flow data for lower-risk/lower-ticket cases, then add richer financial analysis when expected loss and exposure justify the incremental underwriting cost.

### Transferability

**Highly transferable with prerequisites.**

Required:
- Open Banking / transaction-data access;
- rules/models that can use cash-flow behavior;
- ticket-based credit authority;
- digital document ingestion;
- clear escalation path for larger exposure.

### Counter-evidence / limitation

iwoca's strong public economics are **group-level UK + Germany**, not German product-level economics. Public Germany-specific vintage loss, default, NPL and unit economics are not disclosed, so we can observe the operating model more confidently than its local risk-adjusted return.

---

## 0. Scope and comparability

This teardown distinguishes:
1. iwoca Germany product/journey evidence;
2. group-level iwoca financial evidence covering the UK and Germany;
3. inferred mechanisms.

Do not attribute group revenue/profit directly to the German portfolio.

---

## 1. Position and business model

iwoca is a specialist non-bank SME lender focused on fast working-capital and flexible business credit.

Its model differs from a relationship bank in three ways:
- acquisition/application is primarily digital;
- underwriting starts from operational cash-flow evidence rather than requiring a full relationship-manager package;
- the product can be repeatedly redrawn/top-upped after repayment performance is observed.

Public Germany materials state that iwoca is not a bank and that financing is provided through its financing structure.

---

## 2. Product portfolio

### Business loan / flexible credit

| Attribute | Public evidence |
|---|---|
| Amount | €1,000–€500,000 |
| Term | 1 day to 5 years |
| Pricing | roughly 1%–2.99% per month, risk-dependent |
| Fees | no hidden fees; interest calculated on outstanding principal |
| Eligibility | Germany-based; ≥2 months trading; >€22k annual revenue |
| Security | public pages position the product as flexible SME finance; guarantee/security details can vary by case |
| Early repayment | possible; interest only accrues while balance remains outstanding |
| Repeat/top-up | available subject to performance/eligibility |

Primary sources:
- https://www.iwoca.de/kredit-fuer-unternehmen
- https://www.iwoca.de/finanzierung

### Important product caveat

“Fast” does not mean a single uniform document set.

#### €1k–€50k
- business-account transactions for the last 90 days;
- Open Banking or PDF statements.

#### €50,001–€500k
- transaction data;
- BWA + SuSa for the prior two fiscal years;
- current BWA/SuSa, generally no more than four months old.

This is one of the clearest public process breakpoints in the project.

---

## 3. Underwriting / decision architecture

### Publicly evidenced inputs

- business-account transactions;
- Open Banking;
- SCHUFA / Creditreform;
- current business performance;
- BWA/SuSa for larger tickets;
- company/personal applicant information.

### Decision architecture

**Lower ticket:** high automation potential.  
**Larger ticket:** richer financial-data package and greater underwriting intensity.

Public product materials say some requests can be decided immediately; broader SLA is normally within 24–48 hours / up to 48 hours.

### What is not public

- scorecard variables/weights;
- approval cutoff;
- manual-review rate;
- approval rate;
- Germany-specific PD/LGD;
- automated-vs-manual loss outcomes.

---

## 4. Customer journey

### Scenario

German small business, new to iwoca, seeking a €30k working-capital facility.

| Stage | Customer-visible action | Evidence | Implication |
|---|---|---|---|
| Discovery | Select business finance / amount | Official page | Simple entry |
| Application | Enter company and personal information | Official step screen | Fully digital intake |
| Data | Connect business account or upload statements | Official product/step evidence | Transaction data substitutes for many documents |
| Credit check | iwoca evaluates business data + bureau | Official FAQ/product | Backstage underwriting |
| Decision | Immediate in some cases; otherwise up to 24–48h | Official SLA | Speed is segment-dependent |
| Offer | Review amount/price/term | Official product | Personalized terms |
| Contract | Digital acceptance | Official journey | No branch required |
| Funding | Public SLA within 24–48h after process/approval | Official page | Digital fulfillment |
| Servicing | Repay, see availability, potentially top up | Official support/product | Repeat relationship can reduce friction |

### Larger-ticket scenario

For >€50k, the visible journey adds financial-document requirements. Therefore the “same” digital product contains materially different underwriting journeys by exposure.

---

## 5. Visual customer journey

iwoca exposes official step images on its Germany product page.

### Screen 1 — Application / company information

![iwoca Step 1 — application](https://cdn.prod.website-files.com/62e9302315b6e0c45f706ad7/6787ebf92a960a796f7bbce9_Step%201-min.png)

**What it proves:** digital application is structured as a lightweight first step rather than a full financial-file submission.

### Screen 2 — Data / underwriting input

![iwoca Step 2 — data](https://cdn.prod.website-files.com/62e9302315b6e0c45f706ad7/6787ebf9869c1caafa0a6bb7_Step%202-min.png)

**What it proves:** customer journey explicitly moves from application into data/document sharing.

### Screen 3 — Offer / completion

![iwoca Step 3 — decision / offer](https://cdn.prod.website-files.com/62e9302315b6e0c45f706ad7/6787ebf9f16c37fd417e3cc6_Step%203-min.png)

**What it proves:** iwoca publicly presents the journey as a short digital sequence.

### Screen gaps

- exact Open Banking consent screen: **screen evidence missing**
- BWA/SuSa upload screen: **screen evidence missing**
- detailed pricing/contract screen: **screen evidence missing**
- funding confirmation: **screen evidence missing**
- servicing/top-up dashboard: **screen evidence missing**

---

## 6. Risk and portfolio quality

Germany-specific public portfolio-risk disclosure is limited.

### Observable
- bureau data are used;
- transaction/cash-flow data are used;
- financial evidence increases with ticket;
- repeat/top-up eligibility is re-evaluated over time.

### Missing
- DPD/NPL;
- charge-off rate;
- cost of risk;
- vintage curves;
- approval rate;
- repeat-vs-first-loan performance.

**Risk confidence: Medium on architecture; Low on portfolio outcomes.**

---

## 7. Lending economics

### Group-level 2025 evidence — UK + Germany

iwoca reported:
- revenue: **£366m**, +56%;
- SME funding: **£1.5bn** in 2025 vs £952m in 2024;
- roughly **100k SME loans** funded in 2025;
- profit: **£85.1m**;
- cumulative lending above **£6bn** since 2012.

Source:
https://www.iwoca.co.uk/news/revenue-increases-by-over-50-as-iwoca-launches-new-products-to-solve-more-sme-problems

### What this establishes

The model has reached meaningful scale and positive reported profitability at group level.

### What it does not establish

We still cannot calculate Germany-specific:
- yield;
- funding cost;
- cost of risk;
- contribution margin;
- RAROC.

---

## 8. Distinctive capabilities

1. **Explicit ticket-based data requirements**
2. **Open Banking as a low-ticket document substitute**
3. **Digital onboarding for both new and repeat borrowers**
4. **Repeat/top-up capability**
5. **Non-bank specialist operating model**
6. **Profitable group-scale evidence**

---

## 9. Hypothesis tests

### H2 — Speed is segmentation, not magic: strongly supported
The clearest evidence is the €50k document breakpoint.

### H4 — UX comes from data substitution: strongly supported
Transaction feeds replace more traditional documentation at lower tickets.

### H5 — SME is several businesses: supported
The underwriting package changes materially as exposure grows even within one lender.

### H3 — Funding advantage remains important: unresolved
iwoca is profitable at group level, but public data are insufficient to compare its risk-adjusted spread with deposit-funded banks.

---

## 10. Strategic implication

For a bank designing SME lending, the strongest lesson is:

> **Do not choose between “fully automated” and “manual SME underwriting.” Build a ladder.**

Example architecture:
- low-ticket + strong transaction data → automated;
- medium ticket → automated + exceptions;
- higher ticket / weaker data → financial-document and analyst layer.

That can preserve UX where automation is economically justified without forcing high-exposure credit into an unsuitable low-information process.

---

## 11. Transferability prerequisites

- consented transaction-data access;
- robust bureau;
- digital KYC/KYB;
- risk policy by ticket;
- document ingestion for escalated cases;
- ability to price risk;
- repeat-loan monitoring.

**Transferability: High with infrastructure prerequisites.**

---

## 12. Evidence gaps

1. Germany loan book / originations.
2. Germany approval rate.
3. Germany cost of risk and charge-offs.
4. Automated-decision share by ticket.
5. Median ticket and term.
6. Repeat-loan share.
7. Actual observed time-to-cash distribution.
8. Funding structure by market.

---

## 13. Sources

Primary:
- https://www.iwoca.de/kredit-fuer-unternehmen
- https://www.iwoca.de/finanzierung
- https://www.iwoca.de/schnellkredit
- https://support.iwoca.de/
- https://www.iwoca.co.uk/news/revenue-increases-by-over-50-as-iwoca-launches-new-products-to-solve-more-sme-problems
