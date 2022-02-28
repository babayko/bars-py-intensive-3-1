def fib(n):
    """ Функция-генератор для последовательности Фибоначчи"""
    first_fib, second_fib = 1, 1

    for _ in range(n):
        yield first_fib
        first_fib, second_fib = second_fib, first_fib + second_fib
