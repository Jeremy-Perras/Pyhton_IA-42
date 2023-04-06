
import sys


def main():
    assert len(
        sys.argv) == 2, "More than one or less than one argument are provided"
    assert not sys.argv[1].isdigit(), "argument is not an string"
    text_analyzer(sys.argv[1])


def text_analyzer(text: str):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text"""
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    upper = 0
    lower = 0
    punctuation = 0
    space = 0

    for c in text:
        if (c.islower()):
            lower += 1
        elif (c.isupper()):
            print(c)
            upper += 1
        elif (c.isspace()):
            space += 1
        elif (c in punctuations):
            punctuation += 1

    print("The text contains", len(text), "character(s):\n", "- ",
          upper, "upper letter(s)\n", "- ",
          lower, "lower letter(s)\n", "- ",
          punctuation, "punctuation mark(s)\n",
          "- ", space, "space(s)\n")


if (__name__ == "__main__"):
    main()
    print(text_analyzer.__doc__)
