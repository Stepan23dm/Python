import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
E = float(1.5)

R = 0
i = 0
R_matrix = []
I_matrix = []
while i < 10:
    i += 1
    R += 1
    R1 = 3 * R
    R2 = 4 * R
    R3 = 3 * R
    R4 = 4 * R
    R5 = 2 * R
    R_matrix.append(R)
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
    I_matrix.append(X[0])

plt.scatter(R_matrix, I_matrix)
plt.plot(R_matrix, I_matrix)
plt.show()





