from typing import List
from utils.table import Table
from random import shuffle


class Openspace:
    """
    OpenSpace Class
    """

    def __init__(self, tables: List[Table], number_of_tables: int) -> None:
        """
        Constructor for the Open Space Class
        """
        self.tables = tables
        self.number_of_tables = number_of_tables

    def __str__(self) -> str:
        """
        Representation of object OpenSpace
        """
        return f"This class has {self.number_of_tables}"

    def organize(self, names: List[str]) -> None:
        """
        Assigning names to table
        """
        shuffle(names)
        for name in names:
            for table in self.tables:
                if table.capacity > 0:
                    table.assign_seat(name)
                    break

    def display(self) -> None:
        """
        Displaying students on table with specific seat assigned
        """
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1}")
            table.display_table()

    def store(self, filename: str) -> None:
        """storing classroom organisation in a CSV file"""
        pass
