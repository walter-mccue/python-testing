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
print ('%02d/%02d/%04d %02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute))

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
