from abc import ABC
from exceptions import LowFuelError


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = int(weight)
        self.fuel = int(fuel)
        self.fuel_consumption = int(fuel_consumption)

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
            raise LowFuelError()

    def move(self, distance):
         max_distance = self.fuel // self.fuel_consumption
         expected = self.fuel - max_distance * self.fuel_consumption


    def __str__(self):
        return


first_test = Vehicle(False, 10, 2, 10)

print(first_test.move)