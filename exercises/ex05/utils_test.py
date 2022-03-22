"""Utils Test."""

__author__ = "730464883"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens() -> None:
    """Test when there is no numbers at all."""
    only: list[int] = []
    assert only_evens(only) == []


def test_only_evens_odds() -> None:
    """Test when there are only odd numbers."""
    only: list[int] = [1, 3, 5]
    assert only_evens(only) == []


def test_only_evensoo() -> None:
    """Test when there are only odd numbers."""
    only: list[int] = [2, 4, 6]
    assert only_evens(only) == [2, 4, 6]


def test_sub() -> None:
    """Test when length is 0."""
    numbers: list[int] = [1, 2, 3]
    a: int = 5
    b: int = 9
    assert sub(numbers, a, b) == []


def test_sub_negative() -> None:
    """Test when a is neg."""
    numbers: list[int] = [10, 20, 30]
    a: int = -1
    b: int = 2
    assert sub(numbers, a, b) == [10, 20]


def test_sub_two() -> None:
    """Test when more than one number is returned."""
    numbers: list[int] = [10, 20, 30, 40]
    a: int = 1
    b: int = 3
    assert sub(numbers, a, b) == [20, 30]


def test_concat_none() -> None:
    """Test what will happen when there are no words."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_one_list() -> None:
    """Test when only one list is active."""
    first: list[int] = [1, 2, 3, 4, 5]
    second: list[int] = []
    assert concat(first, second) == [1, 2, 3, 4, 5]


def test_concat_two_list() -> None:
    """Test when both lists are active."""
    first: list[int] = [1, 2, 3]
    second: list[int] = [4, 5]
    assert concat(first, second) == [1, 2, 3, 4, 5]
