"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
https://drive.google.com/file/d/1OUiNWCs2Cnrpy3lykDJOxvc-_HglLLtr/view?usp=sharing
"""

print("Задача: вывести уравнение прямой")
print("Введите координаты первой точки x1, y1")
x1 = float(input('x1: '))
y1 = float(input('y1 : '))
print("Введите координаты второй точки x2, y2")
x2 = float(input('x2: '))
y2 = float(input('y2 : '))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f'y = {round(k, 2)}*x + {round(b, 2)}')
