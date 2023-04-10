class Evaluator:
    @staticmethod
    def zip_evaluate(coefs: list, word: list):
        count = 0
        if (len(coefs) != len(word)):
            return (-1)
        zipe = [e for e in map(list,  zip(word, coefs))]
        for e in zipe:
            count += e[1] * len(e[0])
        print(count)

    @ staticmethod
    def enumerate_evaluate(coefs, word):
        count = 0
        if (len(coefs) != len(word)):
            return (-1)
        for inc, e in enumerate(coefs):
            count += len(word[inc]) * e
        print(count)


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
