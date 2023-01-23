def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

sum = add(3, 4, 5, 6)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
    
result = calculate(2, add=3, multiply=5)
print(result)

class Car:
    #use get not to get any error if you do not initializa a defined kwargs. Get will return none if not initialized
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        
car = Car(make="Nissan")
print(car.make)