class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.hp_max = hp
        self.hp = self.hp_max
        self.defense = defense
        self.attack = attack
        self.held_item = None 
        
        """
        Ideas:
        Elemnts
        Armor (Random chance * level / arena type)
        Status 
        """


        