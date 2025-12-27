from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")

payment1 = CreditCard()
payment1.pay(1000)

payment2 = UPI()
payment2.pay(500)
