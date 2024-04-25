import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def print_info(self):
        print(self.name, self.age)

    def save(self, filename='person.json'):
        dct = {"name": self.name,
               "age": self.age}

        with open(filename, 'w') as file:
            json.dump(dct, file)

    def load(self, filename='person.json'):
        with open(filename, 'r') as file:
            dct = json.load(file)

        self.name = dct['name']
        self.age = dct['age']

    @classmethod
    def load_person(cls, filename='person.json'):
        with open(filename, 'r') as file:
            dct = json.load(file)

        return cls(name=dct['name'],
                   age=dct['age'])


person = Person("Max", 16)
# person.birthday()
# person.birthday()
# person.birthday()
#
# person.save()
#
# person.load()
# person.print_info()

person.save()

read_person = Person.load_person()
read_person.print_info()

