"""Combining two lists into a dictionary."""

__author__ = 730555961


def zip(strlist: list[str], intlist: list[int]) -> dict[str, int]:
    """Returns a dict given two lists."""
    newdict: dict[str, int] = {}
    i: int = 0
    if len(strlist) == len(intlist):
        for str in strlist:
            newdict[str] = int(intlist[i])
            i = i + 1
    return newdict

def zip1(strlist: list[str], intlist: list[int]) -> dict[str, int]:
    """Returns a dict given two lists."""
    newdict: dict[str, int] = {}
    if len(strlist) == len(intlist):
        for elem in range(0, len(strlist)):
            newdict[strlist[elem]] = int(intlist[elem])
    return newdict
