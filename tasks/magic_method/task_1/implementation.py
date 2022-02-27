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
        try:
            result = Multiplier(self.value / other.value)
        except ZeroDivisionError:
            raise Exception

        return result


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        if type(value) == int:
            self.value = value * 100
        else:
            raise TypeError


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        if type(value) == int:
            self.value = value * 1000
        else:
            raise TypeError


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        if type(value) == int:
            self.value = value * 1000000
        else:
            raise TypeError
