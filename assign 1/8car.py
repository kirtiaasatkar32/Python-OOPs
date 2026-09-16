"""Assignment 8: Car Mileage Calculator

 A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:

Car brand

Car model

Distance travelled in km

Fuel consumed in litres

Petrol price per litre

Create the following methods:

calculate_mileage() – Calculate kilometres per litre.

calculate_fuel_cost() – Calculate total fuel cost.

display_trip_details() – Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105"""

class car:
    def __init__(self,model,dis,fuel,price):
        self.model = model
        self.distancce = dis
        self.fuel = fuel
        self.price = price

    def calculate_mileage(self):
        self.mileage = self.distancce / self.fuel
        return self.mileage

    def  calculate_fuel_cost(self):
        self.cost = self.fuel * self.price
        return self.cost

    def display_trip_details(self):
        print("Mileage:",self.calculate_mileage())
        print("Petrol Price:",self.calculate_fuel_cost())

brand = input("Enter Car Brand: ")
model = input("Enter Car Model: ")
distance = int(input("Enter Distance: "))
Fuel = int(input("Enter Fuel Consumed: "))