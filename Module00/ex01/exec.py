import sys


def main():
    i = len(sys.argv) - 1
    while (i != 0):
        j = len(sys.argv[i])-1
        while (j != -1):
            if (sys.argv[i][j].islower()):
                print(sys.argv[i][j].upper(), end="")
            elif (sys.argv[i][j].isupper()):
                print(sys.argv[i][j].lower(), end="")
            else:
                print(sys.argv[i][j], end="")
            j -= 1
        i -= 1


if (__name__ == "__main__"):
    main()
