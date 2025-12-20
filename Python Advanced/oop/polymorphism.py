# Mnay forms means polymorphism

# name = "Bishal Rijal"

# print(len(name))

# birds = ["sparrow", "pigeon", "parrot", "eagle"]
# print(len(birds))

# user  ={
#     "name": "Bishal Rijal",
#     "age": 24,
#     "country": "Nepal"
# }

# print(len(user))

# school = ("St. Xaviers", "Kathmandu", 1995)
# print(len(school))

class Car:
    def start(self):
        print("Car is moving forward in a road.")
class Boat:
    def start(self):
        print("Boat is moving forward in a river.")
class Plane:
    def start(self):
        print("Plane is flying in the sky.")
        
obj = Car()
obj.start()

oj2 = Boat()
oj2.start()

obj3 = Plane()
obj3.start()