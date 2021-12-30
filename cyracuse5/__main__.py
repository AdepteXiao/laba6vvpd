from .cyracuse_f import syracuse_sequence, syracuse_max
import pytest
import unittest


def main():
    wha = int(input('1 - examples\n2 - pytest\n3 - unittest\n'))
    if wha == 1:
        print('Пример 1')
        print('Входные параметры: 12')
        print('Площадь пересечения:', syracuse_sequence(12))
        print('Площадь объединения:', syracuse_max(12))
        print('Пример 2')
        print('Входные параметры: 21')
        print('Площадь пересечения:', syracuse_sequence(21))
        print('Площадь объединения:', syracuse_max(21))
        print('Пример 3')
        print('Входные параметры: 2, 2, 3, 1, 2, 5, 7, 1')
        print('Площадь пересечения:', syracuse_sequence(21))
        print('Площадь объединения:', syracuse_max(21))
    elif wha == 2:
        pytest.main([r'rect_intersect\tests\pytest_testing.py', '-v'])
    elif wha == 3:
        unittest.main(r'rect_intersect.tests.unittest_testing')


if __name__ == '__main__':
    main()
