
print("Part 1.","\n")
count = 1
sum = 0
count2 = 0
while count > 0:
	count = 0
	numb = int(input("Provide a number: "))
	sum += numb
	print(sum)
	count2 += 1
	cont = input("Would you like to continue yes or no? ")
	if cont == "yes":
		count += 1
print("Your number average is: ", (sum / count2))
