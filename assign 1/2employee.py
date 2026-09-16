"""Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.

calculate_da() – Calculate DA.

calculate_gross_salary() – Calculate gross salary.

display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA"""

class employee:
    def calculate_hra(self):
        self.hra=(self.basic_salary*self.hra_percentage)/100
        return self.hra
    def cal_da(self):
        self.da=(self.basic_salary * self.da_percentage)/100
        return self.da
    def cal_gross_salary(self):
        self.gs=self.basic_salary + self.hra + self.da
        return self.gs
    def display(self):
        print("Employee ID : ",self.emp_id)
        print("Employee Name : ",self.name)
        print("Employee Salary : ",self.basic_salary)
        print("HRA : ",self.hra)
        print("DA : ",self.da)
        print("Gross Salary : ",self.gs)

e1=employee()
e1.emp_id=int(input("Enter Employee ID : "))
e1.name=input("Enter Employee name : ")
e1.basic_salary=float(input("Enter Salary : "))
e1.hra_percentage=float(input("Enter HRA Percentage : "))
e1.da_percentage=float(input("Enter DA Percentage : "))

e1.calculate_hra()
e1.cal_da()
e1.cal_gross_salary()
e1.display()
















