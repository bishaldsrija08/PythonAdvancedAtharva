# Method overriding means defining a method in the child class that already exists in the parent class. And when the method is called using an object of the child class, the child class's version of the method is executed.

class Mcc:
    def display_info(self):
        print("Welcome to MCC Campus")

class Br(Mcc):
    def display_info(self):
        super().display_info()  # Call the method from the parent class
        print("Welcome to BR Campus")
        
obj = Br() # Create an object of the child class
obj.display_info()  # This will call the overridden method in the Br class