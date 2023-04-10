def what_are_the_vars(*args, **kwargs):


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


def main():
    what_are_the_vars()


if (__name__ == "__main__"):
    main()
