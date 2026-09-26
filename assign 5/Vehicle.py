'''A bank provides different types of accounts.

Create the following hierarchy:

Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount

REQUIREMENTS:

1. Create a parent class Account.

Attributes:

* account_number
* customer_name
* balance

2. SavingsAccount should inherit from Account.

Additional attribute:

* interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.

Additional attribute:

* cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:

display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:

@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.
'''

class Vehical:
    def __init__(self,no,brand,rent):
        self.no = no
        self.brand = brand
        self.__rent_per_day = rent

    def calculate_rent(self,day):
        self.rent = self.__rent_per_day*day

    @property
    def rent_per_day(self):
        return self.__rent_per_day

    @rent_per_day.setter
    def rent_per_day(self,rent):
        self.__rent_per_day = rent

    @rent_per_day.deleter
    def rent_per_day(self):
        del self.__rent_per_day

    def display(self):
        print("Vehicle Number: ",self.no)
        print("Brand: ",self.brand)
        print("Rent Per Day: ",self.__rent_per_day)
        print("Vehicle Type: ",tp)

class Car(Vehical):
    def __init__(self, no, brand, rent,seats):
        self.seats = seats
        super().__init__(no, brand, rent)

    def calculate_rent(self,day):
        super().calculate_rent(day)
    
    def display(self):
        super().display()
        print("Number of Seats:",self.seats)
        print()
        print("Rental Days:",day)
        print("Total Rent:",self.calculate_rent(day))

class Bike(Vehical):
    def __init__(self, no, brand, rent,eng):
        self.eng = eng
        super().__init__(no, brand, rent)

    def calculate_rent(self,day):
        super().calculate_rent(day)
    
    def display(self):
        super().display()
        print("Enter Rent Per Day:",self.eng)
        print()
        print("Rental Days:",day)
        print("Total Rent:",self.calculate_rent(day))

no = input("Enter Vehicle Number: ")
brand = input("Enter Brand: ")
rpd = int(input("Enter Rent Per Day: "))
t = int(input("Enter Vehicle Type: "))
if t == 1:
    tp = "Car"
    seat = int(input("Enter Number of Seats: "))
    v = Car(no,brand,rpd,seat)
else:
    tp = "Bike"
    eng = input("Enter Engine CC: ")
    v = Bike(no,brand,rpd,eng)
day = int(input("Enter Number of Rental Days: "))
v.display()