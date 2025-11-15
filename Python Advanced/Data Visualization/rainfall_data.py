import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [3.2, 3.8, 4.1, 2.9, 2.5, 1.8, 1.5, 1.7, 2.0, 2.4, 3.0, 3.5]

plt.plot(months, rainfall, marker='*', linestyle=':', color='b')
plt.title('Monthly Rainfall Data')
plt.xlabel('Months')
plt.ylabel('Rainfall (inches)')
plt.show()