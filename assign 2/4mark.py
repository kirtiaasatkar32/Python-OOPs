
"""Question 4: Student Result Processing System
Scenario
A college wants to automate result generation by calculating total marks, percentage, and grade.
Requirements
Create a class named Student with:
roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B"""

class Student:
    def __init__(self,roll,name,m1,m2,m3):
        self.roll=roll
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def total(self):
        self.total=self.m1 + self.m2 + self.m3    
        self.per=self.total/3
        if self.per >= 90:
            self.grade="A"          
        elif self.per >= 75:
            self.grade = "B"
        elif self.per >=60:
            self.grade = "C"
        else:
            self.grade="D"
           
    def display(self):
        print("------ Student Result ------")   
        print("Roll Number      : ",self.roll)
        print("Student Name     : ",self.name)
        print("Total Marks      : ",self.total)
        print("Percentage       : ",self.per)
        print("Grade            : ",self.grade)

roll=input("Enter Roll No : ")
name=input("Enter Name : ")
m1=int(input("Marks 1 : "))
m2=int(input("Marks 2 :"))
m3=int(input("Marks 3 :"))

s1=Student(roll,name,m1,m2,m3)
s1.total()
s1.display()











