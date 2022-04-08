import matplotlib.pyplot as plt
import math
from tabulate import tabulate

q = 33.3 * (10 ** (-9))
r_zar = 5.01 * (10 ** (-6))
o = 75 * (10 ** (-6))
e0 = 8.85 * (10 ** (-12))
r = 0.01

mas_r = []
mas1 = []
mas2 = []
mas3 = []

while r <= 0.06:
    E = (q / (4 * math.pi * e0 * (r ** 2)))
    E1 = (r_zar / (2 * math.pi * e0 * r))
    E2 = (o / (2 * e0))
    mas_r.append(round(r, 2))
    r += 0.01
    mas1.append(E)
    mas2.append(E1)
    mas3.append(E2)

out_result = [['Точечный заряд', mas1[0], mas1[1], mas1[2], mas1[3], mas1[4]],
              ['Однородно заряженная нить', mas2[0], mas2[1], mas2[2], mas2[3], mas2[4]],
              ['Заряженная плоскость', mas3[0], mas3[1], mas3[2], mas3[3], mas3[4]],
              ]
headers = ['Расстояние (r, m)', mas_r[0], mas_r[1], mas_r[2], mas_r[3], mas_r[4]]
print(tabulate(out_result, headers, tablefmt='github'))

plt.plot(mas_r, mas1, 'r-o', linewidth=2, markersize=4, markerfacecolor='r', label=r'$Точечный$ $заряд$')
plt.plot(mas_r, mas2, 'b-o', linewidth=2, markersize=4, markerfacecolor='b', label=r'$Однородно$ $заряженная$ $нить$')
plt.plot(mas_r, mas3, 'g-o', linewidth=2, markersize=4, markerfacecolor='g', label=r'$Заряженная$ $плоскость$')
plt.title(r'$Напряженность$ $электрического$ $поля$ $E(r)$')
plt.legend(loc='best')
plt.grid()
plt.show()