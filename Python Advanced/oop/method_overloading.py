# Method Overloading in Python can be achieved by using default arguments.
class Mcc:
    def display_info(self, name = " "):
        print("Welcome to MCC "+ name)

obj = Mcc()
obj.display_info()
obj.display_info("Atharva")