"""

In the Book class, create a property named price such that the price of a book cannot be less than 50 or more than 1000.

"""


class Book:
    def __init__(self,isbn, title,author,publisher,pages,price,copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def price_check(self):
    	if self.price < 50 or self.price > 10000:
    		print("The price is invalid, enter it again.")
    		self.price = 50
   
    def display(self):
        print(self.title)
        print('ISBN : ' ,self.isbn)
        print('Price : ', self.price)
        print('Number of copies : ', self.copies)
        print('.' * 50)

    def in_stock(self):
    	if self.copies > 0:
    		return True
    	else:
    		return False

    def sell(self):
    	if self.copies > 0:
    		self.copies = self.copies - 1
    	else:
    		print("Sorry, the book is out of stock!")


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.display()
book2.display()
book3.display()
book4.display()

"""

For the Book class that you have created, write a method named in_stock that returns True if number of copies is more than zero, otherwise it returns False.

Create another method named sell that decreases the number of copies by 1 if the book is in stock, otherwise it prints the message that the book is out of stock.

"""

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 49,0)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)

book1.price_check()
print(book1.price)


print(book1.in_stock())

book2.sell()
book2.sell()

"""

Create a list named books that contains the 4 Book instance objects that you have created in question 2. 

Iterate over this list using a for loop and call display() for each object in the list.

Write a list comprehension to create another list that contains title of books written by Jack.

"""

books = [book1, book2, book3, book4]

counter = 0
while counter < len(books):
	dummy = books[counter]
	dummy.display()
	counter += 1



