def syracuse_sequence(n: int):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        result.append(n)
    return result


def syracuse_max(n: int):
    maxim = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n > maxim:
            maxim = n
    return maxim
