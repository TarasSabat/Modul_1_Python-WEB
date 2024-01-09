from functools import wraps


def wrap_class(cls):

    #@wraps(cls)
    def wrapper(*args, **kwargs):
        '''

        :param args:
        :param kwargs:
        :return:
        '''
        # print(cls.__name__)
        # print(cls.__doc__)
        return cls(*args, **kwargs)
    return wrapper


@wrap_class
class Car:
    '''
    Car class
    it return all his attributes in value() method
    '''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def value(self):
        print(self.make, self.model, self.year)


car = Car('Honda', 'Civic', 2018)
car.value()
print(Car.__doc__ )
