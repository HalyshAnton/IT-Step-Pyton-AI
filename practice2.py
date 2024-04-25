import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


person = Person("Max", 16)

with open("data.json", 'w') as file:
    json.dump(person, file)