# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность
# первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.


from itertools import cycle
from random import randrange
from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        colors = {'red': 7, 'yellow': 2, 'green': 1}
        colors_list = list(colors)

        previous_color = None

        for color in cycle(colors):
            if randrange(1, 6) == 3:
                color = 'red'

            if previous_color and previous_color != colors_list[colors_list.index(color) - 1]:
                raise ValueError('Your color is wrong')

            self.set__color(color)
            print(self.__color)
            sleep(colors[color])

            previous_color = color

    def set__color(self, color):
        self.__color = color


new_obj = TrafficLight()

new_obj.running()
