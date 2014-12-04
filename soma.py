# A command line application for streaming soma.fm stations, written 
# in Python, and licensed under the GNU GPLv3. See LICENSE.txt for 
# more information.

# =====================================================================

# import os in order to use the os.system() command 
# import sys in order to use the sys.exit() command
# import csv in order to read the comma separated value file that 
# contains the soma.fm station listing.

import os
import sys
import csv

# Initialize a list to hold station objects after the info has
# been read from stations.csv

stationList = []

class Station:
    """A class for each soma.fm station, containing the station name, 
    description, and stream URL. It also has a method to play each
    station with the play() function. 
    """
    
    def __init__(self, stationName, description, streamURL):
        self.stationName = stationName
        self.description = description
        self.streamURL = streamURL

    def play(self):
        """Plays the selected station with mplayer"""
        os.system("mplayer --nocache --quiet " + self.streamURL)   

def stripAndLower(stringToModify):
    """Removes spaces and converts all characters to lower case"""
    lowered = stringToModify.lower()
    stripped = lowered.replace(" ", "")
    return stripped

# Read the stations.csv file and instantiate a list of 'Station' 
# objects from the station listings there. 

with open ('stations.csv', 'rb') as csvfile:
    station_reader = csv.reader(csvfile, delimiter='|')
    for stationName, description, streamURL in station_reader:
        stationList.append(Station(stationName, description, streamURL))

# List the stations along with their description in a nice, columnar format

for item in stationList:
    print "{0:23} {1}".format(item.stationName, item.description)
