class Coffee:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):

        return str(f'{self.ingredients}')

    @classmethod
    def cappuccino(cls):

        return cls(['кофе', 'сливки', 'сахар'])

    @classmethod
    def latte(cls):

        return cls(['эспрессо', 'молоко'])

    @classmethod
    def glace(cls):

        return cls(['кофе', 'мороженое'])


if __name__ == '__main__':

    cappuccino = Coffee.cappuccino()
    latte = Coffee.latte()
    glace = Coffee.glace()
    print(cappuccino)
    print(latte)
    print(glace)
