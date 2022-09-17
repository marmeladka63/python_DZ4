# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import collections, functools, operator
import sympy as sym

f = open("Z4_4.txt",'r')
equ1 = f.readline()
print (equ1)

g = open("Z4_41.txt",'r')
equ2 = g.readline()
print (equ2)
# st = ''
def Dict(st):
    st = st.replace('= 0',"+ 0") #меняем символ 
    s=st.replace("*x**", " + ") #меняем символ
    s1=s.replace("*x", " + 1") # меняем символ
    text = s1.split('+') # разделяем список на символы через разделитель "+"
    text = list(map(int,text)) # преобразовываем символы в числа  

    myDict = ({text[i + 1]:text[i]  for i in range(0, len(text), 2)}) # получаем словарь с ключами и значениями
    return (myDict)

print (Dict(equ1))
print (Dict(equ2))

dict1 = Dict(equ1)
dict2 = Dict(equ2)

dict3 = dict1.copy()
for k,v in dict2.items():
    dict3[k] =dict3.get(k,0)+v #складываем цифры в двух словарях по ключам
    
print(dict3)

x = sym.Symbol('x')
# И дальше у меня затык.Хочу циклом пройти по ключам и значениям словаря и
#  засунуть их в формулу многочлена. При b += выпадает ошибка что тип mul 
# не итерируется. Почитала преобразовани словарей :) ничего не помогло. 
#подскажи как сделать. Вывод получилось сделать, но он тупой с костылями
#  и лишними знаками и не в файл :)
b = []
for key,valu in dict3.items():
    b =valu*x**key
    print(f'{b}+', end='')
    
 






