import random


def main():
    print("This is an interactive guessing game!\n",
          "You have to enter a number between 1 and 99 to find out the \
              secret number.\n",
          "Type 'exit' to end the game.\n", "Good luck!")
    flag = 0
    rand = random.randint(1, 99)
    inc = 0
    while (flag == 0):
        print("What's your guess between 1 and 99?")
        i = input()
        if (i == "exit"):
            flag = 1
        inc += 1
        if (i.isdecimal()):
            i = int(i)
            if (i == rand):
                print("Congratulations, you've got it!")
                if (inc == 1):
                    print("Congratulations! You got it on your first try!")
                else:
                    print("You won in", inc, "attempts!")
                if (rand == 42):
                    print(
                        "The answer to the ultimate question of life, the\
                            universe and everything is 42")
                flag = 1
            elif (i > rand):
                print("Too high!")
            elif (i < rand):
                print("Too Low!")


if (__name__ == "__main__"):
    main()
