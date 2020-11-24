# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


import sys
from random import randrange


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.get_car_name()} has run')

    def stop(self):
        print(f'{self.get_car_name()} has stopped')

    def turn(self, direction):
        print(f'{self.get_car_name()} has turned {direction}')

    def show_speed(self):
        print(f'Your speed is {self.speed} km/h')

    def get_car_name(self):
        return (f'Police car ' if self.is_police else f'Car ') + self.name

    def is_speed_exceeded(self):
        return self.max_speed and self.speed > self.max_speed

    def show_speed_exceeded_warning(self):
        print(f'You exceeded speed limit by {self.speed - self.max_speed} km/h')

    def handle_speed(self):
        if self.is_speed_exceeded():
            self.show_speed_exceeded_warning()
        else:
            Car.show_speed(self)


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        self.handle_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        self.handle_speed()


class PoliceCar(Car):
    pass


for car in [TownCar(randrange(50, 90), 'blue', 'Volvo'),
            SportCar(randrange(200, 450), 'red', 'Bugatti'),
            WorkCar(randrange(30, 50), 'orange', 'Ford'),
            PoliceCar(randrange(0, sys.maxsize), 'blue-white', 'Ford-RS', True)]:
    car.stop()
    car.go()
    car.turn(['Right', 'Left', 'Straight', 'Around'][randrange(0, 4)])
    car.show_speed()
    print()
