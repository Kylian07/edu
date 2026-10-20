# 🧑‍🏫 Instructor guide

For faculty, TAs and mentors who use **BiologyToMath** alongside CMU 02-680 *Essential Mathematics
and Statistics for Scientists*, as a bridge course for biology students entering computational
biology, as recitation material, or as structured self-study for undergraduate researchers.
Students should start from the [README](README.md). This guide covers the design principles,
formats, learning outcomes, the map from the 02-680 topics to the modules, per-module teaching notes
and common difficulties, assessment, errata in the source material, and maintenance.

**Design principles.**

1. **Self-contained.** The notebooks teach the 02-680 content themselves — every definition,
   theorem, proof, worked example, figure (re-drawn by code), table, common misconception and
   question to the class of the teaching material — explained more slowly and more concretely, with
   code that checks it. 📘 *Lecture notes* boxes summarise each subtopic so that a student who reads
   only those boxes has a complete, correct summary of the topic.
2. **Synthetic data with a known truth.** The repository stores no data or pictures. Every data set
   is simulated by code (or is a short classic table typed into a cell and labelled as such; see
   [`DATA.md`](DATA.md)), and every simulator returns the truth it was built from, so every method
   can be checked against it.
3. **Implement, then check with a library.** Every computation is first done the way a student would
   do it on paper — a cofactor expansion, a Gauss–Jordan reduction with exact fractions, a likelihood
   differentiated by hand — and then checked with NumPy, SymPy or SciPy, side by side.
4. **Robust to the reorganisation of 02-680.** The 02-680 lectures and notes change order and
   numbering from year to year. The notebooks never refer to them: they name topics by content, and
   cross-references go only to this course's modules. The map below is by topic name only, so a new
   syllabus needs, at most, a new row order in this table — never a change to a notebook.
5. **Biology everywhere, honestly.** Each module opens with a real biological question and uses
   biological examples throughout; simulated data are labelled SIMULATED and illustrative numbers
   illustrative.

---

## Formats that work

