import matplotlib.pyplot as plt
categories = ['A', 'B', 'C']

values = [50, 30, 20]

plt.pie(values, labels=categories, autopct='%1.1f%%')

plt.title("Pie Chart Example")

plt.show()