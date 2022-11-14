# Вариант 1
# Дан список размера N. Найти номера тех элементов списка, которые больше своего
# правого соседа, и количество таких элементов. Найденные номера выводить в
# порядке их возрастания.
from random import *


def countList(n):
    a = [randint(1, 100) for i in range(n)]
    print(f'Ваш сипсок:\n{a}')
    count = []
    for j in range(1, n):
        if a[j - 1] > a[j]:
            count.append(j)
    print('Номера списка, значение которых больше правых от них:\n{}\nИх количество:\n{}'.format(count, len(count)))


try:
    length = int(input('Введите длину списка:'))
    countList(length)
except ValueError:
    print('Ошибка ввода значения')
