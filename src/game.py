from player import Player


player = Player()


def main_loop():
    while True:
        action = input('> ')

        if action == 'stats':
            print(f'HP: {player.hp} / {player.hp_max}, Attack: {player.attack}, Defense: {player.defense}')


if __name__ == '__main__':
    main_loop()