| Format | Plan | Notes |
|---|---|---|
| Companion to 02-680 | Modules 00–01 before the semester, then topic by topic as in the [README](README.md#following-02-680-by-topic) | recitations can run a module's key section live; ✏️ exercises make good warm-up problems; 📘 boxes are ready-made revision sheets; ✅ checkpoints work as entry or exit tickets |
| Summer bridge before 02-680 | Parts A–C (00–13) over 6–8 weeks at ≈ 6 h per week, Parts D–G during the semester | front-loads notation, proof and linear algebra, which biology majors find least familiar |
| Bridge before 02-620 / BiologyToML | the whole course over 10–12 weeks at ≈ 8 h per week (a shorter path is in the README) | then [BiologyToML](../../../ml/tutorial/BiologyToML/README.md), whose Part A becomes a review |
| One-semester self-study | the 15-week plan in the README (≈ 8–10 h per week) | pair students and meet weekly to discuss the 🧠 questions |
| Refresher for graduate students | Parts C and E–G only, with the 📘 boxes and the checkpoints | for students entering 02-710 or 02-750 without a recent mathematics course |
| Lab onboarding | 00–01, then the part a project needs (linear algebra for imaging, probability and statistics for genomics) | continue with the topic courses listed in the README |

**Before the first session.** Ask students to open Module 00 in Colab and run it top to bottom
(about a minute) to catch account and browser problems early. No downloads are needed: every data
set is generated in the notebook.

---

## Learning outcomes by part

| Part | Students can… | Evidence |
|---|---|---|
| A · Getting started (00–01) | read and write the notation of the course (Σ, Π, ∈, ⊆, ∀, ∃, ⇒, ⇔, f: S → T, set-builder); run and modify notebooks; mirror sets, tuples, functions, sums and matrices in Python; check a hand calculation with SymPy | a notation quiz; a Python function for a sum or a product checked against SymPy; a LaTeX snippet typeset correctly |
| B · Foundations (02–06) | translate statements into logic, prove equivalences by truth table and negate nested quantifiers; compute with sets, functions, tuples and strings; prove Big-O statements with witnesses; compute degrees, paths, components and spanning trees and recognise trees and bipartite graphs | the De Morgan truth table; the Venn diagram and Jaccard index of infection-response genes; the genetic code analysed as a function; a Big-O proof; BFS on the inflammation network |
| C · Linear algebra (07–13) | compute products, determinants, inverses and RREFs by hand; parametrise solution sets and null spaces; prove subspace properties; decide independence; find bases, coordinates and ranks; compute eigenvalues, eigendecompositions and the SVD; interpret them on expression data and population models | det = −49 by cofactor expansion; the inverse with det −17; the 3 × 5 system in parametric form; the rank of a genotype design matrix; λ³ − 7λ + 6 and its eigenvectors; the SVD of the infection experiment, interpreted |
| D · Calculus (14–15) | differentiate and integrate with every rule and derive the power rule; solve one-variable optimisation problems; compute gradients and Jacobians; derive and solve the normal equations; find equilibria and decide stability | the global minimum of the quartic; AUC of a one-compartment drug model; the insulin regression by gradient descent and by the normal equations; the SIR threshold R₀ = β/γ |
| E · Probability (16–20) | derive consequences of the axioms; compute conditional probabilities and apply Bayes' rule; distinguish independence from conditional independence; work with PMFs, PDFs and CDFs of the named distributions; marginalise and condition joint tables; factorise Bayesian networks; compute with Markov chains | a screening-test calculation; naïve-Bayes cell typing with a confusion table; the horse-kick Poisson fit; the BRCA1/P53 classifier; P(T ∣ S) in the bronchitis network; a CpG-island scan |
| F · Statistics: from data to estimates (21–24) | compute expectations, variances and conditional expectations; explain the LLN and CLT and build and interpret confidence intervals; derive MLEs; derive conjugate posteriors and MAP estimates and explain pseudocounts | the buggy-coin variance; a coverage simulation of 100 intervals; Bernoulli, normal and Poisson MLEs on paper; the allele-frequency MLE; the coin-drawer Bayes table |
| G · Inference in practice (25–28) | state hypotheses; compute z, t and χ² statistics; reason about Type I/II errors, power and sample size; control the FWER and FDR; fit and test a linear regression and state its limits; take a question to a quantitative answer | a paired t-test on the cholesterol trial; Mendel's χ²; a Hardy–Weinberg test; Benjamini–Hochberg on 400 genes with precision and recall against the truth; the insulin regression with confidence intervals; the capstone report |

---

## The 02-680 topics → modules

The notebooks never point to 02-680's lectures or notes, but instructors can use this map to align
recitations with the course. It is by **topic name only**: whatever order or numbering a semester
uses, look up the topic here.

| 02-680 topic (by content) | Modules | What the modules add or where parts live |
|---|---|---|
| Course overview: why scientists need mathematics and statistics; course objectives; reference textbooks | [00](notebooks/00_welcome_math_for_biology.ipynb) | a notation crash course, LaTeX for homework, a guided tour of all parts; computing prerequisite in [01](notebooks/01_python_for_mathematics.ipynb) |
| Propositional and predicate logic | [02](notebooks/02_logic.ipynb) | Boolean gene-regulation rules; quantifiers as loops |
| Sets, set operations and functions | [03](notebooks/03_sets_and_functions.ipynb) | number sets, Venn diagrams, power sets, partitions, Jaccard, nearest-neighbour labelling; the genetic code as a function |
| Asymptotic notation and the growth of functions | [05](notebooks/05_asymptotics_growth_of_functions.ipynb) | algorithm costs in bioinformatics; the number of phylogenetic trees |
| Tuples, Cartesian products, sequences and strings | [04](notebooks/04_tuples_sequences_strings.ipynb) | k-mers, codons and reading frames; the recap of tuples (ℚ as pairs, RGB) also opens [07](notebooks/07_vectors.ipynb) |
| Graphs and trees | [06](notebooks/06_graphs_and_trees.ipynb) | regulatory, interaction and metabolic networks; phylogenies; adjacency-matrix powers in [08](notebooks/08_matrices.ipynb) |
| Vectors | [07](notebooks/07_vectors.ipynb) | expression profiles, distances, cosine similarity and correlation |
| Matrices and determinants | [08](notebooks/08_matrices.ipynb) | pathway scores by matrix product; determinants as area scaling |
| Linear systems and matrix inverses | [09](notebooks/09_linear_systems_inverses.ipynb) | balancing reactions, metabolic steady states, cell-type deconvolution |
| Vector spaces and subspaces | [10](notebooks/10_vector_spaces.ipynb) | function spaces; affine sets vs subspaces |
| Linear independence, span, basis and rank | [11](notebooks/11_independence_basis_rank.ipynb) | the genotype-coding trap; rank of expression programmes |
| Eigenvalues and eigenvectors (incl. symmetric and positive semidefinite matrices) | [12](notebooks/12_eigenvalues_eigenvectors.ipynb) | Leslie population models; power iteration |
| Eigendecomposition, similar matrices and the SVD | [13](notebooks/13_diagonalization_svd.ipynb) | the SVD of an expression matrix (eigengenes); low-rank approximation |
| Calculus review: derivatives, integrals, rules, one-variable optimisation | [14](notebooks/14_calculus_derivatives_integrals.ipynb) | growth curves, enzyme kinetics, pharmacokinetics, Euler's method |
| Calculus review: gradient-based optimisation, least squares, Jacobians, equilibria and stability | [15](notebooks/15_multivariable_calculus_dynamics.ipynb) | the tRNA model, SIR epidemics, Gauss–Newton for Michaelis–Menten |
| Introduction to probability | [16](notebooks/16_probability_spaces.ipynb) | the genetics motivation; Punnett squares as sample spaces |
| Conditional probability and Bayes' rule | [17](notebooks/17_conditional_probability_bayes.ipynb) | diagnostic testing; naïve Bayes for single cells |
| Random variables | [18](notebooks/18_random_variables_distributions.ipynb) | read counts, sequencing errors and Phred scores, waiting times between mutations |
| Multiple random variables | [19](notebooks/19_multiple_random_variables.ipynb) | the BRCA1/P53 classifier; the multivariate normal |
| Graphical representations of random variables | [20](notebooks/20_bayesian_networks_markov_chains.ipynb) | CpG islands; stationary distributions as eigenvectors |
| Expectation and moments | [21](notebooks/21_expectation_variance_moments.ipynb) | highly variable genes; the mean–variance relationship of counts |
| The law of large numbers, the central limit theorem, sampling and confidence intervals | [22](notebooks/22_sampling_lln_clt_confidence.ipynb) | coverage by simulation; replicates and sample size; bootstrap |
| Parameter estimation and maximum likelihood | [23](notebooks/23_maximum_likelihood.ipynb) (with the LLN/CLT recap in [22](notebooks/22_sampling_lln_clt_confidence.ipynb)) | allele frequencies; expression rates; numerical MLE |
| Maximum a posteriori estimation (exponential family, conjugate priors) | [24](notebooks/24_bayesian_estimation_map.ipynb) | pseudocounts in motif models; Gamma–Poisson shrinkage |
| Hypothesis testing (errors, power, z- and t-tests) | [25](notebooks/25_hypothesis_testing.ipynb) | the paired cholesterol trial; differential expression of one gene |
| Hypothesis testing for categorical data; multiple testing | [26](notebooks/26_categorical_tests_multiple_testing.ipynb) | Mendel, Hardy–Weinberg, association tables; FDR on 400 genes; enrichment |
| Review via linear regression | [27](notebooks/27_linear_regression_review.ipynb) | a "whole course" map; a cumulative review |
| Course project / cumulative review | [28](notebooks/28_capstone.ipynb) | one biological question answered with the tools of the whole course |

---

## Per-module teaching notes

Each row gives the one idea to land, the most common difficulty, and a discussion prompt.

| Module | Idea to land | Typical difficulty | Discussion prompt |
|---|---|---|---|
| 00 | mathematics is the language for biological rules (logic), data (linear algebra), change (calculus) and uncertainty (probability and statistics) | reading notation: indices, Σ and Π, symbols with several meanings | Pick a question from your biology courses — which part of this course would answer it? |
| 01 | every Python object mirrors a mathematical one: set vs tuple vs list vs dict; loops as Σ and Π; `def` as f: S → T | floating-point surprises (0.1 + 0.2 ≠ 0.3); 0-based indexing; mutable vs immutable | When is it safe to compare two floats with `==`? |
| 02 | implication is not causation; the contrapositive is equivalent, the converse is not; negating quantifiers | vacuous truth; translating "only if" and "unless"; precedence; the order of nested quantifiers | A knockout abolishes phenotype Y. Which implication did the experiment test? |
| 03 | sets as gene lists and partitions; functions defined by domain, codomain and range | ⊂ vs ⊆; 2 vs {2}; complement needs a universe; the order of composition | Is the genetic code injective? What would a bijective genetic code imply? |
| 04 | order matters: tuples, Cartesian products and strings; counting by the product rule | (A × B) × C vs A × B × C; the Kleene star contains the empty string | Why do genome assemblers use k-mers of length ≈ 31 rather than 8? |
| 05 | Big-O is a set of functions defined with quantifiers and witnesses | reading "f = O(g)" as an equation; dropping constants without justification; log-scale plots | Why does building phylogenies require heuristics? |
| 06 | graphs model networks and phylogenies; degree, paths, connectivity, trees | the two path-length conventions; self-loops in the degree; induced vs arbitrary subgraphs | Is a hub gene necessarily important, or just well studied? |
| 07 | a sample is a vector; dot products, norms and angles measure similarity | dimension mismatches and NumPy broadcasting; ℓ1 vs ℓ2 intuition | Which distance would you use to find a sample's nearest neighbour, and why? |
| 08 | the matrix product as weighted sums (and as composition); the determinant as volume scaling | the size rule; non-commutativity; cofactor signs | What does (samples × genes)(genes × pathways) compute? |
| 09 | elimination keeps the solution set; a square system has a unique solution iff det ≠ 0 | bookkeeping with fractions; inconsistent vs under-determined systems; `inv` vs `solve` | What does the null space of a stoichiometric matrix mean biologically? |
| 10 | a vector space is closed under linear combinations and contains 0; functions are vectors too | proving all axioms vs finding one failing axiom; numerical tests can disprove but not prove | Do cell-type fractions (which sum to 1) form a vector space? |
| 11 | independence, span, basis, dimension and rank | the direction of the definition (only the trivial combination gives 0); row vs column conventions for change of basis | When is a genotype design matrix rank-deficient, and what then? |
| 12 | eigenvectors are the directions a matrix only stretches | "A − λI must be 0" (it must be singular); complex eigenvalues for rotations; `eigh` sorts ascending | What does the dominant eigenvalue of a Leslie matrix predict — and what can it not? |
| 13 | diagonalisation is a change to eigen-coordinates; the SVD exists for every matrix | V vs Vᵀ; full vs thin shapes; arbitrary signs of singular vectors | Is an "eigengene" a biological programme? How would you test it? |
| 14 | the derivative is a rate, the integral an accumulation; optima where f′ = 0 | limits; the chain rule; the second-derivative test when f″ = 0 | Is a drug's exposure better summarised by its AUC or its peak concentration? |
| 15 | the gradient points uphill; least squares via the normal equations; stability from eigenvalues of the Jacobian | shapes of gradients and Jacobians; choosing a step size | Which single number decides whether an epidemic grows? |
| 16 | probability is a measure on events; every rule follows from three axioms | adding probabilities of overlapping events; P(X = x) = 0 for continuous outcomes | Frequentist or Bayesian: what does "a 30 % risk" mean for one patient? |
| 17 | conditioning restricts the sample space; Bayes' rule inverts conditionals | P(A ∣ B) vs P(B ∣ A); independence vs conditional independence | Why can most positive results of a good screening test be false? |
| 18 | a random variable is a function; PMF, PDF and CDF; the named distributions and their stories | a density above 1; Poisson vs binomial; SciPy parameterisations | Are RNA-seq counts Poisson? What would you check first? |
| 19 | joint → marginal → conditional; covariance measures linear dependence only | Cov = 0 does not imply independence; summing over the right variable | Could the (illustrative) BRCA1/P53 table be used as a clinical classifier? What is missing? |
| 20 | a graph encodes a factorisation; Markov chains forget the past given the present | which independence is used in which step; the time index of the start; row-stochastic convention | What does an arrow in a disease network claim, and what does it not? |
| 21 | expectation is linear; variance measures spread; highly variable genes | linearity needs no independence; 1/n vs 1/(n − 1); LOTUS vs (E X)² | Why are housekeeping genes used for normalisation? |
| 22 | the sample mean is a random variable; LLN, CLT; what a confidence interval means | "95 % probability that μ is in this interval"; σ/√n vs σ²/n | How many mice per group would you need? |
| 23 | the likelihood is a function of θ; the MLE recipe | likelihood vs probability; maxima at the boundary; numerical underflow | When is the MLE a bad estimate (think: zero counts)? |
| 24 | posterior ∝ likelihood × prior; MAP; conjugacy; pseudocounts | MAP vs posterior mean; what hyperparameters mean | How strong should a prior be for a rare variant? |
| 25 | a test controls error rates; what a p-value is and is not; paired designs | "accepting" H₀; the p-value as P(H₀); one- vs two-sided tests | Give an example of a statistically significant but biologically irrelevant result. |
| 26 | χ² tests for counts; false-discovery control at genome scale | expected counts, not proportions; degrees of freedom; Bonferroni vs Benjamini–Hochberg | Were Mendel's data "too good to be true"? |
| 27 | regression ties together vectors, matrices, calculus, likelihood and tests | the order of (XᵀX)⁻¹Xᵀy; collinear predictors; correlation vs causation | What would you need to claim that STAT1 regulates MX1? |
| 28 | from a biological question to a quantitative answer, with honest uncertainty | choosing among methods; reporting limitations | Which result would you report, and what would you tell a biologist who asks "so is it real?" |

---

## Assessment

- **Checkpoints** (✅, with hidden answers; 8–12 per module) work as entry and exit tickets.
- **Lab notes** (📝 template at the end of each notebook): one per module; grade for correct inputs,
  outputs and method, a sensible failure mode and a correct connection to the 02-680 topic.
- **Hand-calculation quizzes** that mirror exam questions: the worked examples listed in
  [`STUDY_GUIDE.md` §2](STUDY_GUIDE.md#2-worked-examples-to-recompute-by-hand) — truth tables,
  determinants, inverses, RREF and null spaces, characteristic polynomials, derivatives and optima,
  Bayes' rule, Bayesian-network queries, expectations and variances, MLEs and MAPs, χ² statistics.
- **Proof and derivation quizzes**: the table in
  [`STUDY_GUIDE.md` §3](STUDY_GUIDE.md#3-the-proofs-and-derivations-to-master) lists the results every
  student should reproduce on a blank page.
- **"Break the simulator" mini-projects**: change one simulator parameter and report what changes —
  fewer replicates in the infection experiment (how many true DE genes are still found?), inbreeding
  in the genotypes (does the Hardy–Weinberg test notice?), a smaller drug effect (power of the paired
  t-test), more noise in the insulin study (width of the confidence intervals).
- **Capstone** (Module 28): a short report and presentation. Suggested rubric:

| Criterion | Excellent (4) | Adequate (2–3) | Insufficient (0–1) |
|---|---|---|---|
| Question and model | biological question stated precisely; variables, assumptions and the mathematical model written down before the analysis | most elements present | model chosen after seeing the results, or not stated |
| Mathematical correctness | every derivation complete and correct, in clean notation | minor slips that do not change conclusions | errors that change conclusions |
| Computation and verification | hand results checked by code; method checked against the simulated truth; seeded and runs end to end | partial checks | no checks; cannot be rerun |
| Uncertainty and interpretation | intervals or tests with correct interpretation; limits of the biological claim stated | some uncertainty reported | point estimates only; causal claims from associations |
| Communication | typeset mathematics, labelled figures with units, a clear one-page summary | understandable with effort | unclear figures or notation |

---

## Errata in the source material

While turning the 02-680 teaching material into self-contained notebooks, every worked example was
recomputed with code and every definition was checked. The notebooks teach the correct statement
directly — where students are likely to meet the wrong version, in a short ⚠️ *Common confusion*
note — and never refer to the source. The lists below record each finding as **a common slip in
versions of the teaching material**, described by its content (not by lecture, page or file
number, which change between years), so that the material can be fixed in a future revision. Each
entry reads *slip → correct statement*. Numerical corrections were recomputed with code; the most
consequential ones are in **bold**.

### Introduction and course overview (Modules 00–01)

- "All the textbooks are freely available online" → only Liben-Nowell and *Mathematics for Machine
  Learning* are free from their authors; some links point to unofficial copies of other books.
  The notebooks link only to official sources.
- The "this course provides…" overview names logic, linear algebra and probability/statistics but
  not calculus → calculus is its own block of the course.
- The outline lists the exponential family twice ("sufficient statistics and exponential family"
  and "exponential family and Bayesian learning") → one topic (Module 24).
- Minor: speaker-note headings off by one; repeated speaker notes; "integraty",
  "automationPrepares".

### Logic (Module 02)

- A precedence table puts ∧, ∨ and ⊕ on one level → conventions differ (Python and many texts bind
  ∧ more tightly than ∨); ¬ binds first and ⇔ last, and parentheses are the safe choice.
- A nested-negation example uses x for both quantified variables → ¬[∃x∀y P(x, y)] ⇔
  ∀x∃y ¬P(x, y).
- The "incorrect quantifier order" example writes ∃x∀y: x = −y but reads it aloud with the roles of
  x and y swapped → both readings are false; the notebook uses one consistent version.
- A De Morgan example says "if not both p and p" → p and q.
- "Negation and implication are not associative or commutative" → negation is unary, so these
  properties do not apply to it at all.
- The hidden-grid example states ∃r∃c P(r, c) but negates P(c, r); its pseudo-code is
  column-major while its picture is row-major → one consistent indexing.
- The cover-letter exercise's solution names a city that is not in the problem.
- Propositions with known truth values are called "tautologies" → a tautology is true under
  every assignment of truth values.
- "Universal/existential qualifier" → quantifier.
- Speaker notes that describe a different operation (the notes for "defining ∧" describe p ∨ q;
  the notes for the De Morgan truth-table proof describe Venn diagrams).
- "Minnesota's mascot is the Badger" is used as a proposition → it is false (Golden Gopher; the
  badger is Wisconsin's); fine as an example once its truth value is stated.
- Minor: "mututal implication".

### Sets and functions (Module 03)

- **The "not a function" example evaluates 3x² + 2 at 1.5 as (1.5)² + 3 = 5.25 → 3 · 2.25 + 2 =
  8.75**, which is not an integer, so 3x² + 2 is not a function ℝ → ℤ. The same sentence omits the
  word "codomain".
- A subset table writes "S ⊂ B … every element in S is also in B" → S ⊂ T.
- Composition is defined as f ∘ g with g applied first, and then x is called "the input to f" →
  one convention, (g ∘ f)(x) = g(f(x)), with the other convention mentioned.
- Σ_{x∈S} 2^x = 8 + 16 + 36 = 56 → 8 + 16 + 32 = 56.
- The complement ~B written {−∞, …, ∞} includes ±∞, which are not integers → ℤ \ {4, 9} =
  {…, 3, 5, …, 8, 10, …}.
- A proper-superset example says "B″ ⊆ B′ but B″ ≠ B′" → B″ = B′.
- The domain of √x is written ℝ⁺ = {x | x ≥ 0}, clashing with ℤ⁺ excluding 0 → ℝ≥0 = [0, ∞).
- "Jacquard measures the correlation of two sets" → Jaccard; it measures set similarity.
- A mod-3 partition labels blocks with the wrong remainders ({1, 4, 7, 10} has remainder 1) and
  calls {odds}, {evens} "evens and odds".
- "Think of union and intersection like and (∧) and or (∨)" pairs them in reverse → ∪ ↔ ∨,
  ∩ ↔ ∧.
- The range definition is written "{y ∈ B : ∃x ∈ A …}" for f: S → T → {y ∈ T : ∃x ∈ S, f(x) = y}.
- f: S ↦ T is used throughout → strictly → goes between sets and ↦ between elements (noted, not
  treated as an error). ℕ is defined as the positive integers and ℝ as "decimal numbers"
  (conventions flagged).
- A three-tissue Venn diagram of differentially expressed genes has no citation (its counts are
  internally consistent and are used only as illustrative numbers).

### Tuples and strings (Module 04)

- The binary-number construction unions over i = 1, …, 7 while the text says i = 0, …, 7 → starting
  at 1 loses one number (254 instead of 255).
- "S⁰ = ⟨⟩" → S⁰ = {⟨⟩}, the set containing the empty tuple.
- "Fractions like ⟨2, 4⟩ and ⟨1, 4⟩ are equivalent" → ⟨2, 4⟩ ≡ ⟨1, 2⟩.
- "ℚ = ℤ × ℤ⁺" → only a representation: many pairs name the same number (lowest terms or
  equivalence classes are needed).
- Minor: "Liben-Newell" → Liben-Nowell.

### Asymptotic growth (Module 05)

- The polynomial is written p(x) = Σ aᵢxᵏ (and the Σ is missing in one version) → Σ aᵢxⁱ.
- The proof idea states "aᵢxⁱ < |aᵢ|xᵏ for any n > 1" → ≤, for x ≥ 1.
- "log x ∈ O(n^ε)" → O(x^ε).
- The 4x vs x² plot is labelled f(x)/g(x) but plots f and g.
- The alternative definitions of o and ω ("O but not Ω", "Ω but not O") are not equivalent to the
  ∀c definitions in general (counterexample: h = x² for even x, x for odd x, against g = x²); they
  agree when lim h/g exists.
- The exercise on 3x + 4y + 5xy needs a two-variable definition of O, which is not given.
- The even/odd example uses x % 2, so its domain must be ℤ≥0, not ℝ≥0.

### Graphs and trees (Module 06)

- The length of a path ⟨v₁, …, v_k⟩ is k in one version and k − 1 in another → length = number of
  edges = k − 1.
- The degree as "the number of incident edges" (an alternative definition marked for revision) →
  correct only if a self-loop counts twice.
- The neighbourhood definition lacks set braces and switches between u and v; "the in-neighbourhood
  of u … the in-neighbours of v" → of u; N_G(v) = N^in(v) ∪ N^out is missing "(v)".
- "A connected component is a subgraph that is connected" → a **maximal** connected subgraph.
- "Fully connected" in the definition of a tree → connected (not complete).
- A cycle condition "k ≥ 2" lets ⟨v₁, v₂, v₁⟩ count as a cycle (putting a cycle in every tree) →
  undirected cycles need at least 3 distinct nodes and no repeated edge.
- A ∩ B = ∅ is attached to the directed case of bipartite graphs → it is required for all
  bipartite graphs.
- "T4 is not a full k-ary tree for any m" → for any k.
- "Exigent species" → extant species.
- Spanning-tree condition "|E| = |V| − 1" → |E′| = |V| − 1 (the edges of the tree).
- The multigraph exercise cannot be answered with the |N(v)| + 𝟙 formula, because a set counts
  parallel edges once → count edge ends.
- A sentence on the factorisation of p(a, b, c) is cut off → p(a, b, c) = p(a) p(b | a) p(c | a, b).
- "The moral graph of a polytree will contain loops" → only when some node has two or more parents.

### Vectors (Module 07)

- "Fractions like ⟨2, 4⟩ and ⟨1, 4⟩ are equivalent" (recap) → ⟨2, 4⟩ ≡ ⟨1, 2⟩.
- Points vs arrows: "…but the latter is sometimes useful" → the former.
- ℝ written with subscript n → ℝⁿ.
- The ℓp norm is defined for p ∈ ℤ≥1 → any real p ≥ 1 (for p < 1 the triangle inequality fails).
- "a ≥ 0, c ≤ 0 ⇒ ac negative" → ac ≤ 0; a strict inequality needs a > 0 and c < 0.
- aₓ is called the "scalar product", which usually means the dot product (flagged as a ⚠️
  confusion).
- Minor: "they the dot product will be 0".

### Matrices (Module 08)

- **(1, 2, 3) • (7, 9, 11) = 1·7 + 2·9 + 3·11 = 5 → 58.**
- The matrix-multiplication size rule mixes letters ("rows from C, columns from D, so E is m × p")
  → one consistent naming of the factors and the product.
- Row–column rule: A ∈ ℝⁿˣᵖ, B ∈ ℝᵖˣᵐ, but cᵢⱼ = aᵢ₁b₁ⱼ + … + aᵢₙbₙⱼ → the sum runs to p, the inner
  dimension; worked examples say "1 ≤ j ≤ m" for C ∈ ℝⁿˣᵖ → 1 ≤ j ≤ p.
- Vectorisation: "M ∈ ℝⁿˣᵐ can be represented as M ∈ ℝⁿˣᵐ by stacking all n columns" →
  a vector in ℝⁿᵐ, stacking the m columns.
- The columns of an n × m matrix are named v₁ … v_p → v₁ … v_m.
- 2 × 2 determinant written "A₁₁A₂₂ − A₂₁A₂₁" → A₁₁A₂₂ − A₁₂A₂₁. Elsewhere "ad − (−b)(−c)" → present
  it as ad − bc.
- "It can also be defined for a fixed i and sum over i" (cofactor expansion) → sum over j.
- The determinant is described "with the range of all square matrices" → domain.
- The adjugate's Ã is called "the matrix of coefficients" → matrix of cofactors ("adjoint" also
  clashes with the conjugate transpose).
- "I_n is symmetric and tr(I_n)." is cut off → tr(I_n) = n.
- "There is no operation that mirrors across the anti-diagonal" is overstated → anti-symmetry
  concerns the main diagonal only.
- "The trace is distributive across sum and scalar product" → the trace is linear:
  tr(A + B) = tr A + tr B and tr(cA) = c tr A.
- E_ij = C_{i,[p]} · D_{[p],j}ᵀ → the transpose is unnecessary for a dot product of two vectors.
- Minor: row-operation rules numbered 1), 2), 2).

