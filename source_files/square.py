number_to_square = input("Please enter a number to square: ")

# It is necessary to convert this input to an integer becausee otherwise we
# would be multiplying two strings, which is an illegal operation.
number_to_square = int(number_to_square)
print (number_to_square * number_to_square)
