# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# https://drive.google.com/file/d/11PvzXsyN7pVuQf04Do4A79oIbQp1PiQU/view?usp=sharing

for i in range(32, 128):
    if i % 10 == 0:
        print(f'\t{i}-{chr(i)}')
    else:
        print(f'\t{i}-{chr(i)}', end='')
