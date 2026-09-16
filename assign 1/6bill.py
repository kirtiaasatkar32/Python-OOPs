"""Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600"""

class ElectricityBill:
    def __init__(self,consumer_number,consumer_name,unit,rate,charge):
        self.consumer_number=consumer_number    
        self.consumer_name=consumer_name
        self.unit=unit
        self.rate=rate
        self.charge=charge
    def calculate_energy_charge(self):
        self.echarge=self.unit*self.rate
        return self.echarge 

    def calculate_total_bill(self):
        self.bill=self.echarge+self.charge
        return self.bill
    def display(self):
        print("Energy Charge : ",self.calculate_energy_charge())
        print("Total Bill : ",self.calculate_total_bill())


consumer_number=int(input("Consumer Number : "))
consumer_name=input("Consumer Name : ")
unit=int(input("Units : "))
rate=int(input("Rate : "))
charge=int(input("Charge : "))

e1=ElectricityBill(consumer_number,consumer_name,unit,rate,charge)
e1.display()
