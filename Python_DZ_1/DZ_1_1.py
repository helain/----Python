"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

a = 1
b = 4.5
a_str = 'строка'
i_set = {1, 2, 3, 4, 5}
a_dict = {1: 'one', 2: 'two', 3: 'three'}

user_int = int(input(print('Введите целое число: ')))
user_float = float(input(print('Введите число с точкой: ')))
user_str = input(print('Введите текст: '))

print(f'a = {a}')
print(f'Тип переменной - {type(a)}')

print(f'b = {b}')
print(f'Тип переменной - {type(b)}')

print(f'a_str = {a_str}')
print(f'Тип переменной - {type(a_str)}')

print(f'i_set = {i_set}')
print(f'Тип переменной - {type(i_set)}')

print(f'a_dict = {a_dict}')
print(f'Тип переменной - {type(a_dict)}')

print(f'Вы ввели целое число {user_int}')
print(f'Тип переменной - {type(a)}')

print(f'Вы ввели число с точкой {user_float}')
print(f'Тип переменной - {type(user_float)}')

print(f'Вы ввели текст {user_str}')
print(f'Тип переменной - {type(user_str)}')

