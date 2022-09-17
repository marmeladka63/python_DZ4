# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from re import X
import sympy as sym

x = sym.Symbol('x')



k = int(input("введите число k="))
a=[]

for i in range(0,k):
    a.append(random.randint(0,100) )
    
print(a)

b = a[0]
for i in range (len(a)):
    b +=a[i]*x**k
    k = k-1
print(f'{b} = 0')
print(type(b))

f = open("Z4_4.txt", "w")
f.write(f'{b} = 0')
f.close()



