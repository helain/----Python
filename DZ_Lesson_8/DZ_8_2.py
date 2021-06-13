"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""

class User_error(Exception):
    def __init__(self, error_massage):
        self.error_massage = error_massage

while True:
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
        if b == 0:
            raise User_error('Деление на ноль невозможно. Повторите ввод:\n')
        else:
            x = a/b
            print('Результат деления - ', x)
            break
    except User_error as err:
        print(err)
    except ValueError:
        print("Некорректные данные. Повторите ввод: ")





