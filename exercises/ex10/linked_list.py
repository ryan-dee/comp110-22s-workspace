"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730464883"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if Node.next is None:
        return Node.data
    else:
        return last(head)


def value_at(head: Optional[Node], index: int) -> int:
    count: int = 0
    if count == index:
        return Node.data
    else:
        count += 1
        return value_at(head, index) 


def max(head: Optional[Node]) -> int:
    ret_max: int = 0
    if Node.next is None:
        return ret_max
    else:
        if Node.data > ret_max:
            ret_max = Node.data
        return max(head)


def linkify(items: list[int]) -> Optional[Node]:
    iteration: int = 0
    if iteration == len(items):
        return Node.data
    while iteration < len(items):
        Node.data = items[iteration]
        iteration += 1
        return linkify(items)


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    if Node.next is None:
        return Node.data
    else:
        Node.data == Node.data * factor
        return scale(head, factor)