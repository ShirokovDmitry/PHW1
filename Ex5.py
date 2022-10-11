# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
import math
Ax = int(input('Введите координату A x: '))
Ay = int(input('Введите координату A y: '))

Bx = int(input('Введите координату B x: '))
By = int(input('Введите координату B y: '))

distance = (Bx - Ax)**2 + (By - Ay)**2
x = math.sqrt(distance)
print(round(x, 3))
