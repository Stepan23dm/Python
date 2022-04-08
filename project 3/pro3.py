import matplotlib.pyplot as plt
import math as m

q1 = 20
q2 = 30

k = 9 * (10 ** 9)
r = 0.02

mas1 = []
mas2 = []
while r <= 0.1:
    f = k * ((m.fabs(q1 * q2) / (r ** 2)))
    r += 0.005
    mas1.append(f)
    mas2.append(r)

plt.title(r'$Напряженность$ $электрического$ $поля$')
plt.plot(mas1, mas2, '-r', linewidth=3)
plt.show()

