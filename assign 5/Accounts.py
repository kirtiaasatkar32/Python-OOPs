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

class Account:
    def __init__(self,no,name,balance):
        self.no = no
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self,amount):
        self.__balance = amount

    @balance.deleter
    def balance(self):
        del self.__balance

    def deposit(self,amount):
        self.__balance += amount
        print("After Deposit:")
        print("Balance:",self.__balance)

    def withdraw(self,amount):
        self.__balance -= amount
        print("After Withdrawal:")
        print("Balance:",self.__balance)

    def display(self):
        print("Account number:",self.no)
        print("Customer name:",self.name)
        print("Balance:",self.__balance)

class SavingsAccount(Account):
    def __init__(self, no, name, balance,rate):
        self.rate = rate
        super().__init__(no, name, balance)

    def display(self):
        super().display()
        print()
        print("Account Type: ",tp)
        print("Interest Rate: ",self.rate,"%")

class PremiumSavingAccount(SavingsAccount):
    def __init__(self, no, name, balance,rate,cashback):
        self.cashback = cashback
        super().__init__(no, name, balance,rate)

    def display(self):
            super().display()
            print("Cashback:",self.cashback)


no = int(input("Enter Account Number: "))
name = input("Enter Customer Name: ")
balance = int(input("Enter Initial Balance: "))
t = int(input("Enter Account Type: "))
ir = int(input("Enter Interest Rate: "))
cb = int(input("Enter Cashback Percentage: "))
d = int(input("Enter amount to deposit: "))
w = int(input("Enter amount to withdraw: "))

if t == 1:
    tp = "Saving Account"
    acc = PremiumSavingAccount(no,name,balance,ir,cb)
else:
    tp = "Premium Saving Acoount"
    acc = PremiumSavingAccount(no,name,balance,ir)

print()
acc.display()
print()
acc.deposit(d)
print()
acc.withdraw(w)
print()