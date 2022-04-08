import matplotlib.pyplot as plt

Q = float(input('Введите значение Q (в нКл): '))
L = float(input('Введите значение L (в см): '))

def main(Q, L):
    e = float(8.85) * (10 ** (-12))
    mass1 = []
    mass2 = []

    r = 1
    while r < 10:
        res = ((r ** 3) * 10 ** (-2))
        mass1.append(res)
        r += 0.5
        E = 9 * ((2 * Q * (L * (10 ** (-2)))) / (res))
        mass2.append(E)
        print(f"Напряженность E электростатического поля при r = {res}: ", str(E))

    plt.title(r'$Напряженность$ $электрического$ $поля$')
    plt.plot(mass1, mass2, '-r', linewidth=3)
    plt.show()

if __name__ == "__main__":
    main(Q, L)