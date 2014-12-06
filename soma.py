# A command line application for streaming SomaFM stations, written
# in Python, and licensed under the GNU GPLv3. See LICENSE.txt for
# more information.

# =====================================================================

# import os in order to use the os.system() command
# import sys in order to use the sys.exit() command
# import csv in order to read the comma separated value file that
# contains the SomaFM station listing.

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
        os.system("mplayer --nocache --quiet " + self.streamURL + " &")

# Read the stations.csv file and instantiate a list of 'Station'
# objects from the station listings there.

with open('stations.csv', 'rb') as csvfile:
    station_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for stationName, description, streamURL in station_reader:
        stationList.append(Station(stationName, description, streamURL))

# List the stations along with their description in a nice, columnar format
# Start with a counter initialized at 1 and incremented as the listing
# progresses. This give the user a number corresponding to a station for them
# to select.

print "\n"

counter = 1

for item in stationList:
    print "{0:3} {1:23} {2}".format(counter,
                                    item.stationName, item.description)
    counter += 1

# Then we ask the user to choose what station to play.

print "\n"
print "Select station or 'q' to quit:"
selection = raw_input()

# Quit if user input is "q" or "Q"

if selection in ("q", "Q"):
    sys.exit()

# Take the user's selection and subtract one to find
# the index from the stationList of the selection.
# Store that in the stationToPlay variable.

stationToPlay = (int(selection) - 1)

# Play the selected station.

stationList[stationToPlay].play()
