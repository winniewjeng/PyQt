import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui
import UI_MovieInfo

class UI_CentralWindow(PyQt5.QtWidgets.QDialog):

    """This class holds the key GUI elements"""

    def __init__(self, parent=None):
        super(UI_CentralWindow, self).__init__(parent) # call super on the base class

        enterMovieLabel = PyQt5.QtWidgets.QLabel("Movie to Look Up")
        enterMovieLineEdit = PyQt5.QtWidgets.QLineEdit()
        enterMoviePushButton = PyQt5.QtWidgets.QPushButton("Look Up Movie")
        posterLabel = PyQt5.QtWidgets.QLabel("Poster Goes Here")
        pixmap = PyQt5.QtGui.QPixmap() # sometimes using QtWidgets and sometimes using QtGui?
        awardsDisplay = PyQt5.QtWidgets.QTextEdit()
        awardsDisplay.setReadOnly(True)

        vBoxInfo = PyQt5.QtWidgets.QVBoxLayout()
        vbox = PyQt5.QtWidgets.QVBoxLayout()

        hBoxSearch = PyQt5.QtWidgets.QHBoxLayout()
        hBoxInfoAndPoster = PyQt5.QtWidgets.QHBoxLayout()
        hBoxInfo1 = PyQt5.QtWidgets.QHBoxLayout()
        hBoxInfo2 = PyQt5.QtWidgets.QHBoxLayout()
        hBoxInfo3 = PyQt5.QtWidgets.QHBoxLayout()
        hBoxInfo4 = PyQt5.QtWidgets.QHBoxLayout()
        hBoxInfo5 = PyQt5.QtWidgets.QHBoxLayout()

        directorInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Director:")
        actorInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Actor:")
        releaseDateInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Release Date:")
        budgetInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Budget:")
        revenueInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Revenue:")
        runTimeInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Run Time:")
        voteCountInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Vote Count:")
        voteAverageInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Vote Average:")
        statusInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Status:")
        monthlyRevenueMeanInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Monthly Revenue Mean:")
        monthlyRevenueMedianInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Monthly Revenue Median:")
        monthlyRevenueStdInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Monthly Revenue STD:")
        annualRevenueMeanInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Annual Revenue Mean:")
        annualRevenueMedianInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Annual Revenue Median:")
        annualRevenueStdInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Annual Revenue STD:")







