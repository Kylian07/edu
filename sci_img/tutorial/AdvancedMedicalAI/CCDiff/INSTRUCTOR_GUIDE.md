# Instructor guide — CCDiff undergraduate tutorial sequence

## Learning design

The student is a first-year biology major. Teach data and experiment design before machine learning; teach vectors and correlation before CCA; teach the difference between an embedding similarity and a fact; and *always* pair reported improvements with limitations and controls.

Each tutorial is built from seven recurring sections: biology-first question, technical explanation, runnable guided example, extension, independent experiment, formative questions, and connection to the paper. The lesson exercises generally fit one 90-minute supervised lab plus two hours of independent work. Additional time in long weeks should be devoted to reading, mathematical practice, and interpretation, not training large models.

## Recommended assessment calendar

| Week | Checkpoint | Minimum criterion |
|---:|---|---|
| 4 | Morphology data mini-report | Correct sample unit; labeled plot; acquisition confound identified |
| 10 | Mathematical skills assessment | Explain shapes, projections, cosine, covariance, PCA versus CCA |
| 15 | Multimodal embedding lab | Compute and interpret an image-by-text similarity matrix |
| 21 | Canonical-correlation oral exercise | Write CCA objective; show pairing dependence; explain low-rho heuristic |
| 26 | End-to-end CCDiff-style demonstration | Inspect code/array shapes; produce two directional rankings; use null control |
| 30 | Capstone paper defense | Interpret the paper, reproductions, limitations, and independent experiment |

## Formative grading rubric (100 points)

- 20: Biological question, sampling units, and possible confounds.
- 20: Mathematics and correct data shapes (including CCA/cosine distinctions).
- 25: Executable, understandable, well-labeled code and numeric results.
- 20: Baselines and experiments challenging the method's assumptions.
- 15: Clear claims, source attribution, and appropriate limitations.

## Frequent misunderstandings to correct

**“Inverse CCA minimizes correlation.”** More precisely, the paper fits CCA and sorts the resulting canonical components by ascending absolute correlation. This ranking is not a theoretical guarantee that a concept is absent from the other set.

**“Anticorrelation means low correlation.”** A Pearson correlation of -0.95 indicates *strong negative association*. The paper uses `1 - |rho|`, giving that direction a low inverse-correlation score. The manuscript occasionally uses 'anti-correlated' informally to describe low-correlation directions; teach the mathematics explicitly.

**“CLIP similarity is proof of biology.”** It is a learned representation and may be affected by acquisition details, out-of-domain imagery, and pretrained biases.

**“Repeated candidate text vectors are independent paired observations.”** They are not: modulo pairing creates repeated text rows. The statistical validity of resulting CCA directions demands scrutiny.

**“No LLM tokens at all.”** The manuscript's zero-token comparison specifically applies to the core discovery pipeline. Caption generation and GPT-based semantic evaluation are distinct.

**“Synthetic demonstration equals benchmark reproduction.”** It does not. The teaching package purposely does not include heavyweight model checkpoints, hidden prompts, or credentialed medical data.

## Independent research project suggestion

Start from two synthetically simulated cell-image sets, one round and one elongated, with equal background distributions. Then create an intentionally confounded acquisition batch with brighter exposure. Compare (a) direct measured aspect-ratio differences, (b) average text-image cosine difference, and (c) CCDiff-style ranking with a fixed conceptual bank. Include a null experiment comparing the same set to itself and 20 shuffled pairings. Report false-positive descriptions, stability, limitations and possible improvements.

## Final oral questions

1. In the paper, what exactly is paired with what to discover concepts for set A relative to B?
2. Explain why an uncorrelated projection is not sufficient evidence for a useful natural-language difference.
3. What changes when the concept bank omits the true property?
4. Why might CCA correlation be unstable when embedding dimension is high and the candidate pool is small?
5. What does the alpha-weighted score capture, and what does it *not* mean?
6. Why does the same clinical image set require special handling compared with everyday images?
7. Which result supports the paper's computational efficiency claim, and which steps remain excluded from the token accounting?
8. Design a null experiment capable of falsifying a claimed set-specific phrase.

## Key source sections

- Source manuscript Introduction: pp. 1–2.
- Overview and examples: Figure 1 and Figure 2, p. 3.
- Section 3 and Algorithm 1: pp. 4–6.
- Main benchmark comparisons and settings: Tables 1–2, pp. 7–8.
- CCA background: Appendix A.1, p. 16.
- Candidate quality and ablations: Appendices D–E, pp. 19–20.
- MIMIC-CXR evaluation: Section 4.5 and Appendix G, pp. 8 and 21–25.
- Limitations and broader impact: Section 5, p. 9; Appendix L, p. 28.

The manuscript itself is not included in this package because it was supplied separately by the user and may have sharing restrictions.
