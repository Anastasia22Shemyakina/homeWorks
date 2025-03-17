### Домашнее задание "Классы"

> **Важно:** импортируйте модули и классы относительно корня проекта, а не папки с домашкой. 
> То есть импорт исключений должен выглядеть так `from hw_2.exceptions import LowFuelError, NotEnoughFuel` 
> или так `from hw_2 import exceptions`,
> (а не так `from exceptions import LowFuelError, NotEnoughFuel`, и не так `import exceptions`).
> 
> Соответственно, импорт других классов тоже будет выглядеть так `from hw_2.base import Vehicle`, 
> **но не так** `from base import Vehicle`.

> Не делайте переопределение методов, например `__init__`, если внутри единственная строчка — это вызов родительского метода с теми же аргументами `super().__init__(...)`. Эта запись не несёт смысловой нагрузки (переопределить метод, чтобы вызвать родительский, с теми же аргументами). 
> Есть смысл переопределять методы только если вы меняете их поведение (добавляете новые аргументы, устанавливаете новые свойства).

#### Задача:

- в модуле `exceptions` объявите следующие исключения:
    - `LowFuelError`
    - `NotEnoughFuel`
    - `CargoOverload`
- доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, 
      и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет, 
      что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
- создайте датакласс `Engine` в модуле `engine`, добавьте атрибуты `volume` и `pistons`
- в модуле `car` создайте класс `Car`
    - класс `Car` должен быть наследником `Vehicle`
    - добавьте атрибут `engine` классу `Car`
    - объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`
- в модуле `plane` создайте класс `Plane`
    - класс `Plane` должен быть наследником `Vehicle`
    - добавьте атрибуты `cargo` и `max_cargo` классу `Plane`
    - добавьте `max_cargo` в инициализатор (переопределите родительский)
    - объявите метод `load_cargo`, который принимает число, проверяет, что в сумме с текущим `cargo` не будет перегруза, и обновляет значение, в ином случае выкидывает исключение `exceptions.CargoOverload`
    - объявите метод `remove_all_cargo`, который обнуляет значение `cargo` и возвращает значение `cargo`, которое было до обнуления

#### Тесты:

Для запуска тестов необходимо выполнить следующее:

1. Создать виртуальное окружение:
```bash
python -m venv venv
```
2. Активировать виртуальное окружение:

* Windows:
```bash
. venv/Scripts/activate 
```
* macOS/Linux:
```bash
source venv/bin/activate
```

3. С активированным окружением установить `pytest`:
```bash
pip install pytest
```
4. Запустить тесты:
```bash
pytest
```

Это запустит все тесты, находящиеся в папке `tests`, и выведет отчет о результатах тестирования в терминал.

