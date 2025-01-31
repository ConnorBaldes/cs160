
def get_list():
	input_list = []
	count = 1
	while count > 0:
		count = 0
		numbers = input("Input the number you would like to be added to the list: ")
		input_list.append(numbers)
		count = int(input("If you want to add another number to the list enter 1 if not enter 0: "))
	return input_list

def check_list(list_check):
	
	num_list = []
	for i in range(len(list_check)):
	
		if int(list_check[i]) >= 1 and int(list_check[i]) <= 100:
			num_list.append(list_check[i])
	print(num_list)
	return 	

def get_fruit():
	count = 1
	while count > 0:
		count = 0
		fruit_list = []
		fruit = input("Input the fruit you would like to use: ")
		weight = str(input("Input the weight of that fruit in pounds: "))
		fruit_w = fruit + " " + weight
		fruit_list = fruit_list.append(fruit_w)
		count = int(input("If you would like to enter another fruit input 1 if not enter 0: "))
	print(fruit_list)
	return fruit_list


def list_sort(list_s):

	list_s.sort()
	
	print(list_s)


def main():

	g_list = get_list()

	check_list(g_list)

	fruit_weight = get_fruit()

	list_sort(fruit_weight)
main()
