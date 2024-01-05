# Title: advanced_battleship.py
# Author: Walter McCue
# Date 12/22/23
#

from random import randint
import json

with open ('battleship_rankings.json') as data:
  ranks = json.load(data)

#top_scores = json.dumps(ranks, indent = 4)
#print (top_scores)
  
name = "Walter"
def print_scores(name):
  for item in ranks:
    for key in item:
      if item[key] == name:
        record = ranks.index(item)
        last_game = ranks[record]["last_single_play"]
        best_score = ranks[record]["best_single_play"]
        print ("Previous Game Score: " + str(last_game))
        print ("Best Score: "+ str(best_score))
print (print_scores(name))


# Will return true if player record is found
def overwrite_ranks(name):
  for item in ranks:
    for key in item:
      if item[key] == name:
        return True
  

# Battleship board set-up
def new_board():
  board = [["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 "], \
          ["A "], ["B "], ["C "], ["D "], ["E "], ["F "], ["G "]]
  for x in range(1, 8):   # Creates empty spaces on board
    for i in range(1, 8):
      board[i].append("O ")
  return board


# Removes quotes from the lists and makes board a grid
def print_board(board):
  for row in board:
    print (" ".join(row))
  

# Creates Carrier coordinates
def make_carrier():
  location = [[], [], []]
  orientation = randint(0, 1)
  if orientation == 0:    # Vertical placement
    row = randint(1, len(new_board()) - 1)
    col = randint(1, len(new_board()) - 3)
    location[0].append(row)
    location[0].append(col)
    location[1].append(row)
    location[1].append(col + 1)
    location[2].append(row)
    location[2].append(col + 2)
  else:   # Horizontal placement
    row = randint(1, len(new_board()) - 3)
    col = randint(1, len(new_board()) - 1)
    location[0].append(row)
    location[0].append(col)
    location[1].append(row + 1)
    location[1].append(col)
    location[2].append(row + 2)
    location[2].append(col)
  return location


# Creates Destroyer coordinates
def make_destroyer():
  location = [[], []]
  orientation = randint(0, 1)
  if orientation == 0:    # Vertical placement
    row = randint(1, len(new_board()) - 1)
    col = randint(1, len(new_board()) - 2)
    location[0].append(row)
    location[0].append(col)
    location[1].append(row)
    location[1].append(col + 1)
  else:   # Horizontal placement
    row = randint(1, len(new_board()) - 2)
    col = randint(1, len(new_board()) - 1)
    location[0].append(row)
    location[0].append(col)
    location[1].append(row + 1)
    location[1].append(col)
  return location


# Creates Gunship coordinates
def make_gunship():
  location = []
  location.append(randint(1, len(new_board()) - 1))
  location.append(randint(1, len(new_board()) - 1))
  return location


# Creates all 3 battleship coordinates
def ship_locations():
  locations =[]
  carrier = make_carrier()    # Carrier

  # Creates Destroyer but does not allow overlap of coordinates with Carrier
  def destroyer_overlap():
    destroyer = make_destroyer()
    while destroyer[0] == carrier[0] or destroyer[0] == carrier[1] or \
      destroyer[0] == carrier[2] or destroyer[1] == carrier[0] or \
      destroyer[1] == carrier[1] or destroyer[1] == carrier[2]:
      destroyer = make_destroyer()
    return destroyer
  destroyer = destroyer_overlap()

  # Creates Gunship but does not allow overlap of coordinates with Destroyer or Carrier
  def gunship_overlap():
    gunship = make_gunship()
    while gunship == destroyer[0] or gunship == destroyer[1] or \
      gunship == carrier[0] or gunship == carrier[1] or gunship == carrier[2]:
      gunship = make_gunship()
    return gunship
  gunship = gunship_overlap()

  locations.append(carrier)
  locations.append(destroyer)
  locations.append(gunship)
  return locations


