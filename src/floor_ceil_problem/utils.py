import numpy


def floor():
    numpy.set_printoptions(legacy='1.13')
    my_arr = numpy.array(input("Enter value:").split(), float)
    print(numpy.floor(my_arr))
    return my_arr


def ceil():
    numpy.set_printoptions(legacy='1.13')
    my_arr = numpy.array(input("Enter value:").split(), float)
    print(numpy.ceil(my_arr))
    return my_arr


def int():
    numpy.set_printoptions(legacy='1.13')
    my_arr = numpy.array(input("Enter value:").split(), float)
    print(numpy.rint(my_arr))
    return my_arr
