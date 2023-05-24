def mutation():
    string = "abracadabra"
    new_string = list(string)
    new_string[5] = "k"
    string = ''.join(new_string)
    print(string)
    return string
