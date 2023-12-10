class Car:
    gas = 0
    mileage = 0

    def __init__(self, gas=0, capacity=0, gas_per_100km=0, mileage=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, fil_of_gas) -> None:
        if self.capacity - fil_of_gas < 0:
            print(f"Вы пытаетесь заправить больше, чем вмещает бак на {fil_of_gas - self.capacity} литров")
            self.gas = self.capacity
        else:
            self.gas = fil_of_gas

    def ride(self, distance):
        if (self.gas_per_100km / 100) * distance > self.gas:
            self.mileage = self.mileage + self.gas / (self.gas_per_100km / 100)
            self.gas = 0
        else:
            self.mileage = self.mileage + distance
            self.gas = self.gas - (self.gas_per_100km / 100) * distance
        print(f"Проехали {self.mileage} киллометров")

    def info(self):
        print(f"Топлива в баке = {self.gas} л")
        print(f"Пробег = {self.mileage} км")


capacity_ = int(input("Введите объем бака: "))
gas_per_100km_ = int(input("Введите расход топлива на 100 км: "))
fil_of_gas_ = int(input("Введите сколько топлива залить: "))
distance_ = int(input("Введите сколько киллометров необходимо проехать: "))

car1 = Car(0, capacity_, gas_per_100km_, 0)

car1.fill(fil_of_gas_)

car1.ride(distance_)

car1.info()

