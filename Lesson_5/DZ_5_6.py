"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from typing import Dict, Any

result_dict = {}

with open('DZ_5_6_example.txt', encoding='utf8') as user_lessons:
    for line in user_lessons:
        lesson_name, *lessons = line.split()
        overall_lessons = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '-' ]
        lesson_name = lesson_name.rstrip(':')
        result_dict.update({lesson_name: sum(overall_lessons)})

print(result_dict)



