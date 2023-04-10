def generator(text: str, sep, option=None):
    "Splits the text according to sep value and yield the substrings. option precise if a action is performed to the substrings before it is yielded."
    if (option not in ["shuffle", "unique", "ordered", None]):
        print("Error")
        return (text)
    assert text.isprintable(), "Error"
    if (option is None):
        return (text.split(sep))
    if (option == "shuffle"):
        return (list(set(text.split(sep))))
    if (option == "unique"):
        return ([c for c in set(text.split(sep))])
    if (option == "ordered"):
        return (sorted(text.split(sep)))


def main():
    test = generator("df fsdfsdf sdf fd sdfd fez fez fd ff ez",
                     sep=" ")
    print(test)
    test = generator("df fsdfsdf sdf fd sdfd fez fez fd ff ez",
                     sep=" ", option="shuffle")
    print(test)
    test = generator("df fsdfsdf sdf fd sdfd fez fez fd ff ez",
                     sep=" ", option="unique")
    print(test)
    test = generator("df fsdfsdf sdf fd sdfd fez fez fd ff ez",
                     sep=" ", option="ordered")
    print(test)


if (__name__ == "__main__"):
    main()
