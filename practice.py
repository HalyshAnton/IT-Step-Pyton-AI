import json


data = {"name": "John", 'age': 42, "info": {"city": "Kharkiv", "birthday": "2001"}}


# with open("data.json", 'w') as file:
#     json.dump(data, file)


with open("data.json", 'r') as file:
    read_data = json.load(file)

print(read_data)
