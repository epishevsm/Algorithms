# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(f'Создан массив {array}')

repetitive_num = array[0]
count = 0

for i in range(len(array)):
    x = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            x += 1
    if x > count:
        count = x
        repetitive_num = array[i]
print(f'Число {repetitive_num} повторяется в массиве чаще остальных: {count} раз(а)  ')
