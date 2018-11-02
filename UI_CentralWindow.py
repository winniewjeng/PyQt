import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtGui  # !? I need this
import PyQt5.QtCore  # !? I need this
import UI_MovieInfo
import sys


# 7. no logic done here
class UI_CentralWindow(PyQt5.QtWidgets.QDialog):

    """This class holds the key GUI elements"""

    def __init__(self, parent=None):
        super(UI_CentralWindow, self).__init__(parent)  # call super on the base class

        # enterMovieLabel is a QLabel
        self.enterMovieLabel = PyQt5.QtWidgets.QLabel("Movie to Look Up")
        # entermovieLineEdit is a QLineEdit
        self.enterMovieLineEdit = PyQt5.QtWidgets.QLineEdit()
        # enterMoviePush Button is a QPushButton
        self.enterMoviePushButton = PyQt5.QtWidgets.QPushButton("Look Up Movie")

        # posterLabel is a QLabel
        self.posterLabel = PyQt5.QtWidgets.QLabel("Poster Goes Here")
        # pixmap is a class member of QPixmap
        self.pixmap = PyQt5.QtGui.QPixmap()  # using QtGui instead of QWidgets?

        # awardsDisplay is a class member of QTextEdit
        self.awardsDisplay = PyQt5.QtWidgets.QTextEdit()
        # awardsDisplay calls setReadOnly() method and evals to True
        self.awardsDisplay.setReadOnly(True)

        # vboxInfo and vbox are two VBoxes
        self.vboxInfo = PyQt5.QtWidgets.QVBoxLayout()
        self.vbox = PyQt5.QtWidgets.QVBoxLayout()

        # hboxSearch is an HBOX
        self.hboxSearch = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfoAndPoster = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo1 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo2 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo3 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo4 = PyQt5.QtWidgets.QHBoxLayout()
        self.hboxInfo5 = PyQt5.QtWidgets.QHBoxLayout()

        # create 15 UI_MovieInfo instances
        self.directorInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Director:")
        self.actorInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Actor:")
        self.releaseDateInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Release Date:")

        self.budgetInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Budget:")
        self.revenueInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Revenue:")
        self.runTimeInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Run Time:")

        self.voteCountInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Vote Count:")
        self.voteAverageInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Vote Average:")
        self.statusInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Status:")

        self.monthlyRevenueMeanInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Monthly Revenue Mean:")
        self.monthlyRevenueMedianInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Monthly Revenue Median:")
        self.monthlyRevenueStdInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Monthly Revenue STD:")

        self.annualRevenueMeanInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Annual Revenue Mean:")
        self.annualRevenueMedianInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Annual Revenue Median:")
        self.annualRevenueStdInformation = UI_MovieInfo.UI_MovieInfo(self.parent, "Annual Revenue STD:")

        # add to hboxSearch, using addWidget() method, the three QMethods we declared at the top of the class:
        #  a label, a line edit, and a button
        self.hboxSearch.addWidget(self.enterMovieLabel, self.enterMovieLineEdit, self.enterMoviePushButton)

        # ? 7.(C)-xv
        # add to hboxInfo1, using getLayout() method, three of the 15 UI_Movie instances
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo1.addLayout(self.directorInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo1.addLayout(self.actorInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo1.addLayout(self.releaseDateInformation))

        # likewise, add to hboxInfo2
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo2.addLayout(self.budgetInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo2.addLayout(self.revenueInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo2.addLayout(self.runTimeInformation))

        # likewise, add to hboxInfo3
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo3.addLayout(self.voteCountInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo3.addLayout(self.voteAverageInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo3.addLayout(self.statusInformation))

        # likewise, add to hboxInfo4
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo4.addLayout(self.monthlyRevenueMeanInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo4.addLayout(self.monthlyRevenueMedianInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo4.addLayout(self.monthlyRevenueStdInformation))

        # likewise, add to hboxInfo5
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo5.addLayout(self.annualRevenueMeanInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo5.addLayout(self.annualRevenueMedianInformation))
        UI_MovieInfo.UI_MovieInfo.getLayout(self.hboxInfo5.addLayout(self.annualRevenueStdInformation))

        # for vboxInfo, use addLayout() method to add in hboxInfo 1-5
        self.vboxInfo.addLayout(self.hboxInfo1)
        self.vboxInfo.addLayout(self.hboxInfo2)
        self.vboxInfo.addLayout(self.hboxInfo3)
        self.vboxInfo.addLayout(self.hboxInfo4)
        self.vboxInfo.addLayout(self.hboxInfo5)

        # for hboxInfoAndPoster, addWidget for posterLabel and awardsDisplay
        self.hboxInfoAndPoster.addWidget(self.posterLabel)
        self.hboxInfoAndPoster.addWidget(self.awardsDisplay)

        # 7-(c)-xxii
        # for hboxInfoAndPoster, add in vboxInfo using addLayout() method
        self.hboxInfoAndPoster.addLayout(self.vboxInfo)

        # for vbox, add in hboxSearch and hboxInfoAndPoster using addLayout() method
        self.vbox.addLayout(self.hboxSearch)
        self.vbox.addLayout(self.hboxInfoAndPoster)

        # setLayout to vbox
        self.setLayout(self.vbox)

    # 7-(d)
    def updatePoster(self, posterFileName=None):
        """This moethod loads the specified poster name into the GUI"""
        # load the posterFileName instance into pixmap
        self.pixmap.load(posterFileName)  # ? 7-(d)-i
        # scaled the pixmap image via scaled() method using posterLabel size and KeepAspectRatio
        self.pixmap.scaled(self.posterLabel.width(), self.posterLabel.height(), PyQt5.QtCore.Qt.KeepAspectRatio)
        # call setPixmap of the posterLabel with pixmap
        self.posterLabel.setPixmap(self.pixmap) # what does it even mean dude?
        # for posterLabel, set scaled content to false
        self.posterLabel.setScaledContents(False)


