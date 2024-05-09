import math


class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number

    # create a dunder method to add two pages (overload the addition (+) operator)
    def __add__(self, other):
        new_words = self.words + " " + other.words
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)


page1 = Page("Kelli is a great programmer!", 1)
page2 = Page("This is another page", 2)
page3 = page1 + page2
print(page3.words)  # Kelli is a great programmer! This is another page
print(page3.page_number)  # 3


class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.after_tax_price = 0
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1 + self.TAX), 2)

    # create a dunder method to subtract a number from price of store item (overload the subtraction (-) operator)
    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

    # create a dunder method to multiply the price of a store item by a value (overload the multiplication (*) operator)
    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)


bread = StoreItem("Bread", 7)
discounted_bread = bread - 2
print(discounted_bread.after_tax_price)  # 5.65
discounted_bread = bread * 0.8
print(discounted_bread.after_tax_price)  # 6.33


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    # overload the division (/) operator
    def __truediv__(self, factor):
        new_point1 = self.point1[0] / factor, self.point1[1] / factor
        new_point2 = self.point2[0] / factor, self.point2[1] / factor
        return Line(new_point1, new_point2)

    # overload the division (//) operator
    def __floordiv__(self, factor):
        new_point1 = self.point1[0] // factor, self.point1[1] // factor
        new_point2 = self.point2[0] // factor, self.point2[1] // factor
        return Line(new_point1, new_point2)

    # overload the len() function
    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)  # len function must return an integer

    # overload the comparison (==) operator
    def __eq__(self, other):
        if not isinstance(other, Line):
            return False

        return self.point1 == other.point1 and self.point2 == other.point2

    # overload the comparison (!=) operator
    def __ne__(self, other):
        return not self.__eq__(other)

    # overload the comparison (>) operator
    def __gt__(self, other):
        return len(self) > len(other)

    # overload the comparison (>=) operator
    def __ge__(self, other):
        return len(self) >= len(other)

    # overload the comparison (<) operator
    def __lt__(self, other):
        return len(self) < len(other)

    # overload the comparison (<=) operator
    def __le__(self, other):
        return len(self) <= len(other)


line1 = Line((10, 5), (20, 10))
line2 = line1 / 2
print(line2.point1, line2.point2)  # (5.0, 2.5) (10.0, 5.0)
line3 = line1 // 2
print(line3.point1, line3.point2)  # (5, 2) (10, 5)
print(len(line1))  # 11
line4 = Line((10, 5), (20, 10))
print(line1 == line4)  # True
print(line1 != line4)  # False
print(line1 > line2)  # True
print(line3 >= line4)  # False


class Page2:
    def __init__(self, text, page_number):
        self.text = text
        self.page_number = page_number

    def __len__(self):
        return len(self.text)

    # overload the print() method
    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()


class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number

    def __len__(self):
        return len(self.pages)

    def __str__(self):
        output = f"Book({self.title}, {self.author}, {self.id_number})"
        for page in self.pages:
            output += str(page)

        return output

    # overload the repr() function
    def __repr__(self):
        return f"Book(ID Number = {self.id_number})"


page1 = Page2("Page 1!", 1)
page2 = Page2("This is page 2.", 2)
book = Book("Kelli is Great", "Kelli", [page1, page2], 1)
print(len(page1))  # 7
print(len(page2))  # 15
print(len(book))  # 2
print(page1, page2)  # Page 1! This is page 2.
print(book)  # Book(Kelli is Great, Kelli, 1)Page 1!This is page 2.
print(repr(book))  # Book(ID Number = 1)

'''
Vector Class
Write a "Vector" class that implements the following dunder methods.
    - "__init__(self, a, b)" initializes the vector by storing the components "a" and "b"
    - "__eq__(self, vector)" returns "True" if the current vector and the "vector" parameter are equal
    - "__repr__(self)" returns the formal string representation of the vector
    - "__add__(self, vector)" creates and returns a new "Vector" object that has components equal to the sum of the components 
      in the current vector and the vector represented by the "vector" parameter
    - "__sub__(self, vector)" creates and returns a new "Vector" object that has components equal to the difference of the components 
      in the current vector and the vector represented by the "vector" parameter
    - "__mul__(self, vector)" returns the dot product of the current vector and the vector represented by the "vector" parameter. The 
      dot product of two vectors is equsl to the sum of the multiplication of their individual components.
'''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    def __repr__(self):
        output = f"Vector({self.a}, {self.b})"
        return output

    def __add__(self, vector):
        new_a = self.a + vector.a
        new_b = self.b + vector.b
        return Vector(new_a, new_b)

    def __sub__(self, vector):
        new_a = self.a - vector.a
        new_b = self.b - vector.b
        return Vector(new_a, new_b)

    def __mul__(self, vector):
        new_a = self.a * vector.a
        new_b = self.b * vector.b
        return new_a + new_b