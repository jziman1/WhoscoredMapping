import json

from pitch import Pitch
from functions import *
from whoscored_scraper import *

"""
TODO
if__main__ then run
logger
look at using csv file
pass map on top of heatmap
enter link to match
download as img with name of what it is on top
use pass reception coordinates and pass coordinates to calculate carries
pass network
if selection == False then loop with message please use valid parameters"
selection = False if player not chosen or invalid and if numbers arent chosen for heatmap/mapping or if numbers are out of range
make diff error for each one using logger
fix imports
comments for functions
put name and signiture at top of files amnd give credit to socplot/statsbomb for pitch.py
"""
pitch = Pitch()

player = input("Enter player name: ")
print("\n")
map_option = input("0: Completed passes" + "\n" "1: Incompleted passes" + "\n" + "2: Both completed and incompleted passes" + "\n")
print("\n")
heatmap_option = input("0: No heatmap" + "\n" "1: Heatmap" + "\n")

try:
    ids, events = get_data('https://www.whoscored.com/Matches/1485551/Live/England-Premier-League-2020-2021-Arsenal-Brighton')
    
    for key, value in ids.items():
        if player in value:
            player_id = key

    if map_option == "0":
        passes = player_pass_data(events, player_id)
        add_completed_passes(pitch, passes)
    elif map_option == "1":
        passes = player_pass_data(events, player_id)
        add_incompleted_passes(pitch, passes)
    elif map_option == "2":
        passes = player_pass_data(events, player_id)
        add_completed_passes(pitch, passes)
        add_incompleted_passes(pitch, passes)

    if heatmap_option == "1":
        add_heatmap(pitch, x_array, y_array)

    pitch.show()
except Exception as e:
    print(e)