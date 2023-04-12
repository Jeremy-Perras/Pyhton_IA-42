from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor


if (__name__ == "__main__"):
    arr = ImageProcessor().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module03/ex03/elon.png")
    # ImageProcessor().display(arr)
    cf = ColorFilter()

    # ImageProcessor().display(cf.invert(arr))
    # ImageProcessor().display(cf.to_green(arr))

    # ImageProcessor().display(cf.to_red(arr))
    # ImageProcessor().display(cf.to_blue(arr))
    # ImageProcessor().display(cf.to_celluloid(arr))
    # ImageProcessor().display(cf.to_grayscale(arr, 'm'))
    ImageProcessor().display(cf.to_grayscale(
        arr, 'weight', weights=[0.2, 0.3, 0.5]))
