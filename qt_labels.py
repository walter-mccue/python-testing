#
#
# Testing PyQt
#

# import PyQt5 # Imports PyQt5

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Only needed for access to command line arguments
#import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("BATTLESHIP GAME")
    self.setMinimumSize(QSize(900, 600))

    # Label set up
    widget = QLabel("Hello")

    font = widget.font() # font sizing
    font.setPointSize(16)
    widget.setFont(font)

    #widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Alignment
    widget.setAlignment(Qt.AlignCenter)
    
    self.setCentralWidget(widget)


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
