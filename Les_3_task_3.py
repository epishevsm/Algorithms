# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Создан массив {array}')


min_inx = 0
max_idx = 0

for i, j in enumerate(array):
    if j < array[min_inx]:
        min_inx = i
    elif j > array[max_idx]:
        max_idx = i
print(f'минимаотное число {array[min_inx]} под индексом {min_inx}\n'
      f'максимальное число {array[max_idx]} под индексом {max_idx}')
array[max_idx], array[min_inx] = array[min_inx], array[max_idx]
print(f'поменяли местами максимальное и минимальное число {array}')
