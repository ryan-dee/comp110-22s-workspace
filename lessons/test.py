"""Test Function."""


def f(a: str, b: int) -> str:
    return_string = ""
    i: int = 0
    idx: int = 0
    while i < len(a):
        while idx < b:
            return_string = return_string + a[i]
            idx = idx + 1
        i = i + 1
    return return_string
