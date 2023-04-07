import datetime
from recipe import Recipe
import sys


class Book:
    name: str
    lastupdate: datetime.datetime
    creation_date: datetime.datetime
    recipes_list: dict
    recipes_list = {"starter": [],
                    "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        if (isinstance(name, str)):
            for key, values in self.recipes_list.items():
                for value in values:
                    if (value == name):
                        return (value)
        else:
            print("Wrong name type")
            sys.exit()

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (recipe_type in ["starter", "lunch", "dessert"]):
            for elem in self.recipes_list[recipe_type]:
                print(elem)
        else:
            print("Wrong recipe type")
            return

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipee_type].append(recipe)
