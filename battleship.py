#
#
#    Battleship
#
from random import randint

def play_battleship():
  board = []                                               #battleship board

  for x in range(0, 5):                                    #creates a 5x5 board
    board.append(["O"] * 5)

  def print_board(board):                                  #removes quotes from the lists and makes board a grid
    for row in board:
      print (" ".join(row))

  print_board(board)

  def random_row(board):                                   #sets the row for the ship to occupy
    return randint(0, len(board) - 1)

  def random_col(board):                                   #sets the column for the ship to occupy
    return randint(0, len(board[0]) - 1)

  ship_row = random_row(board)                             #assigns the row to the board
  ship_col = random_col(board)                             #assigns the col to the board
  #print (ship_row)                                        #debugging only
  #print (ship_col)                                        #debugging only

  for turn in range(5):                                    #user has 4 turns
    print ("You have 5 turns. Turn: " + str(turn + 1))
    turn + 1

    guess_row = int(input("Guess Row (0-4): "))                 #user input for the row
    guess_col = int(input("Guess Col (0-4): "))                 #user input for the col

    def game_over():                                       #game_over function
      print ("Game over")

    if guess_row == ship_row and guess_col == ship_col:    #if user sinks battleship
      print ("Congratulations! You sunk my battleship!")
      break
    else:                                                  #if user fails to sink battleship
      if (guess_row < 0 or guess_row > 4) or \
        (guess_col < 0 or guess_col > 4):                  #if user does not enter 0-4
        print ("Oops, that's not even in the ocean.")
      elif(board[guess_row][guess_col] == "X"):            #if user already guessed that spot
        print ("You guessed that one already.")
        if turn == 4:                                      #game over
          game_over()
          break
      else:                                                #if user missed the battleship
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        if turn == 4:                                      #game over
          game_over()
          break

      print_board(board)
  
  play_again = input("Would you like to play again Y or N?").lower()
  if play_again == "y":                                   #starts game again
    play_battleship()
  else:                                                   #exit game
    exit()

play_battleship()                                         #starts game
