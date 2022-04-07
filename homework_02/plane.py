"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = Vehicle()

    def load_cargo(self, add_num):
        add_num += self.cargo

        if self.max_cargo > add_num:
            raise CargoOverload()

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp