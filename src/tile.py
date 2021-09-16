class Tile:
    def __init__(self, graphic, interactable: bool = None):
        self.graphic = graphic
        
        if interactable is not None:
            self.interactable = True
        else:
            self.interactable = False

