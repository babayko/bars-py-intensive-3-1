from tasks.common import MyException


class ClassFather:
    registered_list = []

    def __init__(self):
        self._name = 'as yet unnamed'
        self._registered = False

    def register(self):
        if not isinstance(self, (User1, User2)):
            raise MyException
        self._registered = True

        return ClassFather.registered_list.append(self)

    def get_name(self):
        if self._registered is not True:
            raise MyException

        return self._name


class User1(ClassFather):
    _name = ''


class User2(ClassFather):
    _name = ''
