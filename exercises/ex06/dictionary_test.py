"""Dictionaries Test."""

__author__ = "730464883"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


def test_case_invert() -> None:
    """Test a use case."""
    insert: dict[str, str] = {'apple': 'a'}
    assert invert(insert) == {'a': 'apple'}


# def test_use_invert() -> None:
#     """Test another use case."""
#     insert: dict[str, str] = {'Tar': 'Heels', 'Go': 'Heels'}
#     assert invert(insert) == {'doe': 'john', 'namath': 'joe'}


with pytest.raises(KeyError):
    my_dictionary = {'Tar': 'Heels', 'Go': 'Heels'}
    invert(my_dictionary)


def test_edge_invert() -> None:
    """Test an edge case."""
    insert: dict[str, str] = {'': ''}
    assert invert(insert) == {'': ''}


def test_favorite_color() -> None:
    """Test a use case of favorite_color."""
    color: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert(favorite_color(color)) == 'blue'


def test_favorite_color_use() -> None:
    """Tese a use case of favorite_color when there is more than one color."""
    color: dict[str, str] = {'Ryan': 'azul', 'Coop': "rojo", 'Carly': 'rojo', 'Leah': 'azul'}
    assert(favorite_color(color)) == 'azul'


def test_favorite_color_edge() -> None:
    """Test an edge case of favorite_color."""
    color: dict[str, str] = {'': ''}
    assert favorite_color(color) == ''


def test_count() -> None:
    """Test a case of colors."""
    start: list[str] = ['Go', 'Heels', 'Go', 'America']
    assert count(start) == {'Go': 2, 'Heels': 1, 'America': 1}


def test_count_norm() -> None:
    """Test a normal case."""
    start: list[str] = ['Tar', 'Heel', 'Born', 'Tar', 'Heel', 'Bred']
    assert count(start) == {'Tar': 2, 'Heel': 2, 'Born': 1, 'Bred': 1}


def test_count_edge() -> None:
    """Test an edge case."""
    start: list[str] = ['']
    assert count(start) == {'': 1}