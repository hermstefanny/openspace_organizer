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
        self.names = names
        shuffle(name)
        for name in names:
            for table in self.tables:
                if table.has_free_spot == True:
                    table.assign_seat(name)
                    break

    def display(self):
        """displaying students on table with specific seat assigned"""
        for table in self.tables:
            table.display_table()
            print("table : {table}")

    def store(self, filename):
        """storing classroom organisation in a CSV file"""