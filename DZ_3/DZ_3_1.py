"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

a = input(print('Введите число a: '))
b = input(print('Введите число b: '))

def div_func(*args):
    try:
        x1 = int(args[0])
        x2 = int(args[1])
        result = x1 / x2
        return result
    except ZeroDivisionError:
        print('Деление на ноль')
    except ValueError:
        print('Введены неверные данные')

print(div_func(a, b))
