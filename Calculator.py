# Calculator

def calculator():
  try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    oper = input("Enter the operator: (+, -, *, /, %, ^):")

    if oper == '+':
      return num1 + num2
    elif oper == '-':
      return num1 - num2
    elif oper == '*':
      return num1 * num2
    elif oper == '/':
      return num1 / num2
    elif oper == '%':
      return num1 % num2
    elif oper == '^':
      return num1 ** num2
    else:
      print("Invalid operator!")
    
  except ValueError as e:
    print(e)

while True:
  play = input("Do you want to do a calculation?(yes/no)") 
  
  if play.lower() == 'no':
    break

  print(calculator())