### Linear systems and inverses (Module 09)

- The matrix form writes the unknowns x₁ … xₙ although C is n × m → x₁ … xₘ.
- **A 3 × 5 reduction writes the x₄ coefficient in row 2 as −56/52 = −14/13 → 11 − 20 · 30/52 =
  −28/52 = −7/13**, so the parametric form reads x₂ = 2 + (7/13)s − t and the first free direction
  has entry 7/13.
- The Type III elementary matrix is named with the same letter as Type II.
- "We need the number of equations equal to (or larger than) the number of unknowns" → necessary
  for a unique solution but not sufficient (counterexample: parallel lines).
- The "−1 trick" for null spaces silently assumes the pivots are in the first columns → in general
  the −1 entries go at the free-column positions.
- A⁻¹ = Eₖ⁻¹ … E₁⁻¹ in one version and A⁻¹ = Eₖ … E₁ in another (different meanings of Eᵢ) → one
  consistent version.
- The invertible matrix theorem lists "A is invertible" among the conditions equivalent to "A is
  invertible" (circular).
- Unreduced fractions in step-by-step reductions (e.g. −48/52) → reduced (−12/13) or explained.

### Vector spaces (Module 10)

- Scalar multiplication assigns to "any a ∈ V" → a ∈ ℝ; "binary operation on v" → on V.
- For the non-standard addition ⟨a₁ + b₁, a₂ − b₂⟩, axiom 8 is listed among the satisfied axioms →
  **axiom 8 fails** ((α + β)v ≠ αv + βv in the second coordinate), and so does **axiom 3**
  (associativity), which neither version mentions. The notebook checks every axiom with code.
