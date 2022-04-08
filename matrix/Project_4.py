import numpy as np

massiv_a = np.array([[2, -4],
              [3, 5],
              [-1, 0]])

arr_a = matrix_b = np.squeeze(np.asarray(massiv_a))
A = arr_a.transpose()

massiv_b = np.array([[1, 2, 7],
              [-3, -4, 0],
              [5, 2, 1]])

arr_b = matrix_b = np.squeeze(np.asarray(massiv_b))
B = arr_b.transpose()

massiv_c = np.array([[6, -3, 9],
              [4, -5, 2],
              [8, 1, 5]])

arr_c = matrix_b = np.squeeze(np.asarray(massiv_c))

res1 = A * 2
res2 = A.dot(arr_c)
res3 = res1.dot(B)
res = res2 - res3
print(f'Минимальный элемент в матрице D: {res.min()}')
