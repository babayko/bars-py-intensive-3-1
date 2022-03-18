from tasks.common import MyException


class ClassFather:
    registered_list = []

    @classmethod
    def register(cls):
        """ Регистрация только для наследника класса ClassFather """
        if cls == ClassFather or not issubclass(cls, ClassFather):
            raise MyException

        return ClassFather.registered_list.append(cls)

    @classmethod
    def get_name(cls):
        """ Возвращаем _name если наследник зарегистрирован, иначе - ошибку """
        if (cls == ClassFather or not issubclass(cls, ClassFather) or
                cls not in ClassFather.registered_list):
            raise MyException
        return cls._name


class User1(ClassFather):
    _name = 'Max'

    def close_access(self):
        """ Закрываем доступ к регистрации из экземпляра класса """
        raise AttributeError

    registered_list = property(close_access)


class User2(ClassFather):
    _name = 'Dja'

    def close_access(self):
        """ Закрываем доступ к регистрации из экземпляра класса """
        raise AttributeError

    registered_list = property(close_access)
