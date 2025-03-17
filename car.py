from hw_2.base import Vehicle
from hw_2.engine import Engine

class Car(Vehicle):
    def __init__(self, weight=1500, fuel=70, fuel_consumption=12.0, engine=None, **kwargs):
        super().__init__(weight, fuel, fuel_consumption, **kwargs)
        self._engine = engine

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value: Engine):
        if not isinstance(value, Engine):
            raise ValueError("Должен быть экземпляр класса Engine")
        self._engine = value

    def set_engine(self, engine: Engine):
        self.engine = engine

