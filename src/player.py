import utils
import random
import enemy
import world

class Player:
    def __init__(self, hp, max_hp, attack, defense):
        self.hp = hp
        self.max_hp = 100
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
        '''
        Fights with a given enemy
        
        Arguments:
            enemy (Enemy): The enemy to fight
        note: most of the enemy combat code is in enemy.py in the function
        interact()
        '''

        print(f'{enemy.name} attacked!\n{enemy.attack - self.defense} damage taken!\n')
        self.hp -= (enemy.attack - self.defense)

    
    
    def forceStop(self):
        quit()
             




