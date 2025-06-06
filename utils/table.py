from typing import List


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
