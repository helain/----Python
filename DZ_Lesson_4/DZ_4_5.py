"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

"""версия для проверки"""
# result_list = [el for el in range(1, 11, 2)]

result_list = [el for el in range(100, 1001, 2)]
result = reduce(lambda x, y: x * y, result_list)

print(result_list)
print(result)
