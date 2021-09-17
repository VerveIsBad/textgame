class Tile:
    def __init__(self, graphic, interactable: bool = None):
        self.graphic = graphic

        self.interactable = False
        if interactable is not None:
            self.interactable = True

    def interact(self, world, player):
        pass

