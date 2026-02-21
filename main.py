def brew_coffee(coffee_type: str):
    coffee_types = {
        "espresso": {"strength": 3, "coffee_amount": 30, "milk_amount": 0},
        "latte": {"strength": 1, "coffee_amount": 30, "milk_amount": 150},
        "cappuccino": {"strength": 2, "coffee_amount": 30, "milk_amount": 100},
        "macchiato": {"strength": 3, "coffee_amount": 30, "milk_amount": 10},
        "flat_white": {"strength": 2, "coffee_amount": 30, "milk_amount": 120},
        "ristretto": {"strength": 4, "coffee_amount": 20, "milk_amount": 0},
        "cortado": {"strength": 2, "coffee_amount": 30, "milk_amount": 60},
    }

    return coffee_types.get(coffee_type, "Unknown coffee type")


print(brew_coffee("espresso"))
my_coffee = brew_coffee("cappuccino")

if isinstance(my_coffee, dict):
    print(my_coffee["milk_amount"])  # Output: 100


print(brew_coffee("mocha"))  # Output: Unknown coffee type

# Type something simple to test
print("Hello from Codespace!")

l1 = [1, 2, 3]
l2 = [4, 5, 6]
result = list(zip(l1, l2))
print(result)
