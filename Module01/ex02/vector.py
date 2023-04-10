class Vector:
    values: list
    shape: tuple

    def __repr__(self):
        txt = str(self.values)
        return txt

    def __str__(self):
        txt = str(self.values)
        return txt

    def __init__(self, values) -> None:
        if (isinstance(values, list)):
            self.shape = (len(values), len(values[0]))
            if (self.shape[0] == 1):
                self.values = [[0] * self.shape[1]]
                for i in range(self.shape[1]):
                    self.values[0][i] = values[0][i]
            elif (self.shape[1] == 1):
                self.values = [[0] for i in range(self.shape[0])]
                for i in range(self.shape[0]):
                    self.values[i][0] = values[i][0]
            else:
                raise ValueError("Invalid Init")
        elif (isinstance(values, int)):
            self.shape = (values, 1)
            self.values = [[i] for i in range(self.shape[0])]
        elif (isinstance(values, tuple)):
            self.shape = (values[1] - values[0], 1)
            self.values = [[values[0] + i] for i in range(self.shape[0])]
        else:
            raise ValueError("Invalid values for Vector")

    def __add__(self, other):
        if (self.shape == other.shape):
            if (self.shape[0] == 1):
                empty = [[0] * self.shape[1]]
                for i in range(self.shape[1]):
                    empty[0][i] = self.values[0][i] + other.values[0][i]
                self.values = empty
            if (self.shape[1] == 1):
                empty = [[0] for i in range(self.shape[0])]
                for i in range(self.shape[0]):
                    empty[i][0] = self.values[i][0] + other.values[i][0]
                self.values = empty
            return (Vector(empty, self.shape))
        raise ValueError("Invalid for addition")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if (self.shape == other.shape):
            if (self.shape[0] == 1):
                empty = [[0] * self.shape[1]]
                for i in range(self.shape[1]):
                    empty[0][i] = self.values[0][i] - other.values[0][i]
                self.values = empty
            if (self.shape[1] == 1):
                empty = [[0] for i in range(self.shape[0])]
                for i in range(self.shape[0]):
                    empty[i][0] = self.values[i][0] - other.values[i][0]
                self.values = empty
            return (Vector(empty, self.shape))
        raise ValueError("Invalid for sub")

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if (isinstance(other, Vector)):
            if (self.shape == other.shape):
                if (self.shape[0] == 1):
                    empty = [[0] * self.shape[1]]
                    for i in range(self.shape[1]):
                        empty[0][i] = self.values[0][i] * other.values[0][i]
                    self.values = empty
                if (self.shape[1] == 1):
                    empty = [[0] for i in range(self.shape[0])]
                    for i in range(self.shape[0]):
                        empty[i][0] = self.values[i][0] * other.values[i][0]
                    self.values = empty
                return (Vector(empty, self.shape))
        elif (isinstance(other, int)):
            if (self.shape[0] == 1):
                empty = [[0] * self.shape[1]]
                for i in range(self.shape[1]):
                    empty[0][i] = self.values[0][i] * other
                self.values = empty
            if (self.shape[1] == 1):
                empty = [[0] for i in range(self.shape[0])]
                for i in range(self.shape[0]):
                    empty[i][0] = self.values[i][0] * other
                self.values = empty
            return (Vector(empty, self.shape))
        raise ValueError("Invalid for multiplication")

    def __rmul__(self, other):
        if (isinstance(other, Vector)):
            if (self.shape == other.shape):
                if (self.shape[0] == 1):
                    empty = [[0] * self.shape[1]]
                    for i in range(self.shape[1]):
                        empty[0][i] = self.values[0][i] * other.values[0][i]
                    self.values = empty
                if (self.shape[1] == 1):
                    empty = [[0] for i in range(self.shape[0])]
                    for i in range(self.shape[0]):
                        empty[i][0] = self.values[i][0] * other.values[i][0]
                    self.values = empty
                return (Vector(empty, self.shape))
        elif (isinstance(other, int)):
            if (self.shape[0] == 1):
                empty = [[0] * self.shape[1]]
                for i in range(self.shape[1]):
                    empty[0][i] = self.values[0][i] * other
                self.values = empty
            if (self.shape[1] == 1):
                empty = [[0] for i in range(self.shape[0])]
                for i in range(self.shape[0]):
                    empty[i][0] = self.values[i][0] * other
                self.values = empty
            return (Vector(empty, self.shape))
        raise ValueError("Invalid for multiplication")

    def __truediv__(self, other):
        try:
            if (isinstance(other, Vector)):
                if (self.shape == other.shape):
                    if (self.shape[0] == 1):
                        empty = [[0] * self.shape[1]]
                        for i in range(self.shape[1]):
                            empty[0][i] = self.values[0][i] / \
                                other.values[0][i]
                        self.values = empty
                    if (self.shape[1] == 1):
                        empty = [[0] for i in range(self.shape[0])]
                        for i in range(self.shape[0]):
                            empty[i][0] = self.values[i][0] / \
                                other.values[i][0]
                        self.values = empty
                    return (Vector(empty, self.shape))
            elif (isinstance(other, int)):
                if (self.shape[0] == 1):
                    empty = [[0] * self.shape[1]]
                    for i in range(self.shape[1]):
                        empty[0][i] = self.values[0][i] / other
                    self.values = empty
                if (self.shape[1] == 1):
                    empty = [[0] for i in range(self.shape[0])]
                    for i in range(self.shape[0]):
                        empty[i][0] = self.values[i][0] / other
                    self.values = empty
                return (Vector(empty, self.shape))
            raise ValueError("Invalid for division")
        except ZeroDivisionError:
            print("Cannot divided by zero")
            return (self)

    def __rtruediv__(self, other):
        try:
            if (isinstance(other, Vector)):
                if (self.shape == other.shape):
                    if (self.shape[0] == 1):
                        empty = [[0] * self.shape[1]]
                        for i in range(self.shape[1]):
                            empty[0][i] = self.values[0][i] / \
                                other.values[0][i]
                        self.values = empty
                    if (self.shape[1] == 1):
                        empty = [[0] for i in range(self.shape[0])]
                        for i in range(self.shape[0]):
                            empty[i][0] = self.values[i][0] / \
                                other.values[i][0]
                        self.values = empty
                    return (Vector(empty, self.shape))
            elif (isinstance(other, int)):
                if (self.shape[0] == 1):
                    empty = [[0] * self.shape[1]]
                    for i in range(self.shape[1]):
                        empty[0][i] = self.values[0][i] / other
                    self.values = empty
                if (self.shape[1] == 1):
                    empty = [[0] for i in range(self.shape[0])]
                    for i in range(self.shape[0]):
                        empty[i][0] = self.values[i][0] / other
                    self.values = empty
                return (Vector(empty, self.shape))
            raise ValueError("Invalid for division")
        except ZeroDivisionError:
            print("Cannot divided by zero")
            return (self)

    def T(self):

        if (self.shape[0] == 1):
            empty = [[0] for i in range(self.shape[1])]
            for i in range(self.shape[1]):
                empty[i][0] = (self.values[0][i])
            self = Vector(empty)
        elif (self.shape[1] == 1):
            empty = [[0] * self.shape[0]]
            print(empty)
            for i in range(self.shape[0]):
                empty[0][i] = (self.values[i][0])
            self = Vector(empty)

    def dot(self, other):
        if (self.shape == other.shape):
            if (self.shape[0] == 1):
                raise ValueError(
                    "Dot product impossible ")
            elif (self.shape[1] == 1):
                count = 0
                for i in range(self.shape[0]):
                    count = count + self.values[i][0] * other.values[i][0]
                return (count)
