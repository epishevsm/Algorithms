# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -500
MAX_ITEM = -100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Создан массив {array}')

idx_min_num = None
super_min_num = float('-inf')
for i, j in enumerate(array):
    if 0 > j > super_min_num:
        super_min_num = j
        idx_min_num = i

print(f'Индекс максимального отрицательного числа {idx_min_num} само число {super_min_num}')
