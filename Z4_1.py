# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141




def π(d):   
    i = len(d) - d.index('.') - 1 #считаем количество цифр после точки у числа d
    π = str((4/1)-(4/3)+(4/5)-(4/7)+(4/9)-(4/11)+(4/13)-(4/15)) #Используя ряд Грегори-Лейбница вычислим π. У формулы не хватает итераций, поэтоиу точность низкая. Взяла для примера не много :)
    j = π.index(".") #считаем количество цифр у числа π до запятой
    π_round = π[:j+i+1] #делаем срез 
    print(π_round)
    
d = str(input("введите точность вычисления d="))
π(d)
