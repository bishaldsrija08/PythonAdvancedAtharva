
import csv
count = 0
with open("./data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        count = count+1
        print(row)

print(f"Total rows: {count}") 
  
with open('./data.csv', 'r') as file:
    for line in file:
        print(line.strip())