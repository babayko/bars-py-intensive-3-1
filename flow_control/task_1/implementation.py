def get_numbers():
    values = []
    for value in range(1000, 2001, 1):
        if value % 7 == 0 and value % 5 != 0:
            values.append(value)
    return values


print(get_numbers())
