"""Assignment 7: Mobile Phone Data Usage

A mobile user wants to calculate their remaining internet data.

Create a class MobilePlan with the following attributes:

Customer name

Mobile number

Total data in GB

Used data in GB

Validity in days

Create the following methods:

calculate_remaining_data() – Calculate remaining data.

calculate_usage_percentage() – Calculate the percentage of data used.

display_plan() – Display the plan details and results.

Sample data:

Total Data: 50 GB
Used Data: 18 GB
Validity: 28 days

Expected result:

Remaining Data: 32 GB
Usage Percentage: 36.0%"""

class mobileplan:
    def __init__(self,num,data,used,validity):
        self.num = num
        self.data = data
        self.used = used
        self.validity = validity

    def calculate_remaining_data(self):
        self.remans = self.data - self.used
        return self.remans

    def calculate_usage_percentage(self):
        self.per = (self.used*100)/self.data
        return self.per

    def display_plan(self):
        print("Remaining Data:",self.calculate_remaining_data())
        print("Usage Percentage:",self.calculate_usage_percentage())

name = input("Enter customer Name: ")
num = int(input("Enter Customer Number: "))
data = int(input("Enter Total data in GB: "))
used = int(input("Enter Used data in GB: "))
validity = int(input("Enter Validity in days: "))

name = mobileplan(num,data,used,validity)
name.display_plan()