# Game Rules
def rules():
  print ("Rules:\n \
      1. Single Players: You only have 20 turns to sink the fleet.\n \
         Two Players: Each player will get a turn until a player sinks the other's fleet.\n \
      2. Ships are placed randomly.\n \
      3. There are three battleships per fleet.\n \
      4. Gunships take a single space.\n \
      5. Destroyers take two spaces.\n \
      6. Carriers take three spaces.\n \
      7. O is an unknown location.\n \
      8. M is a missed attack.\n \
      9. X is a direct hit.")


# Player turn
def player_turn(turn_board, ships, score):
  attack = []
  choice = input ("Which coordinates would you like to attack (ex: A7)?\n").upper()
  for x in choice:
    attack.append(x)
  # Sets index 0 to to int or to 0 if invalid
  if attack[0] == "A":
    attack[0] = 1
  elif attack[0] == "B":
    attack[0] = 2
  elif attack[0] == "C":
    attack[0] = 3
  elif attack[0] == "D":
    attack[0] = 4
  elif attack[0] == "E":
    attack[0] = 5
  elif attack[0] == "F":
    attack[0] = 6
  elif attack[0] == "G":
    attack[0] = 7
  else:
    attack[0] = 0

  # Sets index 1 to int or to 0 if invalid
  try:
    attack[1] = int(attack[1])
  except:
    attack[1] = 0
  else:
    attack[1] = int(attack[1])
  if attack[1] > 7:
    attack[1] = 0

  # Determines where attacks land
  hit = turn_board[attack[0]][attack[1]] = "X "
  if attack[0] == 0 or attack[1] == 0:    # Invalid attack
    print ("Oops. Your attack wasn't even in the ocean!")
  elif turn_board[attack[0]][attack[1]] == "X" or turn_board[attack[0]][attack[1]] == "M":    # Attack on a previous target
    print ("Oops. You already attacked that location.")
  elif attack == ships[0][0] or attack == ships[0][1] or \
  attack == ships[0][2]:    # Attack hit Carrier
    print ("You hit the Carrier!")
    hit
    score += 1
    if turn_board[ships[0][0][0]][ships[0][0][1]] == "X " and \
      turn_board[ships[0][1][0]][ships[0][1][1]] == "X " and \
      turn_board[ships[0][2][0]][ships[0][2][1]] == "X ":
      print ("You sunk the Carrier!!!")
  elif attack == ships[1][0] or attack == ships[1][1]:    # Attack hit Destroyer
    print ("You hit the Destroyer!")
    hit
    score += 1
    if turn_board[ships[1][0][0]][ships[1][0][1]] == "X " and \
      turn_board[ships[1][1][0]][ships[1][1][1]] == "X ":
      print ("You sunk the Destroyer!!!")
  elif attack == ships[2]:    # Attack hit Gunship
    print ("You sunk the Gunship!!!")
    hit
    score += 1
  else:   # Attack missed a target but landed on the board
    print ("Sorry, you missed.")
    turn_board[attack[0]][attack[1]] = "M "
  print ("\n\n")
  return turn_board, score


# Single Player
def play_single():
  player = input ("What is your name?\n")
  print ("Hello "+ player)
  player_board = new_board()
  player_ships = ship_locations()
  player_score = 0
  
  # Player has 20 turns
  for turn in range(21):
    turn += 1
    print ("You have 20 turns. Turn: " + str(turn))
    print (print_board(player_board))
    print (player_ships)
    current_turn = player_turn(player_board, player_ships, player_score)    # Calls the player_turn function
    player_board = current_turn[0]    # Puts the last attack on the board
    player_score = current_turn[1]
    
    # Scoreboard
    if player_score == 6:    # When player has hit all 6 marks, they win
      print ("You Win!")
      break
    if turn == 21:    # After 20 turns, game over
      print ("Game Over")
      break

  # Player Record
  overwrite = overwrite_ranks(player)   # Determines if player record exists
  if overwrite == True:   # If record exists, overwrite last game score with this score
    for item in ranks:    # And check to see if this score beats the record
      for key in item:    # If new score beats the record, sets new high record
        if item[key] == player:
          item["last_single_play"] = turn
          if item["best_single_play"] > turn:
            item["best_single_play"] = turn
  else:   # If player record does not exist, create it
    ranks.append({ "name": player, \
                  "last_single_play": turn, \
                  "best_single_play": turn, \
                  "competitive_wins": 0, \
                  "competitive_losses": 0 })
  json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )    # Updates the battleship_rankings

  exit()
    

