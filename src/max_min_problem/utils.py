import numpy


def max_min():
    my_array = ([4, 2], [2, 5], [3, 7], [1, 3], [4, 0])

    min_array = (numpy.min(my_array, axis=1))

    result = numpy.max(min_array)
    print("Result:", result)
    return result
