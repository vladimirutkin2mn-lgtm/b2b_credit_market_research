---
name: product-feature-taxonomy
description: Inventory and normalize SME lending products, commercial terms, digital capabilities and servicing features across banks and fintech lenders.
---

# SME Lending Product & Feature Taxonomy

## Objective

Create a normalized catalog that lets us compare *what the borrower actually gets* rather than only product names.

## Product families

Classify each offer into one or more:
- working-capital term loan;
- revolving line of credit;
- overdraft;
- business credit card;
- invoice finance / factoring;
- asset / equipment finance;
- commercial real-estate secured loan;
- merchant cash advance / revenue-based finance;
- trade finance;
- guarantee-backed loan;
- embedded / point-of-sale business credit.

Do not assume similarly named products have the same economics or mechanics.

## Commercial terms

Capture:
- min/max amount;
- typical amount if disclosed;
- currency;
- min/max term;
- amortizing / bullet / revolving;
- fixed / floating;
- interest rate range;
- APR/effective rate when available;
- origination fee;
- service/monthly fee;
- draw fee;
- early repayment fee;
- late/default fee;
- collateral;
- personal guarantee;
- covenant / information requirements;
- grace period;
- repayment frequency.

Always note whether a figure is “from”, “up to”, representative, personalized or guaranteed.

## Eligibility

Capture:
- entity type;
- geography;
- minimum firm age;
- turnover/revenue;
- profitability/cash-flow requirements if public;
- existing bank relationship;
- current account requirement;
- owner/guarantor requirements;
- excluded industries;
- credit history;
- collateral requirements.

## Application capabilities

Track:
- instant eligibility checker;
- pre-qualified / pre-approved offer;
- save and resume;
- mobile / web;
- digital identity;
- business registry autofill;
- open-banking connection;
- accounting connection;
- tax-data connection;
- document OCR/upload;
- bank statement upload;
- multi-owner/director handling;
- e-sign;
- digital guarantee signing;
- real-time status tracking.

## Decision and fulfillment

Track:
- advertised decision SLA;
- evidence for actual time-to-decision;
- human review;
- conditional offer;
- offer options;
- amount/term customization;
- pricing transparency;
- contract preview;
- disbursement SLA;
- destination account restrictions.

Do not treat “decision in X minutes” as “cash in X minutes”.

## Servicing

Track:
- loan dashboard;
- balance and payoff amount;
- repayment schedule;
- autopay;
- manual/extra payments;
- early payoff;
- drawdown management;
- statement/document download;
- covenant/doc refresh;
- change repayment account;
- limit increase;
- renewal;
- top-up;
- refinance;
- payment holiday / hardship;
- support / RM access;
- collections self-service.

## Integrations and data

Track:
- bank account feeds;
- accounting packages;
- e-commerce/marketplace data;
- POS/acquiring data;
- invoicing;
- payroll;
- tax;
- business registry;
- bureau;
- APIs / embedded lending.

Only mark an integration as underwriting-relevant if evidence supports that use.

## Output matrix

For every field use:
- `Yes`
- `No`
- `Partial`
- `Unknown`
- value / range
- source/date

Do not convert Unknown to No.

## Change tracking

Where useful, save:
- current value;
- prior value;
- date changed;
- source/archive evidence.

Product limits and pricing can move quickly.

## Hard rules

- Product page copy is evidence of an offered capability, not usage/adoption.
- App screenshots are evidence of UI capability, not underwriting logic.
- A feature counts only if evidence shows it exists for the relevant SME segment and geography.
