class Meal:
    def __init__(
        self,
        name,
        person_cooking,
        quick_meal=False,
    ):
        self.name = name
        self.person_cooking = person_cooking
        self.quick_meal = quick_meal
        self.ingredients = {}  # ingredient: quantity
        self.ratings = {}  # person: rating

    def add_ingredient(self, ingredient, quantity):
        """Add an ingredient to the meal."""
        self.ingredients[ingredient] = quantity

    def add_rating(self, person, rating):
        """Add a rating from a person (1-5)."""
        if 1 <= rating <= 5:
            self.ratings[person] = rating
        else:
            raise ValueError("Rating must be between 1 and 5")

    def average_rating(self):
        """Calculate average rating of the meal."""
        if not self.ratings:
            return 0
        return sum(self.ratings.values()) / len(self.ratings)

    def __str__(self):
        return f"Meal: {self.name} (cooked by {self.person_cooking}, quick: {self.quick_meal})"

    def __repr__(self):
        return f"Meal(name='{self.name}', person_cooking='{self.person_cooking}', quick_meal={self.quick_meal})"


class WeeklyMealPlanner:
    def __init__(self):
        self._meals = {}  # day: Meal

    @property
    def meals(self):
        return dict(self._meals)

    def add_meal(self, day, meal):
        """Add a meal to a specific day."""
        valid_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        if day not in valid_days:
            raise ValueError(f"Day must be one of {valid_days}")
        self._meals[day] = meal

    def get_meal(self, day):
        """Get meal for a specific day."""
        return self._meals.get(day, None)

    def remove_meal(self, day):
        """Remove meal from a specific day."""
        if day in self._meals:
            del self._meals[day]

    def get_quick_meals(self):
        """Get all quick meals for the week."""
        return [meal for meal in self._meals.values() if meal.quick_meal]

    def get_shopping_list(self):
        """Generate shopping list from all meals."""
        shopping_list = ShoppingList()
        for meal in self._meals.values():
            for ingredient, quantity in meal.ingredients.items():
                shopping_list.add_ingredient(ingredient, quantity)
        return shopping_list

    def __str__(self):
        return f"Weekly Meal Planner with {len(self._meals)} meals planned"


class ShoppingList:
    def __init__(self):
        self.ingredients = {}  # ingredient: quantity

    def add_ingredient(self, ingredient, quantity=1):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

    def remove_ingredient(self, ingredient):
        """Remove an ingredient from the list."""
        if ingredient in self.ingredients:
            del self.ingredients[ingredient]

    def update_ingredient(self, ingredient, quantity):
        """Update quantity of an ingredient."""
        self.ingredients[ingredient] = quantity

    def total_items(self):
        """Get total number of items."""
        return sum(self.ingredients.values())

    def get_ingredients(self):
        """Return a copy of ingredients."""
        return dict(self.ingredients)

    def clear_list(self):
        """Clear all ingredients."""
        self.ingredients.clear()

    def __str__(self):
        items = "\n".join(
            [f"  - {ing}: {qty}" for ing, qty in self.ingredients.items()]
        )
        return f"Shopping List ({self.total_items()} items):\n{items}"

    def __repr__(self):
        return f"ShoppingList(items={len(self.ingredients)})"


# ============ EXAMPLE USAGE ============

if __name__ == "__main__":
    # Create meals
    pasta = Meal("Spaghetti Carbonara", "Alice", quick_meal=True)
    pasta.add_ingredient("Pasta", 400)
    pasta.add_ingredient("Eggs", 3)
    pasta.add_ingredient("Bacon", 200)
    pasta.add_ingredient("Cheese", 100)

    curry = Meal("Chicken Curry", "Bob", quick_meal=False)
    curry.add_ingredient("Chicken", 500)
    curry.add_ingredient("Curry Paste", 2)
    curry.add_ingredient("Coconut Milk", 1)
    curry.add_ingredient("Rice", 250)

    salad = Meal("Caesar Salad", "Charlie", quick_meal=True)
    salad.add_ingredient("Lettuce", 300)
    salad.add_ingredient("Croutons", 100)
    salad.add_ingredient("Parmesan", 50)
    salad.add_ingredient("Dressing", 100)

    # Add ratings
    pasta.add_rating("Alice", 5)
    pasta.add_rating("Bob", 4)
    pasta.add_rating("Charlie", 5)

    curry.add_rating("Bob", 4)
    curry.add_rating("Alice", 3)

    salad.add_rating("Charlie", 5)
    salad.add_rating("Alice", 4)

    # Create weekly planner
    planner = WeeklyMealPlanner()
    planner.add_meal("Monday", pasta)
    planner.add_meal("Tuesday", curry)
    planner.add_meal("Wednesday", salad)
    planner.add_meal("Friday", pasta)

    # Display information
    print("=" * 50)
    print("MEAL INFORMATION")
    print("=" * 50)
    print(f"\n{pasta}")
    print(f"Average rating: {pasta.average_rating():.2f}")
    print(f"Ingredients: {pasta.ingredients}\n")

    print(f"{curry}")
    print(f"Average rating: {curry.average_rating():.2f}\n")

    # Weekly planner
    print("=" * 50)
    print("WEEKLY MEAL PLAN")
    print("=" * 50)
    print(f"\n{planner}")
    print(f"Meals planned: {len(planner.meals)}")

    for day, meal in planner.meals.items():
        print(f"  {day}: {meal.name}")

    # Quick meals
    print(f"\nQuick meals: {[m.name for m in planner.get_quick_meals()]}")

    # Shopping list
    print("\n" + "=" * 50)
    print("SHOPPING LIST")
    print("=" * 50)
    shopping_list = planner.get_shopping_list()
    print(f"\n{shopping_list}")
    print(f"Total items to buy: {shopping_list.total_items()}")

    # Remove and update ingredients
    print("\n" + "=" * 50)
    print("SHOPPING LIST OPERATIONS")
    print("=" * 50)
    shopping_list.remove_ingredient("Croutons")
    print(f"After removing Croutons: {shopping_list.total_items()} items")

    shopping_list.update_ingredient("Pasta", 800)
    print(f"After updating Pasta to 800: {shopping_list.total_items()} items")
    print(f"\nUpdated list:\n{shopping_list}")


