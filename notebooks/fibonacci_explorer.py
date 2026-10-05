
import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci

    return mo, plt, fibonacci


@app.cell
def _(mo):
    mo.md(r"""
    # Fibonacci Explorer

    Pick a range of Fibonacci indices and explore the corresponding
    Fibonacci numbers interactively. The values are displayed as a
    list and visualized as a chart.

    This notebook consumes the installed `fibonacci_kata` package —
    it does not reimplement the Fibonacci function.
    """)
    return


@app.cell
def _(mo):
    start = mo.ui.slider(
        0,
        30,
        value=0,
        label="Range start",
    )

    end = mo.ui.slider(
        0,
        30,
        value=10,
        label="Range end",
    )

    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, fibonacci, start):
    lo, hi = sorted((start.value, end.value))

    indices = list(range(lo, hi + 1))
    results = [fibonacci(n) for n in indices]
    return indices, results


@app.cell
def _(indices, mo, results):
    mo.md(f"""
    ### Results

    **Indices:** `{indices[0]} → {indices[-1]}`

    **Fibonacci values:**

    `{results}`
    """)
    return


@app.cell
def _(indices, plt, results):
    fig, ax = plt.subplots()

    ax.bar(indices, results)

    ax.set_xlabel("Fibonacci index")
    ax.set_ylabel("Fibonacci value")
    ax.set_title("Fibonacci numbers over the selected range")

    fig
    return


if __name__ == "__main__":
    app.run()
