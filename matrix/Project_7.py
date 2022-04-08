import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
#Ввод переменных
R = float(input('Введите значение R: '))
E = float(input('Введите значение e: '))

R1 = 3 * R
R2 = 4 * R
R3 = 3 * R
R4 = 4 * R
R5 = 2 * R

A = np.array([[1, -1, 0, 0, -1, 0],
              [0, 1, -1, -1, 0, 0],
              [0, 0, 0, 1, 1, -1],
              [0, R1, R2, 0, 0, 0],
              [0, R1, 0, R3, -R4, 0],
              [0, 0, R2, -R3, 0, -R5]])

B = np.array([[0],
              [0],
              [0],
              [E],
              [0],
              [0]])

X = np.linalg.solve(A, B)

print('Значение I: ' + str(X[0]))
print('Значение I1: ' + str(X[1]))
print('Значение I2: ' + str(X[2]))
print('Значение I3: ' + str(X[3]))
print('Значение I4: ' + str(X[4]))
print('Значение I5: ' + str(X[5]))



