# Market Infrastructure for SME Lending — 8 Markets

**Version:** 2026-10-02

## Executive answer

SME credit operating models are constrained by the market's **data and risk-sharing rails**.

The most important transferable infrastructure dimensions are:

1. transaction / Open Banking data;
2. business identity and registry;
3. tax / e-invoice data;
4. guarantee / risk-sharing infrastructure;
5. ability to authenticate and act digitally on behalf of a business.

A product pattern should not be called transferable until these prerequisites are checked.

---

# Summary matrix

| Market | Transaction-data rail | Business identity / registry | Tax / invoice rail | Guarantee / risk-sharing rail | Main transferability implication |
|---|---|---|---|---|---|
| United States | Fragmented for business; Section 1033 rule covers specified consumer financial products and compliance dates are stayed | EIN + state/business registries; no single universal business eID | Tax data available but no single lender-facing SME rail comparable with India/Mexico | SBA 7(a) is major federal guarantee infrastructure | Embedded/account-led models are highly transferable; standardized business Open Banking less plug-and-play |
| United Kingdom | Mature Open Banking explicitly supports business account-data sharing | Companies House + mandatory identity verification for directors/PSCs | HMRC/Companies House ecosystem; lender-specific integrations | Growth Guarantee Scheme | Strong environment for Open Banking + digital SME journeys |
| Brazil | Open Finance with regulated institutions; 2026 scope includes credit-portability services | CNPJ + e-CNPJ / gov.br mechanisms | Extensive Receita/SPED/e-document ecosystem | BNDES FGI / FGI PEAC | Strong for bank/account/payment-data underwriting and guarantee-backed digital credit |
| Germany | PSD2 account-information services | ELSTER / Mein Unternehmenskonto | ELSTER / e-invoice/tax infrastructure | Bürgschaftsbanken; guarantees can cover up to 80% within program rules | Strong for Open Banking but relationship/accounting evidence remains important in larger SME |
| India | Account Aggregator network at large scale | Udyam + Aadhaar/PAN/GST-linked registration | GST/e-invoice + income-tax data | CGTMSE / public guarantee architecture; multiple policy schemes | Exceptional multi-rail environment for cash-flow/data-driven MSME lending |
| Netherlands | PSD2 / bank transaction access | KVK + eHerkenning business eID | Dutch digital tax/accounting ecosystem | BMKB up to €1.5m | Strong for transaction-data substitution and digital authorization |
| Australia | Consumer Data Right banking live; non-bank lender rollout expanding in 2026 | ABN + myID + RAM | ATO digital business services / accounting ecosystem | Pandemic SME guarantee schemes closed in 2022; no comparable broad current national guarantee identified in this pass | Strong bank-data portability and digital authorization; less guarantee-driven than UK/Brazil/India/NL |
| Mexico | Fintech/Open Finance legal framework exists; practical standardized SME data-sharing remains less mature than UK/Brazil | RFC + SAT e.firma | SAT/e-invoicing is a major machine-readable underwriting rail | Nafin programs/guarantees; 2026 Plan México includes guarantee support | Tax/e-invoice underwriting may be more transferable than Open Banking-style underwriting |

---

# United States

## Transaction-data rail

The CFPB's Personal Financial Data Rights regulation requires covered providers to make certain data available electronically, but the current rule covers specified **consumer** products such as Regulation E accounts and Regulation Z credit cards.

Important current-status caveat:
- compliance dates were stayed by a federal court on 29 October 2025;
- CFPB has been reconsidering aspects of the rule.

Sources:
- https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/
- https://www.consumerfinance.gov/rules-policy/regulations/1033/111/

### SME implication

Do not treat US commercial-account data sharing as a standardized business Open Banking rail comparable with UK Open Banking or EU PSD2.

Private aggregators and direct bank integrations remain important.

## Business identity

EIN is the federal business tax identifier and is commonly needed for bank accounts and business credit.

