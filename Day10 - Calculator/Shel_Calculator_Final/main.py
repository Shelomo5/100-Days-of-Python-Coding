
#Calculator
from art import logo
      
#Adding function
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1/n2
    
operations = {
"+":add,
'-':subtract,
'*':multiply,
'/':divide    
}
#calculator is a recursion function to rerun program from beginning
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for operator in operations:
        print(operator)
        
    calculation_on = True
    
    while calculation_on:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_name = operations[operation_symbol]
        answer = calculation_name(num1,num2)
        
        print(f"{num1}{operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            calculation_on = False
            calculator()
            
calculator()    

        
        
    