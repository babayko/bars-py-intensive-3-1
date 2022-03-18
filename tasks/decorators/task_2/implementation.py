import time

from tasks.common import factorial, MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapped(args):
        if type(args) == int and args >= 0:
            result = func(args)
        else:
            raise MyException
        return result
    return wrapped


def cached(func):
    """
    Обертка, кэширующая результат.
    """
    cache = {}

    def wrapped(*args):
        nonlocal cache
        if not cache.get(args):
            result = func(*args)
            cache[args] = result
            return result
        else:
            return cache[args]
    return wrapped


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapped(args):
        start_time = time.perf_counter()
        result = func(args)
        print(f'Время вычисления факториала {args} -  {time.perf_counter() - start_time} секунд')
        return result
    return wrapped


@time_execution
@check_value
@cached
def validate_number(number):
    return factorial(number)


if __name__ == '__main__':

    validate_number(100000)
    validate_number(100000)
