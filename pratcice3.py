class MyMeta(type):
    needed_methods = ['info', 'get_name']

    def __new__(cls, name, bases, dct):
        for method_name in cls.needed_methods:
            if method_name not in dct:
                raise AttributeError(f'There is no method {method_name} in class {name}')
            if not callable(dct[method_name]):
                raise AttributeError(f'{method_name} is not callable in class {name}')

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=MyMeta):
    age = 20
    name = 'Mary'

    def info(self):
        print(f'Name: {self.name}, age: {self.age}')

    def get_name(self):
        return self.name


class Person1(metaclass=MyMeta):
    info = 10
    get_name = 10

# print(callable(print))