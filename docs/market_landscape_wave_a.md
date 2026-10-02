# Wave 2 — Market Landscape: Wave A First Extraction

Version date: 2026-10-02.

## Status

Wave 2 data collection has started.

Machine-readable data:
`data/market_landscape.csv`

The first extraction intentionally stores only datapoints that can be mapped cleanly to the canonical Metric Dictionary. Missing cells are not filled with proxies yet.

## First observations

### United States

The strongest first-pass evidence is demand/funnel rather than a single clean national SME loan-stock series.

In the 2025 Small Business Credit Survey:
- 60% of small employer firms applied for financing in the prior 12 months;
- 38% applied specifically for a loan, line of credit or merchant cash advance;
- among financing applicants, 42% received the full amount sought and 36% received some/most.

These figures use the Fed SBCS population of firms with fewer than 500 employees and come from a convenience sample. They therefore remain a separate evidence lane from regulatory balance-sheet data.

## United Kingdom

British Business Bank reports **£68bn gross SME bank lending in 2025**, up **9%** year on year.

Bank of England reports the effective interest rate on new SME lending at **6.61% in July 2026**.

Important:
- gross SME bank lending is a flow;
- it is not total SME external finance;
- the BoE effective new-lending rate is not APR.

## Brazil

BCB SGS series 27701 reports **R$1,337,102 million** of outstanding credit to micro, small and medium companies in August 2026.

That is approximately **6.65%** above August 2025 on the same series.

Important:
BCB's credit-reporting `MPMe` classification includes a medium-company category much broader than Brazil's legal/tax ME/EPP framework, so the value is not directly comparable to an EU SME stock without rebucketing.

## Germany

The most comparable latest SME-specific signal in the first pass is access rather than stock.

KfW-ifo reports that in Q2 2026 **four out of ten SMEs with an interest in borrowing** experienced difficulty obtaining credit.

Separately, KfW estimates that new lending by German banks to enterprises and self-employed persons grew only **1.4% YoY in Q4 2025**. This second figure is broader than SMEs and is stored with that borrower population explicitly.

## India

RBI reports scheduled-commercial-bank MSME credit of:
- **₹31.3 lakh crore at March 2025**, up **14.8% YoY**;
- **₹36.79 lakh crore at 31 December 2025** in later RBI communication.

These two points straddle the MSME definition change effective **1 April 2025**. They are therefore deliberately tagged with different borrower-definition IDs. We should not present the increase from ₹31.3 to ₹36.79 lakh crore as organic market growth.

---

# Why this first extraction is long-form

A single wide country table is visually convenient but analytically dangerous at this stage.

The long-form dataset preserves:
- metric ID;
- source-native borrower definition;
- product scope;
- period;
- denominator;
- evidence type;
- confidence;
- source URL;
- caveats.

After we have enough aligned metrics, a wide presentation table can be generated from this evidence layer.

---

# Next extraction targets

## United States
- regulated-bank small business loan stock / small-loan proxies;
- pricing;
- bank-side standards;
- credit quality proxies.

## United Kingdom
- outstanding SME bank stock;
- approval/application survey metrics;
- arrears/default where comparable.

## Brazil
- new credit concessions;
- 90+ DPD series;
- borrower counts;
- interest rates by company size.

## Germany
- loan stock/rates from Bundesbank/ECB;
- SAFE application outcomes;
- KfW financing volumes where definition can be retained.

## India
- latest micro/small/medium stock split under new classification;
- NBFC contribution;
- rates/credit-quality evidence;
- borrower-account counts.

---

# Quality flag

This is **first-pass extraction**, not the finished cross-country comparison.

A country-level metric becomes presentation-ready only when its source definition and denominator are aligned enough to survive the comparability checks in `docs/metric_dictionary.md`.