"""
THE EXAMPLE DEMONSTRATES:
1. Creating Meals - 3 different meals with ingredients
2. Adding Ratings - Each meal gets rated by different people
3. Calculating Averages - Showing average rating (Carbonara: 4.67/5)
4. Weekly Planner - Planning 4 meals across different days
5. Filtering - Getting only quick meals
6. Shopping List - Auto-generating aggregated shopping list from all meals
7. List Operations - Removing and updating ingredients


# OUTPUT SHOWS WEEKLY MEAL PLAN AND SHOPPING LIST DETAILS

==================================================
MEAL INFORMATION
==================================================

Meal: Spaghetti Carbonara (cooked by Alice, quick: True)
Average rating: 4.67
Ingredients: {'Pasta': 400, 'Eggs': 3, 'Bacon': 200, 'Cheese': 100}

Meal: Chicken Curry (cooked by Bob, quick: False)
Average rating: 3.50

==================================================
WEEKLY MEAL PLAN
==================================================

Weekly Meal Planner with 4 meals planned
Meals planned: 4
  Monday: Spaghetti Carbonara
  Tuesday: Chicken Curry
  Wednesday: Caesar Salad
  Friday: Spaghetti Carbonara

Quick meals: ['Spaghetti Carbonara', 'Caesar Salad', 'Spaghetti Carbonara']

==================================================
SHOPPING LIST
==================================================

Shopping List (2709 items):
  - Pasta: 800
  - Eggs: 6
  - Bacon: 400
  - Cheese: 200
  - Chicken: 500
  - Curry Paste: 2
  - Coconut Milk: 1
  - Rice: 250
  - Lettuce: 300
  - Croutons: 100
  - Parmesan: 50
  - Dressing: 100
Total items to buy: 2709

==================================================
SHOPPING LIST OPERATIONS
==================================================
After removing Croutons: 2609 items
After updating Pasta to 800: 2609 items

Updated list:
Shopping List (2609 items):
  - Pasta: 800
  - Eggs: 6
  - Bacon: 400
  - Cheese: 200
  - Chicken: 500
  - Curry Paste: 2
  - Coconut Milk: 1
  - Rice: 250
  - Lettuce: 300
  - Parmesan: 50
  - Dressing: 100
(.venv) PS C:\Users\fckat\Desktop\Learn Python>
(.venv) PS C:\Users\fckat\Desktop\Learn Python> python meal_planner.py
==================================================
MEAL INFORMATION
==================================================

Meal: Spaghetti Carbonara (cooked by Alice, quick: True)
Average rating: 4.67
Ingredients: {'Pasta': 400, 'Eggs': 3, 'Bacon': 200, 'Cheese': 100}

Meal: Chicken Curry (cooked by Bob, quick: False)
Average rating: 3.50

==================================================
WEEKLY MEAL PLAN
==================================================

Weekly Meal Planner with 4 meals planned
Meals planned: 4
  Monday: Spaghetti Carbonara
  Tuesday: Chicken Curry
  Wednesday: Caesar Salad
  Friday: Spaghetti Carbonara

Quick meals: ['Spaghetti Carbonara', 'Caesar Salad', 'Spaghetti Carbonara']

==================================================
SHOPPING LIST
==================================================

Shopping List (2709 items):
  - Pasta: 800
  - Eggs: 6
  - Bacon: 400
  - Cheese: 200
  - Chicken: 500
  - Curry Paste: 2
  - Coconut Milk: 1
  - Rice: 250
  - Lettuce: 300
  - Croutons: 100
  - Parmesan: 50
  - Dressing: 100
Total items to buy: 2709

==================================================
SHOPPING LIST OPERATIONS
==================================================
After removing Croutons: 2609 items
After updating Pasta to 800: 2609 items

Updated list:
Shopping List (2609 items):
  - Pasta: 800
  - Eggs: 6
  - Bacon: 400
  - Cheese: 200
  - Chicken: 500
  - Curry Paste: 2
  - Coconut Milk: 1
  - Rice: 250
  - Lettuce: 300
  - Parmesan: 50
  - Dressing: 100
"""