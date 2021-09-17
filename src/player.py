class Player:
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.held_item = None
        self.graphic = '\033[33m◉\033[0m'
        self.pos = {'x': 1, 'y': 1}

    def move(self, d, world):
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

