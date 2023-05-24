string = "AABCAAADA"
k =3


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_string = ''
        for j in range(k):
            if string[i + j] not in sub_string:
                sub_string = sub_string + string[i + j]
            else:
                continue
        print(sub_string)
        return sub_string

