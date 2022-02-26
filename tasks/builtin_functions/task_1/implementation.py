from tasks.common import MyException


class Value:
    def __init__(self, value):
        if isinstance(value, (int, float)):
            self.value = value
        else:
            raise TypeError

    def __str__(self):

        return str(self.value)

    def __repr__(self):

        return repr(self.value)

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError

        return self.value + other

    def __sub__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError

        return self.value - other

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError

        return self.value * other

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError
        try:
            result = self.value / other
        except ZeroDivisionError:
            raise MyException

        return result
