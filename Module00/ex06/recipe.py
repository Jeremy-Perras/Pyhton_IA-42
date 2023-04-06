cookbook = {'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'],
                         'lunch', '10'),
            'cake': (['flour', 'sugar', 'eggs'], 'dessert', '60'),
            'salad': (['avocado', 'arugula', 'tomatoes', 'spinach'],
                      'lunch', '15')}


def printAll(cookbook: dict):
    for k in cookbook:
        print(k)


def printDetail(recipe: str, cookbook: dict):
    print(cookbook[recipe])


def delete(recipe: str, cookbook: dict):
    del (cookbook[recipe])


def add(cookbook: dict):
    print('Enter your name:')
    name = input()
    print('number of ingrediens')
    n = int(input())
    print('list of ingredien:')
    ingrediens = []
    for i in range(0, n):
        ingrediens .append(input())
    print('meal type:')
    meal = input()
    print('time:')
    time = int(input())
    cookbook[name] = (ingrediens, meal, time)


def main():
    flag = 0
    print("Welcome to the Python Cookbook !\n", "List of available option:\n",
          "1: Add a recipe\n"
          "2: Delete a recipe\n"
          "3: Print a recipe\n"
          "4: Print the cookbook\n"
          "5: Quit")
    # fundict = {"add": (add)}
    # print(fundict["add"](cookbook))
    # pointer on function
    while (flag == 0):
        print("Please select an option:")
        option = input()
        assert option.isdecimal(), "Sorry this option does not exist"
        option = int(option)
        assert option >= 1 and option <= 5, "Sorry this option does not exist"
        if (option == 1):
            add(cookbook)
        elif (option == 2):
            print("select a recipe")
            recipe = input()
            delete(recipe, cookbook)
        elif (option == 3):
            print("select a recipe")
            recipe = input()
            printDetail(recipe, cookbook)
        elif (option == 4):
            printAll(cookbook)
        elif (option == 5):
            flag = 1


if (__name__ == "__main__"):

    main()
