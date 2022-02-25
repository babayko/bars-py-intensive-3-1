import datetime


class MathClock:
    time_store = datetime.datetime.strptime('00:00', '%H:%M')

    def __init__(self, time=time_store):
        """ При создании экземпляра класса значение time по умолчанию равно 00:00 """
        self.time = time

    def get_time(self):
        """  возвращает время в формате 'hh:mm' """

        return str(self.time_store.time())[0:5]

    def __add__(self, other):
        """ сложение с числом увеличивает количество минут на входящее значение """
        self.time_store += datetime.timedelta(minutes=other)

        return self.time_store

    def __sub__(self, other):
        """ вычитание числа уменьшает количество минут на входящее значение """
        self.time_store -= datetime.timedelta(minutes=other)

        return self.time_store

    def __mul__(self, other):
        """ умножение на число увеличивает количество часов на входящее значение """
        self.time_store += datetime.timedelta(hours=other)

        return self.time_store

    def __truediv__(self, other):
        """ деление на число уменьшает количество часов на входящее значение """
        self.time_store -= datetime.timedelta(hours=other)

        return self.time_store
