import pickle


data = {"login": "gfkhd", "password": "1231534"}

# serialized_data = pickle.dumps(data)
#
# print(serialized_data)
#
# read_data = pickle.loads(serialized_data)
#
# print(type(read_data), read_data)

# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file)

with open('data.pickle', 'rb') as file:
    read_data = pickle.load(file)

print(type(read_data), read_data)
