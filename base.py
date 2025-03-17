from hw_2.exceptions import LowFuelError, NotEnoughFuel, CargoOverload

class Vehicle:
    def __init__(self, weight=0, fuel=70, fuel_consumption=12.0, **kwargs):
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        self._started = kwargs.get('started', False)

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._weight = value

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            raise ValueError("Топливо не может быть отрицательным")
        self._fuel = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value <= 0:
            raise ValueError("Расход топлива должен быть больше 0")
        self._fuel_consumption = value

    @property
    def started(self):
        return self._started

    def start(self):
        if self._started:
            raise ValueError("Двигатель уже запущен")
        if self._fuel > 0:
            self._started = True
        else:
            raise LowFuelError("Недостаточно топлива для запуска")

    def move(self, distance):
        if not self._started:
            raise ValueError("Двигатель не запущен.")
        
        needed_fuel = (distance / 100) * self._fuel_consumption
        if self._fuel >= needed_fuel:
            self._fuel -= needed_fuel
        else:
            raise NotEnoughFuel(
                f"Недостаточно топлива для движения: требуется {needed_fuel}, доступно {self._fuel}"
            )