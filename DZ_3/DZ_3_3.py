"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    a_set = sorted(args)
    max_sum = a_set[-1] + a_set[-2]
    return max_sum


# проверка

print(my_func(10, 7, 6))

print(my_func(10, -1, 0))

print(my_func(10, 2, 5))
