"""Core Fibonacci functions."""


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""

    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def fibonacci_mod(n: int, m: int = 1_000_000_000) -> int:
    """Return the nth Fibonacci number modulo m.

    Uses the fast doubling algorithm, allowing very large
    values of n such as 10**18.
    """

    if n < 0:
        raise ValueError("n must be non-negative")

    if m <= 0:
        raise ValueError("m must be positive")

    def fast_doubling(k: int) -> tuple[int, int]:
        """Return (F(k) mod m, F(k+1) mod m)."""

        if k == 0:
            return 0, 1

        a, b = fast_doubling(k // 2)

        c = (a * ((2 * b - a) % m)) % m
        d = (a * a + b * b) % m

        if k % 2 == 0:
            return c, d

        return d, (c + d) % m

    return fast_doubling(n)[0]
