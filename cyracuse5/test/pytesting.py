import pytest
from cyracuse5.cyracuse_f import syracuse_sequence, syracuse_max


@pytest.fixture()
def another_data():
    """Большое число"""
    return 224


@pytest.fixture()
def also_data():
    """Ещё больше"""
    return 1000


test_par = [
    {
        'test_inp': 5,
        'expected': [5, 16, 8, 4, 2, 1]
    },
    {
        'test_inp': 23,
        'expected': [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    }
]


@pytest.mark.parametrize('test_params', test_par)
def test_some_data(test_params):
    assert syracuse_sequence(test_params['test_inp']) == test_params['expected']


def test_another_data(another_data):
    assert syracuse_sequence(another_data) == [224, 112, 56, 28, 14, 7, 22, 11, 34,
                                               17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_also_data(also_data):
    assert syracuse_sequence(also_data) == [1000, 500, 250, 125, 376, 188, 94, 47,
                                            142, 71, 214, 107, 322, 161, 484,
                                            242, 121, 364, 182, 91, 274, 137, 412,
                                            206, 103, 310, 155, 466, 233, 700,
                                            350, 175, 526, 263, 790, 395, 1186, 593,
                                            1780, 890, 445, 1336, 668, 334,
                                            167, 502, 251, 754, 377, 1132, 566, 283,
                                            850, 425, 1276, 638, 319, 958,
                                            479, 1438, 719, 2158, 1079, 3238, 1619,
                                            4858, 2429, 7288, 3644, 1822, 911,
                                            2734, 1367, 4102, 2051, 6154, 3077, 9232,
                                            4616, 2308, 1154, 577, 1732, 866,
                                            433, 1300, 650, 325, 976, 488, 244, 122,
                                            61, 184, 92, 46, 23, 70, 35, 106,
                                            53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_another_data_max(another_data):
    assert syracuse_max(another_data) == 224


def test_also_data_max(also_data):
    assert syracuse_max(also_data) == 9232
