def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    if to_scale == 'C':
        return int((value - 32) * 5/9)
    elif to_scale == 'F':
        return int((value * 9/5) + 32)
    else:
        return value
