import random
import timeit
import cProfile


def test_1(SIZE):
    MIN_ITEM = 1
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    min_inx = 0
    max_idx = 0

    for i, j in enumerate(array):
        if j < array[min_inx]:
            min_inx = i
        elif j > array[max_idx]:
            max_idx = i

    array[max_idx], array[min_inx] = array[min_inx], array[max_idx]
    return array


# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Les_4_task_1.py:6(test_1)
#      1    0.000    0.000    0.000    0.000 Les_4_task_1.py:9(<listcomp>)
#     10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     10    0.000    0.000    0.000    0.000 random.py:244(randint)
#     10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# print(timeit.timeit('test_1(10)', number=1000, globals=globals()))  # 0.006928500000000004
# print(timeit.timeit('test_1(100)', number=1000, globals=globals()))  # 0.061448600000000006
# print(timeit.timeit('test_1(1000)', number=1000, globals=globals()))  # 0.5965638
# print(timeit.timeit('test_1(10000)', number=1000, globals=globals()))  # 5.9644636


def test_2(SIZE):
    MIN_ITEM = 1
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array


#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:42(test_2)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:45(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# print(timeit.timeit('test_2(10)', number=1000, globals=globals()))  # 0.006439300000000037
# print(timeit.timeit('test_2(100)', number=1000, globals=globals()))  # 0.05770129999999973
# print(timeit.timeit('test_2(1000)', number=1000, globals=globals()))  # 0.5579283999999998
# print(timeit.timeit('test_2(10000)', number=1000, globals=globals()))  # 5.5255393

# этот вариант работает немного быстрее и, как и прочие варианты ммеет сложность O(n). Сам вариант
# удобнее в написании? поэтому при всех равных и с учетом более высокой скорости считаю его опримальным.
#


def test_3(SIZE):
    MIN_ITEM = 1
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array


#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:76(test_3)
#         1    0.000    0.000    0.000    0.000 Les_4_task_1.py:79(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# print(timeit.timeit('test_3(10)', number=1000, globals=globals()))  # 0.006787800000001454
# print(timeit.timeit('test_3(100)', number=1000, globals=globals()))  # 0.06137709999999963
# print(timeit.timeit('test_3(1000)', number=1000, globals=globals()))  # 0.6077557999999996
# print(timeit.timeit('test_3(10000)', number=1000, globals=globals()))  # 6.033512399999999

cProfile.run('test_1(1000)')
cProfile.run('test_2(1000)')
cProfile.run('test_3(1000)')
