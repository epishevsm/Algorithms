# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/11PvzXsyN7pVuQf04Do4A79oIbQp1PiQU/view?usp=sharing

number = int(input('Введите натуральное число: '))
even_num = 0
odd_num = 0
while number > 0:
    if number % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    number = number // 10
print(f'В введенном вами числе {even_num} четных чисел, и {odd_num} нечетных')


# Рекурсия: честно признаюсь в голове сложно ложится применение рекурсии,
# поэтому мой пример основан на том, что я увидел на уроке.

def recursion(number, rec_even_num=0, rec_odd_num=0):
    if number == 0:
        return rec_even_num, rec_odd_num
    if number % 2 == 0:
        rec_even_num += 1
    else:
        rec_odd_num += 1
    number = number // 10
    return recursion(number, rec_even_num, rec_odd_num)


number = int(input('Введите натуральное число: '))
print(f'в вашем числе четных и нечетных чисел: {recursion(number)}')
