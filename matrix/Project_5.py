import numpy as np

a = np.array([[1, 2],
              [3, 4]])

c = np. array([[8, 1],
               [18, -1]])

y = np.linalg.solve(a, c)
print(f'X в данном уравнение равен: \n{y}')