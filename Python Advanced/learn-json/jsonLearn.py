# Json data are in key and value pair format
# Example of Json data
import json
person = {
    # Key: value
    "name": "Bishal",
    "age": 25,
    "hobbies": ["reading", "traveling", "coding"],
    "is_student": False
}

print("Type of person:", type(person))

# Convert Python dictionary to JSON string
json_string = json.dumps(person)
print(json_string)
print("Type of json_string:", type(json_string))

# Convert JSON string back to Python dictionary
person_dict = json.loads(json_string)
print(person_dict)
print("Type of person_dict:", type(person_dict))