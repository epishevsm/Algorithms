"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
https://drive.google.com/file/d/1OUiNWCs2Cnrpy3lykDJOxvc-_HglLLtr/view?usp=sharing
"""

i = int(input('Введите трёхзначное целое число: '))

a = i // 100
b = i // 10 % 10
c = i % 10
sum = a + b + c
multi = a * b * c
print(f'Сумма чисел введенного Вами числа равна: {sum}')
print(f'Произведение чисел введенного Вами числа равна: {multi}')



