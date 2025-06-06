class Seat():
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