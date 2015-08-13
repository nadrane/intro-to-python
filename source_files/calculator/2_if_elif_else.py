operand1 = input("enter the first operand: ")
operand2 = input("enter the second operand: ")

operand1 = int(operand1)
operand2 = int(operand2)

operator = input("enter an operator (+, -, *, /): ")

# We are able to replace repeated if statements with elif (else if) statements.
# When we use repeated if statements, we know that the interpreter is going to evaluate every single if statement to determine if its true.
# Not only is this inefficient, it can actually lead to bugs.
# As programmers, we know that the if statements are mutually exclusive; that is, only a single one of them can ever evaluate to true.
# This is why we use elif. If any of the preceding elif (or the first if) statements evaluate to true, all subsequent elif and else statements are skipped.

if operator == "+":
    print (operand1 + operand2)
    
elif operator == "-":
    print (operand1 - operand2)
    
elif operator == "*":
    print (operand1 * operand2)
    
elif operator == "/":
    print (operand1 / operand2)
 
# The else statement says, if every if-elif statement in the preceding block of if-elif statements evaluates to False, then I evaluate to true.
# This means that if an operator other than +, -, *, or / is passed in, then we will always print "That is not a valid operator"   
else:
    print ("That is not a valid operator")

print ("program finished")
