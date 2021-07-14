import json

from pitch import Pitch
from functions import *
from whoscored_scraper import *

"""
if__main__ then run
look at using csv file
matchCentreData!!! has all events (tag) line 1449/1350 and look at player id. PassEndX and PassEndY
pass map on top of heatmap
enter link to match
enter player name
enter 0 for only completed passes, 1 for only incomplete passes, 2 for both completed and incomplete passes, 3 for complted carries
enter 0 if you don't want a heatmap, 1 if you want a heatmap overlayed
download as img with name of what it is on top
use pass reception coordinates and pass coordinates to calculate carries
pass network
"""
pitch = Pitch()

player = input("Enter player name: ")
map_option = input("0: Completed passes" + "\n" "1: Incompleted passes" + "\n" + "2: Both completed and incompleted passes" + "\n" + "3. Completed carries" + "\n")
heatmap_option = input("0: No heatmap" + "\n" "1: Heatmap" + "\n")

# if selection == False then loop with message please use valid parameters"
# selection = False if player not chosen or invalid and if numbers arent chosen for heatmap/mapping or if numbers are out of range
# make diff error for each one using logger

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
    elif map_option == "3":
        carries = player_carry_data(events, player_id)
        add_carries(pitch, carries)

    if heatmap_option == "1":
        add_heatmap(pitch, x_array, y_array)

    pitch.show()
except Exception as e:
    print(e)