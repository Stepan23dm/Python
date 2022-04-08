import numpy as np

#Ввод координатов 1-ого вектора
print('Введите координаты x, y, z вектора - A.')
massiv_a = []
for i in range(3):
    massiv_a.append([])
    for j in range(1):
        print(f"Введите элемент матрицы [{i + 1}:{j + 1}]")
        massiv_a[i] += [float(input())]

matrix_a = np.squeeze(np.asarray(massiv_a))

#Ввод координатов 2-ого вектора
print('Введите координаты x, y, z вектора - B.')
massiv_b = []
for i in range(3):
    massiv_b.append([])
    for j in range(1):
        print(f"Введите элемент матрицы [{i + 1}:{j + 1}]")
        massiv_b[i] += [float(input())]

matrix_b = np.squeeze(np.asarray(massiv_b))

print(f'Скалярное произведение векторов: {np.dot(matrix_a, matrix_b)}')
print(f'Векторное произведение векторов: {np.cross(matrix_a, matrix_b)}')