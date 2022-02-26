from tasks.common import some_func


def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    counter = 0

    def wrapped(*args):
        nonlocal counter
        func(*args)
        counter += 1
        return counter

    return wrapped
