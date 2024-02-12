"""This module is a calculator"""

class Operation:
    """ Class for standard operations """
    @staticmethod
    def add(num1, num2):
        """add function"""
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        """subtract function"""
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        """multiply function"""
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        """divide function"""
        if num2 != 0:
            return num1 / num2
        raise ZeroDivisionError

class Calculation:
    """ Class to compute operations """
    def __init__(self, num1: float, num2: float, operation: str):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def compute(self):
        """ Compute function """
        return self.operation(self.num1, self.num2)

class CalculationHistory:
    """ Class to save calculation history"""
    history = []

    @classmethod
    def add_history(cls, answer):
        """ method to add a calculation to history"""
        cls.history.append(answer)

    @classmethod
    def get_history(cls):
        """ Method to get history"""
        return cls.history

class Calculator:
    """Class to create calc obj"""
    def __init__(self):
        self.operations = Operation()

    def do_calc(self, num1: float, num2: float, operation: str):
        """Method to use Calculator obj to do calc"""
        calculation = Calculation(num1, num2, operation)
        result = calculation.compute()
        CalculationHistory.add_history(calculation)
        return result

    def get_calc_history(self):
        """Method to get calculation history"""
        return CalculationHistory.get_history()

calculator = Calculator()
print(calculator.do_calc(2, 0, Operation.add))
