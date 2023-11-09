"""Challenge question in class 10/17."""

__author__ = 730555961


def w_sum(vals: list[float]) -> float:
    """Sums list values using while loop."""
    i: int = 0
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums list values using for loop."""
    sum: float = 0
    for elem in vals:
        sum = elem + sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums list values using for loop with range function."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum