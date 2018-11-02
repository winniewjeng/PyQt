import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui  # !? I think I need this ?!
import sys

# 6
class UI_MovieInfo(PyQt5.QtWidgets.QDialog):
    """
    this level holds together a few GUI elements that get repeated several times
    """

    def __init__(self, parent=None, title=None):

        super(UI_MovieInfo, self).__init__(parent)

        self.title = title
        self.hBox = PyQt5.QtWidgets.QHBoxLayout()  # 6-(c)-iii

        self.titleLabel = PyQt5.QtWidgets.QLabel(self.title)  # iv
        self.titleLabelFont = PyQt5.QtGui.QFont()  # v
        self.titleLabelFont.setBold(True)  # v
        self.titleLabel.setFont(self.titleLabelFont)  # ? 6.(C)-vi--set BOLD font
        # self.titleLabelFont.setFont(self.titleLabel)

        self.infoLabel = PyQt5.QtWidgets.QLabel("info")  # vii

        self.hBox.addWidget(self.infoLabel)
        # self.hBox.addLayout(self.titleLabel)
        self.hBox.addWidget(self.titleLabel)
        # self.hBox.addLayout(self.infoLabel)

    def getLayout(self):  # (d)
        return self.hBox


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gui = UI_MovieInfo()
    gui.show()
    app.exec_()
