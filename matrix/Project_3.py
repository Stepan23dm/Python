import numpy as np

a = np.array([[1, 2, 3, 4],
             [2, 2, -4, 5]])

b = np.array([[1, 1, 1, 2],
             [2, 3, 5, 6]])

c = (a * 3) - (b * 4)

print(f'Матрица С: {c}')
print(f'Наименьший элемент матрицы С: {c.min()}')