"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
average_salary = []
low_employee = []
with open('DZ_5_3_example.txt', encoding='utf8') as salary:
    for line in salary:
        employee = line.split()
        average_salary.append(int(employee[1]))
        if int(employee[1]) < 20000:
            low_employee.append(employee[0])
avg_sal = sum(average_salary) / len(average_salary)

print('Сотрудники с зарплатой меньше 20000:')
print(low_employee)
print('Средняя зарплата сотрудников')
print(avg_sal)


