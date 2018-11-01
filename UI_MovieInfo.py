import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui


class UI_MovieInfo(PyQt5.QtWidgets.QDialog):
    """
    this level holds together a few GUI elements
    that get repeated several times
    """

    def __init__(self, parent=None, title=None):
        super(UI_MovieInfo, self).__init__(parent, title) # call super on the base class. What is base class?

        titleLabel = PyQt5.QtWidgets.QLabel(title)
        titleLabelFont = PyQt5.QtGui.QFont()
        titleLabelFont.setBold(True)
        titleLabelFont.setFont(titleLabel) # ? 6.(C)-vi--set BOLD font

        infoLabel = PyQt5.QtWidgets.QLabel("info")

        hBox = PyQt5.QtWidgets.QHBoxLayout()
        hBox.addLayout(titleLabel)
        hBox.addLayout(infoLabel)

    def getLayout(self):
        return self.HBoxLayout

