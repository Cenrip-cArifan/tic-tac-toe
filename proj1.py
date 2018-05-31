#File:        proj1.py
#Author:      Gabriel Kilungya
#Date:        04/18/16
#Lab Section: 15
#UMBC email:  kilgab1@umbc.edu
#Description: Python game file. In this python file I am creating a game between two players
#	      If a player moves in a taken spot display error, player goes again
#	      If game is a draw, print message ask user to play again
#	      If a player wins, display winner and then ask user if he want to play again 



import random

#setRandom function: Returns a random integer 0 or 1

# to get a random player between 1 and 2
# I used 0 & 1 instead of 1 & 2 because I could alternate
# between player 1 & player 2 easily (odd & even)


def setRandom():

	return random.randint(0,1)


#Set the function to player so I could call it again in main()
#So the game can operate always the same when deciding random
#player if I have not exited the game

player = setRandom()

	

#setSymbol function: Returns a random integer 1 or 2

# to get a random symbol between 1 and 2


def setSymbol():

	return random.randint(1,2)

#Set the function to symbol so I could call it again in main()
#So the game can operate always the same when deciding random
#letter assigned to players if I have not exited the game


symbol = setSymbol()


# you will need to convert 1 and 2 to "X" and "O"


#printBoard() function: takes in the parameter board.
#This is where the board will print row by columns, 
#using nested for loops to design board

#If-statements: If the index of the board is equal to a 0, print "X" 
#or index of board is equal to a 1, print "O",
#otherwise if index of board is equal to -1: print the cell number
#Output: prints the board

def printBoard(board):

	for i in range(3):
		for j in range(3):
			if board[i*3+j] == 1:
				print playerSymbol(1),
			elif board[i*3+j] == 0:
				print playerSymbol(0),
			elif board[i*3+j] == -1:
				print (i*3+j)+1,
			
			
			if (j != 2):
				print " | ",
			
		print

		if (i != 2):
			print "-------------"


#This function takes the printBoard function board content and converts and makes it into a string
#This function is for the purposes of writing/saving the board into a file
#Output: returns the board as a string

def placeBoard(board):
	
	s = ""

	for i in range(3):
		for j in range(3):
			if board[i*3+j] == 1:
				s += playerSymbol(1)
				
			elif board[i*3+j] == 0:
				s += playerSymbol(0)
			elif board[i*3+j] == -1:
				s += str((i*3+j)+1)
			
			
			if (j != 2):
				s += " | "
			
		s += "\n"
		if (i != 2):
			s += "----------\n"

	return s





# playerName function: Takes in an integer.
# Input: If integer is even, player 1's turn, otherwise player 2's turn
# Output: Return name (name of player who is going first)

def playerName(num):

	if(num % 2 == 0):

		name = "Player 1"
		

	else:

		name = "Player 2"

	return name




#playerSymbol function: Takes in an integer and returns a string
#if symbol is equal to 1, return 'X' otherwise return 'O'
#Output: Returns either letter "X" or letter "O", depending on the randomness
#of who goes first 


def playerSymbol(num):

	if(num == player and symbol == 1):

		return "X"
	elif(num == player and symbol == 2):

		return "O"

	elif(num != player and symbol == 1):

		return "O"

	else:

		return "X"


#while the turn is True ask user for input
#-1 or -2 will be used to save or load the game respectively
#this command will be inputted in the code at the end of testing code functionality
	
def move(currentPlayer,board):

	choice = int(input("(1-9) or -2 to save or -3 to load: "))

	currentSymbol = symbol


	#while the choice is INVALID,
	#loop until it is VALID
	
	while(True):				
		
		#if there is an error in the input,
		
		if ((choice < 1 or choice > 9) and (choice != -2 and choice != -3)):

			print("Error! Invalid move")
			print(playerName(currentPlayer) + " what is your choice? ")
			
			#ask for input again,			
			choice = int(input("(1-9) or -2 to save or -3 to load: "))

		elif(choice == -2):
	
			saveGame(board, currentPlayer, currentSymbol)

			return choice

		elif(choice == -3):

			loadGame()

			return choice

			
		elif(board[choice - 1] != -1 ):

			print("That space is already taken.")
			print(playerName(currentPlayer) + " what is your choice? ")
			choice = int(input("(1-9) or -2 to save or -3 to load: "))

			
		else:
			#otherwise, input is great, do what we need to do and return.

			board[choice - 1] = currentPlayer

			return (choice - 1)

		
