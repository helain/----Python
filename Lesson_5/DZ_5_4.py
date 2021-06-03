"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

numb_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('DZ_5_4_example.txt', 'r') as text_f:
    for line in text_f:
        text_line = line.split()
        r_word = numb_dict[text_line[0]]
        with open('DZ_5_4_result.txt', 'a', encoding='utf8') as result:
            result.write(f'{r_word} {text_line[1]} {text_line[2]}\n' )
