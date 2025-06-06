from typing import List
from utils.table import Table
from random import shuffle


class Openspace:
    """
    OpenSpace Class
    """

    def __init__(self, tables: List[Table], number_of_tables: int):
        self.tables = tables
        self.number_of_tables = number_of_tables

    def organize(self, names):
        """Organize seats and students"""
        # self.names = names
        shuffle(names)
        for name in names:
            for table in self.tables:
                print(f"{table.capacity}")
                if table.capacity > 0:

                    table.assign_seat(name)
                    break

                # if table.capacity == 0:
                #     continue

    def display(self):
        """displaying students on table with specific seat assigned"""
        for table in self.tables:
            print(f"table : {table}")
            table.display_table()

    def store(self, filename):
        """storing classroom organisation in a CSV file"""
