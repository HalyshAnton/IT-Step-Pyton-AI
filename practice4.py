class MyMeta(type):
    def __new__(cls, name, bases, dct):
        for method_name, method in dct.items():
            if callable(method):
                dct[method_name] = cls.meta_decor(method)

        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def meta_decor(method):
        def decored_method(*args, **kwargs):
            print('hello from metaclass')
            return method(*args, **kwargs)

        return decored_method


class Number(metaclass=MyMeta):
    value = 10

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * other.value

    def __sub__(self, other):
        return self.value - other.value

    def __truediv__(self, other):
        return self.value / other.value


num1 = Number()
num2 = Number()

print(num1 + num2)
print(num1 / num2)
print(num1 - num2)
print(num1 * num2)