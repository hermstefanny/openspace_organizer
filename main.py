from utils.openspace import Openspace
from utils.table import Table
from utils.file_utils import load_names


if __name__ == "__main__":

    """
    Main function which executes the program
    and establishes initial conditions
    """

    colleagues_names = load_names("./data/colleagues.csv")
    table_capacity = 4
    number_of_tables = 6

    while len(colleagues_names) > table_capacity * number_of_tables:
        number_of_tables += 1

    tables = [Table(table_capacity) for i in range(0, number_of_tables)]

    openspace = Openspace(tables, number_of_tables)
    openspace.organize(colleagues_names)
    openspace.display()
    # openspace.store("seats_assigned.csv")