Source:
https://www.irs.gov/newsroom/how-to-get-an-employer-identification-number-for-your-business

The US does not have one universal national business digital identity/registry equivalent to eHerkenning/Udyam.

## Guarantee

SBA 7(a):
- max loan generally $5m;
- guarantee up to 85% for loans ≤$150k;
- up to 75% above $150k for most standard 7(a).

Source:
https://www.sba.gov/loans/7a-loans/

## Strategic implication

Most transferable US data-driven SME patterns are:
- existing-bank transaction data;
- card/acquiring data;
- accounting integrations;
- private data aggregators;
- SBA guarantee products.

---

# United Kingdom

## Open Banking

UK Open Banking explicitly supports businesses sharing current financial data with regulated third parties for:
- credit;
- cash-flow management;
- payments.

By July 2026, the UK ecosystem had processed more than:
- 1bn Open Banking payments;
- 100bn API calls across CMA9 banks.

Sources:
- https://www.openbanking.org.uk/how-open-banking-can-help-businesses/
- https://www.openbanking.org.uk/news/open-banking-surpasses-one-billion-payments-and-100-billion-api-calls/

## Business identity

From 18 November 2025, identity verification became a legal requirement for relevant Companies House directors/PSCs, with a 2025–26 transition.

Source:
https://www.gov.uk/guidance/verifying-your-identity-for-companies-house

## Guarantee

Growth Guarantee Scheme:
- government-backed;
- up to £2m per business group;
- turnover ≤£45m;
- term loans, overdrafts, asset finance, invoice finance and asset-based lending.

Source:
https://www.gov.uk/business-finance-support/growth-guarantee-scheme

## Strategic implication

UK is structurally well suited to:
- Open Banking-based underwriting;
- new-to-lender digital finance;
- guarantee-supported digital products.

---

# Brazil

## Open Finance

Banco Central Open Finance includes regulated banks, payment institutions, finance companies and cooperatives.

BCB's 2026 Open Finance data/service scope version 8.0 added credit-portability services.

Sources:
- https://www.bcb.gov.br/meubc/faqs/p/os-bancos-e-instituicoes-que-participam-do-open-finance
- https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=759&tipo=Instru%C3%A7%C3%A3o+Normativa+BCB

## Business identity / tax

Core rails:
- CNPJ;
- Receita Federal digital services;
- e-CNPJ / digital certificate;
- gov.br electronic signature in eligible contexts.

Sources:
- https://www.gov.br/pt-br/servicos/inscrever-no-cnpj
- https://www.gov.br/governodigital/pt-br/identidade/assinatura-eletronica/assinatura-eletronica/
- https://www.gov.br/receitafederal/pt-br/assuntos/empresas-e-negocios

## Guarantee

BNDES FGI:
- traditional guarantee fund is a permanent complement to collateral for MSMEs;
- FGI PEAC is a separate time-bound/special program;
- current PEAC rules were updated during 2026.

FGI PEAC eligibility publicly includes firms with annual gross revenue up to R$300m under current program rules.

Sources:
- https://www.bndes.gov.br/wps/portal/site/home/financiamento/garantias/bndes-fgi/informacoes-a-empresas-empreendedores/informacoes-empresas-empreendedores/
- https://bndes.gov.br/wps/portal/site/home/financiamento/garantias/peac/faq-peac/
- https://www.bndes.gov.br/wps/portal/site/home/financiamento/garantias/peac/normativos-peac/

## Strategic implication

Brazil combines:
- banking transaction data;
- payments/acquiring;
- Open Finance;
- digital tax identity;
- guarantees.

This explains why very different digital SME models can coexist.

---

# Germany

## Transaction-data rail

PSD2 created regulated:
- payment initiation;
- account information services.

BaFin is the national supervisory authority for payment-service licensing/supervision.

Source:
https://www.bafin.de/ref/19619686

