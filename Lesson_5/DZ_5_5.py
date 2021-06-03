"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('DZ_5_5_example.txt', 'w') as user_numbers:
    user_numbers.write(input('введите набор чисел через пробел: '))

with open('DZ_5_5_example.txt') as user_numbers:
    for line in user_numbers:
        numbers = line.split()
        user_sum = 0
        for i in numbers:
            user_sum += int(i)
        print('Сумма')
        print(user_sum)