#isWon function: Takes in the parameter board
#It creates a tuple that is assigned to the 'win' variable
#The tuple presents all the possible ways to win the game according to the cell number
#For loop: checks for the position of board and if the x equals y equals z is true or not
#Output: Returns true a winning condition is met: otherwise false
	
def isWon(board):

	win = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))

	for (x,y,z) in win:

		if(board[x - 1] == board[y - 1] and board[y - 1] == board[z - 1] and board[x - 1] != -1):

			return True

	return False


#isDraw function: Takes in the parameter board
#Output: returns True if there are no spaces left on the board

def isDraw(board):

	return -1 not in board


#saveGame function: Takes in the 3 parameters: board, currentPlayer, currentSymbol
#Open up a file and give it a filename and write to it the three parameters when game needs to
#be paused and continued at a later time
#When finished close the file

def saveGame(board, currentPlayer, currentSymbol):

	save = open("currentGame.txt", "w")

	
	placeBoard(board)
	playerName(currentPlayer)
	playerSymbol(currentSymbol)
	
	
	save.write(placeBoard(board) + '\n')

	save.write(playerName(currentPlayer) + '\n')

	save.write(playerSymbol(currentSymbol) + '\n')
	
	save.close()

#loadGame function: reads in a file and strips each line out and appends content to board
#Output: Prints the saved game content board

def loadGame():
	
	load = open("currentGame.txt", "r")

	for eachLine in load:

		eachLine = eachLine.strip()

		print(eachLine)

			
	
#main function: This is where all the functions are called into and the program is ran
#first print the board: My board will be appended by -1 so my save choice is set to -2
#load choice is set to -3

#set gamePlay to True, this bool will be used to run the game
#while loop: while gamePlay = True, print the board, ask the user randomly picked to go first
#where he would like to move or if he wants to save(-2) or load(-3):
#This will be done by calling the move function

#While the players are taking turns, check to see if anyone has won the game.
#If someone has won, print winner and set gamePlay to False to end move function method
#Ask if the user wants to play again

#If it is a draw, display the game is a draw
#Ask if the user wants to play again

#If the user saves the game process, display message
#Ask if the user wants to play again

#If the user wants to load a game
#Continue from where the saved game left off


def main():

	print("Welcome to Tic-Tac-Toe")
	print("This is for two players")

	#Since my player and symbol random functions are called into a function
	#They are only accessable from the function are not global to main, so i set them as global function in main
	#So when the game ends, and I ask user again to play, the player and symbol are random and not permanently set
	
	player = setRandom()
	symbol = setSymbol()


	
	print

	board = []
	
	for i in range(9):

		board.append(-1)

	gamePlay = True	

	currentPlayer = player
	

	print(playerName(currentPlayer) + " will go first and will play with symbol " + playerSymbol(currentPlayer))

	while(gamePlay == True):	

		printBoard(board)	
		
		print('\n' + playerName(currentPlayer) + " what is your choice? ")

		user = move(currentPlayer, board)

				 
		if (isWon(board)):
			
			printBoard(board)	

			print ('\n%s, with %s has WON!' % (playerName(currentPlayer), playerSymbol(currentPlayer)))
			
			gamePlay = False

					
		elif (isDraw(board)):

			printBoard(board)

			print("The Game ends in a Draw!")		

			gamePlay = False

		else:

			if(user == -2):

				print("File Saved")

				gamePlay = False

			elif(user == -3):
	
				print("Game Loaded")

				gamePlay = True
				
			else:

				currentPlayer = (currentPlayer + 1) % 2

	
	
	again = input("Play again? ")

	if(again == "n" or again == "N" or again == "no" or again == "NO" or again == "No" or again == "nO"):

		gamePlay = False

	else:
		player = setRandom()
		symbol = setSymbol()
		
		main()

	

main()	
