class Coffee:
    class_name = 'Кофе'

    def __init__(self):
        self.coffee = 'кофе'
        self.espresso = 'эспрессо'
        self.milk = 'молоко'
        self.cream = 'сливки'
        self.sugar = 'сахар'
        self.ice_cream = 'мороженое'

    def get_cappuccino(self):
        return f'Ингредиенты Капучино: {self.coffee}, {self.cream}, {self.sugar}'

    def get_latte(self):
        return f'Ингредиенты Латте: {self.espresso}, {self.milk}'

    def get_glace(self):
        return f'Ингредиенты Гляссе: {self.coffee}, {self.ice_cream }'


if __name__ == '__main__':
    my_coffee = Coffee()
    print(my_coffee.get_cappuccino())
    print(my_coffee.get_latte())
    print(my_coffee.get_glace())
