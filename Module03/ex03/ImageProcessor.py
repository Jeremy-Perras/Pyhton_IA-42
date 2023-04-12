from PIL import Image
from numpy import asarray
import numpy as np


class ImageProcessor():
    @staticmethod
    def load(path):
        try:
            image = Image.open(path)
            data = asarray(image)
            arr = np.array(image)
            print(data.shape)
            return (np.divide(arr[:, :, 0:3], 255))
        except Exception as error:
            print(
                f"Exception : {error.__class__.__name__} -- strerror: {error}")
        return None

    @staticmethod
    def display(array):
        array = np.multiply(array, 255)
        array = array.astype(np.uint8)
        img = Image.fromarray(array, 'RGB')
        img.show()
