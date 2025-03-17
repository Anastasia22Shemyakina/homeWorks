from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight=10000, fuel=200.0, fuel_consumption=50.0, cargo=0, max_cargo=1000, **kwargs):
        super().__init__(weight, fuel, fuel_consumption, **kwargs)
        self._max_cargo = max_cargo
        self._cargo = cargo

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, value):
        if value < 0:
            raise ValueError("Максимальный груз не может быть отрицательным")
        self._max_cargo = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if value < 0:
            raise ValueError("Груз не может быть отрицательным")
        if value > self._max_cargo:
            raise CargoOverload("Превышен максимальный грузоподъёмность")
        self._cargo = value

    def load_cargo(self, amount):
        if self._cargo + amount > self._max_cargo:
            raise CargoOverload("Превышен максимальный грузоподъёмность")
        self._cargo += amount

    def remove_all_cargo(self):
        old_cargo = self._cargo
        self._cargo = 0
        return old_cargo