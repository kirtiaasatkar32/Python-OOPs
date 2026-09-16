"""Assignment 5: Shopping Bill Calculator

 A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:

Product name

Product price

Quantity

Discount percentage

GST percentage

Create the following methods:

calculate_subtotal() – Calculate price × quantity.

calculate_discount() – Calculate the discount amount.

calculate_gst() – Calculate GST on the discounted amount.

calculate_final_bill() – Calculate the final payable amount.

display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST"""

class Bill:
    def __init__(self,pro_name,pro_price,quantity,dis_per,gst):
        self.pro_name=pro_name
        self.pro_price=pro_price
        self.quantity=quantity
        self.dis_per=dis_per
        self.gst=gst
    
    def cal_subtotal(self):
        self.subtotal=self.pro_price*self.quantity
        return self.subtotal
    def cal_dis(self):
        self.discount=self.subtotal-(self.subtotal*self.dis_per)/100
        return self.discount
    def cal_gst(self):
        self.gst=(self.discount*self.gst)/100
        return self.gst
    def cal_bill(self):
        self.bill=self.discount+self.gst
        return self.bill
    def display(self):
        print("Product Name : ",self.pro_name)
        print("Product Price : ",self.pro_price)
        print("Quantity : ",self.quantity)
        print("Discount : ",self.dis_per)
        print("GST : ",self.gst)
        print("Final Bill : ",self.bill)

pro_name=input("Product Name : ")
pro_price=int(input("Product price : "))
quantity=int(input("Quantity : "))
dis_per=int(input("Discount Percentage : "))
gst=int(input("GST : "))

b1=Bill(pro_name,pro_price,quantity,dis_per,gst)
b1.cal_subtotal()
b1.cal_dis()
b1.cal_gst()
b1.cal_bill()
b1.display()










