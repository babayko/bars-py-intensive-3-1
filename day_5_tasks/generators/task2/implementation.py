def check_errors(file_name: str) -> str:
    """ Вывод строк из входящего файла содержащих слово 'error' """
    try:
        file = open(file_name, 'r')
    except OSError as error:
        print('Ошибка открытия файла', error)
    else:
        counter = 0
        with file:
            for line in file.readlines():
                counter += 1
                if 'error' in line.lower():

                    yield str(f'Строка {counter}: {line}')


if __name__ == '__main__':

    gen = check_errors('log.txt')

    for line in gen:
        print(line)
