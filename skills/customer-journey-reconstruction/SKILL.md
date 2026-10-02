---
name: customer-journey-reconstruction
description: Reconstruct the real SME borrowing journey from observable product flows, help/legal content, screenshots, reviews and borrower evidence without inventing hidden steps or emotions.
---

# SME Lending Customer Journey Reconstruction

## Objective

Reconstruct what a borrower actually experiences from need recognition through repayment and repeat borrowing.

This is an evidence synthesis task, not a hypothetical service-design exercise.

A journey is not considered fully evidenced by text alone when customer-visible screens can reasonably be obtained. **Screenshots, screen sequences and screenflows are first-class evidence.**

## Step 1 — Define actor and scenario

Specify:
- borrower segment;
- company size / age;
- existing vs new customer;
- loan purpose;
- target amount;
- product;
- geography;
- channel;
- single vs multiple directors/owners where relevant.

A generic “SME customer” journey is too broad.

## Step 2 — Evidence sources

Priority:
1. direct walkthrough / screenshots / video;
2. official application pages;
3. official help/FAQ/terms;
4. public demos / app store materials;
5. reviews, forums, borrower reports;
6. inferred steps only when unavoidable.

For every journey step label evidence as:
- Observed;
- Officially documented;
- Reported by users;
- Inferred;
- Unknown.

For customer-visible steps also capture, where possible:
- screenshot or screen sequence;
- screen source;
- capture/publication date;
- screen evidence type: observed / official / reported;
- scenario to which the screen applies;
- annotation: what exactly the screen proves;
- `screen evidence missing` when no visual evidence is available.

Do not treat a decorative marketing image as evidence of an application step unless it clearly represents the relevant product flow.

## Step 3 — Standard lending stages

Adapt as needed:

1. Need / discovery
2. Product exploration
3. Eligibility / pre-check
4. Authentication / onboarding
5. Business and owner information
6. Data connections / document collection
7. Credit assessment
8. Additional-information loop
9. Decision
10. Offer / amount / term / pricing
11. Contract / guarantee / e-sign
12. Disbursement
13. First repayment setup
14. Ongoing servicing
15. Limit increase / top-up / repeat borrowing
16. Early payoff / refinance
17. Missed payment / collections / hardship, where visible

## Step 4 — Capture each step

For every stage capture:
- user goal;
- entry point / screen / channel;
- screenshot / screen sequence if available;
- visual-evidence status: available / missing;
- user action;
- information requested;
- documents requested;
- external data connection;
- permissions/consents;
- waiting time;
- stated SLA;
- actual timing evidence if available;
- decision/result;
- next action;
- support path;
- pain point;
- source.

Do not invent “emotions”. Add emotion only when directly supported by research evidence; otherwise omit or mark unknown.

## Step 5 — Build the visual screenflow

For the main customer-visible path, assemble screens in chronological order.

Target coverage, where available:
1. discovery / landing;
2. eligibility / pre-check;
3. application start;
4. business and owner data;
5. data connections;
6. document upload;
7. review/status;
8. additional-information request;
9. decision;
10. offer / pricing / terms;
11. guarantee / collateral disclosure;
12. signing;
13. disbursement confirmation;
14. servicing dashboard;
15. repayment / payoff;
16. renewal / top-up / limit increase.

Annotate each screen with:
- journey stage;
- user action;
- key fields / disclosures;
- friction or automation observed;
- evidence source/date.

The screenflow is an evidence artifact, not decoration.

## Step 6 — Quantify friction where possible

Useful metrics:
- number of screens/steps;
- number of required fields;
- number of documents;
- number of redirects;
- number of data connections;
- manual handoffs;
- additional-info loops;
- time to decision;
- time to cash;
- drop-off point;
- error/retry loops;
- support contacts.

A shorter form is not necessarily a faster journey if underwriting shifts friction later.

## Step 7 — Distinguish hidden and visible process

Maintain two lanes:

**Customer-visible**
what the borrower sees and does.

**Backstage / inferred**
KYB/KYC, bureau pulls, scoring, analyst review, committee, fraud checks, collateral checks, etc.

Never state backstage steps as fact unless evidenced.

## Step 8 — Moments of truth

Look for evidence around:
- knowing whether one is eligible;
- pricing transparency;
- document burden;
- uncertainty during review;
- request for additional information;
- amount lower than requested;
- guarantee/collateral surprise;
- signing;
- speed of disbursement;
- first repayment;
- self-service after disbursement;
- repeat borrowing.

## Step 9 — Compare journeys

Normalize scenarios before comparing lenders:
- same borrower type;
- same target amount;
- same new/existing-customer status;
- similar product and security.

Otherwise explicitly explain differences.

## Output

1. Persona/scenario.
2. Journey timeline.
3. Evidence table by step.
4. **Visual screenflow / screenshot sequence** for customer-visible stages where evidence is available.
5. Annotated screenshots explaining what each screen proves.
6. Explicit `screen evidence missing` markers for uncovered key stages.
7. Customer-visible flow.
8. Backstage evidence/inferences.
9. Friction metrics.
10. Moments of truth.
11. Unknowns.
12. Improvement hypotheses clearly separated from observed facts.

## Hard rules

- Customer screens are first-class evidence, not optional decoration.
- Do not claim a customer-visible flow is fully reconstructed when key screens are missing; mark the gap.
- Never invent or recreate a bank screen and present it as observed evidence.
- A marketing mockup must be labeled as such and not silently treated as a live flow.
- Journey maps may contain Unknown.
- Do not fill gaps for aesthetics.
- Advertised SLA ≠ observed SLA.
- Review anecdotes ≠ prevalence.
- Do not infer decline reasons unless disclosed.
