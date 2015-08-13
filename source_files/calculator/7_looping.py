def addition(operand1, operand2):
    print (operand1, "+", operand2, "=", operand1 + operand2)

def subtraction(operand1, operand2):
    print (operand1, "-", operand2, "=", operand1 - operand2)

def multiplication(operand1, operand2):
    print (operand1, "*", operand2, "=", operand1 * operand2)

def division(operand1, operand2):
    if operand2 == 0:
        print ("cannot divide by 0.")
    else:
        print (operand1, "/", operand2, "=", operand1 / operand2)

# This while statement says repeat the code inside the indentation level forever and ever
# True, just like a string or an integer, has a truthyness value, which is obviously always true.
while True:
    operand1 = input("enter the first operand: ")

    if operand1:
        operand1 = int(operand1)
    # Now that we are using a looping construct, we can tell the program to start over if an invalid operand is entered
    else:
        print ("Invalid first operand value")
        continue   # This continue statement tells the program to go back to the first line of the while loop.

    operand2 = input("enter the second operand: ")
    if operand2:
        operand2 = int(operand2)
    # Now that we are using a looping construct, we can tell the program to start over if an invalid operand is entered
    else:
        print ("Invalid second operand value")
        continue    # This continue statement tells the program to go back to the first line of the while loop.

    operator = input("enter an operator (+, -, *, /, all, stop): ")

    # We no longer need to check the operand values here anymore... Seeing as we check the operand values before converting them to integers,
    # we actually fixed the bug where an operand value of 0 would no longer work
    if operator:
        if operator == "+":
            addition(operand1, operand2)

        elif operator == "-":
            subtraction(operand1, operand2)

        elif operator == "*":
            multiplication(operand1, operand2)

        elif operator == "/":
            division(operand1, operand2)

        elif operator == "all":
            addition(operand1, operand2)
            subtraction(operand1, operand2)
            multiplication(operand1, operand2)
            division(operand1, operand2)

        elif operator == "stop":
            # This break command tells the interpreter to completely exit the loop it is in.
            # This means that regardless of the truthyness of the whole loop, we still exit it 
            # and continue to the next statement after it (The one that prints I hope you enjoyed calculator forever)
            break

        else:
            print ("That is not a valid operator")
    else:
        print ("Please enter a non-empty operator")

print ("I hope you enjoy calculator forever")