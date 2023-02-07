# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input("enter count elements: "))
list_ = list()
numUser = int(input("enter number: "))
minDiff = 0
minNum  = 0
for i in range(n + 1):
    num = random.randint(0, 10)
    list_.append(num)
    if i == 0:
        minDiff = num - numUser
        minDiff = (minDiff*minDiff)**0.5
        minNum = num
    if minDiff > ((num - numUser)**2)**0.5:
        minDiff = ((num - numUser)**2)**0.5
        minNum = num
print(*list_)
print(minNum)
