import numpy as np


def create_average_kernel(size: int):
    assert size > 0, 'Size of a kernel must be positive!'
    return np.ones((size, size)) / size ** 2

def create_gaussian_kernel(size: int, sigma: float):
    assert size > 0, 'Size of a kernel must be positive!'
    kernel = []

    for x in range(-(size // 2), (size // 2 + size % 2)):
        kernel.append([])

        for y in range(-(size // 2), (size // 2 + size % 2)):
            kernel[-1].append(
                1 / (2 * np.pi * sigma ** 2)
                * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
                )
    return np.array(kernel) / np.array(kernel).sum()
