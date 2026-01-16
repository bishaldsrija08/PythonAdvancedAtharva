expenses = [] # List to store expense records
from collections import defaultdict
import matplotlib.pyplot as plt

# Function to add a new expense
def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter expense date (YYYY-MM-DD): ")
    expenses.append({
        "category": category,
        "amount": amount,
        "date": date
    })
    

# Allow users to add multiple expenses
while True:
    add_expense()
    choice = input("Do you want to add another expense? (y/n): ")
    if choice.lower()!='y':
        break
    
    
# Display all recorded expenses
print("\nRecorded Expenses:")
for expense in expenses:
    print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")
    

# Summarize expenses by category
category_totals = defaultdict(float)
for expense in expenses:
    category_totals[expense['category']] += expense['amount']

# Display summary of each category
print("\nExpense Summary by Category:")
for category, total in category_totals.items():
    print(f"Category: {category}, Total Amount: {total}")
    

# Visualize expenses by category using a pie chart
categories = list(category_totals.keys())
ammounts = list(category_totals.values())

# Pie Chart
plt.bar(categories, ammounts, color = "skyblue")
plt.xlabel("Categories")
plt.ylabel("Total Amount")
plt.title("Expenses by Category")
plt.show()