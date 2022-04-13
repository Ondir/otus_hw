"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, engine):
        self.engine = Engine()

    def set_engine(self):
        self.engine = Engine()
