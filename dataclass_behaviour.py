# EXAMPLE OF DATA CLASSES AND CLASS ATTRIBUTES
################################################

# This code demonstrates the use of class attributes and instance attributes
# in Python, as well as how to override class attributes on a per-instance basis.
# It also shows the use of the @dataclass decorator to simplify class definitions.


from dataclasses import dataclass


@dataclass
class Person:
    species = "Human"  # class attribute (shared)
    name: str  # instance attribute
    age: int
    city: str

    def is_adult(self) -> bool:
        return self.age >= 18


person = Person(name="Alice", age=30, city="New York")
person1 = Person(name="Bob", age=25, city="Los Angeles")

print(person.is_adult())  # True
print(person1.is_adult())  # True

print(Person.species)  # Human (class)
print(person.species)  # Human (shared)
print(person1.species)  # Human (shared)

# Override on ONE instance only
person.species = "Martian"
print(person.species)  # Martian (instance override)
print(person1.species)  # Human (still class value)
print(Person.species)  # Human (class still unchanged)

print("---" * 40)


# SIMPLE CLASS WITHOUT @dataclass
##################################
class Person:
    species = "Human"  # class attribute

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


p1 = Person("Alice", 30, "NY")
p2 = Person("Bob", 25, "LA")

p1.species = "Martian"  # override only on p1
print(p1.species)  # Martian
print(p2.species)  # Human
print(Person.species)  # Human
