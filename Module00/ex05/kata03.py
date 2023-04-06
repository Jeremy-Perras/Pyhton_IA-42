def main():
    kata = "The right format"
    while len(kata) != 42:
        kata = "-" + kata
    print(kata, end="")


if (__name__ == "__main__"):
    main()
