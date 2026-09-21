import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return


@app.function
def fibonacci(n:int)->int:
    pass


@app.cell
def test_fib1():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    return


@app.cell
def test_fib2():
    assert fibonacci(2) == 1

    return


if __name__ == "__main__":
    app.run()
