class Calculator:
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
  print (num1, operator, num2)