import pandas as pd

data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Bishal"],
        "Age": [25, 30, 35, 40, 45, 50]
        }

df = pd.DataFrame(data)
print(df)

# Access column

print(df["Name"])
print(df["Age"])

# # Add a column

df["Salary"] = [50000, 60000]

print(df)

# # Filter rows

filtered = df[df["Age"] > 25]
print(filtered)


# filterr salary
filtered_salary = df[df["Salary"]>55000]
print(filtered_salary)


print(df.isnull().sum())
