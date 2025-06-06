from typing import List


class Seat:
    """Seat Class"""

    def __init__(self, free: bool, occupant: str) -> None:
        """setting up the classroom"""
        self.free = free
        self.occupant = occupant

    def __str__(self):
        """Representation of object Seat"""
        return f"The seat is ({self.free}) with {self.occupant}"

    def set_occupant(self, name) -> None:
        """fonction that asign a student to a seat"""
        if self.free == True:
            self.occupant = name
            self.free = False
        else:
            print("not free")

    def remove_occupant(self) -> None:
        """fonction that remove a student from a seat"""
        if self.free == False:
            self.occupant = "remove"
        else:
            print(f"Seat is not free, {self.occupant} is on it")


class Table:
    """This is the class Table"""

    def __init__(self, capacity: int) -> None:
        """Constructor for the Table class"""
        self.capacity = capacity
        table_seats = [Seat(True, None) for i in range(0, self.capacity)]
        self.seats = table_seats

    def __str__(self) -> str:
        """Representation of object Table"""
        return f"The table has {self.capacity} free seats"

    def has_free_spot(self) -> bool:
        """Asserts if the seat is free"""
        if self.capacity > 0:
            return True

    def assign_seat(self, name: str) -> None:
        """Assign the occupant to the free seats in table"""
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    self.capacity -= 1
                    break

    def left_capacity(self) -> int:
        """Returns the capacity of the table"""
        return self.capacity

    def display_table(self) -> None:
        """Displays the table with its occupants"""
        for i, seat in enumerate(self.seats):
            print(f"Seat {i+1}: {seat.occupant}")
