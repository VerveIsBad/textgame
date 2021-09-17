import utils


class Player:
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.held_item = None
        self.graphic = '\033[33m◉\033[0m'
        self.pos = {'x': 1, 'y': 1}

    def move(self, d, world):
        '''Moves the player in a specified direction

        Arguments:
            d (str): The direction to move in, must be 'up', 'down', 'left', or 'right'
            world (World): the world (nope, still not a JoJo reference, defintely not.)
        '''
        if d == 'up':
            world.move_tile(self.pos, {'x': self.pos['x'], 'y': self.pos['y'] - 1})
            self.pos['y'] -= 1
        elif d == 'down':
            world.move_tile(self.pos, {'x': self.pos['x'], 'y': self.pos['y'] + 1})
            self.pos['y'] += 1
        elif d == 'left':
            world.move_tile(self.pos, {'x': self.pos['x'] - 1, 'y': self.pos['y']})
            self.pos['x'] -= 1
        elif d == 'right':
            world.move_tile(self.pos, {'x': self.pos['x'] + 1, 'y': self.pos['y']})
            self.pos['x'] += 1

    def fight_with(self, enemy):
        '''Fights with a given enemy
        
        Arguments:
            enemy (Enemy): The enemy to fight
        '''
        print('(fight) Type \'help\' for fight help')

        while self.hp >= 0 or enemy.hp >= 0:
            utils.clear()

            print(f'(fight) HP: {self.hp}\n(fight) Enemy HP: {enemy.hp}')
            action = input('(fight) > ')
            
            if action == 'fight':
                # do fight things
                pass
            elif action == 'help':
                print('--Commands (Fight)--\nfight - Fights the enemy\nhelp - Get help')
            
            input('(fight) Press enter to continue.')
