class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'{cls=}')
        print(f'{name=}')
        print(f'{bases=}')
        print(f'{dct=}')
        return super().__new__(cls, name, bases, dct)


class Parent:
    country = "Ukraine"


class Person(Parent, metaclass=MyMeta):
    age = 20
    name = 'Mary'

    # def __init__(self, country='Ukraine'):
    #     self.country = country

    def info(self):
        print(f'Name: {self.name}, age: {self.age}')
