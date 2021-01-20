"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
https://drive.google.com/file/d/1OUiNWCs2Cnrpy3lykDJOxvc-_HglLLtr/view
"""
a = int(input('Введите число от 1 до 26: '))
a = ord('a') + a - 1
print(f'Вашему числу соответствует буква {chr(a)}')
