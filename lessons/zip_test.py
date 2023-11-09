"""Unit test for zip."""

__author__ = 730555961

from lessons.zip import zip


def test_zip_length_1() -> None:
    """Testing combining a list[str] and a list[int] into a dict of length 1."""
    test_strlist: list[str] = ["chocolate"]
    test_intlist: list[int] = [1]
    assert zip(test_strlist, test_intlist) == {"chocolate": 1}


def test_zip_length_3() -> None:
    """Testing combining two lists of length 3 each."""
    test_strlist: list[str] = ["chocolate", "vanilla", "rocky road"]
    test_intlist: list[int] = [5, 1, 3000]
    assert zip(test_strlist, test_intlist) == {"chocolate": 5, "vanilla": 1, "rocky road": 3000}


def test_zip_unequal_length() -> None:
    """Testing combining two lists of different lengths."""
    test_strlist: list[str] = ["chocolate"]
    test_intlist: list[int] = []
    assert zip(test_strlist, test_intlist) == {}
