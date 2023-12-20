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
city = input('Which city are you traveling to?\nCharlotte\nTampa\nPittsburgh\nor Los Angeles\n').capitalize()
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
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
print ('Your trip total to ' + city + ' is: ' + str(trip_cost(city, days, spending_money)))
