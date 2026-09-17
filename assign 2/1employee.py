"""Question 1: Employee Salary Management System
Scenario
A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.
Requirements
Create a class named Employee with the following attributes:
employee_id
employee_name
basic_salary
Initialize the values using a constructor.
Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0"""

class Employee:
    def __init__(self,id,name,salary,hra,da):
        self.id=id
        self.name=name
        self.salary=salary
        self.hra=hra
        self.da=da
        
    def calculate_hra(self):
        self.hra=(self.salary*self.hra)/100
        return self.hra
    def cal_da(self):
        self.da=(self.salary * self.da)/100
        return self.da
    def cal_gross_salary(self):
        self.gs=self.salary + self.hra + self.da
        return self.gs
    def display(self):
        print("------ Employee Salary Details ------")
        print("Employee ID   : ",self.id)
        print("Employee Name : ",self.name)  
        print("Basic Salary  : ",self.salary)  
        print("HRA           : ",self.calculate_hra())
        print("DA            : ",self.cal_da())
        print("Gross Salary  : ",self.cal_gross_salary())
id=input("Employee ID : ")
name=input("Employee Name : ")
salary=float(input("Basic Salary : "))
hra=int(input("HRA : "))
da=int(input("DA : "))

e1=Employee(id,name,salary,hra,da)
e1.display()