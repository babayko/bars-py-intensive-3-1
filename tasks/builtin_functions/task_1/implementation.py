from tasks.common import MyException


class Value(int):
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        try:
            result = self.value / other
        except ZeroDivisionError:
            raise MyException
        return result
