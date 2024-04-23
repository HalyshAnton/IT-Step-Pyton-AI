import pickle
import gzip


data = {"login": "gfkhd", "password": "1231534"}


# with gzip.open("data.gz", 'wb') as file:
#     serialized_data = pickle.dumps(data)
#     file.write(serialized_data)


with gzip.open('data.gz', 'rb') as file:
    serialized_data = file.read()
    read_data = pickle.loads(serialized_data)

print(type(read_data), read_data)