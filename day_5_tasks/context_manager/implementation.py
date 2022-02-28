from contextlib import contextmanager
import typing


@contextmanager
def file(file_name: str, method: str) -> typing.TextIO:
    """ По умолчанию печатаем количество строк в открываемом файле """

    file = open(file_name, method)
    print('Количество строк в файле:', len(file.readlines()))
    file.close()
    file = open(file_name, method)

    yield file

    file.close()


if __name__ == '__main__':

    with file('logs.txt', 'r') as opened_file:
        print(opened_file.read())
