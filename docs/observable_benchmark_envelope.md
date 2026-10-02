# Observable Benchmark Envelope — SME Lending

**Version:** 2026-10-02  
**Purpose:** summarize the **observed public performance envelope** across researched SME credit factories.

> This is **not a target-setting document**.
>
> The figures below show what is publicly observable in comparable journey stages. They should be used as an ambition reference, not copied as universal KPIs.

---

# Executive answer

The public benchmark does not support one “best SLA.”

Observed speed depends on the credit factory:

- **existing-customer / embedded pre-approved:** seconds to minutes;
- **new-to-bank digital cash-flow:** minutes to ~48 hours;
- **relationship SME:** digital intake can be minutes, but final decision remains case-specific;
- **receivables:** initial facility can be complex, while subsequent invoice-to-cash can be within ~24 hours;
- **guarantee-backed:** digital journey can be fast, but program eligibility adds an external dependency.

The correct benchmark is therefore:

> **same credit factory × same journey stage × same customer perimeter**

---

# 1. Existing-customer / pre-approved lane

## Observed examples

### CommBank
- application: up to ~10 minutes;
- decision: instant if eligible;
- funds: within minutes.

### Amex BLOC
- repeat draw: reusable line, no fresh full application;
- funds to eligible Amex Business Checking: typically within seconds;
- external ACH: 1–3 business days.

### Nubank
- capital de giro surfaced after recurring eligibility;
- funds credited immediately after approval in the published flow.

### Mercado Pago
- pre-approved offer;
- amount/term selection;
- funds immediately to Mercado Pago balance after acceptance.

## Benchmark envelope

### Discovery / eligibility
**Already known / proactive offer**

### Customer data burden
**Low**

### Decision
**Instant to minutes** in the strongest bounded lanes.

### Funding
**Seconds to minutes** when the lender controls the destination account/wallet.

### Main differentiator
Not form speed — **pre-underwriting depth**.

---

# 2. New-to-bank digital cash-flow lane

## Observed examples

### Funding Circle
- eligibility: ~30 seconds;
- application: ~7 minutes;
- decision: as little as 5 minutes;
- funding: typically within 48 hours.

### Floryn
- application: ~2 minutes;
- account-manager contact: within ~2 hours;
- decision/facility: within ~24 hours;
- subsequent drawdown can be same day.

### iwoca
- some rapid/near-immediate decisions;
- general current public decision/funding framing: within ~24–48 hours depending case/data.

### Konfío
- rapid preapproval / personalized-offer flow;
- funding typically 24–72 hours depending validation.

## Benchmark envelope

### Application
**~2–10 minutes** for the visible digital intake.

### Data
Open Banking / bank statements / tax / accounting connection.

### Decision
**Minutes to ~24–48 hours** depending:
- ticket;
- data;
- exceptions;
- documentation.

### Funding
**Same day to ~48 hours** for strong digital cases.

### Main differentiator
**How often the case remains inside the machine-readable-data lane.**

---

# 3. Relationship / medium-SME lane

## Observed examples

### Commerzbank
- initial request: ~2 minutes;
- adviser: within 48 hours;
- up to €100k can be decided in adviser conversation.

### Allica
- digital decision-in-principle;
- full package;
- explicit underwriter review;
- case-specific final turnaround.

### Judo
- relationship-led;
- direct banker / credit executive;
- case-specific decision and settlement.

## Benchmark envelope

### Digital intake
Can still be **minutes**.

### Final decision
Not meaningfully benchmarkable as “instant” across complex cases.

### Relevant speed metrics
- time to complete credit file;
- time from complete file to decision;
- number of handoffs;
- number of clarification loops;
- time to conditions / legal completion.

### Main differentiator
**Organizational latency and decision authority**, not STP rate.

---

# 4. Embedded merchant lane

## Observed examples

### Square
- daily merchant eligibility review;
- application/final review generally 1–2 business days;
- funds instantly to Square Checking or 1–3 days externally.

### Stone
- proactive offer;
- in-app tracking;
- published flow indicates up to 4 business days to funding in the shown process.

### Mercado Pago
- pre-approved offer;
- immediate wallet funding after acceptance.

## Benchmark envelope

### Offer creation
**Continuous / proactive**

### Customer effort
Very low relative to open-market credit.

### Decision/funding
Can range from **immediate** to **1–4 business days** depending final review and transfer rails.

### Main differentiator
**How much of merchant risk is already observable before the loan event.**

---

# 5. Guarantee-backed lane

## Observed examples

### Itaú
- revenue authorization / program eligibility;
- simulation and contracting in app;
- digital token acceptance.

### SBI
- digital and guarantee-backed MSME products coexist with automated data rails.

## Benchmark envelope

The journey can be digitally compact, but end-to-end SLA depends on:
- program eligibility;
- government data;
- guarantee registration;
- claim/coverage rules.

### Main differentiator
**Integration of guarantee-program steps into the bank workflow.**

---

# 6. Receivables lane

## Observed example

### Bibby
- facility setup required;
- eligible invoices can release up to ~85% of value;
- access to funds often within ~24 hours after invoice/facility conditions;
- 24/7 client portal monitoring.

## Benchmark envelope

### Initial onboarding
Potentially slower / specialist.

### Repeat funding event
Can be **same day / ~24 hours** once the facility exists.

### Main differentiator
**reusable facility + invoice ingestion**, not one-time underwriting speed.

---

# 7. Observable automation / document breakpoints

Public examples:

| Lender | Breakpoint | What changes |
|---|---:|---|
| iwoca | €50k | richer financial docs above threshold |
| Allica | £75k | 3 vs 6 months bank statements + richer accounts |
| Commerzbank | €100k | direct adviser decision authority below/at threshold |
| Floryn | €250k | annual accounts and AR/AP return above threshold |
| Rabobank | €250k / 5y | no-annual-accounts fast lane bounded here |
| SBI | product-specific, incl. ₹50 lakh Digi Sugam | larger enhancement can route to branch / richer process |

## Implication

A strong bank should expect **multiple internal breakpoints**, not one SME-wide STP threshold.

---

# 8. Customer-effort benchmark

## Best observed existing-customer pattern

Customer often supplies:
- amount;
- term;
- acceptance;
- authentication.

The bank supplies:
- identity;
- transactions;
- behavior;
- eligibility.

## Best observed new-to-bank pattern

Customer supplies:
- business identity;
- consent to data;
- exceptions/documents only if required.

The lender retrieves:
- transactions;
- tax;
- accounting;
- bureau.

## Best observed relationship pattern

Customer still supplies:
- financials;
- management information;
- context;
- collateral detail.

But the lender should minimize:
- duplicated forms;
- repeated requests;
- internal handoffs;
- opaque status.

---

# 9. How to use this benchmark

## Use it for
- ambition setting;
- identifying obvious process gaps;
- product-lane redesign;
- workshop discussion;
- current-vs-observed comparison.

## Do not use it for
- executive scorecards before definitions align;
- declaring a bank “slow” without factory/ticket context;
- setting loss-neutral automation targets without internal risk data;
- comparing funding SLAs where payment rails differ.

---

# Final benchmark principle

The right ambition is not:

> “Every SME loan should be instant.”

It is:

> **Every SME credit factory should operate close to the fastest safe envelope that its data, ticket, risk and legal structure allow.**
