class DiscountCalculator:
    def __init__(self, discount):
        '''
        :param discount: відсоток знижки
        '''

        self._discount = discount / 100

    def __call__(self, price):
        new_price = price - (price * self._discount)
        # new_price = price * (1 - self._discount)
        return new_price


# calculator1 = DiscountCalculator(20)
# print(calculator1(50))
# print(calculator1(100))
# print(calculator1(360))
# print()
#
# calculator2 = DiscountCalculator(15)
# print(calculator2(50))
# print(calculator2(100))
# print(calculator2(360))

class Demo:
    def __init__(self, func):
        self.func = func
        print("Привіт з конструктора!")

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        print("Привіт з функтора!")


@Demo
def decor(*args):
    print("Тест декоратора", *args)

#decor = Demo(decor)


decor(1, 2, 'asd')
print(type(decor))

calculator = DiscountCalculator(20)
calculator.__dict__['_discount'] = 0.3 # calculator._discount = 0.3
print(calculator.__dict__)
print(calculator._discount)
