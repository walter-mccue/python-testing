#
#
# Testing tkinter gui
#


#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Define the size of window or frame
win.geometry("800x500")

win.title("BATTLESHIP GAME")

#Set the Menu initially
menu= StringVar()
menu.set("Do you want to play Battleship?")

#Create a dropdown Menu
drop = OptionMenu(win, menu,"Yes", "No")
drop.pack()

win.mainloop()


