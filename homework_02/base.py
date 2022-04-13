from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 20
    fuel = 70
    fuel_consumption = 4

    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                return
            raise LowFuelError(self.started)

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance <= distance:
            expected = self.fuel - distance * self.fuel_consumption
            self.fuel = expected
        raise NotEnoughFuel()
