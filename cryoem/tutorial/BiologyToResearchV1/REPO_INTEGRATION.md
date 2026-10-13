# Integrating into xulabs/edu

This archive contains **only a new, non-destructive `cryoem/tutorial/BiologyToResearch/` directory**. Copy the folder into a checkout of the `main` branch without replacing existing notebooks.

Suggested addition to the *existing* root `README.md` under Curriculums & Quick Links:

```markdown
- [Biology-to-CryoEM Research Curriculum](cryoem/tutorial/BiologyToResearch/README.md)  
  26 scaffolded Colab notebooks for first-year biology majors, spanning molecular biology, image physics, alignment, classification, segmentation, self-supervision and the Xu Lab publication literature.
```

Suggested addition to `cryoem/readme.md` near the top:

```markdown
> New to cryo-ET from biology? Start with the [Biology-to-CryoEM Research Curriculum](tutorial/BiologyToResearch/README.md) before the specialist modules below.
```

Do not overwrite the existing notebook series. Verify the live main branch because GitHub public views may lag or show incomplete trees. Put this on a feature branch, run `python cryoem/tutorial/BiologyToResearch/validate_notebooks.py` and review the rendered Markdown/notebooks before merging.
