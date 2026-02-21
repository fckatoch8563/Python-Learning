# class Meal:
#     def __init__(
#         self,
#         name,
#         person_cooking,
#         quick_meal=False,
#     ):
#         self.name = name
#         self.person_cooking = person_cooking
#         self.quick_meal = quick_meal
#         self.ingredients = {}  # ingredient: quantity
#         self.ratings = {}  # person: rating

#     # ... more methods


class WeeklyMealPlanner:
    def __init__(self):
        self._meals = {}  # day: Meal

    @property
    def meals(self):
        return dict(self._meals)

    # ... more methods


# class ShoppingList:
#     def __init__(self):
#         self.ingredients = {}  # ingredient: quantity

#     def add_ingredient(self, ingredient, quantity=1):
#         if ingredient in self.ingredients:
#             self.ingredients[ingredient] += quantity
#         else:
#             self.ingredients[ingredient] = quantity

#     # ... more methods


#######################################################################################################
class ShoppingList:
    def __init__(self):
        self.ingredients = {}  # ingredient: quantity

    @classmethod
    def from_meal_planner(cls, meal_planner: WeeklyMealPlanner):
        shopping_list = cls()
        for meal in meal_planner.meals.values():
            if meal is None:
                continue
            for ingredient, quantity in meal.ingredients.items():
                shopping_list.add_ingredient(ingredient, quantity)
        return shopping_list

    def add_ingredient(self, ingredient, quantity=1):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity


# if my_weekly_planner is an instance of 'WeeklyMealPlanner', then...

my_weekly_planner = WeeklyMealPlanner()
shopping_list = ShoppingList.from_meal_planner(my_weekly_planner)
