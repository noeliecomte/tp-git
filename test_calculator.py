from calculator import addition
from calculator import substraction
from calculator import division

def test_addition():
    """
    This function is a test for addition
    :function: unit test of addiction function
    """
    assert addition(1, 2) == 3


def test_substraction():
    """
    This function is a test for substraction
    :function: unit test of addiction function
    """
    assert substraction(2, 1) == 1


def test_division():
    """
    This function is a test for division
    :function: unit test of addiction function
    """
    assert division(6, 2) == 3
