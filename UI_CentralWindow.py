import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import UI_MovieInfo

class UI_CentralWindow(PyQt5.QtWidgets.QDialog):

    """This class holds the key GUI elements"""

    def __init__(self, parent=None):
        super(UI_CentralWindow, self).__init__(parent) # call super on the base class

        enterMovieLabel = PyQt5.QtWidgets.QLabel("Movie to Look Up")
        enterMovieLineEdit = PyQt5.QtWidgets.QLineEdit()
        enterMoviePushButton = PyQt5.QtWidgets.QPushButton("Look Up Movie")
        self.posterLabel = PyQt5.QtWidgets.QLabel("Poster Goes Here")
        self.pixmap = PyQt5.QtGui.QPixmap() # sometimes using QtWidgets and sometimes using QtGui?
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

        hBoxSearch.addWidget(enterMovieLabel, enterMovieLineEdit, enterMoviePushButton)
        # ? 7.(C)-xv
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo1.addLayout(directorInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo1.addLayout(actorInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo1.addLayout(releaseDateInformation))

        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo2.addLayout(budgetInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo2.addLayout(revenueInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo2.addLayout(runTimeInformation))

        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo3.addLayout(voteCountInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo3.addLayout(voteAverageInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo3.addLayout(statusInformation))

        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo4.addLayout(monthlyRevenueMeanInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo4.addLayout(monthlyRevenueMedianInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo4.addLayout(monthlyRevenueStdInformation))

        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo5.addLayout(annualRevenueMeanInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo5.addLayout(annualRevenueMedianInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(hBoxInfo5.addLayout(annualRevenueStdInformation))

        hBoxInfoAndPoster.addWidget(self.posterLabel, awardsDisplay)

        vBoxInfo.addLayout(hBoxInfo1)
        vBoxInfo.addLayout(hBoxInfo2)
        vBoxInfo.addLayout(hBoxInfo3)
        vBoxInfo.addLayout(hBoxInfo4)
        vBoxInfo.addLayout(hBoxInfo5)

        hBoxInfoAndPoster.addLayout(vBoxInfo)
        vbox.addLayout(hBoxSearch, hBoxInfoAndPoster)

        self.setLayout(vbox)



    def updatePoster(self, posterFileName=None):

        self.pixmap.load(posterFileName)  # ? 7-(d)-i
        self.pixmap.scaled(self.posterLabel.width(), self.posterLabel.height(), PyQt5.QtCore.Qt.KeepAspectRatio)
        self.posterLabel.setPixmap(self.pixmap)
        self.posterLabel.setScaledContents(False)




