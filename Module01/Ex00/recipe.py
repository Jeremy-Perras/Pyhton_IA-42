import sys


def valid_value(name: str, cooking_lvl: int, ingredients: list, recipee_type: str, cooking_time: int):
    if (len(name) == 0 or len(ingredients) == 0 or len(recipee_type) == 0):
        print("Wrong argument len")
        return (0)
    if (recipee_type not in ["starter", "lunch", "dessert"]):
        print("Wrong Recipe type")
        return (0)
    try:
        int(cooking_lvl)
        int(cooking_time)
    except ValueError:
        print("cooking lvl and time need to be int")
        return (0)
    return (1)


class Recipe:
    name: str
    cooking_lvl: int
    ingredients: list
    description: str
    cooking_time: int
    recipee_type: str

    def __init__(self, name: str, cooking_lvl: int, ingredients: list, recipee_type: str, cooking_time: int):
        if (valid_value(name, cooking_lvl, ingredients, recipee_type, cooking_time)):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.ingredients = ingredients
            self.recipee_type = recipee_type
            self.cooking_time = cooking_time
        else:
            sys.exit()

    def __str__(self):
        txt = f"name={self.name}\ningredient={[i for i in self.ingredients]}\nlvl={self.cooking_lvl}\nrecipe type={self.recipee_type}\n cooking time = {self.cooking_time}"
        return txt


def main():
    test = Recipe("te", 10, ["t", "e", "a"], "starter", 10)
    print(str(test))


if (__name__ == "__main__"):
    main()
