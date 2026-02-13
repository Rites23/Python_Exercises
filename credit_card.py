class CreditCard:
    def __init__(self, name, number, bank="ABC Bank"):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0

    def change(self, amount):
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <=0):
            print("Change denied")
        else:
            self.balance += amount
        
    def pay(self, amount):
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <=0) or (amount > self.balance):
            print("Change denied")
        else:
            self.balance -= amount
    
    def __str__(self):
        info = f"Name: {self.name} \n Number: {self.number} \n Bank: {self.bank} \n Balance: {self.balance}"
        return info
    

u1 = CreditCard("Robert Welker", 123456789)
print(u1)

u1.change(2000)
print(u1)

u1.pay(500)
print(u1)

# CreditCard Project
#
# This Python script defines a CreditCard class that allows you to:
# - Create a credit card account with a cardholder name, number, and bank
# - Add funds to the card balance
# - Make payments from the card balance
# - Display card details and current balance
#
# The project demonstrates the use of:
# - Instance variables for individual card data
# - Instance methods for modifying and displaying card information
# - Input validation to ensure proper transactions
