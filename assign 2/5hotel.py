"""Question 5: Hotel Room Booking System
Scenario
A hotel wants to generate the final bill of guests based on the duration of their stay.
Requirements
Create a class named Guest with:
guest_id
guest_name
number_of_days
room_charge_per_day
Initialize the values using a constructor.
Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0"""

class Guest:
    def __init__(self,id,name,days,charge):
        self.id=id
        self.name=name
        self.days=days
        self.charge=charge
   
    def bill(self):
        self.bill=days*charge        
        self.gst=(self.bill*12)/100
        self.final_bill=self.bill+self.gst
         
    def display(self):
        print("------ Hotel Bill ------")
        print("Guest ID              : ",self.id)
        print("Guest Name            : ",self.name)     
        print("Number of Days        : ",self.days)     
        print("Room Charge Per Day   : ",self.charge)     
        print("Room Bill             : ",self.bill)     
        print("GST (12%)             : ",self.gst)     
        print("Final Bill            : ",self.final_bill)     
     
id=input("Enter ID : ")
name=input("Enter Name : ")
days=int(input("Enter Number Of Days : "))
charge=int(input("Room Charge Per Day : "))

g1=Guest(id,name,days,charge)
g1.bill()
g1.display()





