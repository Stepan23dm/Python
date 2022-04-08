import numpy as np

a = np.array([[1, 2, 3, 2], [2, 3, 1, 1], [1, 4, 4, 3], [2, 5, 3, 1]])

b = np.array([[4], [-1], [3], [-3]])

x = np.linalg.solve(a, b)

print(x)