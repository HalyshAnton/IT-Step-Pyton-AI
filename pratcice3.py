import pickle
import gzip


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Name {self.name} with age {self.age}')


person = Person("Anna", 31)

# with open('person.pickle', 'wb') as file:
#     pickle.dump(person, file)
#
# with open('person.pickle', 'rb') as file:
#     read_person = pickle.load(file)

with gzip.open("person.gz", 'wb') as file:
    serialized_data = pickle.dumps(person)
    file.write(serialized_data)

with gzip.open("person.gz", 'rb') as file:
    serialized_data = file.read()
    read_person = pickle.loads(serialized_data)


print(type(read_person), read_person)
read_person.print_info()


