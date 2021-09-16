from player import Player
from enemy import Enemy
from world import World
import enemies


player = Player(100, 1, 1)
world = World()
world.print_grid()


def commands(cmd_name):
    if cmd_name.lower() == 'stats':
        print(f'HP: {player.hp} / {player.hp_max}, Attack: {player.attack}, Defense: {player.defense}')


def main_loop():
    pass


if __name__ == '__main__':
    main_loop()
