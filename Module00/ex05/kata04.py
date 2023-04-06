def main():
    kata = (0, 4, 132.42222, 10000, 12345.67)
    for i in kata:
        print(format(round(i, 2), '.2E'))


if (__name__ == "__main__"):
    main()
