import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui  # !? I think I need this ?!


# 6.
class UI_MovieInfo(PyQt5.QtWidgets.QDialog):
    """
    this level holds together a few GUI elements
    that get repeated several times
    """

    def __init__(self, parent=None, title=None):
        super(UI_MovieInfo, self).__init__(parent, title)

        self.hBox = PyQt5.QtWidgets.QHBoxLayout()  # 6-(c)-iii

        self.titleLabel = PyQt5.QtWidgets.QLabel(title)  # iv
        self.titleLabelFont = PyQt5.QtGui.QFont()  # v
        self.titleLabelFont.setBold(True)  # v
        self.titleLabelFont.setFont(self.titleLabel)  # ? 6.(C)-vi--set BOLD font

        self.infoLabel = PyQt5.QtWidgets.QLabel("info")  # vii

        self.hBox.addLayout(self.titleLabel)
        self.hBox.addLayout(self.infoLabel)

    def getLayout(self):  # (d)
        return self.hBox
