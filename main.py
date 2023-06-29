import random

lenX = int(input('Введите число: '))
lenY = int(input('Введите число: '))

matrix = [[]] * lenX
for i in range(lenX):
    matrix[i] = [0] * lenX

for j in range(lenY):
    matrix[j] = [0] * lenY

for i in range(lenX):
    for j in range(lenY):
        matrix[i][j] = random.randint(10, 100)
    print(matrix[i])

m = int(input('Ввести номер строки: ')) #12.6 вывести все эелементы m-строки
print(matrix[m])


numberX = int(input()) # 12.16 найти разность элементов
numberY = int(input())
numberA = int(input())
numberB = int(input())
print(matrix[numberX][numberY])
print(matrix[numberA][numberB])

result = matrix[numberX][numberY] - matrix[numberA][numberB]
print('Разность эелемнтов', result)



 # 12.62 сумма элементов каждой сктроки

def filas(matrix):
    maxEl = [max(i) for i in matrix]
    minEl = [min(i) for i in matrix]
    print('Максимальный эелемент', maxEl) #12.90 Максимальный и минимальный элемент в каждой строке
    print('Минимальный элемент', minEl)
    summa = [sum(i) for i in matrix]
    print('Сумма каждой строки', summa)
filas(matrix)

