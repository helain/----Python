"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Department:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.content = {}
        self.company_name = 'Наша компания'

    def transfer(self, from_department, to_department):



class Equipment:
    def __init__(self, name):
        self.name = name
        self.type = 'Имущество'
        self.owner = 'Наша компания'


class Warehouse(Department):
    def __init__(self, name, type):
        super().__init__(name, type)

    # получение оборудования на склад
    def getting(self, equipment_name, equipment_count):
        equipment_name = input('Введите наименование товара')
        equipment_count = int('Введите количество ')
        if equipment_name in self.content:
            self.content[equipment_name] += equipment_count
        else:
            self.content[equipment_name] = equipment_count

class Office(Department):
    def __init__(self, name, type):
        super().__init__(name, type)

class OfficeEquipment(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Офисная техника'


main_warehouse = Warehouse('Главный склад', 'Склады')
main_office = Office('Главный офис', 'Офисы')
printer = OfficeEquipment('Принтер')
scanner = OfficeEquipment('Сканер')
copy_machine = OfficeEquipment('Ксерокс')

