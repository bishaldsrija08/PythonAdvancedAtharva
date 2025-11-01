import json

data = {
    "name": "Bishal Rijal",
    "age": 24,
    "city": "Chitwan",
    "isStudent": False
}

# Write JSON data to a file
with open("data.json", "w") as file:
    # Data is converted from Python dictionary to JSON format
    json.dump(data, file)

# Read JSON data from a file
with open("data.json", "r") as file:
    # Data is loaded as a Python dictionary
    loaded_data = json.load(file)

print(loaded_data)