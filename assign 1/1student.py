"""Assignment 1: Student Result Calculator

 A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
"""

class student:
        
    def calculate_total(self):
        self.total=self.english+self.math+self.sci
        return self.total
    def calculate_percentage(self):
        self.percentage=(self.total/300)*100
        return self.percentage
    def display(self):
        print("Student Name:",self.name)
        print("Roll Number:",self.roll)
        print("Total Marks:",self.total)
        print("Percentage:",self.percentage,"%")

s1=student()
s1.name=input("Enter Student name : ")
s1.roll=int(input("Enter roll number:"))
s1.english=int(input("Enter English marks : "))
s1.math=int(input("Enter Math Marks : "))
s1.sci=int(input("Enter Science Marks : "))

s1.calculate_total()
s1.calculate_percentage()
s1.display()