- Axioms 8 and 9 quantify over "v₁, v₂" but use a single v; "∃ unique 1 ∈ ℝ" (cosmetic).

### Independence, basis and rank (Module 11)

- A dependence check "(−2t, 0) + (0, −3t) + (2t, 3t) = (0, 0)" uses the reduced columns instead of
  the original vectors → (−2t, −4t) + (−6t, −3t) + (8t, 7t) = (0, 0).
- Pictures labelled "spans in ℝ²" show spans in ℝ³.
- The orthonormal-basis definition lacks i ≠ j → vᵢ · vⱼ = 0 for i ≠ j and ‖vᵢ‖ = 1.
- An alternative system for a coordinate writes "β₁/√2 − β₂/√2 = 3" → −3.
- "Matrix as transformation" multiplies a column vector by T on the right (undefined) → row form
  vT = α or column form α = Tᵀv (they coincide with Tv only because that T is symmetric).
- Rank of a product: for A ∈ ℝ^{m×n}, "B ∈ ℝ^{m×p}" → n × p; the same letter B is then reused for
  A + B with another shape → use a new letter of the same size as A.
- Scalars α₁ = … = αₙ written as a bold zero vector; "∀v ∃α" where uniqueness (∃!) is meant;
  coordinates need an *ordered* basis. Minor: "quals".

