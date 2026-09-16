"""Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000"""

class BankAccount:
    def __init__(self,acc_no,holder_name,balance):
        self.acc_no=acc_no
        self.holder_name=holder_name
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount):
        self.balance=self.balance-amount
    def display(self):
        print("Account Number : ",self.acc_no)
        print("Account Holder Name : ",self.holder_name)
        print("Final Balance : ",self.balance)
    
acc_no=int(input("Enter Account Number : "))
holder_name=input("Enter Account Holder Name : ")
balance=float(input("Opening Balance : "))
a1=BankAccount(acc_no,holder_name,balance)

deposite=float(input("Deposite : "))
a1.deposite(deposite)

withdrawal=float(input("Withdrawal : "))
a1.withdrawal(withdrawal)
a1.display()













    
