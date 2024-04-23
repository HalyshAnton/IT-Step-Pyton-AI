import pickle
import gzip
from pratcice3 import Person


with gzip.open("person.gz", 'rb') as file:
    serialized_data = file.read()
    read_person = pickle.loads(serialized_data)


print(type(read_person), read_person)
read_person.print_info()