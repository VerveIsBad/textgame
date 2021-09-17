class Tile:
    def __init__(self, graphic, interactable: bool = None):
        self.graphic = graphic

        self.interactable = False
        if interactable is not None:
            self.interactable = True

    def interact(self, world, player):
        '''Interacts with the tile

        Arguments:
            world (World): the world (nope... definitely NOT a JoJo reference)
            player (Player): the player
        '''
        pass

