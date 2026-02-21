"""
Different ways to define constants in Python
"""

# ============================================================================
# 1. SIMPLE MODULE-LEVEL VARIABLES (Most Common)
# ============================================================================
print("1. Simple Variables:")
ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

print(f"ESPRESSO: {ESPRESSO}")
print(f"MAX_RETRIES: {MAX_RETRIES}\n")


# ============================================================================
# 2. ENUM (Type-safe, Best for related constants)
# ============================================================================
print("2. Enum:")
from enum import Enum


class CoffeeType(Enum):
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"


print(f"CoffeeType.ESPRESSO: {CoffeeType.ESPRESSO}")
print(f"CoffeeType.ESPRESSO.value: {CoffeeType.ESPRESSO.value}")
print(f"Iteration: {[coffee.name for coffee in CoffeeType]}\n")


# ============================================================================
# 3. TYPING.FINAL (Python 3.8+, Type hint for constants)
# ============================================================================
print("3. typing.Final:")
from typing import Final

ESPRESSO_FINAL: Final = "espresso"
LATTE_FINAL: Final = "latte"
MAX_STRENGTH: Final[int] = 5

print(f"ESPRESSO_FINAL: {ESPRESSO_FINAL}")
print(f"MAX_STRENGTH: {MAX_STRENGTH}\n")


# ============================================================================
# 4. CLASS WITH CONSTANTS
# ============================================================================
print("4. Class with Constants:")


class CoffeeConstants:
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"

    STRENGTH_LEVELS = {
        "espresso": 3,
        "latte": 1,
        "cappuccino": 2,
    }


print(f"CoffeeConstants.ESPRESSO: {CoffeeConstants.ESPRESSO}")
print(f"CoffeeConstants.STRENGTH_LEVELS: {CoffeeConstants.STRENGTH_LEVELS}\n")


# ============================================================================
# 5. FROZEN DATACLASS (Python 3.7+)
# ============================================================================
print("5. Frozen Dataclass:")
from dataclasses import dataclass


@dataclass(frozen=True)
class CoffeeSettings:
    ESPRESSO: str = "espresso"
    LATTE: str = "latte"
    CAPPUCCINO: str = "cappuccino"
    MAX_BREW_TIME: int = 30


settings = CoffeeSettings()
print(f"settings.ESPRESSO: {settings.ESPRESSO}")
print(f"settings.MAX_BREW_TIME: {settings.MAX_BREW_TIME}\n")


# ============================================================================
# 6. NAMEDTUPLE
# ============================================================================
print("6. NamedTuple:")
from typing import NamedTuple


class CoffeeTypes(NamedTuple):
    ESPRESSO: str = "espresso"
    LATTE: str = "latte"
    CAPPUCCINO: str = "cappuccino"


coffee = CoffeeTypes()
print(f"coffee.ESPRESSO: {coffee.ESPRESSO}")
print(f"coffee as tuple: {tuple(coffee)}\n")


# ============================================================================
# 7. DICTIONARY (For grouped configuration)
# ============================================================================
print("7. Dictionary:")
COFFEE_CONFIG = {
    "ESPRESSO": {"strength": 3, "milk": 0},
    "LATTE": {"strength": 1, "milk": 150},
    "CAPPUCCINO": {"strength": 2, "milk": 100},
}

print(f"COFFEE_CONFIG: {COFFEE_CONFIG}\n")


# ============================================================================
# COMPARISON AND USE CASES
# ============================================================================
print("=" * 70)
print("COMPARISON & USE CASES:")
print("=" * 70)

comparison = """
1. Simple Variables
   - Pros: Simple, lightweight, fast
   - Cons: No type safety, easy to pass wrong value
   - Use: Simple constant values, module config

2. Enum
   - Pros: Type-safe, validatable, iterable, clear intent
   - Cons: Slightly more boilerplate
   - Use: Set of related constants (statuses, types, directions)

3. typing.Final
   - Pros: Type hints indicate immutability
   - Cons: Runtime not enforced (type checker only)
   - Use: Single constants you want to type-check

4. Class with Constants
   - Pros: Namespace organization, can have related methods
   - Cons: More verbose
   - Use: Organizing many related constants

5. Frozen Dataclass
   - Pros: Immutable, can have type hints, callable
   - Cons: More boilerplate than simple variables
   - Use: Structured constant configurations

6. NamedTuple
   - Pros: Lightweight, immutable, tuple-like behavior
   - Cons: Less common for constants
   - Use: Simple grouped constants

7. Dictionary
   - Pros: Flexible, easy to extend
   - Cons: No type safety, no validation
   - Use: Configuration data, lookup tables
"""

print(comparison)
