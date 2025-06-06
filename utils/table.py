from typing import List

class Seat:
    """
    Table Class
    """

    def __init__(self, free: bool, occupant: str):
        """setting up the classroom"""
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        """fonction that asign a student to a seat"""
        self.name = name
        if self.free == True:
            self.occupant = name
        print("not free")

    def remove_occupant(self):
        """fonction that remove a student from a seat"""
        if self.free == False:
            self.occupant = None
        return f"{seat_number} is not free, {name} is on it"
            

    def __str__(self):
        """fonction that will print if seat free and if not remove a student"""


class Table:
    """This is the class Table"""

    def __init__(self, capacity: int, seats: List[Seat]) -> None:
        self.capacity = capacity
        self.seats = seats

    def __str__(self) -> str:
        return f"The table has {self.capacity} seats"

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

