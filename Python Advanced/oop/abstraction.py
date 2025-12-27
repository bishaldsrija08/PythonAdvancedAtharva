# Abstraction in Python is the process of hiding implementation details and showing only essential features using abstract classes and abstract methods.
from abc import ABC, abstractmethod

class Vehicle (ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick")

car = Car()
car.start()

bike = Bike()
bike.start()