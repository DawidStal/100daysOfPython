def add(num1,num2):
  return num1+num2
  
def subtract(num1,num2):
  return num1-num2

def multiply(num1,num2):
  return num1*num2

def divide(num1,num2):
  return num1/num2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1=float(input("What's the first number?: "))
  
  should_continue=True
  while should_continue:
    for i in operations:
      print(i)
    operation_symbol=input("Pick an operation from the line   above: ")
    num2=float(input("What's the next number?: "))
    answer=operations[operation_symbol](num1,num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer} or 'n' to star a new calculation: ")=="y":
      num1=answer
    else:
      should_continue=False
      calculator()

calculator()
