#Задание 1
from sys import argv

script_name, hours, stavka, premia = argv
print("Имя скрипта:", script_name)
print("Выработка в часах:", hours)
print("Ставка в час:", stavka)
print("Премия:", premia)

zp = (int(hours) * int(stavka)) + int(premia)
print(f"Заработная плата {zp}")

#Задание 2
list1 = [2,6,3,34,46,32,54,89,90,76]
list2 = [el for el in list1 if el > list1[list1.index(el)-1]]
print(list2)

#Задание 3
n = range(20, 241)
n1 = [el for el in n if el%20==0 or el%21==0]
print(n1)

#Задание 4
list = [3, 4, 3, 8, 8, 1]
list2 = [el for el in list if list.count(el) == 1]
print(list2)

#Задание 5
from functools import reduce

list = [el for el in range(100, 1001, 2)]
print("Список чётных чисел:", list)
print("Произведение всех чисел:", reduce(lambda x,y: x*y, list))

#Задание 6
#a)
from itertools import cycle

list = [5, 9, 1, 6, 2, 5, 8, 4]
for i in cycle(list):
    print(i, end=' ')
#b)
from itertools import count

n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')

#Задание 7
from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break