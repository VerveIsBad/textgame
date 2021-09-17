import random
import player
import utils
class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.held_item = None 
        self.graphic = '?'
        self.interactable = True
        self.is_enemy = True 
        
        """
        Ideas:
        Elements
        Armor (Random chance * level / arena type)
        Status 
        """
    
    def interact(self, world, player, interact_type):
        # target.hp -= (attacker.damage - target.defense)
        '''Interacts with the enemy 
        Arguments:
            world (World): the world (this is the 3rd unintentional JoJo reference)
            player (Player): the player
            interact_type: The type of interaction. Must be a string.
        '''
        
        if interact_type == 'fighting':
            fighting = True
            print("An enemy has appeared!!")
            action = input(f'Fight or Run (You have {player.hp}) > ').lower()

        
        while fighting:
            print('(fight) Type \'help\' for fight help')                
            if action == 'fight':                
                utils.clear()
                player.fight_with(self)
                print(f'{player.hp} hp')
                
                if player.hp <= 0:
                    print("You died . . . ")
                    player.forceStop()
                    break
                elif self.hp <= 0:
                    print(f'{self.name} Has died!')
                    player.hp = player.max_hp
                print("(attack/run)")
                
                action = input('Fight back or run\n').lower()

                if action == 'attack':
                    if player.attack > self.defense:
                        self.hp -= player.attack
                        continue 
                    else:
                        print("The enemies defense is to high! Damage negated")
                        print(f"(your attack: {player.attack}, {self.name}'s defense: {self.defense}")
                        print("after attackng the enenmy, you are no longer able to escape . . . you inevitably die.")
                        player.forceStop()


                elif action == 'run':
                    if random.randint(1,9) == 1 or 6 or 9: # random chance for user to run
                        print("You ran away . . .")
                        utils.clear()
                    else:
                        print("You failed to run away...")
                        continue

            elif action == 'help':
                print('--Commands (Fight)--\nfight - Fight the enemy\nhelp - Get help')
                continue
