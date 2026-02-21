# there's only one __init__() method, but there are multiple ways to create instances.
# Here are the main approaches:

# 1 Direct instantiation with different arguments:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Different ways to call __init__ with different data
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)


# 2. Class methods as alternative constructors (the most common pattern):
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2026 - birth_year
        return cls(name, age)  # Still calls __init__

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))


p1 = Person("Alice", 30)
p2 = Person.from_birth_year("Bob", 1990)
p3 = Person.from_string("Charlie,35")


# 3. Override __new__() for custom object creation (advanced):
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True, both are the same instance

# 4. Using factory functions (outside the class):


def create_person(name, age):
    return Person(name, age)


p4 = create_person("Dave", 40)
# These are the main ways to create instances of a class with a single __init__() method.
# Each method provides flexibility in how objects are instantiated based on different needs.

"""
The class method pattern is the Pythonic way to provide multiple "constructors"—they 
all eventually call __init__(), but offer different ways to initialize the object 
from different data sources.
"""


# Example of Singleton class using attribute to store single instance
class Person:
    _instance = None

    def __new__(cls, name=None, age=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name=None, age=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age


# Create first instance
p1 = Person("Alice", 30)
print(f"p1: {p1.name}, {p1.age}")  # Alice, 30
print(f"p1 id: {id(p1)}")

# Create "second" instance - but it's actually the same object
p2 = Person("Bob", 25)
print(f"p2: {p2.name}, {p2.age}")  # Bob, 25
print(f"p2 id: {id(p2)}")

# Same object!
print(f"p1 is p2: {p1 is p2}")  # True
print(f"p1.name: {p1.name}")  # Bob (changed!)
