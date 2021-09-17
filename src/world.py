import random
import tiles
import enemies

class World:
    def __init__(self, player):
        self.grid = []
        self.player = player

        # y-axis for loop
        for y in range(10):
            self.grid.append([])

            # x-axis for loop
            for x in range(10):
                # adds walls if the x or y is 0 or 9, makes a wall border
                if x == 0 or y == 0 or x == 9 or y == 9:
                    self.grid[y].append(tiles.wall)
                    continue

                # generate the tile to add and add it
                chance = random.randint(0, 8)
                if chance <= 5:
                    self.grid[y].append(tiles.air)
                elif chance == 6:
                    self.grid[y].append(tiles.chest)
                elif chance == 7:
                    self.grid[y].append(enemies.get_random_enemy())
                else:
                    self.grid[y].append(tiles.flag)
                del chance

        self.grid[1][1] = player

    def print_grid(self):
        '''Prints the grid in a pretty fashion
        '''
        print('-\033[32m 0 1 2 3 4 5 6 7 8 9\033[0m')
        for index, _ in enumerate(self.grid):
            print('\033[32m' + str(index) + '\033[0m ', end='')
            for x in self.grid[index]:
                print(x.graphic + ' ', end='')
            print()

    def move_tile(self, at, to):
        '''Moves a given tile and sets the old tile to air.

        Arguments:
            at (dict): the tile to move (Must contain an 'x' and a 'y' value)
            to (dict): the position to move that tile to (Must contain an 'x' and a 'y' value)
        '''
        tile_to_move = self.grid[at['y']][at['x']]
        tile_to = self.grid[to['y']][to['x']]
        self.grid[at['y']][at['x']] = tiles.air
        self.grid[to['y']][to['x']] = tile_to_move

        if tile_to.is_enemy:
            tile_to.interact(self, self.player, 'fighting')
        else:
            tile_to.interact(self, self.player)