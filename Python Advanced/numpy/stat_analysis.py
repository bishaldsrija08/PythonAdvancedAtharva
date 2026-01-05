

import numpy as np


# Load data from a CSV file

data = np.genfromtxt('scores.csv', delimiter=",", skip_header=1)

# Basic statistical analysis
# mean
print("Mean:", np.mean(data))

# median
print("Median:", np.median(data))

# max data
print("Max:", np.max(data))


# min data
print("Min:", np.min(data))


# filter data
filtered_data = data[data > 50]
print("Filtered Data (greater than 50):", filtered_data)