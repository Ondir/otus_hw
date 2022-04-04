from abc import ABC
from exceptions import LowFuelError


class Vehicle(ABC):
    def __init__(self, started, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started:
            pass
        elif self.fuel > 0:
            raise LowFuelError()

    def move(self):
        distance = self.fuel//self.fuel_consumption
        return distance

    def __str__(self):
        return     


first_test = Vehicle(False, 10, 2, 10)

print(first_test.move)