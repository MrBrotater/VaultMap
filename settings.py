import csv

WIDTH = 700
HEIGHT = 700
FPS = 5
ROOMSIZE = 100

# read the map data from file for use in the Level.create_map()
# with open('../map/map_template.csv', 'r') as csv_file:
#     data = csv.reader(csv_file, delimiter=',')
#     WORLD_MAP = [line for line in data]

WORLD_MAP = [
['u', 'u', 'u', 'r', 'u', 'u', 'u'],
['u', 'u', 'r', 'r', 'r', 'u', 'u'],
['u', 'r', 'r', 'r', 'r', 'r', 'u'],
['r', 'r', 'r', 'p', 'r', 'r', 'r'],
['u', 'r', 'r', 'r', 'r', 'r', 'u'],
['u', 'u', 'r', 'r', 'r', 'u', 'u'],
['u', 'u', 'u', 'r', 'u', 'u', 'u'],
]