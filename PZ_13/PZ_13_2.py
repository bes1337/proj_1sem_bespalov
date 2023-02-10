# Вариант 1
# 2. В матрице отрицательные элементы возвести в квадрат.
from random import randint


def matrixPrint(mat):
    for i in range(len(mat)):
        print(mat[i])


matr1 = [[randint(-20, 20) for j in range(5)] for i in range(5)]
matr2 = [list(map(lambda x: x**2 if x < 0 else x, i)) for i in matr1]

print('Исходная матрица:')
matrixPrint(matr1)
print('Матрица с отричательными числами в квадрате:')
matrixPrint(matr2)