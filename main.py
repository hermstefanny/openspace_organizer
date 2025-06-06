from utils.openspace import Openspace
from utils.table import Table, Seat
from utils.file_utils import load_names


if __name__ == "__main__":

    colleagues_names = load_names("./data/colleagues.csv")

    # print("..........")
    # random.shuffle(colleagues_names)
    # print(colleagues_names)

    table_capacity = 4
    number_of_tables = 6

    # table_seats = [Seat(True, None) for i in range(0, table_capacity)]

    tables = [Table(table_capacity) for i in range(0, number_of_tables)]

    openspace = Openspace(tables, number_of_tables)
    openspace.organize(colleagues_names)

    print(colleagues_names)

    openspace.display()
    # openspace.store("seats_assigned.csv")
