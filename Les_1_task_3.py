"""
Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
https://drive.google.com/file/d/1OUiNWCs2Cnrpy3lykDJOxvc-_HglLLtr/view?usp=sharing
"""
import random
print("введите два целых числа от и до какого будет генерироваться случайное целое число")
int_a = int(input('Первое число: '))
int_b = int(input('Второе число: '))

print("введите два вещественных числа от и до какого будет генерироваться случайное вещественных число")
float_a = float(input('Первое число: '))
float_b = float(input('Второе число: '))

print("введите две буквы от "'a'" до "'z'" от и до какой будет генерироваться случайная буква")

letter_a = ord(input('Введите первую букву: '))
letter_b = ord(input('Введите вторую букву: '))

int_f = random.randint(int_a, int_b)
float_f = random.uniform(float_a, float_b)
letter_f = random.randint(letter_a, letter_b)

print(f'Случайное целое число: {int_f}\nСлучайное вещественное число: {round(float_f, 3)}\nСлучайная буква: {chr(letter_f)}')
