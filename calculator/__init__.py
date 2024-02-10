class Operation:  
  @staticmethod
  def add(x, y):
    return x + y
  
  @staticmethod
  def subtract(x, y):
    return x - y
  
  @staticmethod
  def multiply(x, y):
    return x * y
  
  @staticmethod
  def divide(x, y):
    if y != 0:
      return x / y
    else: return "Error division by zero"

class Calculation:
  def __init__(self, num1, num2, operator):
    self.num1 = num1
    self.num2 = num2
    if operator == "+":
      self.operation = "add"
    elif operator == "-":
      self.operation = "subtract"
    elif operator == "*":
      self.operation == "multiply"
    elif operator == "/":
      self.operation == "divide"
  
  def compute(self):
    return self.operation(self.num1, self.num2)


class CalculationHistory:
  history = []

  @classmethod
  def addHistory(cls, answer):
    cls.history.append(answer)
  
  @classmethod
  def getHistory(cls):
    return cls.history

class Calculator:
  
  def __init__(self):
    self.operations = Operation()
  
  def doCalc(self, num1, num2, operator):
    calculation = Calculation(num1, num2, operator)
    result = calculation.compute
    CalculationHistory.addHistory(calculation)
    return result
  
  def getCalcHistory(self):
    return CalculationHistory.getHistory()


validOperators = ["+", "-", "*", "/"]
try:
  print ("Please enter the first number of your equation")
  num1 = float(input())
  print ("Please enter the operator of your equation.")
  operator = str(input())
  print ("Please enter the second number of your equation")
  num2 = float(input())
except: 
  print ("Invalid input, please try again.")
else:
  if operator not in validOperators: raise Exception("Invalid operator inputted. Valid operators are +, -, *, /")

calculator = Calculator()
print(calculator.doCalc(num1, num2, operator))