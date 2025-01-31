def insert_letter(board, position, letter):
	
	board[position] = letter 
	
	
def space_is_free(board, position):


	if  board[position] == " ":
		return True
	else:
		return False

def print_board(board):

	print("   |   |")
	print(" " +  board[1] +  " | " +  board[2] +  " | " +  board[3])
	print("   |   |")
	print("-----------")
	print("   |   |")
	print(" " + board[4] + " | " + board[5] + " | " + board[6])
	print("   |   |")
	print("-----------")
	print("   |   |")
	print(" " + board[7] + " | " + board[8] + " | " + board[9])
	print("   |   |")

	
def is_winner(bo, le):

	return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def player_one_move(board) :

	run = True
	while run:
		move = input("Please select a position to place an \"X\" (1-9): ")
		if len(move) == 1:
			if (move > chr(48) and move <= chr(57)):
				move = int(move)
				if space_is_free(board, move) == True:
					insert_letter(board, move, "X")
					run = False
				else:
					print("Sorry, that space is occupied.")
			else:
			print("Please input a number in the required range.")
		else: 
			print("Please input a number in the required range,")
	return move
			
def player_two_move(board):

	run = True
	while run:
		move = input("Please select a position to place an \"O\" (1-9): ")
		if len(move) == 1:
			if move > chr(48) and move <= chr(57):		
				move = int(move)
				if space_is_free(board, move) == True:
					run = False
				else:
					print("Sorry, that space is occupied.")
			else:
				print("Please input a number in the required range.")
		else:
			print("Please input a number in the required range.")
	return move	

def is_board_full(board):
	
	count = 0
	for i in range(len(board)):
		if board[i] == " ":
			count += 1
	if count > 1:
		return False
	else:
		return True
def game(board):

	while (is_board_full(board)) != True:
		if not (is_winner(board, "O")):
			player_one_move(board)
			print_board(board)
		else:
			print("O\'s won the game!")
			break
		if not (is_winner(board, "X")):
			if is_board_full(board) == True:
				break
			else:
				move = player_two_move(board)
				insert_letter(board, move, "O")
				print_board(board)
		else:
			print("X\'s won the game!")
			break
	if is_board_full(board) == True and (is_winner(board, "O") == False) and (is_winner(board, "X") == False):
		print("Tie game!")
def main():
	count = 1
	while count > 0:
		board = [" " for x in range(10)]
		print("Welcome to Tic Tac Toe! To win complete a straight line of your letter (Horizontal, Vertical, or Diagonal). The board has positions 1-9 starting at the top left.")
		count = 0
		print_board(board)
		game(board)
		play_again = input("If you would like to play again input \"Yes\" if not input \"No\": ")
		if play_again == "Yes" or play_again == "yes":
			count = 1
		elif play_again  == "No" or play_again == "no":
			print("Game over.")
		else:
			print("Invalid input. Game over.")
	return 0


main()