### Eigenvalues and eigenvectors (Module 12)

- **"Since x cannot be 0, A − λI must be 0" → A − λI must be singular: det(A − λI) = 0.** Also,
  for each fixed λ, (A − λI)x = 0 is a linear system in the n unknowns of x; the characteristic
  equation is the (nonlinear) equation in λ.
- In the general procedure, row 2 of A − λI is written "a₁₁, a₁₂ − λ" → a₂₁, a₂₂ − λ.
- **A column-2 cofactor expansion of det(B − λI) uses the signs +, −, + → −, +, −.** So λ³ − 7λ + 6
  is −det(B − λI); the roots are unchanged, but det(B − λI) = −λ³ + 7λ − 6.
- The λ = 1 system for B is written "x₁ − x₂ …; 4x₃ + x₂ − 5x₃" → x₂ − x₃ = 0 and
  4x₁ + x₂ − 5x₃ = 0. The eigenvectors left as an exercise are (1, 2, 1) and (1, 7, 11).
- A 4 × 4 triangular example has D₃₄ = 0 but is expanded with D₃₄ = 1 → one version used throughout
  (the eigenvalues are unaffected; with 1, the λ = 2 eigenvector would be (5, 4, 2, 2)).
- Symmetric example: "for λ₁ = 1, v₂ = …" → λ₂; a decomposition with the unnormalised
  [[1, 1], [−1, 1]] equals 2A → normalise the columns (or use XΛX⁻¹).
