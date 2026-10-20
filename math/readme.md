# Mathematics and Statistics Foundations

Welcome to the **Mathematics and Statistics Foundations** educational track (companion to CMU 02-680 *Essential Mathematics and Statistics for Scientists*). This track builds the mathematical language that computational biology, machine learning and structural biology are written in — logic, sets and graphs, linear algebra, calculus, probability and statistics — with every idea connected to a biological question.

**New to mathematics and programming?** Start with **[From Biology to Mathematics](tutorial/BiologyToMath/README.md)** — a 29-module self-study course written for first-year biology majors (high-school algebra assumed; no programming, linear algebra, probability or statistics). Modules 00–01 teach mathematical notation, LaTeX and Python as a mathematical laboratory; Modules 02–27 teach every 02-680 topic completely inside the notebooks — definitions, theorems with proofs, the classic worked examples, re-drawn figures and common misconceptions — each with biological bridges (gene-regulation logic, sequence spaces, phylogenies, expression matrices, Leslie population models, tRNA and epidemic dynamics, Mendel's and Hardy–Weinberg tests, CpG-island Markov chains, maximum-likelihood allele frequencies, genome-wide multiple testing, regression); a capstone (28) takes one biological question to a quantitative answer with the tools of the whole course. All data are simulated or short classic tables typed in by hand, and all figures are drawn by code.

---

## Contents

| Topic / Subfolder | Core Description | Notebooks |
|-------------------|------------------|-----------|
| [`BiologyToMath`](tutorial/BiologyToMath/) | Complete 29-module course for biology majors. Getting started (00–01): why biology needs mathematics, reading and writing notation, Python/NumPy/SymPy. Foundations (02–06): propositional and predicate logic, sets and functions, tuples and strings, asymptotic growth, graphs and trees. Linear algebra (07–13): vectors, matrices and determinants, linear systems and inverses, vector spaces, independence/basis/rank, eigenvalues and eigenvectors, diagonalization and the SVD. Calculus (14–15): derivatives and integrals, gradients, least squares, Jacobians, equilibria and stability. Probability (16–20): axioms, conditional probability and Bayes' rule, random variables and distributions, joint distributions, Bayesian networks and Markov chains. Statistics (21–27): expectation and moments, LLN/CLT and confidence intervals, maximum likelihood, MAP with conjugate priors, hypothesis testing and power, χ² tests and false-discovery control, linear regression. Capstone (28). Simulated data only; study guide, glossary, data guide and instructor guide | `notebooks/00_welcome_math_for_biology.ipynb` … `notebooks/28_capstone.ipynb` (29 notebooks) |

---

## Where to go next

- **[From Biology to Machine Learning](../ml/tutorial/BiologyToML/README.md)** (CMU 02-620) builds directly on this track: MLE/MAP, regression, PCA, Bayesian networks, HMMs and beyond.
- **[Cryo-EM for Computer Scientists](../cryoem/tutorial/foundation/readme.md)** uses the linear algebra, optimisation and probability developed here.

---

## Further Reading

- Liben-Nowell, D. (2022). *Connecting Discrete Mathematics and Computer Science*. Cambridge University Press.
- Deisenroth, M. P., Faisal, A. A. & Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press.
- Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.). Wellesley-Cambridge Press.
- Betti, M. *Mathematics and Statistics for the Quantitative Sciences*.
- Wasserman, L. (2004). *All of Statistics*. Springer.
- DeGroot, M. H. & Schervish, M. J. (2012). *Probability and Statistics* (4th ed.). Pearson.
- Durbin, R., Eddy, S., Krogh, A. & Mitchison, G. (1998). *Biological Sequence Analysis*. Cambridge University Press.
