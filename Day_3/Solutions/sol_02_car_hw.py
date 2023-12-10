"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...

# Значит должны быть значения по умолчанию
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезает бензина (capacity)
* "расход топлива на 100 км" (gas_per_100km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то бак заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров",
в результате поездки потратится бензин и увеличится пробег.
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (вывести количество бензина в баке и пробег)
"""


class Car:
    def __init__(self, gas=10, capacity=50, gas_per_100km=10, milage=200_000):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.milage = milage

    def fill(self, ai95):
        gas_tank_free_space = self.capacity - self.gas

        if ai95 > 0:
            if ai95 <= gas_tank_free_space:
                self.gas += ai95
                print(f"Заправлено литров: {ai95}. Теперь в баке: {self.gas}")
            else:
                self.gas = self.capacity
                extra_liters = ai95 - gas_tank_free_space
                print(f"Залили до полного бака. Сейчас {self.capacity} литров. {extra_liters} не влезло.")

        if ai95 == 0:
            print('Мужчина, Вы будете заправляться или приехали только посмотреть?')

        if ai95 < 0:
            print(f'Пробуем отсосать литров: {ai95 * (-1)}')
            self.gas = self.gas + ai95

    def ride(self, distance):
        fuel_needed = (distance / 100) * self.gas_per_100km
        if fuel_needed <= self.gas:
            self.gas -= fuel_needed
            self.milage += distance
            print(f"Проехали {distance} километров. Остаток литров: {self.gas} ")
        else:
            potencial = (self.gas / self.gas_per_100km) * 100
            if potencial < 0:
                potencial = 0
            self.milage += potencial
            self.gas = 0
            print(f"Больше не могу. Проехали {potencial} км. Ищи эвакуатор.")

    def info(self):
        print(f"Остаток литров: {self.gas}\nПробег: {self.milage} км.")


car1 = Car()
car1.fill(15)
car1.info()
print('=' * 40)

car1.ride(200)
car1.info()
print('=' * 40)

car1.fill(75)
car1.info()
print('=' * 40)

car1.ride(2000)
car1.info()
print('=' * 40)