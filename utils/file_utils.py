"""
utils
"""


def load_names(filepath: str) -> None:
    list_of_items = []
    with open(filepath, "r") as csv_file:
        content = csv_file.read()
        list_of_items = content.split()
        return list_of_items
