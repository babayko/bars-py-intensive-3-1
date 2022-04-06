from dataclasses import dataclass

from recordpack.provider import DjangoModelProvider


@dataclass(init=False)
class GridItem:
    """
    Пример класса элемента грида
    """
    id: int
    name: str = ''

    def __init__(self, id=None, context=None) -> None:
        self.id = id
        self.name = str(id)
        super().__init__()


class UserProvider(DjangoModelProvider):
    """
    Тестовый провайдер для задания
    """
    pass
