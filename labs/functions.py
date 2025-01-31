def addition():
	a = int(input("Please input a number: "))
	b = int(input("Please input a second number: "))
	print("Your numbers added together equal", (a+b))

def subtraction():
	c = int(input("Please input a number: "))
	d = int(input("Pleasae input a second number: "))
	print("Your numbers subtracted equal: ", (c-d))  

def multiplication():
	e = int(input("Please input a number: "))
	f = int(input("Please input a second number: "))
	print("Your numbers multiplied equal: ", (e*f))
def division():
	g = int(input("Please input a number: "))
	h = int(input("Please input a second number: "))
	if h > 0 or h < 0:
		print("Your numbers divided equal: ", (g/h))
	elif h == 0:
		print("You cannot divide by zero.")

def power():
	i = int(input("Please input a number: "))
	j = int(input("Please input a second number: "))
	print("Your first number raise to the power of your second equals: ", (i**j))

def average():
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

def main():
	count = 1 
	while count > 0:
		count = 0
		function = input("Please choose a math function(+, -, *, /, **, Avg.): ")
		if function == "+":
			addition()
		elif function == "-":
			subtraction()
		elif function == "/":
			division()
		elif function == "*":
			multiplication()
		elif function == "**":
			power()
		elif function == "Avg.":
			average()
		contin = input("Would you like to perform another calculation yes or no? ")
		if contin == "yes":
			count += 1
	return 0
main()
