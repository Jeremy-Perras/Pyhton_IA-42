import time


def ft_progress(list):
    print(1)


def main():
    listy = range(1001)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)


if (__name__ == "__main__"):
    main()
