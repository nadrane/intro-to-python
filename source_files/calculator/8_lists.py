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

def calculate(operand1, operand2, operator):
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

        else:
            print ("That is not a valid operator")

history = []  #Not inside while loop so that contents does not reset after every calculator operation

# A list of all the valid operators
valid_operators = ['+', '-', '*', '/', 'all', 'stop', 'history']


while True:
    operand1 = input("enter the first operand: ")

    if operand1:
        operand1 = int(operand1)
    else:
        print ("Invalid first operand value")
        continue 

    operand2 = input("enter the second operand: ")
    if operand2:
        operand2 = int(operand2)
    else:
        print ("Invalid second operand value")
        continue

    operator = input("enter an operator (+, -, *, /, all, stop, history): ")

    if not operator:
        print ('Please enter a non-empty operator')
        continue

    # This statement says that if the inputted operator is not in the list valid_operators (defined above),
    # then print out that the operator is not valid and restart the loop. We didn't conver this in class...
    if operator not in valid_operators:
        print ("That is not a valid opeartor")
        continue

    if operator == "stop":
        break

    elif operator == "history":
        #print(history[0])
        #print(history[1])
        # History will look like this
        # [ [3, 4, '+']
        #   [34, 2, '*']
        #   [5, 9, '/'] ]
        # The first time this loop runs, item will be equal to [3, 4, '+']
        # The second time this loop runs, item will be equal to [34, 2, '*']
        # The third time this loop runs, item will be equal to [5, 9, '/']

        for item in history:
            # Assuming that we are on our first iteration through the loop,
            # item[0] == 3
            # item[1] == 4
            # item[2] == '+'
            calculate(item[0], item[1], item[2])

    elif operator:
        new_history_item  = [operand1, operand2, operator]
        history.append(new_history_item)
        calculate(operand1, operand2, operator)

print ("I hope you enjoyed this presentation")