"""Assignment 4: Rectangle Calculator

 A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() – Calculate the area.

calculate_perimeter() – Calculate the perimeter.

display_result() – Display length, breadth, area, and perimeter.

Formulas:
Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)
Sample data:
Length: 15
Breadth: 8"""

class Rectangle:
    def length(self,length):
        self.length=length
        return self.length
    def breadth(self,breath):
        self.breadth=breadth
        return self.breadth
    def cal_area(self):
        self.area=self.length*self.breadth
    def cal_peri(self):
        self.perimeter=2 * (length + breadth)
    def display(self):
        print("Length of Rectangle : ",self.length)
        print("Breadth of Rectangle : ",self.breadth)
        print("Area : ",self.area)
        print("Perimeter : ",self.perimeter)


r1=Rectangle() 
length=int(input("Enter Length : "))
r1.length(length)
breadth=int(input("Enter Breadth : ")) 
r1.breadth(breadth)
      
r1.cal_area()
r1.cal_peri()
r1.display()












        