import sys


def main():
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    assert len(sys.argv) == 3, "ERROR"
    lst = []
    assert sys.argv[2].isdecimal(), "ERROR"
    spt = sys.argv[1].split(" ")
    for c in spt:
        if (len(c) > int(sys.argv[2]) and c not in punctuations):
            lst.append(c)
    print(lst)


if (__name__ == "__main__"):
    main()
