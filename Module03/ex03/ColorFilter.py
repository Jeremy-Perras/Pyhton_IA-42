import numpy as np


class ColorFilter ():
    def invert(self, array):
        # new = np.copy(array)
        # size = np.shape(new)
        # for i in range(size[0]):
        #     for j in range(size[1]):
        #         data = array[i, j]
        #         new[i, j] = (255 - data[0], 255 - data[1],
        #                      255 - data[2])
        return 1 - array

    def to_blue(self, array):
        new = np.zeros(array.shape)
        new[:, :, 2] = array[:, :, 2]
        return new

    def to_green(self, array):
        new = np.zeros(array.shape)
        new[:, :, 1] = array[:, :, 1]
        return new

    def to_red(self, array):
        new = np.zeros(array.shape)
        new[:, :, 0] = array[:, :, 0]
        return new

    def to_celluloid(self, array):
        new = np.array(array)
        treshholds = np.linspace(0.0, 1.0, num=4, endpoint=False)
        for shade in treshholds:
            new[array >= shade] = shade
        return new

    def to_grayscale(self, array, filter, **kwargs):
        if filter in ['m', 'mean']:
            new = np.array(array)
            for row in new:
                for pixel in row:
                    gray = pixel.sum() / 3
                    pixel[0] = gray
                    pixel[1] = gray
                    pixel[2] = gray
            return new
        elif filter in ['w', 'weight']:
            new = np.array(array)
            weight = np.array(kwargs['weights'])
            for row in new:
                for pixel in row:
                    gray = (pixel * weight).sum()
                    pixel[0] = gray
                    pixel[1] = gray
                    pixel[2] = gray
            return new
        else:
            return None