# Competitive Play
def play_two():

  # Player one set-up
  player_one = input ("What is player 1 name?\n")
  one_board = new_board()
  one_ships = ship_locations()
  one_score = 0
  one_overwrite = overwrite_ranks(player_one)

  # Player two set-up
  player_two = input ("What is player 2 name?\n")
  two_board = new_board()
  two_ships = ship_locations()
  two_score = 0
  two_overwrite = overwrite_ranks(player_two)

  print (("Hello %s and %s.") % (player_one, player_two))

  # loops until a player has a score of 6
  while one_score != 6 or two_score != 6:

    # Player one turn
    print (player_one + 's Turn:')
    print_board(one_board)
    one_turn = player_turn(one_board, one_ships, one_score)
    one_board = one_turn[0]
    one_score = one_turn[1]

    if one_score == 6:    # Player one winner!
      print (player_one + " is the winner!")

      # Player Record
      if one_overwrite == True:   # If record exists, add 1 to win count
        for item in ranks:
          for key in item:
            if item[key] == player_one:
              item["competitive_wins"] += 1
      else:   # If player record does not exist, create it
        ranks.append({ "name": player_one, \
                      "last_single_play": 0, \
                      "best_single_play": 0, \
                      "competitive_wins": 1, \
                      "competitive_losses": 0 })
      if two_overwrite == True:   # If record exists, add 1 to loss count
        for item in ranks:
          for key in item:
            if item[key] == player_two:
              item["competitive_losses"] += 1
      else:   # If player record does not exist, create it
        ranks.append({ "name": player_two, \
                      "last_single_play": 0, \
                      "best_single_play": 0, \
                      "competitive_wins": 0, \
                      "competitive_losses": 1 })
      json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )    # Updates the battleship_rankings

      break

    # Player two turn
    print (player_two + 's Turn:')
    print_board(two_board)
    two_turn = player_turn(two_board, two_ships, two_score)
    two_board = two_turn[0]
    two_score = two_turn[1]

    if two_score == 6:    # Player two winner!
      print (player_two + " is the winner!")

      # Player Record
      if two_overwrite == True:   # If record exists, add 1 to win count
        for item in ranks:
          for key in item:
            if item[key] == player_two:
              item["competitive_wins"] += 1
      else:   # If player record does not exist, create it
        ranks.append({ "name": player_two, \
                      "last_single_play": 0, \
                      "best_single_play": 0, \
                      "competitive_wins": 1, \
                      "competitive_losses": 0 })
      if one_overwrite == True:   # If record exists, add 1 to loss count
        for item in ranks:
          for key in item:
            if item[key] == player_one:
              item["competitive_losses"] += 1
      else:   # If player record does not exist, create it
        ranks.append({ "name": player_one, \
                      "last_single_play": 0, \
                      "best_single_play": 0, \
                      "competitive_wins": 0, \
                      "competitive_losses": 1 })
      json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )    # Updates the battleship_rankings

      break

  exit()
  

# Game introduction
def play_battleship():
  play = input ("Do you want to play battleship?\n").lower()
  if play == "y" or play == "yes":
    rules()
    players = input ("1 or 2 Players?\n").lower()
    if players == "1":
      play_single()
    elif players == "2":
      play_two()
    else:
      print ("Select a valid option")
      play_battleship()
  elif play == "n" or play == "no":
    exit()
  else:
    print ("Select a valid option")
    play_battleship()


# Starts Game 
play_battleship()
