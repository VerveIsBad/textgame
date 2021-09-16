class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp_max = hp
        self.hp = self.hp_max
        self.defense = defense
        self.attack = attack
        self.held_item = None 
        
        """
        Ideas:
        Elements
        Armor (Random chance * level / arena type)
        Status 
        """


        