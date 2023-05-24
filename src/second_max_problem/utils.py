arr = [2, 3, 5, 4]


def second_max(arr):
    output = sorted(set(arr), reverse=True)[1]
    print(output)
    return output
