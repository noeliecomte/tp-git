from calculator import addition
from calculator import substraction
from calculator import division

def test_addition():
    """
    :function: unit test of addiction function
    """
    assert addition(1, 2) == 3


def test_substraction():
    """
    :function: unit test of addiction function
    """
    assert substraction(2, 1) == 1


def test_division():
    """
    :function: unit test of addiction function
    """
    assert division(6, 2) == 3