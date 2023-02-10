# вариант 1
# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних строках и столбцах матрицы Matr2 произвольного размера.
from random import randint


def matrixPrint(mat):
    for i in range(len(mat)):
        print(mat[i])


matr1 = [[randint(-20, 20) for j in range(5)] for i in range(5)]
matr2 = [i[1:-1] for i in matr1]

print("Исходная матрица: ")
matrixPrint(matr1)

print("Полученная матрица: ")
matrixPrint(matr2)

