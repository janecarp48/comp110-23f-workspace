"""Practice with Dictionaries."""

ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry":5}

ice_cream["mint"] = 3

ice_cream.pop("mint")

print(ice_cream["chocolate"])

ice_cream["vanilla"] = 10

print(ice_cream)

ef zip(strlist: list[str], intlist: list[int]) -> dict[str,list]:
    """Returns a dict given two lists."""
    newdict: dict[str, int] = {}
    i: int = 0
    if len(strlist) == len(intlist):
        for str in strlist:
            newdict[str] = [intlist[i]]
            i = i + 1
    return newdict