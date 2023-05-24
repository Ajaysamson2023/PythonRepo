def finding_percent(k, m):
    for key, value in k.items():
        if key == m:
            n = len(k[m])
            result = sum(value) / n
            print(format(result, ".2f"))
    return result
