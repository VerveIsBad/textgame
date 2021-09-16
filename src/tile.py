from random import randint
# https://unicode-table.com/en/
class Tile:
    def __init__(self, tile_type):
        self.tile_type = tile_type

grid = [['1','0','0'],
        ['0','2','0'],
        ['0','0','3']]


i = -1
for chr in grid:
    i += 1
    print(grid[i])


x = -1

for chr in grid:
    for j in range(len(grid[0] [])):
        # maybe???
