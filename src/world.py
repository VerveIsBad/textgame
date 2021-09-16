import random
import tiles


generate_tiles = (
    tiles.wall,
    tiles.chest
)


class World:
    def __init__(self):
        self.grid = []

        for y in range(10):
            self.grid.append([])
            for _ in range(10):
                self.grid[y].append(random.choice(generate_tiles))
    
    def print_grid(self):
        print('-\033[32m 0 1 2 3 4 5 6 7 8 9\033[0m')
        for index, _ in enumerate(self.grid):
            print('\033[32m' + str(index) + '\033[0m ', end='')
            for x in self.grid[index]:
                print(x.graphic + ' ', end='')
            print()