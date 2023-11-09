"""Testing my summation function."""

from lessons.sum_evens import sum_evens

def test_empty_sum() -> None:
    """Testing the empty case, should be zero."""
    assert sum_evens([]) == 0

def test_list_length_1() -> None:
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sum_evens([test_list]) == 2

def test_list_positives() -> None:
    """Summing list of positive integers."""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens([test_list]) == 6 

def test_list_negative() -> None:
    """Summing list of positive and negative integers."""
    test_list: list[int] = [1, 2, 3, -4]
    assert sum_evens([test_list]) == -2