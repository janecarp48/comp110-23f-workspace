def odd_and_even(input: list[int]) -> list[int]:
    new_list: list(int) = []
    for i in range(len(input)):
        if i % 2 == 0 and input[i] % 2 != 0:
            new_list.append(input[i])
    return new_list

print(odd_and_even([2,3,4,5]))
print(odd_and_even([7,8,10,10,5,12,3,2,11,8]))

def value_exists(input: dict[str, int], int: int) -> bool:
    value_exists: bool = False
    for key in input:
        if input[key] == int:
            value_exists = True
    return value_exists

print(value_exists({"a": 4, "b": 4, "c": 7, "d": 1}, 4))
print(value_exists({"a": 4, "b": 4, "c": 7, "d": 1}, 5))

def short_words(input: list[str]) -> list[str]:
    new_list: list[str] = list()
    for i in range(0, len(input)):
        if len(input[i]) < 5:
            new_list.append(input[i])
        if len(input[i]) >= 5:
            print(f"{input[i]} is too long!")
    return new_list

print(short_words(["sun", "cloud", "sky", "toodleoo"]))

