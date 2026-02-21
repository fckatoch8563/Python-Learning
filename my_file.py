# PLAIN CONCRETE CLASSSES-NO ENFORCEMENT
# NO ENFORCEMENT MEANS THAT THERE IS NO BASE CLASS OR INTERFACE TO IMPOSE A CONTRACT ON THE CONCRETE CLASSES.
# THIS APPROACH RELIES ON THE DEVELOPER TO ENSURE THAT THE CONCRETE CLASSES IMPLEMENT THE REQUIRED METHODS AND PROPERTIES.


class Circle:
    def __init__(self, r):
        self.r = r  # radius

    def area(self):
        return 3.14159 * self.r * self.r  # pi*r^2


# def print_area(shape):
#     print("Area:", shape.area())

# print_area(Circle(2))
# print_area(Square(3))


# ANOTHER WAY TO IMPLEMENT WITHOUT ENFORCEMENT IS TO USE A FACTORY PATTERN.
# HERE IS AN EXAMPLE OF A SHAPE FACTORY THAT CREATES SHAPE OBJECTS BASED ON A TYPE PARAMETER.
class Square:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a


# class ShapeFactory:
#     @staticmethod  # static method decorator is provided to indicate no self parameter is needed for this method. This method can be called on the class itself without creating an instance.
#     def create_shape(shape_type, size):
#         if shape_type == "circle":
#             return Circle(size)
#         elif shape_type == "square":
#             return Square(size)
#         else:
#             raise ValueError(f"Unknown shape type: {shape_type}")


# # Usage
# circle = ShapeFactory.create_shape("circle", 5)
# print("Circle area:", circle.area())
# square = ShapeFactory.create_shape("square", 4)
# print("Square area:", square.area())


# ANOTHER EXAMPLE WITHOUT ENFORCEMENT IS A GENERIC SHAPE CLASS THAT HANDLES MULTIPLE SHAPE TYPES BASED ON PARAMETERS.
# HERE IS AN EXAMPLE:
class Shape:
    def __init__(self, shape_type, size):
        self.shape_type = shape_type
        self.size = size

    def area(self):
        if self.shape_type == "circle":
            return 3.14159 * self.size * self.size
        elif self.shape_type == "square":
            return self.size * self.size
        else:
            raise ValueError(f"Unknown shape type: {self.shape_type}")


# Usage
shape1 = Shape("circle", 5)
print("Shape1 area:", shape1.area())
shape2 = Shape("square", 4)
print("Shape2 area:", shape2.area())

# In summary, while not using abstract base classes or interfaces removes formal enforcement of method implementation,
# developers can still create concrete classes that follow expected contracts through careful design patterns and conventions.
# However, this approach relies on discipline and clear documentation to ensure consistency across implementations.

"""
This works, but there’s no explicit contract: another developer might create a shape class without area and forget tests.
"""
# #######################################################################
# INTRODUCE ABSTRACT BASE CLASS TO ENFORCE CONTRACT.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return area as a float."""


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r * self.r


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a


# Usage
circle = Circle(5)
print("Circle area:", circle.area())
square = Square(4)
print("Square area:", square.area())

# Shape() cannot be instantiated directly:
# shape = Shape()  # This would raise a TypeError

# #######################################################################
