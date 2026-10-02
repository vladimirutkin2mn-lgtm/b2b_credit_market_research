# Consulting-Grade Quality Standard

Version date: 2026-10-02.

## Purpose

The project should aspire to the analytical rigor and executive usefulness expected from top-tier strategy consulting work.

This does **not** mean copying proprietary McKinsey, Bain or BCG materials, language or templates.

It means holding the research to a high professional bar:

**answer-first, hypothesis-driven, mutually coherent, quantified, source-grounded, mechanism-based and decision-relevant.**

A long report is not a good report by default.

The output should allow a senior banking/product/risk executive to understand:
1. what is true;
2. why it is true;
3. how large it is;
4. what causes the difference;
5. what can be transferred;
6. what should be investigated or done next.

---

# 1. Answer-first standard

Every major section starts with a **provisional answer**, not a data dump.

Bad:
> Brazil has many fintechs. Stone has acquiring data. Nubank has 6m business customers. Itaú offers Pronampe.

Better:
> Brazil is unusually useful for studying SME credit because three structurally different models coexist at scale: deposit-funded incumbent lending, account-led digital-bank lending and acquiring-data embedded credit. This allows us to isolate the value of proprietary transaction data from funding and guarantee advantages.

Then provide evidence.

## Rule

For every major section use:

### Answer
1–3 sentences.

### Evidence
The minimum facts needed to support it.

### Mechanism
Why the observed effect is occurring.

### Implication
Why it matters for SME lending strategy.

### Caveat / counter-evidence
What could make the conclusion wrong.

---

# 2. Pyramid principle

Final outputs should follow:

**Executive answer → supporting arguments → supporting evidence**

Not:
**raw research → narrative → eventual conclusion**

For an executive report, the reader should understand the main message from:
- title;
- subtitle / takeaway;
- first paragraph;
- exhibit headline.

Detailed evidence belongs underneath.

---

# 3. Hypothesis-driven research

Before deep research, define:
- hypothesis;
- evidence that would support it;
- evidence that would disprove it;
- highest-value data source.

Example:

### Hypothesis
Existing transaction data materially shortens SME lending journeys.

### Supporting evidence
Existing-customer routes show fewer manual fields/documents and shorter decision SLA.

### Disconfirming evidence
New-to-bank lenders achieve the same speed with comparable risk and economics.

Research should actively look for both.

---

# 4. MECE where useful, not mechanically

Analytical frameworks should aim to avoid:
- overlap;
- missing categories;
- duplicate metrics.

Examples:

Lending economics:
1. revenue;
2. funding;
3. credit loss;
4. operating cost;
5. capital.

Customer journey:
1. discovery;
2. eligibility;
3. application/data;
4. decision;
5. offer/signing;
6. disbursement;
7. servicing;
8. repeat/distress.

But do not force reality into a framework when evidence shows categories overlap.

---

# 5. Quantification standard

Whenever possible, replace qualitative statements with magnitude.

Bad:
> Challenger banks became more important.

Better:
> Challenger and specialist banks represented 59% of UK gross SME bank lending in 2025.

Bad:
> Smaller loans are common.

Better:
> 37% of US SBCS financing applicants seeking loans/LOC/MCA requested no more than $50k; KfW reports 67% of new German SME investment loans at €50k or less.

## Quantify:
- market size;
- growth;
- price;
- loss;
- approval;
- ticket;
- time;
- customer count;
- share;
- economics.

If no reliable number exists, say so explicitly.

---

# 6. Mechanism over correlation

The core question is not only **what differs**, but **why**.

For every important advantage, build a mechanism chain.

Example:

**Acquiring relationship**
→ daily transaction data
→ lower information asymmetry
→ proactive/pre-approved offer
→ fewer borrower inputs
→ lower underwriting cost / faster decision
→ automated sales-linked repayment
→ better monitoring/collections observability

Then test each link with evidence.

If a link is inferred rather than observed, label it hypothesis.

---

# 7. Economics + risk + UX must connect

No product or UX conclusion is complete unless we test its effect on at least one of:

- revenue/conversion;
- credit risk;
- acquisition cost;
- underwriting cost;
- servicing cost;
- funding;
- capital;
- retention/cross-sell.

Example:

A 5-minute application is not inherently valuable.

It becomes strategically valuable if it:
- increases completion/conversion;
- lowers manual underwriting cost;
- preserves risk selection;
- improves repeat borrowing;
- creates cross-sell.

Where impact cannot be measured, state the likely channel and evidence gap.

---

# 8. Comparison must explain structural drivers

Do not stop at:

| Lender | Decision time |
|---|---|
| A | 5 min |
| B | 2 days |

Ask:
- existing vs new customer?
- ticket size?
- secured/unsecured?
- pre-approved vs open application?
- data already held?
- manual review threshold?
- borrower quality?
- guarantee?
- funding model?

Only then compare.

---

# 9. Exhibit standard

Every important table/chart/screenflow should have an **insight headline**, not a neutral label.

Weak:
> SME loan application times

Strong:
> Instant SME decisions are concentrated in low-ticket or data-rich existing-customer journeys; larger tickets reintroduce manual review.

Each exhibit should have:
- one message;
- normalized definitions;
- source/date;
- key caveat;
- no decorative metrics that do not support the message.

---

# 10. Customer-screen standard

Screens are analytical evidence.

Each screen should answer one of:
- what information does the customer provide?
- what data is already known?
- what is disclosed about price/terms?
- where does the customer wait?
- where is manual interaction introduced?
- what is automated?
- what happens after disbursement?

Annotated screenflows are preferable to galleries.

Do not include screenshots merely because they look useful.

---

# 11. Evidence hierarchy

High-impact conclusions should rely on:
1. regulator / official statistics;
2. audited filings / regulatory disclosures;
3. official product/legal/help pages;
4. high-quality independent research;
5. user evidence for UX/friction.

Marketing claims may establish that a feature is offered.

They do not prove:
- adoption;
- conversion;
- actual SLA;
- profitability;
- portfolio quality.

---

# 12. Triangulation requirement

For critical conclusions, seek at least two independent forms of evidence.

Examples:

### Claim
Digital lender approves faster.

Triangulation:
- official SLA;
- observed application journey;
- customer-review timing evidence;
- automation disclosure.

### Claim
Model has superior economics.

Triangulation:
- reported segment profit/yield;
- funding structure;
- credit-cost data;
- operational-efficiency evidence.

One weak source plus another weak source does not equal high confidence.

---

# 13. Counter-evidence / red-team standard

Every major thesis must contain a section:

**What would make this conclusion wrong?**

Actively search for:
- worse vintages;
- hidden selection effects;
- higher pricing;
- funding disadvantages;
- manual exception rates;
- regulatory subsidies;
- different borrower mix.

Example:
Stone provides strong evidence that transaction data and embedded repayment can enable excellent UX, but 2026 NPL/cost-of-risk deterioration is counter-evidence against any simplistic claim that this model automatically produces superior risk.

---

# 14. Separate facts, calculations and judgment

Use explicit labels:

### Fact
Directly reported / observed.

### Calculation
Derived transparently from facts.

### Estimate
Requires assumptions.

### Hypothesis
Plausible causal interpretation.

### Recommendation / implication
What the evidence suggests a lender should consider.

Never let a hypothesis become a fact through repetition.

---

# 15. Decision relevance

Every major finding should answer:

**So what for a lender?**

Possible implications:
- which segment to enter;
- which data connection to build;
- where automation is economically sensible;
- which customer steps can be removed;
- where relationship managers remain necessary;
- whether guarantees change economics;
- which capabilities are prerequisite vs nice-to-have.

Avoid generic implications such as “banks should improve digital UX.”

---

# 16. Transferability test

A practice is not “best practice” simply because a successful lender uses it.

Before calling something transferable, test:

1. **Customer prerequisite**
   - same borrower type?

2. **Data prerequisite**
   - open banking?
   - acquiring data?
   - tax data?

3. **Distribution prerequisite**
   - existing account base?
   - embedded platform?

4. **Funding prerequisite**
   - deposits?
   - wholesale funding?

5. **Risk prerequisite**
   - guarantee?
   - collateral?
   - bureau quality?

6. **Regulatory prerequisite**
   - digital identity?
   - data-sharing regulation?
   - licensing?

7. **Scale prerequisite**
   - sufficient transaction volume / repeat customers?

Use labels:
- highly transferable;
- transferable with prerequisites;
- context-specific;
- insufficient evidence.

---

# 17. Executive synthesis standard

Each country/company/theme synthesis should fit a compact structure:

## What matters
The one-sentence conclusion.

## Proof
2–4 quantified facts.

## Why
Mechanism.

## Strategic implication
What it changes for product/risk/business model decisions.

## Watch-out
Counter-evidence / dependency.

---

# 18. Company teardown quality gate

A company teardown is not complete because all headings contain text.

It is complete when it answers:

### Position
What role does this lender play in the market?

### Customer
Who exactly is served?

### Need
What credit need is being solved?

### Product
What is actually sold and on what terms?

### Journey
What does the customer actually experience?

### Data
What information substitutes for documents/manual underwriting?

### Decision
Where is automation vs human judgment?

### Risk
What happens after origination?

### Economics
How does the lender make money after funding, losses and operating cost?

### Advantage
What is genuinely structural vs easy to copy?

### Transferability
What could another lender replicate, and what prerequisites are required?

If one of these is unknown, state the gap.

---

# 19. Minimum executive-quality artifacts

The final project should contain:

1. **Executive answer deck/report**
   - ~10–15 core messages, not 100 pages of facts.

2. **Evidence book**
   - detailed market/player data behind the conclusions.

3. **Market landscape**
   - comparable country economics and access.

4. **Operating-model map**
   - S1–S7 and how economics/risk/journey differ.

5. **Company teardowns**
   - 18 evidence-rich cases.

6. **Visual Customer Journey Atlas**
   - annotated customer screens and flow comparisons.

7. **Economics / risk benchmark**
   - normalized where defensible.

8. **Pattern library**
   - observed mechanisms, not generic best practices.

9. **Transferability matrix**
   - practice × prerequisite × expected impact × confidence.

---

# 20. Final quality-control questions

Before publishing any section, ask:

1. What is the answer?
2. Is the headline a conclusion or merely a topic?
3. Is the conclusion quantified where possible?
4. Are the comparisons apples-to-apples?
5. What explains the difference?
6. Is the explanation evidenced or hypothesized?
7. Have we looked for counter-evidence?
8. What matters economically?
9. What matters for risk?
10. What matters for the customer journey?
11. What can actually be transferred?
12. What should the reader do differently because of this analysis?

If these cannot be answered, the section is not finished.

---

# Working quality bar

The project should be able to withstand review from:
- a bank CEO / business head;
- a CRO / credit officer;
- a CFO;
- a product leader;
- a strategy team;
- a skeptical investment committee.

The objective is not stylistic imitation.

The objective is **boardroom-grade analytical quality**.
