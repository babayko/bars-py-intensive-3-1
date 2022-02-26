class Coffee:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # def __repr__(self):
    #     return str({self.ingredients})

    def __str__(self):
        return str(f'Coffee({self.ingredients})')
    
    @classmethod
    def cappuccino(cls):

        return cls(['кофе', 'сливки', 'сахар'])
    
    @classmethod
    def latte(cls):
        return cls(['эспрессо', 'молоко'])

    @classmethod
    def glace(cls):
        return cls(['кофе', 'мороженое'])


cappuccino = Coffee.cappuccino()
latte = Coffee.latte()
glace = Coffee.glace()
print(cappuccino)
print(latte)
print(glace)

    # def __init__(self, ingredients=None):
#         self.ingredients = ingredients

#     # def __repr__(self):
#     #     return str({self.ingredients})

#     def __str__(self):
#         return str(f'Coffee({self.ingredients})')

#     def cappuccino(self):
#         return self.__class__(['кофе', 'сливки', 'сахар'])

#     def latte(self):
#         return self.__class__(['эспрессо', 'молоко'])

#     @classmethod
#     def glace(cls):
#         return cls(['кофе', 'мороженое'])


# if __name__ == '__main__':
#     coffee = Coffee()
#     print(coffee.cappuccino())
#     __import__('pdb').set_trace()
#     # print(type(coffee.cappuccino()))
#     # print(type(Coffee.cappuccino()))
#     # print(cappuccino)
#     # print(type(cappuccino))
#     # print(Coffee.latte())

#     # print(Coffee.glace())



# def __init__(self, name):
#         if name == 'cappuccino':
#             self.name = 'cappuccino'
#             self.coffee = 'кофе'
#             self.cream = 'сливки'
#             self.sugar = 'сахар'
#         elif name == 'latte':
#             self.name = 'latte'
#             self.espresso = 'эспрессо'
#             self.milk = 'молоко'
#         elif name == 'glace':
#             self.name = 'glace'
#             self.coffee = 'кофе'
#             self.ice_cream = 'мороженое'

#     def __str__(self):
#         if self.name == 'cappuccino':
#             result = f'Ингридиенты капучино: {self.coffee}, {self.cream}, {self.sugar}', self
#         elif self.name == 'latte':
#             result = f'Ингридиенты латте: {self.espresso}, {self.milk}', self
#         elif self.name == 'glace':
#             result = f'Ингридиенты гляссе: {self.coffee}, {self.ice_cream}', self

#         return result
    
#     def cappuccino(self):
#         return f'Это капучино', self


# if __name__ == '__main__':
#     my_coffee_cuppuccino = Coffee('cappuccino')
#     print(my_coffee_cuppuccino)
#     print(type(my_coffee_cuppuccino))
#     print(my_coffee_cuppuccino.cappuccino())
#     print(type(my_coffee_cuppuccino.cappuccino()))
    
#     my_coffee_latte = Coffee('latte')
#     print(my_coffee_latte)
    
#     my_coffee_glace = Coffee('glace')
#     print(my_coffee_glace)