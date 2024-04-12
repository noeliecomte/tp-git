class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def addition(a, b):
        """
        This function is an addition function
        :type a: float
        :type b: float
        :rtype: float
        :return: result of addition
        """
        result = a + b
        return result

    @staticmethod
    def subtraction(a, b):
        """
        This function is a subtraction function
        :type a: float
        :type b: float
        :rtype: float
        :return: result of subtraction
        """
        result = a - b
        return result

    @staticmethod
    def division(a, b):
        """
        This function is a division function
        :type a: float
        :type b: float
        :rtype: float
        :return: result of division
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        return result
    
