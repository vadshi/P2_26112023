class Car:
    def __init__(self, gas, capacity, gas_per_100km, mileage):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_100km
        self.mileage = mileage

    def fill(self, new_gas):
        if self.gas + new_gas > self.capacity:
            print(f'Вы хотите залить лишние {(self.gas + new_gas) - self.capacity} литров.')
            self.gas = self.capacity
        else:
            self.gas += new_gas

    def ride(self, new_km):
        if self.gas_per_km == 0:
            print('Не задан расход бензина. Расчет не возможен.')
        else:
            if self.gas * 100 / self.gas_per_km >= new_km:
                self.mileage += new_km
                self.gas -= new_km * self.gas_per_km / 100
            else:
                tkm = self.gas * 100 / self.gas_per_km
                print(f'Бензина хватит только на {tkm} км.')
                self.mileage += tkm
                self.gas -= tkm * self.gas_per_km / 100

    def info(self):
        print(f'Пробег: {self.mileage} км., Бензина в баке: {self.gas} л.')


car1 = Car(10, 40, 5, 1000)
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