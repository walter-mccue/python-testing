# Title: advanced_battleship.py
# Author: Walter McCue
# Date 12/22/23
#

from random import randint
import json
import time

with open ('battleship_rankings.json') as data:
  ranks = json.load(data)

  
# Shows user their current scores
def print_scores(name, game):
  for item in ranks:
    for key in item:
      if item[key] == name:
        record = ranks.index(item)
        last_game = str(ranks[record]["last_single_play"])
        best_score = str(ranks[record]["best_single_play"])
        comp_wins = str(ranks[record]["competitive_wins"])
        comp_losses = str(ranks[record]["competitive_losses"])
        if game == "Single":
          print ("Previous Game Score: " + last_game)
          print ("Best Score: " + best_score)
        if game == "Competitive":
          print ("Two Player Wins: " + comp_wins)
          print ("Two Player Losses: " + comp_losses)


# Will return true if player record is found
def find_record(name):
  for item in ranks:
    for key in item:
      if item[key] == name:
        return True


# Creates the player record      
def create_record(name):
  ranks.append({ "name": name, \
                  "last_single_play": 0, \
                  "best_single_play": 0, \
                  "competitive_wins": 0, \
                  "competitive_losses": 0 })
  # Updates the battleship_rankings
  json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )
  

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
  print ("\nRules:\n \
      1. Single Players: Continue entering coordinates until you sink the fleet (A lower score is better.). \n \
         Two Players: Each player will get a turn until a player sinks the other's fleet.\n \
      2. Ships are placed randomly.\n \
      3. There are three battleships per fleet.\n \
      4. Gunships take a single space.\n \
      5. Destroyers take two spaces.\n \
      6. Carriers take three spaces.\n \
      7. O is an unknown location.\n \
      8. M is a missed attack.\n \
      9. X is a direct hit.\n")


# Player turn
def player_turn(turn_board, ships, score):
  attack = []
  choice = input ("\nWhich coordinates would you like to attack (ex: A7)?\n").upper()
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
  if attack[0] == 0 or attack[1] == 0:    # Invalid attack
    print ("Oops. Your attack wasn't even in the ocean!")

  elif turn_board[attack[0]][attack[1]] == "X " or turn_board[attack[0]][attack[1]] == "M ":
    # Attack on a previous target
    print ("Oops. You already attacked that location.")

  elif attack == ships[0][0] or attack == ships[0][1] or \
  attack == ships[0][2]:    # Attack hit Carrier
    print ("You hit the Carrier!")
    turn_board[attack[0]][attack[1]] = "X "
    score += 1

    # If attack sunk the Carrier
    if turn_board[ships[0][0][0]][ships[0][0][1]] == "X " and \
      turn_board[ships[0][1][0]][ships[0][1][1]] == "X " and \
      turn_board[ships[0][2][0]][ships[0][2][1]] == "X ":
      print ("You sunk the Carrier!!!")

  elif attack == ships[1][0] or attack == ships[1][1]:    # Attack hit Destroyer
    print ("You hit the Destroyer!")
    turn_board[attack[0]][attack[1]] = "X "
    score += 1

    # If attack sunk Destroyer
    if turn_board[ships[1][0][0]][ships[1][0][1]] == "X " and \
      turn_board[ships[1][1][0]][ships[1][1][1]] == "X ":
      print ("You sunk the Destroyer!!!")

  elif attack == ships[2]:    # Attack hit Gunship
    print ("You sunk the Gunship!!!")
    turn_board[attack[0]][attack[1]] = "X "
    score += 1

  else:   # Attack missed a target but landed on the board
    print ("Sorry, you missed.")
    turn_board[attack[0]][attack[1]] = "M "

  print ("\n\n")
  time.sleep(1.5)
  return turn_board, score


