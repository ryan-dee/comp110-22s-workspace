"""Utility class for numerical operations."""

from __future__ import annotations
# from optparse import Values
# from readline import set_completion_display_matches_hook

from typing import Union
# from itsdangerous import NoneAlgorithm

# from numpy import number

__author__ = "730464883"


class Simpy:
    values: list[float]
    # TODO: Your constructor and methods will go here.
    
    def __init__(self, values: list[float]):
        """Initialize a list with its parameters."""
        self.values = values

    def __str__(self) -> str:
        """Produce string representation of List."""
        return f"({self.values})"

    def fill(self, numbers: float, amount: int):
        i: int = 0
        while i < amount:
            self.values.append(numbers)
            i = i + 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> list[float]:
        assert step != 0
        res_list: list[float] = []
        i: float = start
        while i <= stop:
            res_list.append(i)
            i = i + step
        return res_list

    def sum(self) -> float:
        ret_value: float = 0
        i: int = 0
        while i < len(self.values):
            ret_value = ret_value + self.values[i]
            i = i + 1
        return ret_value

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add two variables together."""
        ret_list: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                ret_list.append(self.values[idx] + rhs.values[idx])
        elif (isinstance(rhs, float)):
            for values in self.values:
                ret_list.append(values + rhs)
        return Simpy(ret_list)
            
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Multiply by the power of another variable."""
        result_list: list[float] = []        
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                result_list.append(self.values[idx] ** rhs.values[idx])
        elif (isinstance(rhs, float)):
            for idx in range(0, len(self.values)):
                result_list.append(self.values[idx] ** rhs)
        return Simpy(result_list)

    def __eq__(self, rhs: Union[Simpy, bool]) -> list[bool]:
        """Test for equality Magic method."""
        ret_bool: list[bool] = []
        if isinstance(rhs, Simpy):
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    ret_bool.append(True)
                else:
                    ret_bool.append(False)
        elif isinstance(rhs, float):
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs:
                    ret_bool.append(True)
                else:
                    ret_bool.append(False)
        return ret_bool

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than magic method."""
        res_gt: list[bool] = []
        if isinstance(rhs, Simpy):
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    res_gt.append(True)
                else:
                    res_gt.append(False)
        elif isinstance(rhs, float):
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs:
                    res_gt.append(True)
                else:
                    res_gt.append(False)
        return res_gt

    def __getitem__(self, rhs: int) -> float:
        """Get item magic method."""
        ret_float: float = 0
        if rhs < len(self.values):
            ret_float = self.values[rhs]
        return ret_float

    # def __getitems__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
