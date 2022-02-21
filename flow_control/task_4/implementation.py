def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    dict_month = {
        1:  31,
        3:  31,
        4:  30,
        5:  31,
        6:  30,
        7:  31,
        8:  31,
        9:  30,
        10: 31,
        11: 30,
        12: 31,
    }

    if is_leap_year(some_date.year):
        dict_month[2] = 29
    else:
        dict_month[2] = 28

    if some_date.day == dict_month[some_date.month] and some_date.month != 12:
        new_date = some_date.replace(day=1)
        new_date = new_date.replace(month=some_date.month + 1)
    elif some_date.day == dict_month[some_date.month] and some_date.month == 12:
        new_date = some_date.replace(day=1)
        new_date = new_date.replace(month=1)
        new_date = new_date.replace(year=some_date.year + 1)
    elif some_date.day <= dict_month[some_date.month]:
        new_date = some_date.replace(day=some_date.day + 1)

    return new_date