# Single Player
def play_single():
  game = "Single"
  player = input ("\nWhat is your name?\n")
  print ("\nHello "+ player)
  player_board = new_board()
  player_ships = ship_locations()
  player_score = 0

  # Finds player record and shows current scores or creates record if not found
  record = find_record(player)
  if record == True:
    print_scores(player, game)
  else:
    create_record(player)

  print ("\nYour score is determined by how many turns it takes to sink the fleet.\n")
  time.sleep(1)

  # Player turn
  for turn in range(100):
    turn += 1
    print ("Turn: " + str(turn))
    print_board(player_board)
    #print (player_ships)    # For testing only (Shows Ship locations)

    # Calls the player_turn function
    current_turn = player_turn(player_board, player_ships, player_score)
    player_board = current_turn[0]    # Puts the last attack on the board
    player_score = current_turn[1]
    
    # Scoreboard
    if player_score == 6:    # When player has hit all 6 marks, they win
      print ("You Win!")
      break
    if turn == 100:    # After 100 turns, game over
      print ("Game Over")
      break

  # Updates Player Record
  for item in ranks:    # Overwrite last game score with this score
    for key in item:    # And check to see if this score beats the record
      if item[key] == player:   # If new score beats the record, sets new high record
        item["last_single_play"] = turn
        if item["best_single_play"] > turn:
          item["best_single_play"] = turn
  # Updates the battleship_rankings
  json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )

  play_battleship()
    

# Competitive Play
def play_two():
  game = "Competitive"

  # Player one set-up
  player_one = input ("\nWhat is player 1 name?\n")
  one_board = new_board()
  one_ships = ship_locations()
  one_score = 0
  one_record = find_record(player_one)
  print ("\nHello " + player_one)

  # Finds player record and shows current scores or creates record if not found
  if one_record == True:
    print_scores(player_one, game)
  else:
    create_record(player_one)
  
  print ("\n")
  time.sleep(1)

  # Player two set-up
  player_two = input ("What is player 2 name?\n")
  two_board = new_board()
  two_ships = ship_locations()
  two_score = 0
  two_record = find_record(player_two)
  print ("\nHello " + player_two)

  # Finds player record and shows current scores or creates record if not found
  if two_record == True:
    print_scores(player_two, game)
  else:
    create_record(player_two)

  print ("\n")
  time.sleep(1)

  # loops until a player has a score of 6
  while one_score != 6 or two_score != 6:

    # Player one turn
    print (player_one + 's Turn:')
    print_board(one_board)
    #print (one_ships)    # For testing only (Shows Ship locations)
    one_turn = player_turn(one_board, one_ships, one_score)
    one_board = one_turn[0]
    one_score = one_turn[1]

    if one_score == 6:    # Player one winner!
      print (player_one + " is the winner!")

      # Updates Player Records
      for item in ranks:    # Adds 1 to player_one wins
        for key in item:
          if item[key] == player_one:
            item["competitive_wins"] += 1
      for item in ranks:    # Adds 1 to player_two losses
        for key in item:
          if item[key] == player_two:
            item["competitive_losses"] += 1
      # Updates the battleship_rankings
      json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )

      break

    # Player two turn
    print (player_two + 's Turn:')
    print_board(two_board)
    #print (two_ships)    # For testing only (Shows Ship locations)
    two_turn = player_turn(two_board, two_ships, two_score)
    two_board = two_turn[0]
    two_score = two_turn[1]

    if two_score == 6:    # Player two winner!
      print (player_two + " is the winner!")

      # Updates Player Records
      for item in ranks:    # Adds 1 to player_one losses
        for key in item:
          if item[key] == player_one:
            item["competitive_losses"] += 1
      for item in ranks:    # Adds 1 to player_two wins
        for key in item:
          if item[key] == player_two:
            item["competitive_wins"] += 1
      # Updates the battleship_rankings
      json.dump( ranks, open( "battleship_rankings.json", 'w' ), indent = 2 )

      break

  play_battleship()
  

# Game introduction
def play_battleship():
  play = input ("Do you want to play battleship?\n").lower()
  time.sleep(.5)
  if play == "y" or play == "yes":
    rules()
    time.sleep(.5)
    players = input ("1 or 2 Players?\n").lower()
    time.sleep(.5)
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