## Business digital identity

Germany's ELSTER-based **Mein Unternehmenskonto** acts as a digital identity/authentication mechanism for organizations accessing public online services.

ELSTER organization certificates are tied to business tax identity and can support authenticated applications.

Sources:
- https://www.elster.de/eportal/start
- https://download.elster.de/download/dokumente/Datenschutz_Mein_ELSTER.pdf

## Guarantee

Germany's Bürgschaftsbanken help viable SMEs that lack sufficient collateral.

Federal ministry guidance states:
- guarantees can cover up to 80% of the bank loan;
- maximum guarantee amount can be €2m under the described framework.

Source:
https://www.bundeswirtschaftsministerium.de/Redaktion/DE/Dossier/Mittelstandsfinanzierung/buergschaften.html

## Strategic implication

Germany supports Open Banking-style data access, but the Mittelstand segment still makes:
- accounting;
- relationship;
- collateral;
- guarantee infrastructure

particularly important for larger tickets.

---

# India

## Account Aggregator

As of 31 March 2026, India's government reports:
- 179 institutions live as Financial Information Providers;
- 989 as Financial Information Users;
- >2.88bn financial accounts enabled for data sharing;
- 284.6m accounts linked by users.

Consent is explicit.

Source:
https://www.financialservices.gov.in/account-aggregator-framework

## Business identity / formalisation

Udyam:
- online and paperless;
- permanent registration number;
- dynamic QR certificate;
- integrated with PAN, GST and income-tax data;
- Udyam/UAP together had roughly 97m registrations by late Sep/early Oct 2026.

Source:
https://udyamregistration.gov.in/

## Tax / invoice rails

India's GST/e-invoice infrastructure creates machine-readable:
- turnover;
- invoice;
- tax data.

The official e-invoice ecosystem supports authenticated API/data access under consent/authorization arrangements.

Source:
https://einvoice6.gst.gov.in/content/kb/overview-of-data-apis/

## Guarantee

India has a broad public MSME guarantee ecosystem, including CGTMSE and scheme-specific guarantees used by banks.

For company/product analysis, guarantee coverage must be attached to the exact program rather than assumed from generic MSME status.

## Strategic implication

India is unusually favorable for multi-source cash-flow underwriting because identity, registry, GST/tax and financial data-sharing rails can be combined.

---

# Netherlands

## Transaction data

Dutch lenders operate within the EU PSD2 framework, allowing regulated account-information/payment services.

Observed company evidence already demonstrates practical use:
- Rabobank transaction-data underwriting;
- Floryn PSD2 connection.

## Business identity

eHerkenning is the Dutch electronic identity/login mechanism for companies accessing government services.

Source:
https://business.gov.nl/regulations/applying-for-eherkenning/

## Guarantee

BMKB:
- active through 1 July 2027;
- max financing amount €1.5m under the scheme;
- intended to improve collateral/finance access;
- used by banks and accredited non-bank financiers.

Source:
https://english.rvo.nl/subsidies-financing/bmkb

## Strategic implication

The Netherlands combines:
- transactional-data accessibility;
- strong business identity;
- guarantee infrastructure;

making it structurally conducive to “financial-statements optional” small-ticket SME lanes.

---

# Australia

## Consumer Data Right

Banking data sharing under CDR has been live since July 2020 and all Australian banks participate.

In 2026:
- product data obligations began for relevant non-bank lenders on 13 July;
- consumer data sharing for non-bank lenders is scheduled from 9 November 2026.

Source:
https://www.accc.gov.au/by-industry/banking-and-finance/the-consumer-data-right

## Business identity / authorization

Core government digital-business rails:
- ABN;
- myID digital identity;
- Relationship Authorisation Manager (RAM), which links individuals to a business and lets them act on its behalf.

Sources:
- https://www.ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/registration-obligations-for-businesses
- https://softwaredevelopers.ato.gov.au/usingmygovidramandmachinecredentials

