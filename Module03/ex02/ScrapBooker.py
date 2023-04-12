import numpy as np


class ScrapBooker():
    def crop(self, array: np.array, dim, position=(0, 0)):
        return (array[position[0]:position[0]+dim[0], position[1]:position[1]+dim[1]])

    def thin(self, array, n, axis):
        if axis:
            axis_copy = 0
        else:
            axis_copy = 1
        if n > array.shape[axis_copy]:
            return None
        return np.delete(array, n-1, axis_copy)

    def juxtapose(self, array: np.array, n, axis):
        if axis:
            return np.tile(array, (1, n))
        else:
            return np.tile(array, (n, 1))
        # if (axis):
        #     row = array[0]
        #     size = np.shape(array)
        #     new = row
        #     for i in range(0, size[0] - 1):
        #         new = np.row_stack((new, row))
        #     start = new
        #     for i in range(0, n - 1):
        #         new = np.column_stack((new, start))
        #     return (new)
        # else:
        #     column = array[0]
        #     size = np.shape(array)
        #     new = column
        #     for i in range(0, n - 1):
        #         new = np.column_stack((new, column))
        #     start = new
        #     for i in range(0, size[0] - 1):
        #         new = np.row_stack((new, start))
        #     return (new)

    def mosaic(self, array, dim):
        return np.tile(array, dim)
        # new = self.juxtapose(array, np.shape(array)[0] * dim[0], 1)
        # new = self.juxtapose(new, np.shape(new)[1] * dim[1], 0)
        # return (new)


if (__name__ == "__main__"):
    # arr1 = np.arange(0, 25).reshape(5, 5)
    spb = ScrapBooker()
    # print(arr1)
    # print()
    # print(spb.crop(arr1, (3, 1), (1, 0)))
    # arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    # print(arr2)
    arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    # print(np.row_stack((arr3[0], [1, 2, 3])))
    # print(arr3)
    # print()
    print(spb.mosaic(arr3, (1, 1)))
