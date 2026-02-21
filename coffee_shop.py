from enum import Enum


class CoffeeType(Enum):
    ESPRESSO = 1
    LATTE = 2
    CAPPUCCINO = 3
    MACCHIATO = 4
    FLAT_WHITE = 5
    RISTRETTO = 6
    CORTADO = 7
    ESPRESSO_MACCHIATO = 8


# CoffeeType.ESPRESSO: <enum ‘CoffeeType’>
# CoffeeType.ESPRESSO = 10 # This will not change the enum member
# why because Enums are immutable.
print(CoffeeType.ESPRESSO.value)  # Output: 1 <class ‘int’>
print(CoffeeType.LATTE.name)  # Output: LATTE
print(CoffeeType(3))  # Output: CoffeeType.CAPPUCCINO

print(ESSPRESSO := CoffeeType.ESPRESSO)  # Using the walrus operator
# ESPRESSO saves result of CoffeeType.ESPRESSO.
print(CoffeeType.ESPRESSO_MACCHIATO)

print("*" * 70)

# You’ll often use integers as values for enum members—that’s
# why they’re called enumerations. But you don’t have to:


class CoffeeType(Enum):
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"
    MACCHIATO = "macchiato"
    FLAT_WHITE = "flat_white"
    RISTRETTO = "ristretto"
    CORTADO = "cortado"


print(CoffeeType.ESPRESSO)  # CoffeeType.ESPRESSO
print(CoffeeType.ESPRESSO.name)  # ESPRESSO
print(CoffeeType.ESPRESSO.value)  # espresso

# You can use these enum members instead of strings wherever you need
# to refer to each coffee type:

# ...
coffee_types = {
    CoffeeType.ESPRESSO: {"strength": 3, "coffee_amount": 30, "milk_amount": 0},
    CoffeeType.LATTE: {"strength": 1, "coffee_amount": 30, "milk_amount": 150},
    CoffeeType.CAPPUCCINO: {"strength": 2, "coffee_amount": 30, "milk_amount": 100},
    CoffeeType.MACCHIATO: {"strength": 3, "coffee_amount": 30, "milk_amount": 10},
    CoffeeType.FLAT_WHITE: {"strength": 2, "coffee_amount": 30, "milk_amount": 120},
    CoffeeType.RISTRETTO: {"strength": 4, "coffee_amount": 20, "milk_amount": 0},
    CoffeeType.CORTADO: {"strength": 2, "coffee_amount": 30, "milk_amount": 60},
}
# …and again when you call brew_coffee():

"""
# ...
brew_coffee(CoffeeType.CORTADO
"""

# Now you have a safer, neater, and more robust way to handle the
# coffee types... and treat them as constants.
print("*" * 70)

# COMPLETE ABOVE EXAMPLE AT ONE PLACE FOR EASY UNDERSTANDING
# ==========================================================
print(2 * 3 ** 2) 