print("Prompt 1. ")
for x in range(5):
	print("Hello World!")

print("\n")

print("Prompt 2. ")
for x in range(101):
	print("Hello Student", x)

print("\n")

print("Prompt 3. ")
x = 50
while x > -1:
	print(x)
	x -=1

print("\n")

print("Prompt 4. ")
count = 1
while count > 0:
	count = 0
	val = int(input("Provide a whole number between 25 and 50: "))
	if val not in range(25,50):
		count += 1
print("Good Job")

print("\n")

print("Prompt 5. ")
count = 1
while count > 0:
        count = 0
        letter = ord(input("Provide a lower case letter: "))
        if letter  not in range(ord("a"), ord("z")):
                count += 1
print("Good Job")

# print("\n")

# print("Prompt 6. ")
# for row in range(1,6):
#	print(row)

print("\n")

print("Prompt 7. ")

count = 1
while count > 0:
	count = 0
	val1 = int(input("Provide a whole number outside the range of  25 and 50: "))
	if val1 in range(25,50):
		print("The number must be outside the range 25 and 50. Ex: 76 ")
		count += 1
	elif val1 not in range(25,50):
		print (val1)
		
	val2 = int(input("Provide a second whole number outside the range of  25 and 50: "))
	if val2 in range(25,50):
		print("The number must be outside the range 25 and 50. Ex: 76 ")
		count += 1
	elif val2 not in range(25,50):
		print (val2)
	
	val3 = int(input("Provide a third whole number outside the range of  25 and 50: "))
	if val3 in range(25,50):
		print("The number must be outside the range 25 and 50. Ex: 76 ")
		count += 1
	elif val3 not in range(25,50):
		print (val3)
print("Good job")


	

