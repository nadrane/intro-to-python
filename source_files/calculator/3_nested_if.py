operand1 = input("enter the first operand: ")
operand2 = input("enter the second operand: ")


operand1 = int(operand1)
operand2 = int(operand2)

operator = input("enter an operator (+, -, *, /): ")


if operator == "+":
    print (operand1 + operand2)
    
elif operator == "-":
    print (operand1 - operand2)
    
elif operator == "*":
    print (operand1 * operand2)
    
# It turns out that we can nest if statements inside other if statements
# The code will still execute line by line and then drop to the next indentation block if the if statement evaluates to true
elif operator == "/":
    # Only say that we cannot divide by 0 if the user enters 0.
    if operand2 == 0:
        print ("cannot divide by 0.")
    else:
        print (operand1 / operand2)
    
else:
    print ("That is not a valid operator")
    
print ("program finished")

