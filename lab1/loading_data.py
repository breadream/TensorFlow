import numpy as np

xy = np.loadtxt('data-01-test-score.csv', delimiter=',', dtype = np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

# Make sure the shape and data are OK
print(x_data.shape,"\n", x_data, len(x_data))
print(y_data.shape,"\n", y_data)
