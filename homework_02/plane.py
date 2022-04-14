"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 80

    def __init__(self, weight, fuel, fuel_consumption, max_cargo=max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_num):
        self.cargo += add_num
        if self.max_cargo < self.cargo:
            self.cargo = 0
            raise CargoOverload()

    def remove_all_cargo(self):
        temp = self.cargo
        self.cargo = 0
        return temp