- The lower-triangular template starts row 2 with T₁₁ → T₂₁.
- "rank = number of non-zero eigenvalues" → true for diagonalizable matrices (counting
  multiplicity), not in general (counterexample [[0, 1], [0, 0]]).
- "λ₁ ≠ λ₂ ≠ … ≠ λₙ" does not say *pairwise* distinct; "with repeated values linear independence
  exists but…" → a full set of independent eigenvectors may or may not exist (identity vs shear).
- The definition takes λ ∈ ℝ while an example shows a rotation with complex eigenvalues → real
  matrices can have complex eigenvalues.
- Instructor note (not an error): the Leslie-type matrix [[0, 6, 8], [½, 0, 0], [0, ½, 0]] has a
  double eigenvalue −1 with one eigenvector, so it is not diagonalizable.
- Minor: "insertable" (invertible), "WOLG", "characterestic".

### Diagonalization and the SVD (Module 13)

- **"A can be factored as PDP⁻¹ iff the eigenvalues form a basis" → the eigenvectors.**
- **The SVD written R = USV with U ∈ ℝⁿˣⁿ, V ∈ ℝᵐˣᵐ → R = USVᵀ** (or say that V stands for Vᵀ);
  both conventions are explained, including NumPy's `Vh`.
- A users × movies example uses the thin SVD's shapes but calls it the full SVD; "each of the n rows
  is a movie" → columns.
- "σ₁ ≥ … ≥ σₙ ≥ 0" for Σ ∈ ℝᵐˣⁿ → there are min(m, n) singular values.
- uᵢ = Avᵢ/σᵢ "for i = 1, …, min(m, n)" → only for σᵢ > 0; the remaining uᵢ complete an orthonormal
  basis.
- U and V described as "a correlation matrix of genes / of assays" → they are eigenvector matrices
  of AAᵀ and AᵀA, which are proportional to covariance matrices only after centring.
- Minor: "Singlar", "Defintion".

### Calculus (Module 14)

- **"Only x = 3 and 1 are candidates for minima" → x = 3 and x = −1** (f″ > 0 there); x = ½ is a
  local maximum.
- **Gradient descent attributed to Cauchy in 1867 → 1847.**
- Integration-rule tables give ∫xⁿ dx = x^{n+1}/(a + 1) + c → x^{n+1}/(n + 1) + C for n ≠ −1; c is
  used both as a constant multiple and as the constant of integration.
- The discrete growth model y(x + 1) = βy(x) is solved as β^{x+1}y(0) → β^x y(0).
- The log rule mixes bases: log_c g → g′/(g ln a) → g′/(g ln c).
- d/du sec⁻¹u and csc⁻¹u need |u| in the denominator (the sign is wrong for u < −1).
- "The derivative ∫f′(x)" → the integral; dx missing in integral headings.

### Multivariable calculus and dynamics (Module 15)

- **"∇ₓ(xᵀxA) = 2Ax" → ∇ₓ(xᵀAx) = (A + Aᵀ)x**, which is 2Ax for symmetric A; "∇ₓ(bx) = b" →
  ∇ₓ(bᵀx) = b.
- The gradient of a norm printed as [∂e/∂x₁, ∂e/∂x₁] → the second entry is ∂e/∂x₂.
- The gradient is a row vector in some places and a column vector in others; δ is used for ∂ → one
  convention (column), stated.
- Least squares: b ∈ ℝⁿ → b ∈ ℝᵐ; "∄x ∈ ℝ" → x ∈ ℝⁿ; in the expansion "−2Axbᵀ" → −2xᵀAᵀb.
- Jacobian: "m, n ∈ ℝ^{≥2}" → positive integers (any m, n ≥ 1). The worked example writes the
  row vector h(x) = xᵀB diag(x) as a column → consistent column shapes; J is m × n.
- "(JᵀJ)Δx = −Jᵀr" labelled "Newton updates" → Gauss–Newton.
- **tRNA charging model: one version calls m₁ bound and m₂ unbound, the other the opposite → the
  equations only work with m₁ = unbound.**
- The discrete update m₁(t + 1) = α − βm₁ + … drops the m₁(t) term → m(t + 1) = (I + M)m(t) + c.
- dm/dt is called "J_m(t)" → a time derivative; the Jacobian of the right-hand side is M. The
  constant vector is b in one version and c in another.
- In the g(x) example, x − αf′(x) → x − αg′(x). "Only one equilibria" → exactly one equilibrium.

### Probability foundations (Module 16)

- R. A. Fisher's dates given as 1890–1929 → 1890–1962.
- Axiom 3 stated for finitely many "disjoint event spaces" → disjoint *events*; Kolmogorov's axiom
  is countable additivity.
- "P(A) = fraction of outcomes A covers" → only when outcomes are equally likely.
- Ω called the set of outcomes "of an event" → of an experiment; "a set of events is a subset of
  Ω" → an event is a subset of Ω; "event space" used both for Ω and for the collection of events.
- A complement-rule title renders as "P(A) = 1 − P(A)" (lost overbar) → P(Ā) = 1 − P(A).
- "P(A ∪ B) = P(A) + P(B) only when disjoint" → exactly when P(A ∩ B) = 0.

### Conditional probability and Bayes' rule (Module 17)

- **Spam example: P("free" ∣ ¬S)P(¬S) = 0.01 × 0.3 = 0.03 → 0.003; the posterior is ≈ 0.995.**
- **The flu/cough joint table shows P(no flu, no cough) = 0.25, so it sums to 0.9 → 0.35.**
- In the flu/cough example the prior is called "the background probability of a cough" → it is
  P(flu); likewise "susceptible to a cough, so P(A) = 0.5" refers to the flu prior.
- An A–B–C table concludes "A and B are conditionally independent" → only given C̄; given C,
  P(A ∩ B ∣ C) = 1/6 ≠ 1/4.
- "P(A ∩ B ∣ C) = ¼ = P(A ∣ C)·(B ∣ C)" is missing a P.
- Stop codons: "first codon and second codon" → first and second *positions*; the independence of
  positions 1 and 2 is trivial because position 1 is always T.
- "If we have some part of the space" → a *partition* of the space (law of total probability).
- "Independent ⇒ P(A ∣ B) = P(A)" needs P(B) > 0.

### Random variables and distributions (Module 18)

- **Bernoulli second moment written 1²P(X = 1²) + 0²P(X = 0)² → E[X²] = 1² · α + 0² · (1 − α) = α.**
- The success probability is called μ in one figure and α elsewhere → one letter per figure.
- The discrete CDF sums over outcomes {ω ∈ Ω ∣ ω ≤ x} → over values of X: F(x) = Σ_{k ≤ x} p(k).
- The exponential density written f(k) = λe^{−kλ} (a discrete-looking variable, no case x < 0) →
  f(x) = λe^{−λx} for x ≥ 0 and 0 otherwise.
- A density "sums to 1, all the probabilities are non-negative" → integrates to 1; densities are
  non-negative and are not probabilities.
- Density plots label the axes p(ω) and ω → f(x) and x. "N(μ, σ2)" → N(μ, σ²). Minor: "othwerwise".

### Joint distributions (Module 19)

- "P(A) = P(C) = P(T) = P(A) = 1/4" → P(A) = P(C) = P(G) = P(T) = 1/4.
- In the stop-codon example the joint of positions 2 and 3 is headed "positions 1, 2"; the decisive
  cell (joint P(G, G) = 0 vs product 1/9) is not shown.
- Gene-expression × disease table: the margins are swapped (row totals are P_X = 0.4/0.6, column
  totals are P_Y) and the column labels are garbled.
- **"0.25 ≠ 0.16 … hence independent" → not independent (dependent).**
- Multivariate normal: the constant 1/(√(2π)|Σ|^{1/2}) → 1/((2π)^{k/2}|Σ|^{1/2}); the left side is a
  density f(x), not P(X = x); positive definite means xᵀΣx > 0 for x ≠ 0; "Σ⁻¹ is invertible, that
  is |Σ| > 0" → Σ is invertible, and positive definiteness gives |Σ| > 0.

### Bayesian networks and Markov chains (Module 20)

- The product over in-neighbours runs from i = 0 to d for Q₁ … Q_d → from i = 1.
- In the P(T ∣ S) derivation, P(T, C, S)/P(S) = P(T ∣ C, S)P(C, S)/P(S) is labelled "Bayes" → it is
  the product rule.
- An "alternative graph layout" repeats the previous picture, so no alternative factorisation is
  shown → the notebook draws both orders.
- The background-genome case P(X₁ … X_T) = is left blank → ∏ₜ p(xₜ).
- A ratio headed "CpG" computes non-CpG/CpG; sections titled "modelling a single nucleotide" model
  sequences.
- Telephone-line chain: the distribution of X₃ is vP² because v is the distribution of X₁, while
  "three steps after a known state" uses P³ — correct but easy to misread as an off-by-one error →
  state the start of time explicitly.

### Expectation and moments (Module 21)

- **The summation property is stated "for independent variables" for both E and Var → E[ΣXᵢ] =
  ΣE[Xᵢ] always; Var(ΣXᵢ) = ΣVar Xᵢ needs uncorrelated (e.g. independent) Xᵢ.**
- Covariance derivation "E[XY] − μₓE[X] − μₓE[Y] + μₓμᵧ" → E[XY] − μᵧE[X] − μₓE[Y] + μₓμᵧ (the
  result is correct).
- E[U] for U ~ Uniform(−1, 3) integrates x/4 over (−∞, ∞) → over (−1, 3).
- "The expectation of the square is smaller than 1" → the point is E[X²] = 1/3 ≠ (E[X])² = 1/4,
  and the difference is Var X = 1/12.
- "E[X] = (1/n)Σxᵢ" → that is the sample mean, an estimate of E[X].
- The proof that Var X = 0 ⇒ X is constant skips the key step (a non-negative variable with mean
  0 is 0 with probability 1).
- Minor: two points labelled x₄ in the centre-of-gravity figure; "difference between X and E[F]"
  → F; evaluation brackets kept after evaluating; dx missing; "Cummulative".
- Not a slip: the buggy-coin variance (≈ 10.14) is correct.

### Sampling, LLN, CLT and confidence intervals (Module 22)

- **The law of large numbers written lim P(X̄ₙ = μ) → 1 → P(|X̄ₙ − μ| < ε) → 1 for every ε > 0.**
- **The CLT written X̄ₙ ≈ N(μ, σ/√n) and "lim X̄ₙ ~ N(μ, σ/√n)" → N(μ, σ²/n) in the course's
  (mean, variance) notation, and a limit cannot depend on n: Zₙ = (X̄ₙ − μ)/(σ/√n) → N(0, 1).** The
  same issue appears in a recap (Sₙ ≈ N(nμ, √n σ) → N(nμ, nσ²)).
- **A grid of 100 coin flips has 52 heads and 48 tails but is labelled X̄ = 48/100 with heads coded
  1 → 0.52.**
- "Statistical Interference" → Statistical Inference.

### Maximum likelihood (Module 23)

- The probability of a *specific* sequence with 4 heads in 10 is written C(10, 4)p⁴(1 − p)⁶ →
  p⁴(1 − p)⁶; the binomial coefficient belongs to "4 heads in any order" (the maximiser is the
  same).
- "It looks like the coin is not fair" after 4 heads in 10 is not justified (L(0.4)/L(0.5) = 1.22;
  P(≤ 4 heads ∣ fair) = 0.377; the Wald interval [0.096, 0.704] contains 0.5).
- "If there is no critical point, use the maximum allowable parameter value" → the maximum is on
  the boundary towards which the likelihood increases (for Uniform(0, θ), the smallest allowed
  value, max xᵢ).
- "p(θ) is typically uniform" → maximum likelihood ignores the prior (equivalently, treats it as
  flat).
- The Bernoulli product is indexed from i = 0 → i = 1. The log rule should read
  d/dx [a ln f(x)] = a f′(x)/f(x).
- Normal MLE: x written for xᵢ inside the sums; the μ-derivative step is headed "with respect to
  σ"; θ = {μ, σ} and {μ, σ²} are mixed (harmless).

### Bayesian estimation and MAP (Module 24)

- **"A drawer containing 5 coins: 5 of type A, 3 of type B, 2 of type C" → 10 coins.**
- **The coin-drawer posteriors after one tails, 0.510 / 0.490 / 0.041 → 0.641 / 0.308 / 0.051.**
- "P(D ∣ H) is the data distribution" in Bayes' rule → the evidence is P(D).
- Beta density: (1 − x)^{α_F} → (1 − x)^{α_F − 1}; B(α_S, α_F) written Γ(α_S, α_F)/(Γ(α_S)Γ(α_F)) →
  Γ(α_S)Γ(α_F)/Γ(α_S + α_F); the posterior has (1 − p)^{α_T0} missing the −1.
- "If we model the posterior as a Beta" → the **prior** is modelled as a Beta; "find the prior,
  p(θ ∣ D)" → p(θ ∣ D) is the **posterior**.
