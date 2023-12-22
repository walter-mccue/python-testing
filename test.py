#
#
#time and date methods
#
from datetime import datetime
now = datetime.now()
print (now)
print (now.date())
print ('%02d/%02d/%04d' % (now.month, now.day, now.year))
print (now.time())
print ('%02d:%02d' % (now.hour, now.minute))
print ('%02d/%02d/%04d %02d:%02d' % 
       (now.month, now.day, now.year, now.hour, now.minute))

#
#
#    Pig Latin
#
#Will be appended to the end of the new word
pyg = 'ay'
#original word supplied from the user
original = input('Enter a word: ')
#if the original word has at least 1 letter and is only letters
if len(original) > 0 and original.isalpha():
  #sets the word to lowercase
  word = original.lower()
  #captures first letter of the word
  first = word[0]
  #adds the first letter and 'ay' to the end of the word
  new_word = word + first + pyg
  #removes the first letter of the word
  new_word = new_word[1:len(new_word)]
  #tells the user what their word is in pig latin
  print ('Original Word: ' + original.lower())
  print ('Word in Pig Latin: ' + new_word)
else:
  print ('Please enter only letter characters')

#
#
#    Trip Calculator
#
#user input
days = int(input('How many days are you staying?\n'))
nights = int(days) - 1
city = input('Which city are you traveling to?\
             \nCharlotte\
             \nTampa\
             \nPittsburgh\
             \nor Los Angeles\n').capitalize()
spending_money = int(input('How much spending money do you want to allocate to the trip?\n'))

def hotel_cost(nights): #hotel cost
  return 140 * nights
print ('Hotel cost: ' + str(hotel_cost(nights)))

def plane_ride_cost(city): #plane cost
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  else:
    print('Not a valid city.')
    return 0
print ('Plane cost: ' + str(plane_ride_cost(city)))

def rental_car_cost(days): #rental car cost
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
print ('Rental car cost: ' + str(rental_car_cost(days)))

print ('Spending money: ' + str(spending_money))

def trip_cost(city, days, spending_money): #total trip cost
  return rental_car_cost(days) + hotel_cost(days - 1) + \
    plane_ride_cost(city) + spending_money
print ('Your trip total to ' + city + ' is: ' + \
       str(trip_cost(city, days, spending_money)))

#
#
#   Shopping calculator
#
shopping_list = ["banana", "orange", "apple"] #list of shopping items

stock = {    #dictionary of available stock
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {    #dictionary of prices
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

#function to compute a customers bill
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:   #item must be in stock
      stock[item] -= 1    #removes 1 item from stock
      total += prices[item]      #adds the price of that item to the bill
  return total
print (compute_bill(shopping_list))

#
#
#   Gradebook
#
lloyd = {   #student 1
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {    #student 2
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {     #student 3
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):    #function to get average scores
  total = sum(numbers)
  total = float(total)
  total = total / len(numbers)
  return total

def get_average(student):    #function to determine total weighted average score
  homework = average(student["homework"]) * .1
  quizzes = average(student["quizzes"]) * .3
  tests = average(student["tests"]) * .6
  score =  homework + quizzes + tests
  return score

def get_letter_grade(score):    #function to assign a letter grade
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

#print (get_letter_grade(get_average(lloyd)))

def get_class_average(class_list):    #function to get the average off all students in the class
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)

students = [alice, lloyd, tyler]    #stores students in a list

print (get_class_average(students))    #prints total class average
print (get_letter_grade(get_class_average(students)))    #prints class score as a letter grade


