"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        print(f'{self.name} движется')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')

    def is_this_a_police(self):
        if self._is_police is True:
            print('Это полицейская машина')
        else:
            print('Это не полицейская машина')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость, допустимая скорость 60 км/ч, ваша скорость {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed}')

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость, допустимая скорость 40 км/ч, ваша скорость {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

family_car = TownCar(0, 'black', 'Family car')
print(f'{family_car.name}. Цвет - {family_car.color}')
family_car.is_this_a_police()
family_car.go()
family_car.speed = 50
family_car.show_speed()
family_car.turn('налево')
family_car.speed = 70
family_car.show_speed()
family_car.stop()

bus = WorkCar(50, 'yellow', 'Автобус')
bus.go()
print(f'{bus.name}. Цвет - {bus.color}')
bus.show_speed()

patrol = PoliceCar(0, 'White', 'Патрульная машина')
print(f'{patrol.name}. Цвет - {patrol.color}')
patrol.is_this_a_police()
