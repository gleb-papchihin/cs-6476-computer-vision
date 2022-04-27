import numpy as np


def correlation_2d(img, template, padding = 0):
    img = np.pad(img, padding)
    response = []

    assert img.shape[0] >= template.shape[0]
    assert img.shape[1] >= template.shape[1]

    for x in range(img.shape[0] - template.shape[0] + 1):
        response.append([])

        for y in range(img.shape[1] - template.shape[1] + 1):
            sum = 0

            for tx in range(template.shape[0]):

                for ty in range(template.shape[1]):
                    sum += img[x + tx][y + ty] * template[tx][ty]

            response[-1].append(sum)

    return np.array(response)

def normal_correlation_2d(img, template, padding = 0):
    return correlation_2d(img, (template - template.mean()) / template.std(), padding)

