class House:
    def __init__(self, floors):
        self.floors = floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, int):
            return self.floors == other
        return False

    def __add__(self, other):
        if isinstance(other, House):
            self.floors += other.floors
        elif isinstance(other, int):
            self.floors += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
        return NotImplemented

    def __str__(self):
        return f'House with {self.floors} floors'

house1 = House(2)
house2 = House(3)

print(house1 + house2)
print(house1 + 1)
print(house2 == 3)
print(house1 < 3)
