from player import Player
from enemy import Enemy
from world import World


# variables
player = Player(100, 1, 1)
world = World(player)
print('Type \'help\' for help.')


# functions
def execute_command(command):
    '''Executes a command

    Arguments:
        command (str): The command to execute
    '''
    command = command.lower()

    if command == 'stats':
        print(f'--Player Stats--\nHP: {player.hp}\nAttack: {player.attack}\nDefense: {player.defense}')
    elif command == 'w':
        player.move('up', world)
    elif command == 's':
        player.move('down', world)
    elif command == 'a':
        player.move('left', world)
    elif command == 'd':
        player.move('right', world)
    elif command == 'help':
        print('--Commands--\nstats - Prints player stats\nw - Moves the player up\ns - Moves the player down\na - Moves the player left\nd - Moves the player right\nhelp - Prints help')
    elif command == 'exit':
        print('--Exiting--')
        exit()
    elif command == 'quit':
        print('--Quiting')
        quit()



# mainloop
def main_loop():
    '''Looooooooooooooooooooooooooop
    '''
    world.print_grid()
    while True:
        action = input('> ')
        execute_command(action)


# main
if __name__ == '__main__':
    main_loop()
