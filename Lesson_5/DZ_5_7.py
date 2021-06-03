"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

firm_dict = {}
profit_list = []
average_profit = {}
result_obj = []

with open('DZ_5_7_example.txt', encoding='utf8') as firm_list:
    for line in firm_list:
        firm = line.split()
        firm_profit = (int(firm[2]) - int(firm[3]))
        firm_dict.update({firm[0]: firm_profit})
        if firm_profit > 0:
            profit_list.append(firm_profit)

average_profit['average_profit'] = (sum(profit_list) / len(profit_list))
result_obj.append(firm_dict)
result_obj.append(average_profit)

with open('DZ_5_7_result.json', 'x') as file:
    json.dump(result_obj, file)
