import json

user_data = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
    "hobbies": input("Enter your hobbies (comma separated): ").split(", "),
    "favorite_colors": input("Enter your favorite colors (comma separated): ").split(", "),
    "favourite_movies": input("Enter your favourite movies (comma separated): ").split(", ")
    # .split creates a list from the comma-separated string
}

# Save to JSON file
# Write mode overwrites existing content
with open("Python Advanced/learn-json/user_data.json", "w") as file:
    json.dump(user_data, file, indent=4)
    
    
# Load from JSON file and print
with open("Python Advanced/learn-json/user_data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)