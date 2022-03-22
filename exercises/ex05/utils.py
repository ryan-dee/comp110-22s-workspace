"""Utils."""

__author__ = "730464883"


def only_evens(only: list[int]) -> list:
    """Only evens Docstring."""
    evens_list: list[int] = list()
    alt: int = 0
    while alt < len(only):
        if only[alt] % 2 == 0:
            evens_list.append(only[alt])
        alt = alt + 1
    return evens_list


def sub(numbers: list[int], a: int, b: int) -> list:
    """Sub Docstring."""
    i: int = a
    sub_list: list[int] = list()
    if i >= len(numbers):
        return sub_list
    if i < 0:
        i = 0
    if b > len(numbers):
        b = len(numbers)
    while i <= (b - 1):
        sub_list.append(numbers[i])
        i = i + 1
    return sub_list


def concat(first: list[int], second: list[int]) -> list:
    """Concat docstring."""
    num_list: list[int] = list()
    for word in first:
        num_list.append(word)
    for character in second:
        num_list.append(character)
    return num_list