"""Some helpful utility functions for working with CSV file."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """"read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    for row in csv_reader:
        result.append(row)


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:


    file_handle.close()
    return result
