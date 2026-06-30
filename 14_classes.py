print("====================== Classes Course Start =====================")

class Cat:
    # functie denumita constructor:
    def __init__(self, name, owner, temperament="Loving"):
        self.name = name
        self.owner = owner
        self.temperament = temperament

    def __str__(self):
        return f"Cat: name = {self.name}, owner is {self.owner}, its temperament is {self.temperament}"

    def speak(self):
        print(f'{self.name} says: "Meow"')

    def eat(self, food):
        print(f'{self.name} takes a bite out of "{food}!')

    def __repr__(self):
        return f"Cat('{self.name}, {self.owner}, {self.temperament}')"
        
cat1 = Cat("Shadow", "Mark")
cat2 = Cat("Spot", "John", "Shy")
# cat1 = Cat.__init__(cat1)

print(cat1)
cat2.name = "Cerberus"
print(cat2)
cat2.speak()
cat2.eat(cat1)

cats = [cat1, cat2]
print(cats)
# cat1.name = "Shadow"
# cat2.name = "Spot"
#
# print(cat1)
# print(cat2.name)
#
# cat1.owner "Mark"

class BankAccount:
    bank = "ING"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has {self.balance} Euro"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("You're poor, how about not")
        else:
            self.balance -= amount

acc1 = BankAccount("John", 10)
print(acc1)

# acc1.balance = acc1.balance + 100
print(acc1)
acc1.deposit(200)
acc1.withdraw(300)
print(acc1)

acc2 = BankAccount("Gigel", 3000)
print(acc2)

acc1.bank = "BNR"

# creati o clasa Rectangle care are doua atribute interne, x si y. initiati-le din constructor.
# creati doua metode, area() si perimeter() care calculeaza aria si perimetrul acelui Rectangle, si returneaza acea valoare, folosind formulele:
# area: x * y
# perimeter: 2 * x + 2 * y

class Rectangle:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Rectangle has a height of {self.x} and width of {self.y}"

    def area(self, x, y):
        return f"Rectangle has an area of {x*y}"

    def perimeter(self, x, y):
        return f"Rectangle has an area of {2*(x+y)}"


rect1 = Rectangle(4, 7)
print(rect1)

