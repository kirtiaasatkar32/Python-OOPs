"""Question 3: Online Shopping System
Scenario
An e-commerce company wants to calculate the final amount payable by customers after applying discounts.
Requirements
Create a class named Product with:
product_id
product_name
quantity
price_per_item
Initialize the values using a constructor.
Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0"""

class Product:
    def __init__(self,id,name,quantity,price):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
   
    def cal_total_amt(self):
        self.amt=self.quantity*self.price
        if self.amt > 5000:
            self.discount=self.amt/10
        else:
            self.discount=self.amt/5
        self.total=self.amt-self.discount

    def display(self):
        print("Product ID : ",self.id)
        print("Product Name : ",self.name) 
        print("Quantity : ",self.quantity)
        print("Price : ",self.price)
        print("Total Amount : ",self.amt)
        print("Discount : ",self.discount)
        print("Final Amount : ",self.total)

id=input("Enter Product ID : ")
name=input("Enter Product Name : ")
quantity=int(input("Enter Quantity : "))
price=int(input("Enter Price : "))

p1=Product(id,name,quantity,price)
p1.cal_total_amt()
p1.display()


