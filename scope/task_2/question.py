"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):

    def data_transmitter():
        print(message)

    data_transmitter()


print(transmit_to_space('Test message'))

"""
скрипт выведет:

Test message
None

Test message - результат выполнения функции data_transmitter() - печать;
None  - результат выполнения функции transmit_to_space(), так как она
ничего не возвращает

"""
