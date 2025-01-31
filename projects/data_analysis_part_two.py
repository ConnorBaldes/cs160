#This function asks the user for the names that will be used for the rest of the program
def get_input():
	input_list = []
	numbers = str(input("Please enter a list of numbers: "))
	for i in range(len(numbers)):
		input_list.append(numbers[i])
	return input_list



#Checks input given in get_input() to make sure it only contains numbers
def check_input(input_given):
	
	for i in range(len(input_given)):
		if ord(input_given[i]) < ord("0") or ord(input_given[i]) > ord("9") :
			return "false"
	return "true"



#Perforns get_input() and check_input() function in a loop. If input is not valid loop continues and and user is prompted for a list of numbers.
def get_numbers():
	count_check = 1
	while count_check > 0:
		numbers = get_input()
		numbers_check = check_input(numbers)
		if numbers_check == "true":
			count_check = 0
		else:
			print("Your list must only contain numbers.")
	return numbers


# takes list and counts number of postitions in the list
def get_length(list_1):
	count = 0
	for i in range(len(list_1)):
		count += 1
	return count
 

#This function performs the get_length function on two lists then compares the results to see if the lists are the same length if they are it returns "same length: yes"
# if they are not it returns "same length: no"
def check_length(list_1,list_2):
	list_1_length = get_length(list_1)
	list_2_length = get_length(list_2)
	if list_1_length == list_2_length:
		same_length = "Yes"
	elif list_1_length != list_2_length:
		same_length = "No"
	result = ("Same Length: " + same_length) 
	return result


# takes list and creates a running sum of all the ints in list
def get_sum(list_1):
	sum_1 = 0
	for i in range(len(list_1)):
		sum_1 += int(list_1[i])
	return str(sum_1)



#This function performs the get_sum function on two lists then compares the results to see if the lists have the same sum if they do it returns "same sum: yes"
# if they are not it returns "same sum: no" result will also contain the sum of both lists
def check_sum(list_1,list_2):
	list_1_sum = get_sum(list_1)
	list_2_sum = get_sum(list_2)
	if list_1_sum == list_2_sum:
		same_sum = "Yes"
	elif list_1_sum != list_2_sum:
		same_sum = "No"
	result = ("Same Sum: " + same_sum + " - List 1: " + str(list_1_sum) + ", List 2: " + str(list_2_sum))
	return result

#takes two lists and checks to see if they have any of the values in them are the same
#If they are the same they are store in a list 
#If that list is empty the variable result will return no if not empty resut will retun with yes and the list of common values

def check_numbers(list_1, list_2):
	same_list = []
	for i in range(len(list_1)):
		x = list_1[i]
		for z in range(len(list_2)):
			y = list_2[z]
			if x == y:
				same_list.append(x)
	if len(same_list) == 0:
		result = "Common Numbers: No"
	elif len(same_list) > 0:
		result = ("Common Numbers: Yes" + str(same_list))
	return result


#prints results
def print_results(result_1,result_2,result_3):

	print(result_1 + " | " + result_2 + " | " + result_3 + "\n")
	return



def main():

	count = 1
	while count > 0:
		#Step 1: get two numbered lists from user input

		num_list_1 = get_numbers()
		num_list_2 = get_numbers()

		#Step 2: check to see if the lists are the same length 

		same_length = check_length(num_list_1, num_list_2)

		#Step 3: check to see if the sums of the values in the list are the same

		same_sum = check_sum(num_list_1, num_list_2)

		#Step 4: check to see if any of the values in the list are the same

		common_numbers = check_numbers(num_list_1, num_list_2)

		#Step 5: print results

		print_results(same_length, same_sum, common_numbers)

		continue_program = input("If you would like to go again enter yes of not enter no: ")
	
		if continue_program == "yes" or continue_program == "Yes":
			count = 1
		elif continue_program == "no" or continue_program == "No":
			count = 0
		else: 
			print("Invalid input. Program ending.")
			count = 0
	return 0	



main()
