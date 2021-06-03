"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('DZ_5_2_example.txt') as user_file:
    line_numb = 0
    for line in user_file:
        line_numb += 1
        line_str = line.split()
        words = len(line_str)
        print(f'Строка {line_numb} - {words} слов(а)')
    print(f'Всего строк в файле - {line_numb}')