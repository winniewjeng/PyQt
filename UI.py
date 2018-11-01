import PyQt5
import PyQt5.QtWidgets
import UI_CentralWindow
import OpenMovie

class UI(PyQt5.QtWidgets.QMainWindow):
    """
    This class contains the top level UI module that
     connects together the various top level items and signals.
    """

    def __init__(self, moviesJSON=None, parent=None):
        super(UI, self).__init__(moviesJSON, parent)
        self.moviesJSON = moviesJSON
        self.setWindowTitle("Python Movie Project")
        self.setStatusBar(QStatusBar="Status Bar") # ? 8-(d)-4
        self.centralWidget = UI_CentralWindow.UI_CentralWindow()

        """connect the PushButton from our central widget to a handler"""






