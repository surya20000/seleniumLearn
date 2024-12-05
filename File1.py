import json

# def read_data_from_file(file_path):
#     with open(file_path,'r') as file:
#         data = json.load(file)
#     return data

# file_path = "file.json"
# data = read_data_from_file(file_path)
# print(data)


# Function to write data to a JSON file
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

file_path = 'file2.json'
data = [{"name":"Geek","type":"Religion"}]

write_json_file(file_path, data)
print("data written")
