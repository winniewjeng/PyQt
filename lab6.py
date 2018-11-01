# import OpenMovie
import configparser
import json
import logging
import sys
import PyQt5
import UI

"""
File: Jeng_Winnie_Lab6.py

Author: Winnie Wei Jeng
Assignment: Lab 6
Professor: Phil Tracton
Date: 



"""

if __name__ == "__main__":

    try:
        config = configparser.RawConfigParser()
        # read in the "movie.cfg" file
        config.read("movies.cfg")
    except:
        print("Config fail")
        logging.error("Config fail")
        sys.exit()

    # if the configuration has a section named ”LOGGING”,
    # read the LOG_FILE field of it and store the name in log_file_name
    # else set log file name to ”default.log”
    if config.has_section('LOGGING'):
        log_file_name = config.get('LOGGING', 'log_file')

    else:
        log_file_name = "default.log"

    # create a logging basiConfig
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG,
                        format='%(asctime)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    # create a logging instance using log_file_name and log that program starts
    logging.info(" %s opens. Program starts." % log_file_name)

    # contents is a json file instance that reads ”movies.json” file and loads its data
    try:
        contents = open('movies.json', 'r')
    except:
        print("Failed to open JSON file")
        logging.error(" Failed to open JSON file")
        sys.exit()

    # app is a PyQT5 QApplication instance
    app = PyQt5.QtWidgets.QApplication(sys.argv)

    # gui is an instance of UI that takes in a json instance named contents
    gui = UI(contents)

    # start the gui
    logging.INFO(" GUI starts!")
    gui.show()
    app.exec_()
    logging.INFO(" GUI ends!")

    # log that

    """The rest below is not relevant to lab 6"""
    # data is a dictionary loaded from the ”movie posters” field
    data = json.load(contents)

    """test code to print out the data dictionary of json objects """
    # print(data['movie_posters'])
    # for i in data['movie_posters']:
    #     print(i, data['movie_posters'][i])

    # for each item in this dictionary,
    # a. create an instance of OpenMovie using the key for the title and the value for the posterURL
    # b. call the getPoster method of this instance of OpenMovie
    # c. delete this instance of OpenMovie
    for i in data['movie_posters']:
        instance = OpenMovie.OpenMovie(i, data['movie_posters'][i])
        instance.getPoster()
        del instance

    contents.close()