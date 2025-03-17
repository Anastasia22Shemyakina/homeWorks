
class LowFuelError(Exception):
    def __init__(self, message="Недостаточно топлива для запуска"):
        self.message = message


class NotEnoughFuel(Exception):
    def __init__(self, message="Недостаточно топлива для движения"):
        self.message = message


class CargoOverload(Exception):
    def __init__(self, message="Превышена максимальная грузоподъемность"):
        self.message = message
 