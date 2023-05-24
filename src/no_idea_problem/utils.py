def disjoint():
    happiness = 0
    n, m = map(int, input("Enter n,m:").split())
    arr = list(map(int, input("Enter arr:").split()))
    A = set(map(int, input("Enter A:").split()))
    B = set(map(int, input("Enter A:").split()))

    for i in arr:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1
    print(happiness)
    return happiness
