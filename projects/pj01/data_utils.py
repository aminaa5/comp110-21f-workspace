"""Analysis funtions."""

__author__ = "730398576"


from csv import DictReader


def read_csv_rows(DATA_FILE_PATH: str) -> list[dict[str, str]]:
    """Reading the rows of a csv file into a 'table'."""
    data_rows: list[dict[str, str]] = []
    file_handle = open(DATA_FILE_PATH, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        data_rows.append(row)
    file_handle.close()
    return data_rows


def column_values(data_rows: list[dict[str, str]], column: str) -> list[str]:
    """List of strings in a column is produced!"""
    subject_age: list[str] = []
    for row in data_rows:
        item: str = row[column]
        subject_age.append(item)
    return subject_age


def columnar(data_cols: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform from rows to columns!"""
    result: dict[str, list[str]] = {}
    data_rows: dict[str, str] = data_cols[0]
    for column in data_rows:
        result[column] = column_values(data_cols, column)
    return result


def head(data_cols_head: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only first rows of data."""
    data_cols: dict[str, list[str]] = {}
    for key in data_cols_head:
        data_cols[key] = data_cols_head[key][:x]
    return data_cols


def select(data_cols: dict[str, list[str]], data: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a specific subset!"""
    selected_data: dict[str, list[str]] = {}
    for key in data:
        selected_data[key] = data_cols[key]
    return selected_data


def concat(data_cols_head: dict[str, list[str]], additional_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    combined: dict[str, list[str]] = {}
    for column in data_cols_head:
        combined[column] = data_cols_head[column]
    for column in additional_table:
        combined[column] = additional_table[column]
        if data_cols_head[column] == additional_table[column]:
            combined[column] = additional_table[column]
    return combined


def count(selected_data: list[str]) -> dict[str, int]:
    """Function will count the number of times a value appears!"""
    counts: dict[str, int] = {}
    for item in selected_data:
        if item in counts:
            counts[item] += 1
        else: 
            counts[item] = 1
    return counts