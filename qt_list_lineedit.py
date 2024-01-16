#
#
# Testing PyQt
#

# import PyQt5 # Imports PyQt5

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, \
  QListWidget, QLineEdit

# Only needed for access to command line arguments
#import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("BATTLESHIP GAME")
    self.setMinimumSize(QSize(900, 600))
    

  ###List###
    #widget = QListWidget()
    #widget.addItems(["Single Player", "Two Players"])
    ## In QListWidget there are two separate signals for the item, and the str
    #widget.currentItemChanged.connect(self.index_changed)
    #widget.currentTextChanged.connect(self.text_changed)
    #self.setCentralWidget(widget)

  #def index_changed(self, i): # Not an index, i is a QListItem
    #print(i.text())
  #def text_changed(self, s): # s is a str
    #print(s)
  ###
    

  ###LineEdit###
    widget = QLineEdit()
    widget.setMaxLength(10)
    widget.setPlaceholderText("Enter your name")
    # widget.setReadOnly(True) # uncomment this to make readonly
    widget.returnPressed.connect(self.return_pressed)
    widget.selectionChanged.connect(self.selection_changed)
    widget.textChanged.connect(self.text_changed)
    widget.textEdited.connect(self.text_edited)
    self.setCentralWidget(widget)

  def return_pressed(self):
    print("Return pressed!")
    self.centralWidget().setText("BOOM!")

  def selection_changed(self):
    print("Selection changed")
    print(self.centralWidget().selectedText())

  def text_changed(self, s):
    print("Text changed...")
    print(s)

  def text_edited(self, s):
    print("Text edited...")
    print(s)
  ###


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

# Create a Qt widget, which will be our window.
#window = QWidget()
#window = QPushButton("Push Me")
window = MainWindow()

window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
# Your application won't reach here until you exit and the event
# loop has stopped.
