"""
1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_date(cls, date):
        list_date = date.split('-')
        day = int(list_date[0])
        month = int(list_date[1])
        year = int(list_date[2])
        return day, month, year


    @staticmethod
    def data_validation(*args):
        day, month, year = args
        month_list = list(range(1,13))
        day_list = list(range(1, 32))
        if month not in month_list:
            return print('Значение "месяц" не верное')
        if month in (1, 3, 5, 7, 8, 10, 12):
            if day not in day_list:
                return print('Значение "день" не верное')
        elif month in (4, 6, 9, 11):
            if day not in day_list[:30]:
                return print('Значение "день" не верное')
        else:
            if abs(year-2000)%4 == 0:
                if day not in day_list[:29]:
                    return print('Значение "день" не верное')
            else:
                if day not in day_list[:28]:
                    return print('Значение "день" не верное')
        return print('Все значения верны')


day, month, year = Date.convert_date('31-04-2020')
print(type(day))
print(type(month))
print(type(year))

#проверка на число не пройдена в апреле 30 дней
day, month, year = Date.convert_date('31-04-2020')
print('31-04-2020')
Date.data_validation(day, month, year)

#роверка на месяц не пройдена
day, month, year = Date.convert_date('31-15-2020')
print('31-15-2020')
Date.data_validation(day, month, year)

#проверка на день не пройдена, год не высокосный
day, month, year = Date.convert_date('29-02-2021')
print('29-02-2021')
Date.data_validation(day, month, year)
#проверки пройдены, год высокосный
day, month, year = Date.convert_date('29-02-2020')
print('29-02-2020')
Date.data_validation(day, month, year)




