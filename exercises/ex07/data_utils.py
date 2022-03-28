"""Dictionary related utility functions."""

__author__ = "730464883"
# Define your functions below

# from io import TextIOWrapper
# from unittest import result
from csv import DictReader


def read_csv_rows(file: str) -> list[dict[str, str]]:
    """Read CSV file into list."""
    final: list[dict[str, str]] = []

    file_handle = open(file, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        final.append(row)
    
    file_handle.close
    
    return final


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Column values."""
    ret_list: list[str] = []
    for row in table:
        item: str = row[column]
        ret_list.append(item)
    return ret_list


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    new: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        new[column] = column_values(row_table, column)
    
    return new


def head(data: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Give list of columns."""
    if N > len(data):
        return data
    else:
        ret_dict: dict[str, list[str]] = {}
        for columns in data:
            new_list: list[str] = []
            if N < len(data):    
                i: int = 0
                while i < N:
                    new_list.append(data[columns][i])
                    i += 1
                ret_dict[columns] = new_list
        return ret_dict


def select(given: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Give selected values."""
    new_dict: dict[str, list[str]] = {}
    for columns in names:
        new_dict[columns] = given[columns]
    return new_dict


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Give all lists without duplicates."""
    overall: dict[str, list[str]] = {}
    for keys in first:
        overall[keys] = first[keys]
    for columns in second:
        if columns in overall:
            i: int = 0
            while i < len(second[columns]):
                overall[columns].append(second[columns][i])
                i += 1
        else:
            overall[columns] = second[columns]
    return overall