- **Unknown-prior MAP derivation: "d/dp log P(D ∣ p) · log P(p)" → +; the expansion
  pα_T − pα_T0 − p → pα_T + pα_T0 − p; the final denominator has −α_T0 → +α_T0.**
- The Beta mode is missing parentheses → (α − 1)/((α − 1) + (β − 1)).
- The pseudocount formula labelled as an MLE is the posterior *mean* under Beta(c_H0, c_T0); the
  MAP corresponds to pseudocounts one smaller.
- Discrete-prior example: p(0.7 ∣ x) written as L(x ∣ 0.7) · p(0.5) = 0.2² · 0.8³ · 0.89 → each
  likelihood θ²(1 − θ)³ times its own prior, 0.7² · 0.3³ · 0.89 = 0.0118; the values are
  unnormalised but called posteriors (normalised: 0.145 / 0.022 / 0.833; MAP θ = 0.7); the example
  is titled "conjugate priors" although the prior is discrete.
- Gamma–Poisson: e^{−α/θ} → e^{−x/θ}; the scale symbol changes from θ to ε; k is used both for the
  count and for the shape → λ_MAP = (k − 1 + Σxᵢ)/(n + 1/θ), posterior Gamma(k + Σxᵢ, rate n + 1/θ).
- Normal–normal: "σ²_MAP = 1/(1/σ² + 1/σ₀²)" → that is the posterior variance of μ, not an estimate
  of σ² (which is known in this model).
- Exponential-family form of the normal: B(θ) = μ²/(2σ²) + log σ; η and T are vectors for the
  normal, which a one-parameter definition does not cover.

### Hypothesis testing (Module 25)

- Type I and II error rates written as joint probabilities P(reject H₀, H₀ true) → conditional:
  P(reject H₀ ∣ H₀ true).
- "As μ* and μ₀ move apart both errors go down" → with a fixed cut-off, α does not change; only β
  falls.
- **The p-value written P(|T| > (X̄ − μ₀)/(σ/√n)) → P(|Z| ≥ |z_obs|): the absolute value of the
  observed statistic.**
- "Significance level β" → α (β is the Type II error rate); "we accept or reject H₀" → retain or
  reject; the p-value evidence table is a rule of thumb for reading p, not a rule for choosing α.
- X̄ₙ ~ N(x, σ²/n) → N(μ₀, σ²/n) under H₀. The paired statistic (δ̄ − μ₀)/(s_δ/√n) → δ̄ − 0 under
  H₀: δ = 0.
- A one-tailed t table is used without saying to double the tail probability for a two-sided test.
- A one-sided error figure's legend does not match its curve colours. Cholesterol in "210 ml" →
  mg/dL.

### Categorical tests and multiple testing (Module 26)

- **χ² statistic with ṗᵢ in the denominator → Σ (Oᵢ − nṗᵢ)²/(nṗᵢ): the denominator is the expected
  count** (as written, Mendel's value becomes 556 × 0.47 = 261.3).
- **Mendel's p-value given as 0.9524 → ≈ 0.925 (X² ≈ 0.470 with 3 df).**
- Hypotheses written in terms of the observed proportions, and n used both for the number of
  categories and for the sample size → H₀ concerns the true category probabilities; k categories,
  n observations, df = k − 1.
- A χ² density figure is not normalised (e.g. the χ²₂ density at 0 should be 0.5, drawn ≈ 0.17) →
  the notebook draws exact densities.

### Linear regression (Module 27)

- **β̂ = Xᵀy(XᵀX)⁻¹ → (XᵀX)⁻¹Xᵀy** (the written product is undefined).
- **Gaussian constants: 1/(σ²√(2π)) → 1/(σ√(2π)); exp(−(·)²/(2σ)) → exp(−(·)²/(2σ²))**; the
  −(n/2) ln 2π term is dropped silently.
- "y = xᵀβ_s + β₀" is shape-inconsistent → y = β_s · x + β₀.
- "(Y − Xβ)²" and "Y²" for squared norms → ‖y − Xβ‖² = (y − Xβ)ᵀ(y − Xβ) and yᵀy. A stray β² in
  "d/dβ βᵀXᵀXβ²".
- The β derivation stops at "= …" → completed in full in the notebook.
- A cross-reference to other material by its number → refer to topics by content. Minor: "genets".

Notebook authors add further slips here as they find them, phrased by content, with every number
recomputed with code.

---

## Maintenance

- **Developed with** Python 3.13, NumPy 2.5, SciPy 1.18, pandas 3.0, Matplotlib 3.11, SymPy 1.14
  and NetworkX 3.7 on a CPU. Each notebook runs top to bottom in 3–10 s on a laptop CPU (somewhat
  longer on a free Colab CPU); executing all 29 takes about three minutes.
- **Structure check:** `python validate_notebooks.py` checks the notebook schema; that there are 29
  notebooks numbered 00–28; the header (Colab badge pointing to the notebook itself, the
  key-information table with "02-680 topics covered", the educational-use disclaimer); the required
  sections (objectives, contents, biological question, setup, key takeaways, checkpoint, questions,
  bonus, lab note, references, next) and the link to the next module; 📘 *Lecture notes* boxes in
  Modules 00–27 and 🌉 *Bridge* boxes and at least five "*In words:*" readings in Modules 02–27; that
  outputs are stripped; that every relative link resolves; that every toolkit copy is identical to
  `course_toolkit.py`; that a global `SEED` exists; and that nothing points to the 02-680 teaching
  material or to the numbering of its lectures, topics or notes, embeds or links a picture, or reads
  or downloads data. It also rejects stored data or picture files and files over 400 kB, and checks the links of
  the five companion documents. `--only 07 08` checks single modules while they are being written;
  `--execute` also runs every notebook.
- **Editing a notebook:** edit, run it top to bottom, check that every 🔍 paragraph and checkpoint
  answer still quotes the actual outputs (the simulations are seeded), then clear the outputs before
  committing (`jupyter nbconvert --clear-output --inplace notebooks/NN_*.ipynb`).
- **Changing a shared helper:** edit `course_toolkit.py`, then replace the definition in the
  🧰 toolkit cell of every notebook that uses it — the validator lists each stale copy. The toolkit
  cell's header names the toolkit version ("identical to ../course_toolkit.py v1.0"); if you bump
  `__version__`, update those headers too. Changing a simulator changes the numbers in every notebook
  that uses it (see the module lists in [`DATA.md`](DATA.md)); re-check their narratives.
- **When 02-680 is reorganised:** update the topic map above and the topic table in the README. The
  notebooks name topics by content and need no change; if a new topic appears, add a module or a
  section and a row here.
- **Errata:** record new slips in the table above, phrased by content, never by the source's
  numbering.
- **Data policy:** no data files, no pictures, no downloads (see [`DATA.md`](DATA.md)).
