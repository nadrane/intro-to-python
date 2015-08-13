operand1 = input("enter the first operand: ")
operand2 = input("enter the second operand: ")

if operand1:
    operand1 = int(operand1)

if operand2:
    operand2 = int(operand2)

operator = input("enter an operator (+, -, *, /): ")

# We use what is called an and statement here. We need operator to evaluate to true, operand1 to evaluate to true, and operand2 to evaluate to true.
# This means that operator must be a non-empty string, operator1 is an integer with a truthyness of True, and operator2 is an integer with a truthyness of True
# We actually just introduced another subtle bug... we will not enter this if statement if operand1 or operand2 is 0 (even though 0 is a valid input), simply because
# the truthyness of an integer with a value of 0 is false.
if operator and operand1 and operand2:
    if operator == "+":
        print (operand1 + operand2)

    elif operator == "-":
        print (operand1 - operand2)

    elif operator == "*":
        print (operand1 * operand2)

    elif operator == "/":
        if operand2 == 0:
            print ("cannot divide by 0.")
        else:
            print (operand1 / operand2)

    else:
        print ("That is not a valid operator")
else:
    print ("Please enter non-empty operators and operands")

print ("program finished")