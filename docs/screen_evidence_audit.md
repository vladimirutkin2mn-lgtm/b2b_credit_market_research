# Screen Evidence Audit — SME Lending Deep Dives

**Version:** 2026-10-02  
**Purpose:** turn visual-enrichment work into a controlled evidence backlog rather than ad-hoc screenshot hunting.

## Coverage standard

A company is **Strong** only when first-party evidence covers at least three analytically distinct stages of the credit journey, such as:
- eligibility / offer;
- data connection / application;
- decision / status;
- pricing / contract;
- funding;
- servicing / repayment.

Marketing hero images do not count unless they visibly show the credit interface.

---

## Current coverage

| Company | Coverage | First-party stages captured | Highest-value missing screen |
|---|---|---|---|
| Stone | **Strong** | pre-approved offer; status/analysis; servicing/repayment | amount + price simulation |
| Allica | **Strong** | eligibility; bank connection; submission/underwriter handoff; drawdown | formal offer / pricing |
| iwoca | **Strong/Medium** | application; data stage; offer/completion | exact Open Banking consent + contract |
| Amex BLOC | **Strong/Medium** | repeat draw; funding destination; success | initial approval / underwriting |
| Square | **Strong/Medium** | balance/repayment; manual/automatic payment servicing | pre-approved offer + amount configuration |
| Floryn | **Medium/Strong** | approved-facility dashboard; drawdown economics | PSD2 consent + personalized offer |
| Nubank | Partial | credit product surfaced in Nu Empresas | simulation + contract + servicing |
| CommBank | Partial | conditional/pre-approved offer documented on official page | stable first-party conditional-offer / NetBank application asset |
| Rabobank | Partial | live calculator/customer UI; public process | transaction-consent + personalized offer |
| Konfío | Partial | live public simulator | SAT/CIEC consent + personalized offer |
| Funding Circle | Partial | public live application sequence / calculator; backend API flow | customer application / personalized quote screen |
| Mercado Pago | Low/Partial | account/app credit entry context; detailed official textual flow | business credit offer + amount/term screen |
| Itaú | Low | exact app route documented | FGI/Pronampe eligibility + offer |
| SBI | Low | exact product process documented | PABL/Digi Sugam offer/application |
| UGRO | Low/Partial | official embedded-process visual | actual partner-platform offer |
| Commerzbank | Low | online flow documented | online form + adviser/decision state |
| Judo | Low by design | relationship journey | banker/customer case-status tooling if public |
| Bibby | Low | operational flow documented | invoice upload + availability/draw dashboard |

---

## Screen acquisition priorities

### Priority A — most decision-useful

1. **CommBank conditional approval / NetBank application**
   - Why: cleanest existing-vs-new customer natural experiment.
2. **Rabobank transaction-data consent / personalized offer**
   - Why: strongest bank evidence for replacing annual accounts.
3. **Konfío SAT/CIEC consent / personalized offer**
   - Why: canonical tax-data underwriting case.
4. **Mercado Pago business-credit offer / amount-term**
   - Why: canonical marketplace pre-underwriting case.
5. **Itaú FGI/Pronampe app**
   - Why: connects government guarantee to digital journey.

### Priority B — improves completeness

6. Funding Circle personalized quote.
7. SBI PABL / Digi Sugam.
8. UGRO partner-platform embedded offer.
9. Bibby receivables portal.
10. Commerzbank digital request form.

---

## Stop rules

Do **not** add:
- consumer/personal credit screenshots as SME evidence;
- third-party mockups;
- generic mobile banking images that do not prove a credit stage;
- outdated screens when a current official flow contradicts them;
- screenshots without a source URL and capture/evidence note.

A missing screen remains explicitly marked as screen evidence missing.

---

## Research implication

The evidence is now good enough to compare **journey mechanisms** even where every screen is not public.

The remaining screen work is principally useful for:
- presentation quality;
- validating exact disclosure/order of steps;
- identifying hidden customer effort;
- comparing transparency.

It is no longer a blocker to the operating-model conclusions.
