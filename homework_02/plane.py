"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 3
    max_cargo = 80

    def __init__(self, weight, fuel, fuel_consumption, max_cargo=max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_num):
        add_num += self.cargo

        if self.max_cargo < add_num:
            raise CargoOverload()

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp