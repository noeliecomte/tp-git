from calculator import Calculator

def test_addition():
    """
    This function is a test for addition
    :function: unit test of addition function
    """
    calculate = Calculator()
    assert calculate.addition(1, 2) == 3


def test_subtraction():
    """
    This function is a test for subtraction
    :function: unit test of subtraction function
    """
    calculate = Calculator()
    assert calculate.subtraction(2, 1) == 1


def test_division():
    """
    This function is a test for division
    :function: unit test of division function
    """
    calculate = Calculator()
    assert calculate.division(6, 2) == 3
