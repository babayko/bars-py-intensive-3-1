class Multiplier:
    def __init__(self, value):
        self.value = value

    def get_value(self):

        return int(self.value)

    def __add__(self, other):
        if not isinstance(other, Multiplier):
            raise TypeError

        return Multiplier(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, Multiplier):
            raise TypeError

        return Multiplier(self.value - other.value)

    def __mul__(self, other):
        if not isinstance(other, Multiplier):
            raise TypeError

        return Multiplier(self.value * other.value)

    def __truediv__(self, other):
        if not isinstance(other, Multiplier):
            raise TypeError

        return Multiplier(self.value / other.value)


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.value = value * 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.value = value * 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.value = value * 1000000
