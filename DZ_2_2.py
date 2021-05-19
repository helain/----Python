"""
2. Для списка реализовать обмен значений соседних элементов,
 т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
  При нечетном количестве элементов последний сохранить на своем месте.
  Для заполнения списка элементов необходимо использовать функцию input().
"""

start_list = []
result_list = []
list_element = 0


while True:
    list_element = (input(print('введите элемент списка, для завершения введите "stop"')))
    if list_element != 'stop':
        start_list.append(list_element)
    else: break

print('Начальный список')
print(start_list)


i = 0
while i != len(start_list):
    if i == len(start_list)-1:
        result_list.append(start_list[i])
        i += 1
    elif i%2 == 0:
        result_list.append(start_list[i+1])
        i += 1
    else:
        result_list.append(start_list[i-1])
        i += 1


print(result_list)
