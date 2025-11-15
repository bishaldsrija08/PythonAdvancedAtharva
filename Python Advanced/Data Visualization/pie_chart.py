import matplotlib.pyplot as plt

sizes = [25, 30, 20, 25]
labels = ["Math", "Science", "English", "Art"]
colors = ["skyblue", "blue", "green", "red"]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Student Subject Preferences')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()