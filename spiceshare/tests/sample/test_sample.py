"""
    tests.test_recipe
"""
import pytest

def test_5():
    assert 5==5

def test_list1():
    a = (1, 2, 3, 4)
    b = (1, 2, 3, 4)
    assert a == b

def test_list2():
    a = (1, 2, 3, 4)
    b = (1, 2, 3, 4)
    assert a == b

def test_dict():
    a = {'a': 1, 'b': 2, 'c': 3}
    b = {'a': 1, 'b': 2, 'c': 3}
    assert a == b

def test_str():
    a = 'a'
    aa = 'a'
    assert a == aa

@pytest.mark.xfail(strict=True)
def test_fail():
    assert False

a = 2
b = 3
@pytest.mark.parametrize(['a', 'b'], [
    (1, 2),
    (1, 2),
    ])

def test_parameterize(a, b):
    assert a == b
