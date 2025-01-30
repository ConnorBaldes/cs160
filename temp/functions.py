def is_int(num):
	for c in range(len(num)):
		if ord(num[c]) in range(48,57):
			return 'True'
		elif ord(num[c]) not in range(48,57):
			return 'False'


def is_float(num):
	count = 0 
	for d in range(len(num)):
		if ord(num[d]) == 46:
			count += 1
	if count > 0 and count <= 1:
		return "True"
	else:
		return "False"
	

def is_capital(letter):
	for e in range(len(letter)):
		if ord(letter[e]) in range(65,90):
			return "True"
		elif ord(letter[e]) not in range(65,90):
			return "False"

def is_even(num):
	if (num % 2) == 0:
		return "True"
	elif (num % 2) != 0:
		return "False"

def is_odd(num):
	if (num % 2) == 1:
		return "True"
	elif (num % 2) != 1:
		return "False"

def numbers_present(sentence):
	count = 0
	for h in range(len(sentence)):
		if ord(sentence[h]) in range(48,57):
			count += 1 
	if count > 0:
		return "True"
	elif count == 0:
		return "False"

def letters_present(sentence):
	count = 0
	for k in range(len(sentence)):
		if ord(sentence[k]) in range(97,122) or ord(sentence[k]) in range(65,90):
			count += 1
	if count > 0:
		return "True"
	elif count == 0:
		return "False"

def contains_sub_string(sentence):
	count = 0
	for z in range(len(sentence)):
		if ord(sentence[z]) == 34:
			count += 1
	if count > 0 and (count % 2) == 0:
		return "True"
	else:
		return "False"


def make_upper(sentence):
	a = 0
	b = ""
	for m in range(len(sentence)):
		c = ord(sentence[m]) - 32
		a = chr(c)
		b = b + a
	sentence = b
	return sentence
def make_lower(sentence):
	a = 0
	b = ""
	for p in range(len(sentence)):
		c = ord(sentence[p]) + 32
		a = chr(c)
		b = b + a
	sentence = b
	return sentence
	
def main():



	print("Index 0. ")
	for i in range(2):
		num = input('Please input a number: ')
		sum1 = num
		is_int(num)
		for c in range(len(num)):
			if ord(num[c]) in range(48,57):
				exp_val = "True"
			elif ord(num[c]) not in range(48,57):
				exp_val = "False"
		if is_int(num) == exp_val:
			pf = "PASS"
		elif is_int(num) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", is_int(num), "|", pf)



	print("\n")



	print("Index 1.")
	for i in range(2):
		num = input('Please input a number with a decimal value (Ex: 3.45): ')
		sum1 = num
		is_float(num)
		count = 0
		for d in range(len(num)):
			if ord(num[d]) == 46:
				count += 1
		if count > 0 and count <= 1:
			exp_val = "True"
		else:
			exp_val = "False"
		if is_float(num) == exp_val:
			pf = "PASS"
		elif is_float(num) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", is_float(num), "|", pf)



	print("\n")



	print("Index 2. ")
	for i in range(2):
		letter = input('Please input an Upper case letter: ')
		sum1 = letter
		is_capital(letter)
		for e in range(len(letter)):
			if ord(letter[e]) in range(65,90):		
				exp_val = "True"
			elif ord(letter[e]) not in range(65,90):
				exp_val = "False"
		if is_capital(letter) == exp_val:
			pf = "PASS"
		elif is_capital(letter) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", is_capital(letter), "|", pf)



	print("\n")




	print("Index 3. ")
	for i in range(2):
		num = int(input("Please input an even number: "))
		sum1 = num
		is_even(num)
		if (num % 2) == 0:
			exp_val = "True"
		elif (num % 2) != 0:
			exp_val = "False"
		if is_even(num) == exp_val:
			pf = "PASS"
		elif is_even(num) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", is_even(num), "|", pf)



	print("\n")




	print("Index 4. ")
	for i in range(2):
		num = int(input("Please input an odd number: "))
		sum1 = num
		is_odd(num)
		if (num % 2) == 1:
			exp_val = "True"
		elif (num % 2) != 1:
			exp_val = "False"
		if is_odd(num) == exp_val:
			pf = "PASS"
		elif is_odd(num) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", is_odd(num), "|", pf)



	print("\n")



	print("Index 5. ")
	for i in range(2):
		sentence = str(input("Please input a sentece with a number: "))
		sum1 = sentence
		numbers_present(sentence)
		count = 0
		for h in range(len(sentence)):
			if ord(sentence[h]) in range(48,57):
				count += 1
		if count > 0:
			exp_val = "True"
		elif count == 0:
			exp_val = "False"
		if numbers_present(sentence) == exp_val:
			pf = "PASS"
		elif numbers_present(sentence) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", numbers_present(sentence), "|", pf)
		
	

	print("\n")



	print("Index 6. ")
	for i in range(2):
		sentence = str(input("Pleae input a string with a letter: "))
		sum1 = sentence
		letters_present(sentence)
		count = 0
		for k in range(len(sentence)):
			if ord(sentence[k]) in range(97,122) or ord(sentence[k]) in range(65,90):
				count += 1
		if count > 0:
			exp_val = "True"
		elif count == 0: 
			exp_val = "False"
		if letters_present(sentence) == exp_val:
			pf = "PASS"
		elif letters_present(sentence) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", letters_present(sentence), "|", pf)



	print("\n")




	print("Index 7. ")
	for i in range(2):
		sentence = str(input("Please input a sentence with quotes: "))
		sum1 = sentence
		contains_sub_string
		count = 0
		for z in range(len(sentence)):
			if ord(sentence[z]) == 34:
				count += 1
		if count > 0 and (count % 2) == 0:
			exp_val = "True"
		else:
			exp_val = "False"
		if contains_sub_string(sentence) == exp_val:
			pf = "PASS"
		elif contains_sub_string(sentence) != exp_val:
			pf = "FAIL"
		print("Input Value: ", sum1, "| Expectected Output: ", exp_val, "| Actual Output: ", contains_sub_string(sentence), "|", pf)

		
	print("\n")


	
	print("Index 8. ")
	sentence = input("Provide a lowercase letter/letters: ")
	print("Your letter uppercase is", make_upper(sentence))


	print("\n")


	print("Index 9. ")
	sentence = input("Provide an Uppercase letter/letters: ")
	print("Your letter lowercase is", make_lower(sentence))
	

	return 0
main()	
