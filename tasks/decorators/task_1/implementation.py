import time
from tasks.common import factorial


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
def new_factorial(number):
    return factorial(number)


if __name__ == '__main__':

    new_factorial(100000)
