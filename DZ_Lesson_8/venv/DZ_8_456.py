"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
# Warehouse.content = {eq_type:{eq_name:{model:{count:''}}}}

class Warehouse:
    equipment_units = {}

    @classmethod
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]['count' += unit_count

    @classmethod
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]['count']
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]['count'] -=unit_count


class Equipment:
    def __init__(self, name, model, eq_type, count = 0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in [int, float]:
                self.count = 0
                raise ValueError
        except ValueError:
            print('Неверный формат данных')
        else:
            self.count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info[self.name]
            if