"""Question 6: Library Book Management System
A library wants to maintain information about books. The librarian should be able to:
View book details.
Issue the book to a student.
Return the book.
Requirements
Create a class named Book with the following attributes:
book_id
title
author
status (Initially "Available")
Initialize the values using a constructor.
Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available
Book issued successfully.
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued
Book returned successfully.
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available"""


class book:
    def __init__(self,id,tittle,author):
        self.id = id
        self.tittle = tittle
        self.author = author
        self.status = "Available"

    def issue_book(self):
        self.status = "Issued"

    def return_book(self):
        self.status = "Available"

    def display(self):
        print("------ Book Details ------")
        print("Book ID     : ",self.id)
        print("Title       : ",self.tittle)
        print("Author      : ",self.author)
        print("Status      : ",self.status)

id = input("Enter Book ID : ")
title = input("Enter Book Title : ")
author = input("Enter Author Name : ")

book1 = book(id,title,author)
book1.display()
book1.issue_book()
book1.display()
book1.return_book()
book1.display()




































