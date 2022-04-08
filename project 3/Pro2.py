import math as m

r1 = 0.15
r2 = 0.1
r3 = float(input('Введите значение r3 (в м): '))
r4 = float(input('Введите значение r4 (в м): '))

def out_result(x, y):
   try:
       q1 = 2 * (10 ** (-9))
       q2 = -3 * (10 ** (-9))
       e = 8.85 * (10 ** (-12))
       l = 0.2
       cos_b = -((l ** 2) - (x ** 2) - (y ** 2)) / (2 * x * y)
       res = (1 / (4 * m.pi * e)) * m.sqrt((q1 ** 2 / (x ** 4)) + (q2 ** 2 / (y ** 4)) - (((2 * m.fabs(q1) * m.fabs(q2) / (x ** 2 * y ** 2))) * cos_b))
       print(res / 1000)
   except:
       print('Error')

print('___1___')
out_result(r1, r2)
print('___2___')
out_result(r3, r4)

