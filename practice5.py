import pickle
import gzip


data = {"logins": ["hjlk", "jkhj", "hjkj"],
        "passwords": ["2132", "4546843", 13451],
        "info": {"version": "1.0",
                 "date release": "2024"}}


with gzip.open("data.gz", 'wb') as file:
    serialized_data = pickle.dumps(data)
    file.write(serialized_data)


with gzip.open('data.gz', 'rb') as file:
    serialized_data = file.read()
    read_data = pickle.loads(serialized_data)

print(type(read_data), read_data)