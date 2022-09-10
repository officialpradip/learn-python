"""
Write a  Vehicle class that has 4 instance variables:
model
year
type_of_car
unique_id

Add an additional class variable 'no_of_objects' which counts the total number of instances created. 
Define a method 'no_of_vehicles' in the Vehicle class that returns the total number of instances created.
"""


class Car:
    counter = 0

    def __init__(self, model, year, type_of_car, unique_id):
        self.model = model
        self.year = year
        self.type_of_car = type_of_car
        self.unique_id = unique_id
        Car.counter += 1

    def no_of_vehicles(self):
        no_of_objects = Car.counter
        return no_of_objects


demo = Car(model=1, year=2001, type_of_car="economy", unique_id=1)
demo = Car(model=1, year=2001, type_of_car="economy", unique_id=1)
result = demo.no_of_vehicles()
print(result)
