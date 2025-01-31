import random

def get_cap(cap_amount):
	cap_list = []
	for i in range(cap_amount):
		cap_letters = random.randrange(ord("A"), ord("Z"))
		cap_letters = chr(cap_letters)
		cap_list.append(cap_letters)
	return cap_list
        
def get_special(special_characters):
	special_list = []
	for i in special_characters:
		special_list.append(i)
	return special_list


def remaining_characters(character_amount, cap_amount, special_list):
	character_list = []
	character_range = (character_amount - cap_amount - (len(special_list)))
	for i in range(character_range):
		random_char = random.choice([random.randrange(ord("0"),ord("9")), random.randrange(ord("a"), ord("z"))])
		random_char = str(chr(random_char))
		character_list.append(random_char)
                
	return character_list

def password(cap_list, special_list, character_list):

	final_password = cap_list + special_list + character_list
	

	random.shuffle(final_password)
	
	print(final_password)
		

	return

def main():

	count = 1
	while count > 0:

		character_amount = int(input("Input the number of characters you would like the password to be: "))

		special_characters = str(input("Input the special characters you would like to use: "))

		cap_amount = int(input("Input the number of capital letters you would like to use: "))

		cap_list = get_cap(cap_amount)

		special_list = get_special(special_characters)

		remaining_list = remaining_characters(character_amount, cap_amount, special_list)

		password(cap_list, special_list, remaining_list)

		count = int(input("If you would like to continue input 1, if not enter 0: "))

	return 0


main()
