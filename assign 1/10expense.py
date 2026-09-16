"""Assignment 10: Personal Expense Calculator

 A person wants to calculate monthly expenses and savings.

Create a class ExpenseTracker with the following attributes:

Person name

Monthly salary

Rent

Food expenses

Travel expenses

Other expenses

Create the following methods:

calculate_total_expenses() – Calculate all expenses.

calculate_savings() – Calculate salary minus total expenses.

display_expense_report() – Display salary, expenses, and savings.

Formula:

Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses

Sample data:

Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000

Expected result:

Total Expenses: 28000
Savings: 32000"""

class ExpenseTracker():
    def __init__(self,salary,rent,food,travel,other):
        self.salary = salary
        self.rent = rent
        self.food = food
        self.travel = travel
        self.other = other

    def calculate_total_expenses(self):
        total = self.rent + self.food + self.travel + self.other
        return total

    def calculate_savings(self):
        return self.salary - self.calculate_total_expenses()

    def display_expense_report(self):
        print("Total Expenses:",self.calculate_total_expenses())
        print("Savings:",self.calculate_savings())

name = input("Enter name: ")
sal = int(input("Enter Salay: "))
rent = int(input("Enter Rent: "))
food = int(input("Enter Food: "))
Traved = int(input("Travel Expenses: "))
other = int(input("Other Expenses: "))

name = ExpenseTracker(sal,rent,food,Traved,other)
name.display_expense_report()
