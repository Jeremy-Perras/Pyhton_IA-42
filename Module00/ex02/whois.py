
import sys


def main():
    assert len(sys.argv) == 2, "More than one argument are provided"
    assert sys.argv[1].isdigit(), "argument is not an integer"
    if (int(sys.argv[1]) == 0):
        print("I'm Zero")
    elif (int(sys.argv[1]) % 2):
        print("I'm Odd.")
    else:
        print("I'm Even.")


if (__name__ == "__main__"):
    main()
