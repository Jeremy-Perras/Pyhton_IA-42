from PIL import Image
from numpy import asarray


class ImageProcessor():
    @staticmethod
    def load(path):
        try:
            image = Image.open(path)
            data = asarray(image)
            print(data.shape)
            return (data)
        except Exception as error:
            print(
                f"Exception : {error.__class__.__name__} -- strerror: {error}")
        return None

    @staticmethod
    def display(array):
        img = Image.fromarray(array, 'RGB')
        img.show()


if (__name__ == "__main__"):
    data = ImageProcessor().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module03/ex01/42AI.png")
    print(data)
    ImageProcessor().display(data)
