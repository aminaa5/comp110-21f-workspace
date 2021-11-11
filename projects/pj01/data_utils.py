"""Data analysis funtions."""

__author__ = "730398576"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reading the rows of a csv file into a 'table'."""
    data_rows: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        data_rows.append(row)
    file_handle.close()
    return data_rows


def column_values(data_rows: list[dict[str, str]], column: str) -> list[str]:
    """List of strings in a column is produced!"""
    comp_major: list[str] = []
    for row in data_rows:
        item: str = row[column]
        comp_major.append(item)
    return comp_major


def columnar(data_cols: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform from rows to columns!"""
    result: dict[str, list[str]] = {}
    for dicty in data_cols:
        for keys in dicty:
            result[keys] = column_values(data_cols, keys)
    return result


def head(data_cols_head: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only first rows of data."""
    data_cols: dict[str, list[str]] = {}
    for key in data_cols_head:
        rows: list[str] = []
        for y in range(x):
            rows.append(data_cols_head[key][y])
            if x >= len(data_cols_head):
                return data_cols_head
        data_cols[key] = rows
    return data_cols


def select(data_cols: dict[str, list[str]], data: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a specific subset!"""
    selected_data: dict[str, list[str]] = {}
    for key in data:
        selected_data[key] = data_cols[key]
    return selected_data


def count(selected_data: list[str]) -> dict[str, int]:
    """Function will count the number of times a value appears!"""
    counts: dict[str, int] = {}
    for item in selected_data:
        if item in counts:
            counts[item] += 1
        else: 
            counts[item] = 1
    return counts


def helper(data_cols: dict[str, list[str]], cs: str) -> dict[str, int]:
    """Return only comp sci majors, BA or BS, and their number of office hour visits."""
    comp_only: dict[str, int] = {"Yes - BS": 0, "Yes - BA": 0}
    i: int = 0
    while i < len(data_cols[cs]):
        if data_cols[cs][i] == "Yes - BS": 
            comp_only["Yes - BS"] += int(data_cols["oh_visits"][i])
        elif data_cols[cs][i] == "Yes - BA":
            comp_only["Yes - BA"] += int(data_cols["oh_visits"][i])
        i += 1
    return comp_only