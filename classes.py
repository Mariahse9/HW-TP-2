class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.quantity}', '{self.unit}')"

    def __eq__(self, other):

        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for i in self.ingredient:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio):
        new_ingredients = [
            Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            for ing in self.ingredients
        ]
        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return f"{self.title}:\n{self.ingredients}"


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for i in scaled.ingredients:
            self._items.append((i, recipe.title))

    def remove_recipe(self, title):
        self._items = [i for i in self._items if i[1] != title]

    def get_list(self):
        result = {}
        for i, titl in self._items:
            par = (i.name, i.unit)
            if par in result:
                result[par] += i.quantity
            else:
                result[par] = i.quantity

        ingredients = []
        for (name, unit), quantity in result.items():
            ingredients.append(Ingredient(name, quantity, unit))
        ingredients.sort(key=lambda x: x.name)
        return ingredients

    def __add__(self, other):
        new_lst = ShoppingList()
        new_lst._items = self._items + other._items
        return new_lst


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        scaled_recipe = super().scaled(ratio)
        return DietaryRecipe(self.title, self.diet_type, scaled_recipe.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"


import pytest
