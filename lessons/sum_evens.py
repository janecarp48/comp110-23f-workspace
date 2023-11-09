"""Practice summing over lists."""

def sum_evens(input: list[int]) -> int:
    """Sum all even numbers in this list."""
    list_sum: int = 0
    for int in input:
        if int % 2 == 0:
            list_sum =+ int
    return list_sum