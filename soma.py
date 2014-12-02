# A command line application for streaming soma.fm stations, written 
# in Python, and licensed under the GNU GPLv3. See LICENSE.txt for 
# more information.
#
# Currently, the program simply lists the soma.fm stations and asks 
# which the user would like to play. A fairly simple interface. 
# Eventually, I would like to use a curses interface, or possibly 
# urwid, for a more attractive UI and interactvity.

# =====================================================================

# import os so we can use the os.system() command 
# import sys so we can use the sys.exit() command

import os
import sys

# List of soma.fm stations

stations = [("1",
             "BAGeL Radio",
             "What alternative rock radio should sound like.",
             "http://xstream1.somafm.com:9090"),
            ("2",
             "Beat Blender",
             "A late night blend of deep-house and downtempo chill.",
             "http://xstream1.somafm.com:8388"),
            ("3",
             "Black Rock FM",
             "From the Playa to the world, for the 2014 Burning Man festival.",
             "http://xstream1.somafm.com:8040"),
            ("4",
             "Boot Liquor",
             "Americana Roots music for Cowhands, Cowpokes and Cowtippers.",
             "http://xstream1.somafm.com:7000"),
            ("5",
             "Christmas Lounge",
             "Chilled holiday grooves and classic winter lounge tracks. (Kid and Parent safe!)",
             "http://uwstream2.somafm.com:8000"),
            ("6",
             "Christmas Rocks!",
             "Have your self an indie/alternative holiday season!",
             "http://xstream1.somafm.com:6100"),
            ("7",
             "cliqhop idm",
             "Blips'n'beeps backed mostly w/beats. Intelligent Dance Music.",
             "http://xstream1.somafm.com:8062"),
            ("8",
             "Covers",
             "Just covers. Songs you know by artists you don't. We've got you covered.",
             "http://xstream1.somafm.com:8700"),
            ("9",
             "DEF CON Radio",
             "Music for Hacking. The DEF CON Year-Round Channel.",
             "http://xstream1.somafm.com:6200"),
            ("10",
             "Deep Space One",
             "Deep ambient electronic, experimental and space music. A soundtrack for inner and outer space exploration.",
             "http://xstream1.somafm.com:2800"),
            ("11",
             "Digitalis",
             "Digitally affected analog rock to calm the agitated heart.",
             "http://xstream1.somafm.com:8900"),
            ("12",
             "Doomed",
             "Dark industrial/ambient music for tortured souls.",
             "http://xstream1.somafm.com:8300"),
            ("13",
             "Drone Zone",
             "Served best chilled, safe with most medications. Atmospheric textures with minimal beats.",
             "http://uwstream2.somafm.com:80"),
            ("14",
             "Dub Step Beyond",
             "Dubstep, Dub and Deep Bass. May damage speakers at high volume.",
             "http://uwstream2.somafm.com:8400"),
            ("15",
             "Earwaves",
             "Spanning the history of electronic and experimental music from the early pioneers to the latest innovators.",
             "http://xstream1.somafm.com:5100"),
            ("16",
             "Folk Forward",
             "Indie Folk, Alt-folk and the occasional folk classics.",
             "http://xstream1.somafm.com:7400"),
            ("17",
             "Groove Salad",
             "A nicely chilled plate of ambient/downtempo beats and grooves.",
             "http://uwstream1.somafm.com:80"),
            ("18",
             "Iceland Airwaves",
             "Music from bands who will be performing at Iceland Airwaves [explicit]",
             "http://uwstream2.somafm.com:5400"),
            ("19",
             "Illinois Street Lounge",
             "Classic bachelor pad, playful exotica and vintage music of tomorrow.",
             "http://xstream1.somafm.com:8500"),
            ("20",
             "Indie Pop Rocks!",
             "New and classic favorite indie pop tracks.",
             "http://xstream1.somafm.com:8090"),
            ("21",
             "Lush",
             "Sensuous and mellow vocals, mostly female, with an electronic influence.",
             "http://xstream1.somafm.com:8800"),
            ("22",
             "Mission Control",
             "Celebrating NASA and Space Explorers everywhere.",
             "http://xstream1.somafm.com:2020"),
            ("23",
             "PopTron",
             "Electropop and indie dance rock with sparkle and pop.",
             "http://xstream1.somafm.com:2200"),
            ("24",
             "SF 10-33",
             "Ambient music mixed with the sounds of San Francisco public safety radio traffic.",
             "http://uwstream2.somafm.com:2040"),
            ("25",
             "Secret Agent",
             "The soundtrack for your stylish, mysterious, dangerous life. For Spies and PIs too!",
             "http://xstream1.somafm.com:8002"),
            ("26",
             "Seven Inch Soul",
             "Vintage soul tracks from the original 45 RPM vinyl.",
             "http://uwstream2.somafm.com:7770"),
            ("27",
             "Sonic Universe",
             "Transcending the world of jazz with eclectic, avant-garde takes on tradition.",
             "http://uwstream2.somafm.com:8604"),
            ("28",
             "South by Soma",
             "Music from bands who will be performing at SXSW, one of the biggest and best music festivals in the world. [explicit]",
             "http://uwstream2.somafm.com:5500"),
            ("29",
             "Space Station Soma",
             "Tune in, turn on, space out. Spaced-out ambient and mid-tempo electronica.",
             "http://xstream1.somafm.com:8000"),
            ("30",
             "Suburbs of Goa",
             "Desi-influenced Asian world beats and beyond.",
             "http://xstream1.somafm.com:8850"),
            ("31",
             "The Trip",
             "Progressive house / trance. Tip top tunes.",
             "http://xstream1.somafm.com:2504"),
            ("32",
             "Underground 80s",
             "Early 80s UK Synthpop and a bit of New Wave.",
             "http://xstream1.somafm.com:8884"),
            ("33",
             "Xmas in Frisko",
             "SomaFM's wacky and eclectic holiday mix. Not for the easily offended.",
             "http://xstream1.somafm.com:2100")]


def list_stations():
    """ Outputs a nicely formatted list of stations from the 
    stations[] list. Three colums with number, name of station,
    and description.
    """
    print "\n"
    for number, station, description, streamURL in stations:
        print "{0:3} {1:23} {2}".format(number, station, description)


def play_station(streamURL):
    """Plays the selected station with mplayer"""
    os.system("mplayer --nocache --quiet " + streamURL)

# First we display the list of stations to the user.

list_stations()

# Then we ask the user to choose what station to play.

print "\n"
print "Select station or 'q' to quit:"
selection = raw_input()

# Quit if user input is "q" or "Q"

if selection in ("q", "Q"):
    sys.exit()

# Take the user's selection and grab the streamURL from the stations[] list
# and store it in the station_to_play variable. 

station_to_play = [streamURL for (number, station, description, streamURL) in stations if selection == number]

# Play the selected station.

play_station(station_to_play[0])
