import random
import tiles


class World:
    def __init__(self, player):
        self.grid = []
        self.player = player

        for y in range(10):
            self.grid.append([])
            for x in range(10):
                if x == 0 or y == 0 or x == 9 or y == 9:
                    self.grid[y].append(tiles.wall)
                    continue

                chance = random.randint(0, 7)
                if chance <= 5:
                    self.grid[y].append(tiles.air)
                elif chance == 6:
                    self.grid[y].append(tiles.chest)
                else:
                    self.grid[y].append(tiles.flag)
                del chance

        self.grid[1][1] = player

    def print_grid(self):
        print('-\033[32m 0 1 2 3 4 5 6 7 8 9\033[0m')
        for index, _ in enumerate(self.grid):
            print('\033[32m' + str(index) + '\033[0m ', end='')
            for x in self.grid[index]:
                print(x.graphic + ' ', end='')
            print()

    def move_tile(self, at, to):
        tile_to_move = self.grid[at['y']][at['x']]
        tile_to = self.grid[to['y']][to['x']]
        self.grid[at['y']][at['x']] = tiles.air
        self.grid[to['y']][to['x']] = tile_to_move
        self.print_grid()

        if tile_to.interactable:
            tile_to.interact(self, self.player)