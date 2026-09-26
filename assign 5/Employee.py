'''SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:

* employee_id
* employee_name
* salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:

display_details()

4. Developer should have:

programming_language

and a method:

write_code()

5. Manager should have:

team_size

and a method:

manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:

@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.'''

class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,value):
        if value <= 0:
            print("Invalide Salary")
        else:
            self.__salary = value
            print("Salary Updated")

    @salary.deleter
    def salary(self):
        del self.__salary
    

    def display_detail(self):
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)

class Developer(Employee):
    def __init__(self,id,name,salary,language):
        self.language = language
        super().__init__(id,name,salary)

    def write_code(self,code):
        self.code = code

    def display_detail(self):
        super().display_detail()
        print("Enter Employee Type: 1")
        print("Enter Programming Language: ",self.language)
        print()
        print(self.name,"is developing applications using",self.language)

class Manager(Employee):
    def __init__(self,id,name,salary,size):
        self.team_size = size
        super().__init__(id,name,salary)

    def manage_team(self):
        pass
    def display_detail(self):
        super().display_detail()
        print("Enter Employee Type: 2")
        print(self.team_size)
        print()
        print(self.name,"is Manager and have team of",self.team_size)

id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = int(input("Enter Salary: "))
t = int(input("Enter Employee Type: "))

if t == 1:
    language = input("Enter Programming Language: ")
    emp = Developer(id,name,salary,language)
else:
    size = int(input("Enter Team size: "))
    emp = Manager(id,name,salary,size)
print()
emp.display_detail()