operand1 = input("enter the first operand: ")
operand2 = input("enter the second operand: ")


# We haven't seen anything like this before where we simply have an if statement and a variable as opposed to an expression like operand1 < 5.
# Every variable has a truthyness value. These unfortunately need to me memorized, but they are quite sensible!
# When an integer is placed in an if statement, if it non-zero evaluates to True. If it is 0, it evaluates to False.
# When a string is placed in an if statement, if it is not empty, it evaluates to True. If it is empty, it evaluates to False

# If operand1 is not empty (remember, it is still a string!), then convert it to an integer
if operand1:
    operand1 = int(operand1)

# If operand2 is not empty (remember, it is still a string!), then convert it to an integer    
if operand2:
    operand2 = int(operand2)

operator = input("enter an operator (+, -, *, /): ")

# If the operator is empty, this if statement will not evaluate to true, and we will not proceed into the indented code below, thus fixing our bug.
if operator:
    if operator == "+":
        # If we run this program with operand1 or operand2 blank and the other an intger, it will crash.
        # If either of these values is blank, then we will skip the integer conversion on line 12 or line 16 
        # (because the if statement fails because the truthyness of a blank string is false), resulting in a crash since we cannot add a string and an intger
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
    print ("Please enter a non-empty operator")

print ("program finished")
