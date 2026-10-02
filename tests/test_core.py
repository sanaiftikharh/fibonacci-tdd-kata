import pytest

from fibonacci_kata.core import fibonacci, fibonacci_mod


def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_small_values():
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_rejects_negative_n():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_mod_base_cases():
    assert fibonacci_mod(0) == 0
    assert fibonacci_mod(1) == 1
    assert fibonacci_mod(2) == 1


def test_fibonacci_mod_small_values():
    assert fibonacci_mod(5) == 5
    assert fibonacci_mod(10) == 55
    assert fibonacci_mod(20) == 6765


def test_fibonacci_mod_range():
    m = 1_000_000_000

    result = fibonacci_mod(100, m)

    assert 0 <= result < m


def test_fibonacci_mod_large_n():
    m = 1_000_000_000

    result = fibonacci_mod(10**18, m)

    assert result == 560546875


def test_fibonacci_mod_rejects_negative_n():
    with pytest.raises(ValueError):
        fibonacci_mod(-1)


def test_fibonacci_mod_rejects_invalid_modulus():
    with pytest.raises(ValueError):
        fibonacci_mod(10, 0)
