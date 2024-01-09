class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}")


class SportCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.type = 'sport car'


class Truck(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.type = 'truck'


class Camp(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.type = 'Camp'


class CarFactory:
    def __init__(self):
        self.cars = {}

    def register_car(self, car_type, car_class):
        self.cars[car_type] = car_class

    def create_car(self, car_type, make, model, year):
        if car_type in self.cars:
            return self.cars[car_type](make, model, year)
        raise ValueError(f'Invalid car type: {car_type}')


if __name__ == "__main__":
    factory = CarFactory()
    factory.register_car('Camp', Camp)
    factory.register_car('Truck', Truck)

    car = factory.create_car('Camp', 'Toyota', 'Corolla', 2020)
    car_2 = factory.create_car('Truck', 'Toyota', 'Cor', 2010)

    car.get_info()
    car_2.get_info()
    print(car_2.type)





