from montecarlo import MonteCarlo
import csv

player = MonteCarlo()

player.get_value()

names = ['Board', 'Value']
with open('map_playing_itself.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    for key,value in player.policy_map.items():
        writer.writerow([key,value])
