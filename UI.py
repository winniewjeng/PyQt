import PyQt5
import PyQt5.QtWidgets
import UI_CentralWindow
import OpenMovie
import json
import logging
import sys


# 8.
class UI(PyQt5.QtWidgets.QMainWindow):
    """
    This class contains the top level UI module that
     connects together the various top level items and signals.
    """

    def __init__(self, moviesJSON=None, parent=None):
        # self.count = 0  # check if buttons work
        # moviesJSON in the JSON instance from lab6.py
        super(UI, self).__init__(parent)  # no inheriting moviesJSON because why?

        # store the input moviesJSON in a class member of the same name
        self.moviesJSON = moviesJSON

        ## added myself--to be deleted if
        # self.movieTitle = None

        # set the window title
        self.setWindowTitle("Python Movie Project")

        # set the status bar's message
        self.statusBar().showMessage("Status Bar")  # ? 8-(d)-4

        # self.a = PyQt5.QtWidgets.QStatusBar.showMessage("StatusBar")
        # self.setStatusBar(QStatusBar=PyQt5.QtWidgets.QStatusBar.showMessage("StatusBar"))
        # self.setStatusBar(PyQt5.QtWidgets.QStatusBar.showMessage("Status Bar"))
        # self.setStatusBar(QStatusBar)  # ? 8-(d)-4

        # 8-(d)-v
        # class member centralWidget is an instance of UI_CentralWindow
        # this instance....cause the Debugger to complain...
        self.centralWidget = UI_CentralWindow.UI_CentralWindow()

        """connect the PushButton from our central widget to a handler"""
        # 8-(d)-vi
        self.centralWidget.enterMoviePushButton.clicked.connect(self.enterMoviePushButtonClicked)  # 7-(d)-vi

        # show the UI?
        self.centralWidget.show()

    # when the enterMovie button is triggered...
    def enterMoviePushButtonClicked(self):
        # read the movieTitle from enterMovieLineEdit with text() method
        # movieTitle = UI_CentralWindow.UI_CentralWindow.enterMovieLineEdit.text()  # not sure if this is correct...
        self.movieTitle = self.centralWidget.enterMovieLineEdit.text()  # not sure if this is correct...

        print(self.movieTitle)
        # print("Button click %d" % self.count)
        # print(str(self.moviesJSON))
        """The rest below is all very ambiguous"""

        try:
            contents = open('movies.json', 'r')

        except:
            print("Failed to open JSON file")
            logging.error(" Failed to open JSON file")
            sys.exit()

        # data is a dictionary loaded from the ”movie_posters” field of json data
        data = json.load(contents)

        # check if movieTitle is in json data "movie_posters" list of keys
        for i in data['movie_posters']:
            # self.count = self.count + 1
            # i is the movieTitle, which is a key
            print("self.movieTitle is {} and i is {} ".format(self.movieTitle, i))
            print(i)
            if self.movieTitle == i:
                # i is self.movieTite and data['movie_posters'][i] is URL
                instance = OpenMovie.OpenMovie(i, data['movie_posters'][i])
                print("oh hihi")
                if instance.getPoster() is False:
                    return
                else:
                    self.centralWidget.updatePoster(instance.posterFileName)
            else:
                pass

        contents.close()


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gui = UI()
    # gui.show()
    app.exec_()







