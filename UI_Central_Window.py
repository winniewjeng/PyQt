import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui
import UI_MovieInfo

class UI_Central_Window(PyQt5.QtWidgets.QDialog):

    """This class holds the key GUI elements"""

    def __init__(self, parent=None):
        super(UI_Central_Window, self).__init__(parent) # call super on the base class. What is base class?