## Guarantee

The COVID-era SME Recovery Loan Scheme and SME Guarantee Schemes closed to new loans by 30 June 2022.

Sources:
- https://treasury.gov.au/coronavirus/sme-recovery-loan-scheme
- https://treasury.gov.au/flow-credit-flow-credit/sme-loan-guarantee-schemes-schemes

No broad current national SME loan-guarantee scheme directly comparable with UK GGS / Dutch BMKB was identified in this research pass.

## Strategic implication

Australia strongly supports:
- account-data portability;
- digital business authorization;
- accounting-data integrations.

Current SME lending architecture is less centered on a broad national guarantee scheme.

---

# Mexico

## Open Finance framework

Mexico's Fintech Law provides the legal framework for fintech/open-data/API development; CNBV maintains current Fintech regulation.

Source:
https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/Fintech/Paginas/NORMATIVIDAD-FINTECH.aspx

In this research pass, we did **not** establish a business transaction-data ecosystem with the same maturity/coverage as UK Open Banking or Brazil Open Finance.

Therefore Mexico is tagged:
**framework present / standardized business-data usage still partial for our SME-credit comparison.**

## Business identity / tax data

SAT e.firma:
- available to companies/personas morales;
- legally equivalent in effect to handwritten signature;
- supports SAT and other public/private digital services.

Source:
https://sat.gob.mx/portal/public/tramites/firma-electronica-avanzada-pm

Mexico's SAT/fiscal-invoice environment is a major underwriting rail, as observed directly in Konfío/Covalto product journeys.

## Guarantee / development finance

Nafin supports Mipymes through:
- second-floor lending;
- guarantee programs;
- commercial-bank partnerships.

In 2026 Plan México, Nafin/Bancomext announced guarantee support including:
- 70% guarantees for loans up to MXN20m in priority sectors;
- 80% for qualifying first-credit loans up to MXN5m.

Sources:
- https://www.gob.mx/nafin/prensa/detonaran-nafin-y-bancomext-mas-de-120-mdp-en-financiamiento-para-mipymes-y-proyectos-estrategicos-del-plan-mexico
- https://www.nafin.gob.mx/portalnf/content/financiamiento/

## Strategic implication

For Mexico, **tax/e-invoice data** currently appears more strategically actionable for SME underwriting than assuming a UK-style Open Banking architecture.

---

# Cross-market transferability map

## Best environments for transaction-data / Open Banking lending
- UK
- Brazil
- Netherlands
- Australia
- India (through AA and banking data)

## Strong tax/e-invoice underwriting environments
- India
- Mexico
- Brazil

## Strong digital business identity / authorization rails
- India — Udyam + Aadhaar/PAN/GST-linked framework
- Netherlands — eHerkenning
- Australia — myID + RAM
- Germany — ELSTER Unternehmenskonto
- UK — Companies House identity verification
- Mexico — SAT e.firma
- Brazil — CNPJ/e-CNPJ/gov.br ecosystem

## Material guarantee infrastructure in current research
- US — SBA
- UK — GGS
- Brazil — FGI / FGI PEAC
- Germany — Bürgschaftsbanken
- India — public MSME guarantee ecosystem
- Netherlands — BMKB
- Mexico — Nafin / Plan México

Australia's broad pandemic SME guarantee programs are historical rather than current.

---

# Strategic conclusion

The same customer journey can have very different feasibility by market.

Example:

**“Upload no financial statements; share bank data and get a decision.”**

Highly plausible where:
- regulated transaction-data sharing exists;
- business identity is reliable;
- account history is sufficiently long.

Less directly portable where:
- business data sharing is fragmented;
- lender lacks an existing account relationship;
- tax/accounting APIs are weak.

Therefore the final transferability test must always include:

**Practice × Data rail × Identity rail × Guarantee rail × Funding rail × Risk governance.**
