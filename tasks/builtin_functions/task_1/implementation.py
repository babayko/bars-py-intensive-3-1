from tasks.common import MyException


class Value:
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return str(self.value)

    def __repr__(self):

        return repr(self.value)

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError

        return self.value + other

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError

        return self.value - other

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError

        return self.value * other

    def __truediv__(self, other):
        if not isinstance(other, int):
            raise TypeError
        try:
            result = self.value / other
        except ZeroDivisionError:
            raise MyException

        return result
