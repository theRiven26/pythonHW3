# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

n = int(input("enter count elements: "))
list_ = list()
for i in range(n + 1):
    list_.append(random.randint(0, 10))
print(*list_)
print(list_.count(int(input())))