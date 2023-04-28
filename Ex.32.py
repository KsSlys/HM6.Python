''''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint
n = int(input())
min = int(input())
max = int(input())

list_1 = [randint (0,10) for i in range(n)]
print(list_1)

res = []
for i in range(len(list_1)):
    if list_1[i] > min and list_1[i] < max:
        res.append(i)
print(*res)