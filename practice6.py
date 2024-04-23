import pickle
import gzip


# with open("large_file.txt", 'w') as file:
#     for i in range(100_000):
#         file.write(f"Line number {i+1} in large file.\n")

# with gzip.open('large_file.gz', 'wb') as gzip_file:
#     with open("large_file.txt", 'r') as txt_file:
#         data = txt_file.read()
#
#         serialized_data = pickle.dumps(data)
#         gzip_file.write(serialized_data)

# with open('large_file.pickle', 'wb') as pickle_file:
#     with open("large_file.txt", 'r') as txt_file:
#         data = txt_file.read()
#
#         pickle.dump(data, pickle_file)

with gzip.open("large_file.gz", 'rb') as file:
    serialized_data = file.read()
    data = pickle.loads(serialized_data)

    lines = data.split('\n')
    print(*lines[:10], sep='\n')