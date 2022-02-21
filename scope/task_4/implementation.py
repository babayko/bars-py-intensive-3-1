def bad_open(file_path, mode):
    """Некорректная функция открытия файла"""
    raise Exception


def open_and_close_file(file_path):
    """Открывет и закрывает файл
    Args:
        file_path: путь до файла
    """
    open = bad_open

    def correct_open():
        nonlocal open
        import builtins
        open = builtins.open

    correct_open()

    f = open(file_path, 'r')
    f.close()
