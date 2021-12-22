def syracuse_sequence(n: int):
    result = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 2 + 1
        result.append(n)
    return result
    