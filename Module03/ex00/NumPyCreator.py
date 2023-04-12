import numpy as np
import numpy


class NumpyCreator():

    def from_list(self, lst):
        try:
            return (np.array(lst))
        except:
            return None

    def from_tuple(self, tpl):
        return (np.asarray(tpl))

    def from_iterable(self, itr):
        return (np.array(itr))

    def from_shape(self, shape, value=0):
        return (np.ones(shape)*value)

    def random(self, shape):
        return (np.random.random(shape))

    def identity(self, n):
        return (np.identity(n))


if (__name__ == "__main__"):
    npc = NumpyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    # Output :

    print(npc.from_list([[1, 2, 3], [6, 4]]))
    # # Output :
    # None
    print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
    # # Output :

    print(npc.from_list(((1, 2), (3, 4))))
    # # Output :
    # None
    print(npc.from_tuple(("a", "b", "c")))
    # # Output :

    print(npc.from_tuple(["a", "b", "c"]))
    # # Output :
    # None
    print(npc.from_iterable(range(5)))
    # # Output :

    shape = (3, 5)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))
