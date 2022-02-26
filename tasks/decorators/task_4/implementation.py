from tasks.common import MyException
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
        def wrapper(*args, **kwargs):
            for _ in range(1, times + 1, 1):
                try:
                    result = func(*args, **kwargs)
                    if result:
                        return result
                except Exception:
                    time.sleep(delay)
            raise MyException

        return wrapper

    return decorator
