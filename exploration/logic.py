print("Prompt 1.")
osu_student = input("Are you an OSU stident? Yes or no:")
print(osu_student)
print("", "\n")
print("Prompt 2.")
number = int(input("Choose a number between 0 and 50:"))
if number > 25:
	print("You're number is greater than 25")
elif number < 25:
	print("You're number is less than 25")
elif number == 25:
	print("You're number is 25")
print("", "\n")
# I am sure there is a much more efficient way to do prompt 3 but I do not remeber learning it in class and I couldnt figure it out so I am just going to brute force it.
print("Prompt 3.")
student_name = input("What is your last name? ")
if student_name[0] == "a":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "u":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "v":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "w":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "x":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "y":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "z":
	print("Your advisor is Sarah Kyllo")
elif student_name[0] == "o":
	print("Your advisor is Shannon Shivers")
elif student_name[0] == "p":
        print("Your advisor is Shannon Shivers")
elif student_name[0] == "q":
        print("Your advisor is Shannon Shivers")
elif student_name[0] == "r":
        print("Your advisor is Shannon Shivers")
elif student_name[0] == "s":
        print("Your advisor is Shannon Shivers")
elif student_name[0] == "t":
        print("Your advisor is Shannon Shivers")
elif student_name[0] == "e":
	print("Your advisors name is Michelle White")
elif student_name[0] == "f":
        print("Your advisors name is Michelle White")
elif student_name[0] == "g":
        print("Your advisors name is Michelle White")
elif student_name[0] == "h":
        print("Your advisors name is Michelle White")
elif student_name[0] == "i":
        print("Your advisors name is Michelle White")
elif student_name[0] == "j":
        print("Your advisors name is Michelle White")
elif student_name[0] == "k":
        print("Your advisors name is Aaron Worley")
elif student_name[0] == "l":
        print("Your advisors name is Aaron Worley")
elif student_name[0] == "m":
        print("Your advisors name is Aaron Worley")
elif student_name[0] == "n":
        print("Your advisors name is Aaron Worley")
elif student_name[0] == "b":
        print("Your advisors name is Julia Rosenzweig")
elif student_name[0] == "c":
        print("Your advisors name is Julia Rosenzweig")
elif student_name[0] == "d":
        print("Your advisors name is Julia Rosenzweig")
print("", "\n")
print("Prompt 4.")
grade = int(input("Choose a number betweeon 0 and 100: "))
if grade > 100:
	print("How did you get extra credit?")
elif grade >= 90:
	print("Youre grade is an A")
elif grade >= 80:
	print("Youre grade is a B")
elif grade >= 70:
	print("Youre grade is a C")
elif grade >= 60:
	print("Youre grade is a D")
else:
	print("Youre grade is an F")
print("", "\n")
#I do not know how to do prompt 5. I dont know how to code in the alphabet and show which letters come first. 
print("Prompt 5.")
word_1 =  input(str("Please enter a word: "))
word_2 = input(str("Please enter a second word: "))
if word_1[0] > word_2[0]:
	print("Word one comes first in the alphabet.")
print("", "\n")
print("Prompt 6.")
food = input(str( "Do you want a hamburger or hot dog? "))
if food == "hotdog": 
	mustard = input(" Would you like mustard on your hotdog yes or no? ")
	if mustard == "yes":
		print("You got a hotdog with mustard.")
	elif mustard == "no":	
		print("You got a hotdog without mustard.")
elif food == "hamburger":
	cheese = input("Would you like cheese on your hamburger yes or no? ")
	if cheese == "yes":
		print("You got a hamburger with cheese.")
	elif cheese == "no":
		print("You got a hamburger without cheese.")

#This is the third part of Assignment 3 where I am creating the choose your own adventure I made in lab.
print("", "\n")
print("""It is your first day of CS 160 lab and you are running late. Your arrive at Dearborn hall five minutes before 
class starts only to find that the building is a maze and you must work your way through the building by opening doors 
to find your class room. Or a room you like.""")
print("", "\n")
door_1 = input(str("You have four doors infront of you each leading to a differnt room, pick a room by entering 1, 2, 3 or 4: "))
if door_1 == "1":
	print("You find yourself in a room with two empty doors.")
	print("", "\n")
	door_1a = input(str("Enter left or right to choose which door to go through next: "))
	if door_1a == "left":
		print("You walk in the door and are eaten by a tiger.")
	elif door_1a == "right":
		print("You walk in and find the right CS class. Success!")
elif door_1 == "2":
	print("You find a room full of puppoes with a door on the other side.")
	print("", "\n")
	door_1b = input(str("Enter \"stay\" if you would like to stay and play \n with the puppies or \"go\" if you would like to move on and go through the door: "))
	if door_1b == "stay":
		print("You got to play with puppies but failed CS.")
	elif door_1b == "go":
		print("You go through the door and find the right CS lab. Success!")
elif door_1 == "3":
	print("You find a room full of snakes with a door on the other side.")
	print("", "\n")
	door_1c = input(str("To run away enter 1 to make your way through to other side enter 2: "))
	if door_1c == "1":
		print("As you run away you get lost and end up missing class.")
	elif door_1c =="2":
		print("The snakes are venomous. You get bitten and die.")
elif door_1 == "4":
	print("Youf find your CS 160 lab Success! Wait you realize after class that the CS 160 lab you were in ROG 222 not DEAR 222. You fail!")




