class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['country'] = "Ukraine"

        if 'name' not in dct:
            raise AttributeError('There is no attribute name')

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=MyMeta):
    age = 20
    # name = 'Mary'

    def info(self):
        print(f'Name: {self.name}, age: {self.age}')


print(Person.country)
