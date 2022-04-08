import matplotlib.pyplot as plt
import math

R = 0.04
a = 1 * (10 ** (-9))
r = 0.1
r1 = 0
e = 8.85 * (10 ** (-12))

E = (1 / (4 * math.pi * e)) * ((2 * math.pi * r * R * a) / (((r ** 2) + (R ** 2)) ** (3 / 2)))

E1 = (1 / (4 * math.pi * e)) * ((2 * math.pi * r1 * R * a) / (((r1 ** 2) + (R ** 2)) ** (3 / 2)))

print(f'1) На расстоянии r = 0.1 м: {math.trunc(E)}'
      f'\n2) В центре кольца: {E1}'
      f'\n3) Максимальная напряженность поля при r = 0.1 м: {math.trunc(E)}'
      f'\n4) Минимальная напряженность поля при r = 0.1 м: {E1}')

def main():
    mass1 = []
    mass2 = []
    radius = 0
    while radius < 0.1:
        En = (1 / (4 * math.pi * e)) * ((2 * math.pi * radius * R * a) / (((radius ** 2) + (R ** 2)) ** (3 / 2)))
        radius += 0.000001
        mass1.append(En)
        mass2.append(radius)

    plt.title(r'$Напряженность$ $электрического$ $поля$')
    plt.plot(mass2, mass1, 'r-o', linewidth=3, markersize=4, markerfacecolor='b')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()