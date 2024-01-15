#
#
# Testing PyQt
#

# import PyQt5 # Imports PyQt5

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Only needed for access to command line arguments
# import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

  # Initializes the subclass of the QMainWindow class
  def __init__(self):
    super().__init__()
    # Title
    self.setWindowTitle("BATTLESHIP GAME")
    # window size (setFixedSize, setMaximumSize, setMinimumSize)
    self.setMinimumSize(QSize(900, 600))
    # QButton set up

    self.start_game = False
    
    button = QPushButton("Press To Start!")
    button.setCheckable(True)
    button.clicked.connect(self.button_toggled)
    button.setChecked(self.start_game) 
    # Set the central widget of the Window.
    self.setCentralWidget(button)

  # When user clicks button
  def button_toggled(self, checked):
    self.start_game = checked
    if self.start_game == True:
      print("Game Started")




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
