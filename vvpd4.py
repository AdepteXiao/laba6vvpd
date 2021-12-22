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


def main():
    print('Для числа 324:')
    print('Сиракузская последовательность: ', syracuse_sequence(324))
    print('Максимальное число в этой последовательности: ', syracuse_max(324))
    print('Для числа 1233:')
    print('Сиракузская последовательность: ', syracuse_sequence(1233))
    print('Максимальное число в этой последовательности: ', syracuse_max(1233))
    print('Для числа 11:')
    print('Сиракузская последовательность: ', syracuse_sequence(11))
    print('Максимальное число в этой последовательности: ', syracuse_max(11))
    print('Для числа 7:')
    print('Сиракузская последовательность: ', syracuse_sequence(7))
    print('Максимальное число в этой последовательности: ', syracuse_max(7))


if __name__ == '__main__':
    main()