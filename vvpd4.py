def syracuse_sequence(n: int):
    """Функция выводит сиракузскую последовательность
    для заданного числа"""
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        result.append(n)
    return result


def syracuse_max(n: int):
    """Функция выводит максимальное число
    в сиракузской последовательности для введенных данных"""
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
    print('Для числа 5:')
    print('Сиракузская последовательность: ', syracuse_sequence(5))
    print('Максимальное число в этой последовательности: ', syracuse_max(5))
    print('Для числа 23:')
    print('Сиракузская последовательность: ', syracuse_sequence(23))
    print('Максимальное число в этой последовательности: ', syracuse_max(23))
    print('Для числа 224:')
    print('Сиракузская последовательность: ', syracuse_sequence(224))
    print('Максимальное число в этой последовательности: ', syracuse_max(224))
    print('Для числа 1000:')
    print('Сиракузская последовательность: ', syracuse_sequence(1000))
    print('Максимальное число в этой последовательности: ', syracuse_max(1000))


if __name__ == '__main__':
    main()
