from player import Player
from enemy import Enemy
import enemies
player = Player(100, 1, 1)

#print(f'HP: {player.hp} / {player.hp_max}, Attack: {player.attack}, Defense: {player.defense}')

grid = []


def gen_dungeon(size,dif,type):
    pass


def commands(cmd_name):
    if cmd_name.lower() == 'stats':
        print(f'HP: {player.hp} / {player.hp_max}, Attack: {player.attack}, Defense: {player.defense}')

# Player(hp, attack, defense)
# Enemy(name, hp, attack, defense)
def main_loop():
    while True:
        pass




if __name__ == '__main__':
        
        ready = input('Are you ready to start? (Y/N)\n')
        
        if ready == 'Y':
            main_loop()

        elif ready == 'N':
            pass
        
        else:
            print('Error')
            pass
