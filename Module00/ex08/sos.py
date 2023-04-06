import sys


def sos(string: str):

    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "a": ".- ",
                    "b": "-... ",
                    "c": "-.-. ",
                    "d": "-.. ",
                    "e": ". ",
                    "f": "..-. ",
                    "g": "--. ",
                    "h": ".... ",
                    "i": ".. ",
                    "j": ".--- ",
                    "k": "-.- ",
                    "l": ".-.. ",
                    "m": "-- ",
                    "n": "-. ",
                    "o": "--- ",
                    "p": ".--. ",
                    "q": "--.- ",
                    "r": ".-. ",
                    "s": "... ",
                    "t": "- ",
                    "u": "..- ",
                    "v": "...- ",
                    "w": ".-- ",
                    "x": "-..- ",
                    "y": "-.-- ",
                    "z": "--.. ",
                    "0": ".- ",
                    "1": ".- ",
                    "2": ".- ",
                    "3": ".- ",
                    "4": ".- ",
                    "5": ".- ",
                    "6": ".- ",
                    "7": ".- ",
                    "8": ".- ",
                    "9": ".- ",
                    }
    for c in string:
        print(NESTED_MORSE[c], end="")


def main():
    if (len(sys.argv) >= 2):
        for i in range(1, len(sys.argv)):
            for c in sys.argv[i]:
                assert (c.isalpha() or c.isalnum()
                        or c.isspace()), "Bad argument"
        for i in range(1, len(sys.argv)):
            sos(sys.argv[i])
            if (i != len(sys.argv) - 1):
                sos(" ")

    else:
        assert (len(sys.argv) != 1 and len(sys.argv) <= 2), "Bad argument"
        for c in sys.argv[1]:
            assert (c.isalpha()
                    or c.isalnum() or c.isspace()), "Bad argument"
        sos(sys.argv[1])


if (__name__ == "__main__"):
    main()
