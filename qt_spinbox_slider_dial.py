#
#
# Testing PyQt
#

# import PyQt5 # Imports PyQt5

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, \
  QSpinBox, QDoubleSpinBox, QSlider, QDial


# Only needed for access to command line arguments
#import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("BATTLESHIP GAME")
    self.setMinimumSize(QSize(900, 600))
    

  # ###SpinBox###
  #   #QSpinBox for int or QDoubleSpinBox for float
  #   widget = QSpinBox()
  #   # Or: widget = QDoubleSpinBox()
  #   widget.setMinimum(-10)
  #   widget.setMaximum(3)
  #   # Or: widget.setRange(-10,3)
  #   widget.setPrefix("$")
  #   widget.setSuffix("c")
  #   widget.setSingleStep(3) # Or e.g. 0.5 for QDoubleSpinBox
  #   widget.valueChanged.connect(self.value_changed)
  #   widget.valueChanged[str].connect(self.value_changed_str)
  #   self.setCentralWidget(widget)

  # def value_changed(self, i): # Only shows the value (int/float)
  #   print(i)

  # def value_changed_str(self, s): # Shows the value and prefix/suffix, as a string
  #   print(s)
  # ###
    

  # ###Slider###
  #   widget = QSlider(Qt.Vertical) #widget = QSlider(Qt.Vertical or Qt.Horizontal)
  #   widget.setMinimum(-10)
  #   widget.setMaximum(3)
  #   # Or: widget.setRange(-10,3)
  #   widget.setSingleStep(3)
  #   widget.valueChanged.connect(self.value_changed)
  #   widget.sliderMoved.connect(self.slider_position)
  #   widget.sliderPressed.connect(self.slider_pressed)
  #   widget.sliderReleased.connect(self.slider_released)
  #   self.setCentralWidget(widget)

  # def value_changed(self, i):
  #   print(i)

  # def slider_position(self, p):
  #   print("position", p)

  # def slider_pressed(self):
  #   print("Pressed!")

  # def slider_released(self):
  #   print("Released")
  # ###
    

  ###QDial###
    widget = QDial()
    widget.setRange(-10, 100)
    widget.setSingleStep(1)
    widget.valueChanged.connect(self.value_changed)
    widget.sliderMoved.connect(self.slider_position)
    widget.sliderPressed.connect(self.slider_pressed)
    widget.sliderReleased.connect(self.slider_released)
    self.setCentralWidget(widget)

  def value_changed(self, i):
    print(i)

  def slider_position(self, p):
    print("position", p)

  def slider_pressed(self):
    print("Pressed!")

  def slider_released(self):
    print("Released")
  ###


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
#app = QApplication(sys.argv)
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
