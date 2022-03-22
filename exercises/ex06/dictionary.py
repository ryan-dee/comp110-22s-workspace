"""Dictionaries ex06."""

__author__ = "730464883"


def invert(insert: dict[str, str]) -> dict[str, str]:
    """Invert Dictionaries."""
    ret_dict = dict[str, str]
    ret_dict = dict()
    for key in insert:
        ret_dict[insert[key]] = key
    return ret_dict


def favorite_color(color: dict[str, str]) -> str:
    """Return Back Favorite Color."""
    most_colors = dict[str, int]
    most_colors = dict()
    r_string: str = ''
    max_int: int = 0
    for key in color:
        if color[key] in most_colors:
            most_colors[color[key]] += 1
        else:
            most_colors[color[key]] = 1
    for key in most_colors:
        if most_colors[key] > max_int:
            max_int = most_colors[key]
            r_string = key
    return r_string
        

def count(start: list[str]) -> dict[str, int]:
    """Count List."""
    final_dict = dict[str, int]
    final_dict = dict()
    i: int = 0
    while i < len(start):
        if start[i] in final_dict:
            final_dict[start[i]] += 1
        else:
            final_dict[start[i]] = 1
        i = i + 1
    return final_dict