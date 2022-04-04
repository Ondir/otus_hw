"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = Vehicle()

    def load_cargo(self):
        pass