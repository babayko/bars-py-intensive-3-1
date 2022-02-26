from tasks.common import MyException


class ClassFather:
    registered_list = []

    def __init__(self):
        self._name = 'as yet unnamed'

    def ___str___(self):
        
        return str(f'{self._name}')

    def register(self):
        """ Регистрация только для наследника класса ClassFather """
        if (self.__class__ == ClassFather or not
                issubclass(self.__class__, ClassFather)):
            raise MyException

        return ClassFather.registered_list.append(self)

    def get_name(self):
        """ Возвращаем _name если наследник зарегистрирован, иначе - ошибку """
        if (self.__class__ == ClassFather or not
                issubclass(self.__class__, ClassFather) or
                self not in self.registered_list):
            raise MyException

        return self._name


class User1(ClassFather):
    _name = ''


class User2(ClassFather):
    _name = ''
