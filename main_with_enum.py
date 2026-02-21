# Demonstration of Enum usage in Python

from enum import Enum, auto


# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Using auto() for automatic values
class Status(Enum):
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()


# String Enum
class Direction(str, Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


# Usage examples
print(Color.RED)  # Color.RED
print(Color.RED.name)  # RED
print(Color.RED.value)  # 1
print(Color(1))  # Color.RED

# Iteration
for color in Color:
    print(color)

# Comparison
if Status.PENDING == Status.PENDING:
    print("Same status")


###########################################################################
# Using Enums in function parameters
class CoffeeType(Enum):
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"
    MACCHIATO = "macchiato"
    FLAT_WHITE = "flat_white"
    RISTRETTO = "ristretto"
    CORTADO = "cortado"


def brew_coffee(coffee_type: CoffeeType):
    coffee_types = {
        CoffeeType.ESPRESSO: {"strength": 3, "coffee_amount": 30, "milk_amount": 0},
        CoffeeType.LATTE: {"strength": 1, "coffee_amount": 30, "milk_amount": 150},
        CoffeeType.CAPPUCCINO: {"strength": 2, "coffee_amount": 30, "milk_amount": 100},
        CoffeeType.MACCHIATO: {"strength": 3, "coffee_amount": 30, "milk_amount": 10},
        CoffeeType.FLAT_WHITE: {"strength": 2, "coffee_amount": 30, "milk_amount": 120},
        CoffeeType.RISTRETTO: {"strength": 4, "coffee_amount": 20, "milk_amount": 0},
        CoffeeType.CORTADO: {"strength": 2, "coffee_amount": 30, "milk_amount": 60},
    }

    return coffee_types.get(coffee_type, "Unknown coffee type")


print(brew_coffee(CoffeeType.ESPRESSO))
my_coffee = brew_coffee(CoffeeType.CAPPUCCINO)

if isinstance(my_coffee, dict):
    print(my_coffee["milk_amount"])  # Output: 100


# This will cause a type error if you pass a string
# print(brew_coffee("mocha"))  # Type checker will warn about this

# To handle invalid enum values, you'd need to catch exceptions
# or validate the input before calling the function


################################################################################
# another usage of Enums


class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


def get_size_description(size: Size) -> str:
    descriptions = {
        Size.SMALL: "A small size",
        Size.MEDIUM: "A medium size",
        Size.LARGE: "A large size",
    }
    return descriptions.get(size, "Unknown size")


print(get_size_description(Size.MEDIUM))  # Output: A medium size
# print(get_size_description("extra_large"))  # Type checker will warn about this

######################################################################################
# another usage of Enums with string values


class Fruit(str, Enum):
    APPLE = "apple"
    BANANA = "banana"
    CHERRY = "cherry"


def get_fruit_color(fruit: Fruit) -> str:
    colors = {
        Fruit.APPLE: "red",
        Fruit.BANANA: "yellow",
        Fruit.CHERRY: "dark red",
    }
    return colors.get(fruit, "Unknown fruit")


print(get_fruit_color(Fruit.BANANA))  # Output: yellow
# print(get_fruit_color("orange"))  # Type checker will warn about this

######################################################################################
