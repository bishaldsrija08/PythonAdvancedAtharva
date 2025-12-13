class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(f"{self.firstname} {self.lastname}")
        
# x = Person("John", "Doe")
# x.printname()  # Output: John 

# class ChildClass(ParentClass):
class student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname}, age {self.age}!")
y = student("Mike", "Olsen", 21)
y.printname()  # Output: Mike Olsen
y.welcome()
print(y.age)

# pass is used when you do not want to add any other properties or methods to the class. It is like a placeholder.