# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://drive.google.com/file/d/11PvzXsyN7pVuQf04Do4A79oIbQp1PiQU/view?usp=sharing

number = int(input('Введите число: '))
x = 0
while number > 0:
    x = x * 10 + number % 10
    number = number // 10
print(x)

