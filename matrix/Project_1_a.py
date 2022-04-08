import numpy as np
import scipy.linalg as la
from tabulate import tabulate as tbl

matrix_size = int(input('Введите размер матриц: '))

print('Введите значения для первой матрицы.')

a = []
for i in range(matrix_size):
    a.append([])
    for j in range(matrix_size):
        print(f"Введите элемент матрицы [{i+1}:{j+1}]")
        a[i] += [float(input())]

matrix_a = np.array(a) #Create array A
print('Введите значения для второй матрицы.')

b = []
for i in range(matrix_size):
    b.append([])
    for j in range(matrix_size):
        print(f"Введите элемент матрицы [{i+1}:{j+1}]")
        b[i] += [float(input())]

matrix_b = np.array(b) #Create array B

print("Вывод матрицы А:")
print(tbl(a))
print("Вывод матрицы B:")
print(tbl(b))

print(f'Определитель матрицы: {la.det(matrix_a)}') #1
sum_diagonal = np.trace(matrix_a)
print(f'Сумма диагональных элементов: {sum_diagonal}') #2
w, v = np.linalg.eigh(matrix_a)
print(f'Собственные значения: \n{w}') #3
print(f'Собственные вектора: \n{v}')
r = matrix_a.sum() - matrix_b.sum()
print(f'Разности суммы матриц: {r}') #4
print(f'Произведение матриц: \n{np.dot(matrix_a, matrix_b)}') #5
