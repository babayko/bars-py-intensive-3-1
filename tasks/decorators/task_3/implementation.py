from tasks.common import some_func


def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    counter = 0

    def wrapped():
        nonlocal counter
        func()
        counter += 1
        return counter

    return wrapped


@counter
def count_func():
    return some_func()


if __name__ == '__main__':
    count_func()
    count_func()
    count_func()
    count_func()
    print(count_func())
