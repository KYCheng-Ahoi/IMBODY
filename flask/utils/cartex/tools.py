import contextlib
from typing import Callable, List, Union, Iterable, Tuple, NewType
import numpy

@contextlib.contextmanager
def expect_valid_float_image(img: numpy.array, normalize=False):
    """
    Convert given image to valid floating point valued image, which has a type of 32-bits float
    and has a value in [0-1].
    If the input were integer image, this'll consider the maximum value of the range.
    This context does not change source image.

    Example:
        >>> with expect_valid_float_image(img) as valid_image:
        >>>     some_func_expecting_valid_float(img_, , *param, **kargs)

    Args:
        img: numpy.ndarray
    """

    fimg = img.astype(numpy.float32)

    if img.dtype == numpy.uint8:
        fimg /= 0xff

    elif normalize:
        if fimg.min() < 0.:
            fimg -= fimg.min()

        if fimg.max() > 1.:
            fimg /= fimg.max()

    yield fimg
