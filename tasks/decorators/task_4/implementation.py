from tasks.common import specific_func, MyException
import time


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator(func):
        def wrapper(*args, **kargs):
            for step_ in range(1, times + 1, 1):
                try:
                    result = func()
                    if result is not None:
                        return result
                except AssertionError:
                    if step_ == times:
                        raise MyException
                    time.sleep(delay)
        return wrapper
    return decorator


if __name__ == '__main__':
    new_factorial = decorator_maker(3, 0)(specific_func)
    print(new_factorial())
