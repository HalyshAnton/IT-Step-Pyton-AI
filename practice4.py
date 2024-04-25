import json


class Person:
    filename = 'persons.json'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def print_info(self):
        print(self.name, self.age)

    def get_state_dict(self):
        return {"name": self.name,
                "age": self.age}

    @classmethod
    def save_persons(cls, persons):
        data = []

        for person in persons:
            dct = person.get_state_dict()
            data.append(dct)

        #data = [person.get_state_dict() for person in persons]

        with open(cls.filename, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_persons(cls):
        with open(cls.filename, 'r') as file:
            data = json.load(file)

        persons = []
        for dct in data:
            person = cls(dct['name'], dct['age'])
            persons.append(person)

        return persons


person1 = Person("Max", 16)
person2 = Person("John", 42)
person3 = Person("Mary", 25)


Person.save_persons([person1, person2, person3])

for read_person in Person.load_persons():
    read_person.print_info()