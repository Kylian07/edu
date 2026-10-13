# Getting started: zero-to-one guide for the notebooks

This page assumes you know basic cell biology and can use a web browser, but have never programmed. Start with [lesson 00](tutorial/biology_first/00_cell_to_structure.ipynb). Every lesson is a Jupyter notebook: a page made of explanatory text cells and code cells. Code cells run in order and can use variables made by earlier cells.

## Open and run

1. In the repository, open a `.ipynb` file. To run it, use the **Open in Colab** option if available, or in [Google Colab](https://colab.research.google.com/) choose **File → Open notebook → GitHub**, enter `xulabs/edu`, and select `cryoem/tutorial/biology_first/00_cell_to_structure.ipynb`. The raw files can also be uploaded through Colab's file menu.
2. Choose **Runtime → Run all**. A free CPU runtime is enough. If the runtime asks to connect, connect it. No GPU, login to a scientific archive, or large download is required for these lessons.
3. Read the first code cell. It imports NumPy and sets `SEED = 7`, which makes random examples reproducible. Colab normally includes NumPy; if an import fails in another environment, run `%pip install numpy` in a new code cell and restart the runtime.
4. Change the parameter named in **Change one thing**, run that cell again, and compare the output with your prediction. You can reset by choosing **Runtime → Restart and run all**.

## Six Python ideas used repeatedly

| Syntax | Meaning | Example |
|---|---|---|
| `name = value` | Store a value under a name. | `pixel_size_A = 4.0` |
| `np.array([...])` | Make an array of numbers. | `np.array([1, 2, 3])` |
| `array.shape` | See its dimensions. | `(64, 64, 64)` is a 3D volume. |
| `array.mean()` | Average values. | A simple summary, not a proof of structure. |
| `for n in [1,4,16]:` | Repeat code for each choice. | Compare different averaging counts. |
| `assert condition` | Check an expected result. | Stops if the condition is false. |

A line beginning with `#` is an explanation for a human and is not executed. Indented lines belong to a loop or function. Scientific notation such as `1e-3` means `0.001`. NumPy arrays often use `volume[z, y, x]`; a paper may describe physical coordinates as x, y, z. Always write down the convention.

## If something goes wrong

- **`NameError`:** an earlier code cell was not run. Run from the top.
- **`ModuleNotFoundError`:** install the named package as instructed above, then restart.
- **The numbers differ a little:** check whether you changed the seed or the parameter; random examples can fluctuate.
- **The output contradicts your prediction:** keep both! Explain which assumption in your prediction was wrong.
- **The code prints a scientifically odd result:** the toy model may have deliberately omitted real-world effects. Read the “Interpret” section and identify what is missing before changing code.

## Four-line lab note

For each lesson, write this in a notebook or text file:

```text
Lesson and date:
Input: what data or synthetic object was used?
Output: what number, image, or map was produced?
Assumption: what did the toy model simplify?
Failure mode: when would the method mislead a biologist?
```

Do not worry about memorizing code syntax. The purpose is to connect the biological question, measurement, method, and evidence. When a paper uses a new acronym, first classify it as an experiment, data object, algorithm, or evaluation metric. The [research bridge](research_bridge.md) then gives the deeper explanation.
