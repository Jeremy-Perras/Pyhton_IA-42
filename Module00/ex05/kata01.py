def main():
    kata = {'Python': 'Guido van Rossum',
            'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdor', }
    for k, v in kata.items():
        print(k, "was created by", v)


if (__name__ == "__main__"):
    main()
