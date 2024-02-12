'''test addition, subtraction, multiplication and division functions'''

from calculator import Calculator
from calculator import Operation

calc = Calculator()

def test_add():
    '''Test that addition function works '''    
    assert calc.do_calc(2, 2, Operation.add) == 4

def test_subtract():
    '''Test that addition function works '''    
    assert calc.do_calc(2, 2, Operation.subtract) == 0

def test_multiply():
    '''Test that multiply function works '''    
    assert calc.do_calc(2, 2, Operation.multiply) == 4

def test_divide():
    '''Test that division function works '''    
    assert calc.do_calc(2, 2, Operation.divide) == 1
    