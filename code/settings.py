import csv

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# read the map data from file for use in the Level.create_map()
with open('../map/map_template.csv', 'r') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    WORLD_MAP = [line for line in data]
