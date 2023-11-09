"""Exercise 06, dictionary functions."""

__author__ = 730555961


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the given dictionary."""
    new_dict: dict[str, str] = {}
    for key in input:
        new_dict[input[key]] = key
    if len(new_dict) != len(input):
        raise KeyError
    return new_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns the most popular favorite color given a list of names and favorite colors."""
    values: list[str] = list(input.values())
    counts: list[int] = list()
    for color in values:
        count = 0
        for i in range(len(values)):
            if color == values[i]:
                count += 1
        counts.append(count)
    idx: int = 0
    max = counts[idx]
    for i in range(len(counts) - 1):
        if max < counts[i + 1]:
            max = counts[i + 1]
    if max == counts[0] and max == counts[1]:
        return values[0]
    else:
        return values[counts.index(max)]


def count(input: list[str]) -> dict[str, int]:
    """Return a dictionary of how many times a certain list value appeared in the input."""
    new_dict: dict[str, int] = {}
    for idx in range(0, len(input)):
        if input[idx] in new_dict:
            new_dict[input[idx]] += 1
        if input[idx] not in new_dict: 
            new_dict[input[idx]] = 1
    return new_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Produces a dict with the count of words in a list that begin with a specific letter."""
    new_dict: dict[str, list[str]] = {}
    for idx in range(0, len(input)):
        if input[idx][0].lower() in new_dict:
            new_dict[input[idx][0].lower()] += [input[idx]]
        if input[idx][0].lower() not in new_dict:
            new_dict[input[idx][0].lower()] = [input[idx]]
    return new_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Modifies the attendance log given to add the students who were there on each day of the week."""
    if day not in attendance:
        attendance[day] = [student]
        return attendance
    if day in attendance:
        if attendance[day] != [student]:
            attendance[day] += [student]
    return attendance
