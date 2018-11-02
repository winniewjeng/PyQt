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
        # moviesJSON in the JSON instance from lab6.py

        super(UI, self).__init__(moviesJSON, parent)
        # store the input moviesJSON in a class member of the same name
        self.moviesJSON = moviesJSON
        # set the window title
        self.setWindowTitle("Python Movie Project")
        # set the status bar's message
        self.setStatusBar(QStatusBar="Status Bar")  # ? 8-(d)-4

        # 8-(d)-v
        # class member centralWidget is an instance of UI_CentralWindow
        # this instance actually feels more important that previously assumed. Is it not being used?
        self.centralWidget = UI_CentralWindow.UI_CentralWindow()

        """connect the PushButton from our central widget to a handler"""
        # 8-(d)-vi
        # not sure if this is done correctly
        self.button = UI_CentralWindow.UI_CentralWindow.enterMoviePushButton()
        self.button.clicked.connect(self.enterMoviePushButtonClicked)  # 7-(d)-vi

        # show the UI
        self.show()

    # when the enterMovie button is triggered...
    def enterMoviePushButtonClicked(self):
        # read the movieTitle from enterMovieLineEdit with text() method
        movieTitle = UI_CentralWindow.UI_CentralWindow.enterMovieLineEdit.text()  # not sure if this is correct...

        """The rest below is ambiguous"""
        # data = OpenMovie.OpenMovie(movieTitle, )
        try:
            contents = open('movies.json', 'r')
        except:
            print("Failed to open JSON file")
            logging.error(" Failed to open JSON file")
            sys.exit()

        # data is a dictionary loaded from the ”movie_posters” field of json data
        data = json.load(contents)

        """test code to print out the data dictionary of json objects """
        # print(data['movie_posters'])
        # for i in data['movie_posters']:
        #     print(i, data['movie_posters'][i])

        # check if movieTitle is in json data "movie_posters" list of keys
        for i in data['movie_posters']:
            # i the title, which is key
            if movieTitle is i:
                instance = OpenMovie.OpenMovie(i, data['movie_posters'][i])
                if instance.getPoster() is False:
                    return
                else:
                    self.centralWidget.updatePoster(instance.posterFileName)
            else:
                return

        contents.close()







