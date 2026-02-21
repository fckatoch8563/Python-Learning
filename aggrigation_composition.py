# AGGREGATION IN OOP PARADIGM
class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Create a list of Book objects
books = [
    Book("Harry Potter", "J.K Rowling"),
    Book("War and Peace", "Leo Tolstoy"),
    Book("James Bond", "FC Katoch"),
]

# Pass the list of books to the Library
library = Library("New York Library", books)

print(library.name)
print("Books in library:")
for book in library.books:
    print(f"- {book.title} by {book.author}")

#############################################################################################
# COMPOSITION IN OOP


class Library:
    def __init__(self, name, book_data):
        self.name = name
        # Library creates and owns Book objects
        self.books = [Book(title, author) for title, author in book_data]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Library creates its own Book objects (composition)
book_data = [
    ("Harry Potter", "J.K Rowling"),
    ("War and Peace", "Leo Tolstoy"),
    ("James Bond", "FC Katoch"),
]

library = Library("New York Library", book_data)

print(library.name)
print("Books in library:")
for book in library.books:
    print(f"- {book.title} by {book.author}")

##################################################################################
# ANOTHER EXAMPLE OF COMPOSITION.


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.horse_power = Engine(horse_power)
        self.wheel_size = [Wheel(wheel_size) for wheel in range(4)]

    def display_car_info(self):
        print(
            f"Car Make: {self.make}, Model: {self.model}, Horse Power: {self.horse_power.horse_power}"
        )
        print("Wheel Sizes:")
        for wheel in self.wheel_size:
            print(f"- {wheel.size} inches")


car = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
print(car.make)
car.display_car_info()
##################################################################################
