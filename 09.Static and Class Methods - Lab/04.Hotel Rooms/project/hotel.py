from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{str(stars_count)} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests" + \
            f"\nFree rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken is False)}" + \
            f"\nTaken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken is True)}"
