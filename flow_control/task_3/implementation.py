from datetime import datetime


def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    dict_month = {
        'январь':   31,
        'март':     31,
        'апрель':   30,
        'май':      31,
        'июнь':     30,
        'июль':     31,
        'август':   31,
        'сентябрь': 30,
        'октябрь':  31,
        'ноябрь':   30,
        'декабрь':  31,
    }

    if month in dict_month:
        return dict_month[month]
    elif month == 'февраль' and not is_leap_year(datetime.now().year):
        return 28
    elif month == 'февраль' and is_leap_year(datetime.now().year):
        return 29
    else:
        return 0
