import sys


def main():
    assert len(sys.argv) == 3, "Wrong numbers of arguments"
    assert sys.argv[1].isdecimal(
    ) and sys.argv[2].isdecimal(), "Arguments are not int"
    print("Sum:", int(sys.argv[1])+int(sys.argv[2]), "\nDifference:",
          int(sys.argv[1])-int(sys.argv[2]), "\nProduct: ", int(
        sys.argv[1])*int(sys.argv[2]),
        "\nQuotient", int(sys.argv[1])/int(sys.argv[2]),
        "\nRemainder:", int(sys.argv[1]) % int(sys.argv[2]))


if (__name__ == "__main__"):
    main()
