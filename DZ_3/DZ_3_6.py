"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
result_message = []


def cap_letter(word):
    result_word = word.capitalize()
    return result_word


user_massage = input(print('введите список слов через пробел: ')).split()

for message_word in user_massage:
    result_message.append(cap_letter(message_word))

print('Исходная строка')
print(*user_massage)

print('Итоговая строка')
print(*result_message)
