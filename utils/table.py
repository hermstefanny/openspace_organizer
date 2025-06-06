from typing import List


class Seat:
    """Seat Class"""

    def __init__(self, free: bool, occupant: str) -> None:
        """setting up the classroom"""
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name: str) -> None:
        """fonction that asign a student to a seat"""
        if self.free == True:
            self.occupant = name
        else:
            print("not free")

    def remove_occupant(self) -> None:
        """fonction that remove a student from a seat"""
        if self.free == False:
            self.occupant = None
        else:
            print(f"Seat is not free, {self.occupant} is on it")

    def __str__(self):

        return f"The seat is ({self.free}) with {self.occupant}"


class Table:
    """This is the class Table"""

    def __init__(self, capacity: int, seats: List[Seat]) -> None:
        self.capacity = capacity
        self.seats = seats

    def __str__(self) -> str:
        return f"The table has {self.capacity} free seats"

    def has_free_spot(self) -> bool:
        if self.capacity > 0:
            return True

    def assign_seat(self, name: str) -> None:
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    self.capacity -= 1
                    break

    def left_capacity(self) -> int:
        return self.capacity

    def display_table(self) -> None:
        for i, seat in enumerate(self.seats):
            print(f"Seat {i}: {seat.occupant}")
