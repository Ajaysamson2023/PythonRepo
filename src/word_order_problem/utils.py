def word_problem():
    wordlist = {}
    for i in range(int(input("Enter:"))):
        word = input("Enter word:")
        if word in wordlist.keys():
            wordlist[word] += 1
        else:
            wordlist[word] = 1
    lis = list(wordlist.values())
    for num in lis:
        print(num, end=" ")
    return wordlist
