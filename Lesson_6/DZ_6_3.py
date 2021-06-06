"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    @property
    def income(self):
        return self._income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f'Имя работника - {self.surname} {self.name}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print('Общий доход ', total_income)


worker_income = {'wage': 10000, 'bonus': 5000}
junior_worker_income = {'wage': 80000, 'bonus': 3000}
senior_worker_income = {'wage': 20000, 'bonus': 10000}

john_smith = Position('John', 'Smith', 'worker', worker_income)
mike_jones = Position('Mike', 'Jones', 'Junior worker', junior_worker_income)
jane_andrews = Position('Jane', 'Andrews', 'Senior worker', senior_worker_income)

john_smith.get_full_name()
print('Должность - ', john_smith.position)
print(f'Доход:\n'
      f'Оклад - {john_smith.income["wage"]}\n'
      f'Бонус - {john_smith.income["bonus"]}')
john_smith.get_total_income()

mike_jones.get_full_name()
print('Должность - ', mike_jones.position)
print(f'Доход:\n'
      f'Оклад - {mike_jones.income["wage"]}\n'
      f'Бонус - {mike_jones.income["bonus"]}')
mike_jones.get_total_income()

jane_andrews.get_full_name()
print('Должность - ', jane_andrews.position)
print(f'Доход:\n'
      f'Оклад - {jane_andrews.income["wage"]}\n'
      f'Бонус - {jane_andrews.income["bonus"]}')
jane_andrews.get_total_income()