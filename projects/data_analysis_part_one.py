#This function asks the user for the names that will be used for the rest of the program
def get_input():
	name = str(input("Please enter a name: "))
	return name



#Checks input given in get_input() to make sure it only contains letters
def check_input(input_given):
	for i in range(len(input_given)):
		if ord(input_given[i])  not in range(ord("A"), ord("Z")) and ord(input_given[i]) not in range(ord("a"), ord("z")):
			return "false"
		
	return "true"


#Perforns get_input() and check_input() function in a loop. If input is not valid loop continues and and user is prompted for a new name. If name is valid user is asked of they would like to add another name
def get_name():
	input_list = []
	count = "1"
	while count > "0":
		#looping for valid input
		count_check = 1
		while count_check > 0:
			name = get_input()
			name_check = check_input(name)
			if name_check == "true":
				input_list.append(name)
				count_check = 0
			else:
				print("Your name must only contain letters.")

		count = input("If you would like to enter another name enter 1 if not enter 0: ")
		if count < chr(48) or count > chr(49):
			print("Input invalid")
			count = "0"
	return input_list


#takes string and coverts any lowercase letters to uppercase
def make_upper(word_list):
	upper_names = []
	for i in range(len(word_list)):
		for x in word_list[i]:
			if ord(x) in range(ord("A"), ord("Z")):
				#already upper no change needed
				upper_names.append(x)
			elif ord(x) in range(ord("a"), ord("z")):
				#converts lowercase to uppercase using ascii
				x = chr(ord(x) - 32)
				upper_names.append(x)
	return upper_names

#taking list of letters and creating a count of amount of each letter in the list
def get_count(letters):
	count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(len(letters)):
		for x in letters[i]:
			x = ord(x)
			position = (x - 65)
			count_list[position] += 1
	return count_list



#prints the letter and the amount of that letter in the string provided
def print_count(a):
	print("A - ", a[0], ", B - ", a[1], ", C - ", a[2], ", D - ", a[3], ", E - ", a[4], ", F - ", a[5], ", G - ", a[6], ", H - ", a[7], ", I - ", a[8], ", J - ", a[9], ", K - ",a[10], ", L - ", a[11], ", M - ", a[12], ", N - ", a[13], "\n")
	print("O - ", a[14], ", P - ", a[15], ", Q - ", a[16], ", R - ", a[17], ", S - ", a[18], ", T - ", a[19], ", U - ", a[20], ", V - ", a[21], ", W - ", a[22], ", X - ", a[23], ", Y - ", a[24], ", Z - ", a[25])


def main():
	count = 1
	while count > 0:
		#Step 1: get names
		name_list = get_name()

		#Step 2: make all letters in names uppercase
		upper_name = make_upper(name_list)

		#Step 3: count letters in list
		letter_count = get_count(upper_name)

		#Step 4: print count
		print_count(letter_count)
		continue_program = input("If you would like to go again input yes of not input no: ")
		if continue_program == "yes" or continue_program =="Yes":
			count = 1
		elif continue_program == "no" or continue_program == "No":
			count = 0
		else:
			print("Invalid input. Program ending.")
			count = 0
	return 0
	

main()




