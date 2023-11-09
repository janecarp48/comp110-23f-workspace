"""Ex 07 dictionary unit tests."""

__author__ = 730555961

import pytest

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_length_1() -> None:
    """Inverts a dictionary's keys and values with a dict length of one."""
    assert invert({"example": "dict"}) == {"dict": "example"}


def test_invert_length_3() -> None:
    """Inverts a dictionary's keys and values with a dict length of three."""
    assert invert({"even": "longer", "more": "annoying", "dict": "ionary"}) == {"longer": "even", "annoying": "more", "ionary": "dict"}


def test_invert_edge_case() -> None:
    """Raises a KeyError when the invert function is asked to create a dict with two of the same keys."""
    with pytest.raises(KeyError):
        example: dict[str, str] = {"maybe": "nope", "really": "nope"}
        invert(example)


def test_favorite_color_length_3() -> None:
    """Returns the favorite color of the favorite color function with a dict length of three."""
    assert favorite_color({"Alyssa": "purple", "Staub": "pink", "Steiner": "pink"}) == "pink"


def test_favorite_color_length_5() -> None:
    """Returns the favorite color of the favorite color function with a dict length of five."""
    assert favorite_color({"Alyssa": "purple", "Staub": "pink", "Steiner": "blue", "Osterweil": "green", "Rosa": "purple"}) == "purple"


def test_favorite_color_tie() -> None:
    """Returns the first of two tied favorite colors in a dict."""
    assert favorite_color({"Max": "lavender", "Lorelai": "blue", "Rory": "blue", "Luke": "lavender"}) == "lavender"


def test_count_length_3() -> None:
    """Returns the counts of the given list values of a length three in a dict."""
    assert count(["Hello", "World!", "Hello"]) == {"Hello": 2, "World!": 1}


def test_count_length_5() -> None:
    """Returns the counts of the given list values of a length five in a dict."""
    assert count(["Pig", "Chicken", "Horse", "Cow", "Horse"]) == {"Pig": 1, "Chicken": 1, "Horse": 2, "Cow": 1}


def test_count_length_0() -> None:
    """Returns an empty dict when given a list with no unique values to count."""
    assert count([]) == {}


def test_alphabetizer_length_3() -> None:
    """Returns a dict with first letters and corresponding words in an input list of three."""
    assert alphabetizer(["corn", "on", "cob"]) == {"c": ["corn", "cob"], "o": ["on"]}


def test_alphabetizer_length_5() -> None:
    """Returns a dict with first letters and corresponding words in an input list of five."""
    assert alphabetizer(["in", "the", "jungle", "mighty", "jabba"]) == {"i": ["in"], "t": ["the"], "j": ["jungle", "jabba"], "m": ["mighty"]}


def test_alphabetizer_capitals() -> None:
    """Returns a dict with first letters and corresponding words even when there are upper and lowercase letters."""
    assert alphabetizer(["The", "hehe", "thought", "Howl", "alleluia"]) == {"t": ["The", "thought"], "h": ["hehe", "Howl"], "a": ["alleluia"]}


def test_update_attendance_new_day() -> None:
    """Returns mutated attendance log with one new name for a new day."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Alyssa", "Xiuping"], "Tuesday": ["Ella"]}
    assert update_attendance(attendance_log, "Wednesday", "Ella") == {"Monday": ["Alyssa", "Xiuping"], "Tuesday": ["Ella"], "Wednesday": ["Ella"]}


def test_update_attendance_same_day() -> None:
    """Returns mutated attendance log with one new name for an existing day."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Alyssa", "Xiuping"], "Tuesday": ["Ella"]}
    assert update_attendance(attendance_log, "Tuesday", "Sam") == {"Monday": ["Alyssa", "Xiuping"], "Tuesday": ["Ella", "Sam"]}


def test_update_attendance_everyone_absent() -> None:
    """Returns mutated attendance log when no one shows up."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Alyssa", "Xiuping"], "Tuesday": ["Ella"]}
    assert update_attendance(attendance_log, "Wednesday", "") == {"Monday": ["Alyssa", "Xiuping"], "Tuesday": ["Ella"], "Wednesday": [""]}