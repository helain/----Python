"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

n = int(input(print('Введите целое положительное число')))

if n < 0:
    n = int(input(print('Введено некорректное значениею Введите положительное число')))

m = set(str(n))

print(f'Самая большая цифра в числе {n} - {max(m)}')