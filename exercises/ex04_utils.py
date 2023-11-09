"""Exercicse 04 for COMP110 Whoohoo."""

__author__ = 730555961


def all(input_list: list[int], input_int: int) -> bool:
    """Returns a bool indicating whether or not int matches all of ints in the list."""
    i: int = 0
    int_matches: bool = True
    if input_list == []:
        int_matches = False
    while i < len(input_list):
        if input_int != input_list[i]:
            int_matches = False
        i = i + 1
    return int_matches


def max(input_list: list[int]) -> int:
    """Returns maximum int given a list of int."""
    i: int = 0
    max_list_number = input_list[i]
    if len(input_list) == 0:
        raise ValueError("max() arg is an an empty List")
    while i < len(input_list):
        if input_list[i] > max_list_number:
            max_list_number = input_list[i]
        i += 1
    return max_list_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns whether or not the elements of two lists match each other."""
    lists_match: bool = True
    i: int = 0
    if len(list1) != len(list2):
        lists_match = False
        return lists_match
    if list1 == [] or list2 == []:
        lists_match = False
    if list1 == [] and list2 == []:
        lists_match = True
    while i < len(list1):
        if list1[i] != list2[i]:
            lists_match = False
        i += 1
    return lists_match
