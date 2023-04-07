from book import Book
from recipe import Recipe


def main():
    b = Book()
    b.get_recipe_by_name("test")
    test = Recipe("te", 10, ["t", "e", "a"], "starter", 10)
    test2 = Recipe("te", 10, ["t", "e", "a"], "starter", 10)
    test3 = Recipe("te", 10, ["t", "e", "a"], "lunch", 10)
    test4 = Recipe("te", 10, ["t", "e", "a"], "lunch", 10)
    b.add_recipe(test)
    b.add_recipe(test2)
    b.add_recipe(test3)
    b.add_recipe(test4)
    b.get_recipes_by_types("lunch")


if (__name__ == "__main__"):
    main()
