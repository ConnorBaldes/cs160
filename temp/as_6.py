
def get_type():
	count = 0
	while count == 0:
		func_type = input(" 1. Binary to decimal \n 2. Decimal to binary \n 3. Hexadecimal to decimal \n 4. Decimal to Hexidecimal \n Input a number 1-4 corresponding to the conversion you would like to perform: ")
		func_type = int(func_type)
		if func_type == 1 or func_type == 2 or func_type == 3 or func_type == 4:
			return func_type
		else:
			print(" Invalid input choice")

def dec_bin(input_string):
        # Check that input string is a valid decimal
	for i in range(len(input_string)):
		if ord(input_string[i]) < ord('0') or ord(input_string[i]) > ord('9'):
			print(" Not a decimal value.")
			return
	input_int = int(input_string)
	converted_value = bin(input_int)
	print(" Your converted value is: " + str(converted_value))
	return
#checks if input_string is a binary number then converts input_string to  a decimal value
#takes: string input_string expecting  it to be a string
#returns: decimal value of input_string if input_string was a valid binary number
def bin_dec(input_string):
        # Checking if input_string is valid binary number
        # looping for the lenght of characters in string input_string
	for i in range(len(input_string)):
                #if this charracter is not a one and not a  zero do:
		if input_string[i] != '0' and input_string[i] != '1':
			print(" Not a valid binary number.")
			return
                        #exit loop and re prompt
        #if we finish thte loop input_string is a binary number

	valid_str = str(input_string)
	converted_value = int(valid_str, 2)
	print(" Your converted value is: " + str(converted_value))
	return


def hex_dec(input_string):
	#check if string is a valid hexadecimal value
	#looping for length of characters in input_string
	for i in range(len(input_string)):
		if ord(input_string[i]) < ord("0") or ord(input_string[i]) > ord("F"): 
			print(" Not a valid hexadecial value.")
			return
			#exit loop reprompt
	valid_str = str(input_string)
	converted_value = int(valid_str, 16)
	print(" Your converted value is: " + str(converted_value))


def dec_hex(input_string):
	#checking if string is valid decimal value
	#looping for length of characters in input_string
	for i in range(len(input_string)):
		if ord(input_string[i]) < ord("0") or ord(input_string[i]) > ord("9"):
			print(" Not a valid decimal value.")
			return
			#exit loop 
	valid_str = int(input_string)
	converted_value = hex(valid_str)
	print(" Your converted value is: " + str(converted_value))
# This function is called by main to get the value
# Returns Value that has been checked to be the correct type
# Takes: choice_type -> Which is user input for the type of function to use 
# 	should be: 1,2,3,4
def get_value(choice_type):

	# Get the input string with prompt

	if choice_type == 1:
		value = input(" Input a binary number that will be converted into a decimal: ")
		# Call convesion which checks if valid and prints converted value
		# call expecting a bin 
		bin_dec(value)	
		
	elif choice_type == 2: 
		# call expecting dec
		value = input(" Input a decimal value that will be converted into a binary number: ")
		dec_bin(value)
	elif choice_type == 3:
		#call expecting hex
		value = input(" Input a hexadecimal value that will be converted to a decimal value (All input letters must be uppercase): ")
		hex_dec(value)
	elif choice_type == 4:
		#call expecting dec
		value = input(" Input a decimal value that will be converted to a hexadecimal value: ")
		dec_hex(value)			
def main():
	count = 1
	while count > 0:
		count = 0
		# Get function type (assuming this value is valid)
		func_type = get_type()

		# Get value -> need to pass function_type to get a good value
		value = get_value(func_type)

		# Call convert_value which converts the value AND prints the converted value	
		#convert_value(value, function_type)

		# Prompt to see if we should run again
		count = int(input(" Enter a 0 to exit or 1 to try another conversion: "))
		print("\n")
		# PROGRAM ENDS	
	return 0
main()
