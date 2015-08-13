# A function is a tool that allows you to name a couple lines of code that you intend to use over and over.
# It allows you to perform the same operation without copy and pasting code 50 times.

# function in Python is any named followed by a set of open and closing parenthesis.
# We have already seen a couple: int, str, input, and print.
# The values inside the parenthesis separated by commas are known as parameters or arguments. 
# These are the inputs that the function operates on. Different functions will expect different types and quantities of parameters.


# Every function is declared using the def keyword following by the name of the function
# Take a look at these links... Ignore the example where he uses *args
# http://learnpythonthehardway.org/book/ex18.html http://learnpythonthehardway.org/book/ex19.html 
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

operand1 = input("enter the first operand: ")
operand2 = input("enter the second operand: ")

if operand1:
    operand1 = int(operand1)

if operand2:
    operand2 = int(operand2)

operator = input("enter an operator (+, -, *, /, all): ")

if operator and operand1 and operand2:
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

    else:
        print ("That is not a valid operator")
else:
    print ("Please enter non-empty operators and operands")

print ("program finished")