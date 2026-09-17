"""Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.
Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0"""

class customer:
    def __init__(self,id,name,unit):
        self.id=id
        self.name=name
        self.unit=unit

    def calculate_total_bill(self):
        self.bill= (self.unit * 8) + 150
        return self.bill

    def display(self):
        print("------ Electricity Bill ------")
        print("Customer ID : ",self.id)
        print("Customer Name : ",self.name)
        print("Unit Consumed : ",self.unit)
        print("TOtal Bill : ",self.calculate_total_bill())

id=input("Enter ID :")
name=input("ENter Name : ")
unit=int(input("Enter Unit : "))

c1=customer(id,name,unit)
c1.display()



    
    