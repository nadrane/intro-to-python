operand1 = input("Please enter operand 1: ")
operand2 = input("Please enter operand 2: ")
operator = input("Please enter an operator (+, -, *, /): ")

# Note that the operands needs to be converted to integers since the "input" function gives us strings
# If we fail to do these integer conversions, we would could accidentally multiply or subract or divide strings, which is illegal
operand1 = int(operand1)
operand2 = int(operand2)

# Only drop into this if statement if the user entered '+'
if operator == "+":
    print (operand1 + operand2)
    
# Only drop into this if statement if the user entered '-'
if operator == "-":
    print (operand1 - operand2)

# Only drop into this if statement if the user entered '*'
if operator == "*":
    print (operand1 * operand2)
    
# Only drop into this if statement if the user entered '/'
if operator == "/":
    print (operand1 / operand2)

print ("program finished")