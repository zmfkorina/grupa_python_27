#interiorul clasei
from operator import truediv


class BankAccount:
    bank = "ING"

    def __init__(self, owner, balance=0):
        self.owner = owner
        #proprietate privata
        self.__balance = balance
        self.number_of_deposits = 0

    def __str__(self):
        return f"{self.owner} has {self.__balance} EURO"

    #getter
    @property
    def balance(self):
        return self.__balance

    #setter
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value
            self.number_of_deposits += 1

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough funds!")
        else:
            self.__balance = self.__balance - amount

    @staticmethod
    def  is_valid_amount(amount):
        if not isinstance(amount, bool) and isinstance(amount, (int, float)) and amount > 0:
            return True
        else:
            return False

    @classmethod
    def construct_from_string(cls, account_data):
        #account data = "john:300"
        #cls = BankAccount() -> echivalent
        #owner receives account_data.split(':')[0] and amount receives account_data.split(':')[1]
        owner, amount = account_data.split(":")
        obj1 = cls(owner, int(amount))
        return obj1

#exteriorul clasei
ing1 = BankAccount("Corina")
ing1.__balance = 300
ing1.withdraw(10)
print(ing1.balance)
#syntactic sugar
ing1.balance = 300
# print(ing1.__balance)
print(ing1)

# @staticmethod. O metoda care are legatura cu conturi bancare, dar nu are legatura cu un cont anume sau informatii dintr-un "self" anume
# @classmethod. O metoda care opereaza pe clasa, si are o actiune la nivel de clasa.

