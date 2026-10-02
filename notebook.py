import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return


@app.function
def fibonacci(n:int):
    if n <= 1:
        return n

    a , b = 0 , 1
    
    for _ in range(2,n + 1):
        a , b = b , a + b
    
    return b


@app.cell
def test_fib1():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    return


@app.cell
def test_fib2():
    assert fibonacci(2) == 1
    return


@app.function
def test_fibonacci_large():
    result = fibonacci(10_000_000)
    assert result > 0


@app.function
def fibonacci_mod(n: int, m: int = 1_000_000_000):
    if n < 0:
        raise ValueError("n must be non-negative")

    if m <= 0:
        raise ValueError("m must be positive")

    def fast_doubling(k: int):
        if k == 0:
            return 0, 1

        a, b = fast_doubling(k // 2)

        c = (a * ((2 * b - a) % m)) % m
        d = (a * a + b * b) % m

        if k % 2 == 0:
            return c, d

        return d, (c + d) % m

    return fast_doubling(n)[0]


@app.cell
def test_fibonacci_mod_base_cases():
    assert fibonacci_mod(0) == 0
    assert fibonacci_mod(1) == 1
    assert fibonacci_mod(2) == 1
    return


@app.cell
def test_fibonacci_mod_small_values():
    assert fibonacci_mod(5) == 5
    assert fibonacci_mod(10) == 55
    assert fibonacci_mod(20) == 6765

    return


@app.cell
def test_fibonacci_mod_large_n():
    m = 1_000_000_000
    result = fibonacci_mod(10**18, m)

    assert result == 560546875
    
    return


if __name__ == "__main__":
    app.run()
