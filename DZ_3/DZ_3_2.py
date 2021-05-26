"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

first_name = input(print('Введите имя: '))
last_name = input(print('Введите фамилию: '))
year_of_birth = input(print('Введите год рождения: '))
occup_city = input(print('Введите город проживания: '))
email = input(print('Введите электронную почту: '))
phone = input(print('Введите номер телефона: '))


def user_info(f_name, l_name, year, city, f_email, f_phone):
    result = (f'{f_name} {l_name}, '
              f'год рождения: {year}, '
              f'город проживания: {city}, '
              f'контактная информация: {f_email}, {f_phone} ')
    return print(result)


user_info(f_name=first_name, l_name=last_name, year=year_of_birth, city=occup_city, f_email=email, f_phone=phone)

