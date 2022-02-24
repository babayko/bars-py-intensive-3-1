class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        """
        Возвращает отображение значения из объекта.
        """
        return f'{self.args}'

    def __getitem__(self, indices):
        """
        Возвращает значение индекса в объекте.

        Args:
            indices: индекс искомого элемента
        """
        if type(indices) is tuple:
            return f'Передано {len(indices)} эелемента, но ожидается 1'

        return self.args[indices]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        return sum([1 for x in self.args if x == value])

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        for step_ in range(len(self.args)):
            if value == self.args[step_]:
                return step_
        else:
            raise ValueError
