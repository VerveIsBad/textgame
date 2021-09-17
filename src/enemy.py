class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.held_item = None 
        self.graphic = '?'
        self.interactable = True
        
        """
        Ideas:
        Elements
        Armor (Random chance * level / arena type)
        Status 
        """
    
    def interact(self, world, player):
        '''Interacts with the enemy (Starts a fight)
        
        Arguments:
            world (World): the world (this is the 3rd unintentional JoJo reference)
            player (Player): the player
        '''
        player.fight_with(self)


        