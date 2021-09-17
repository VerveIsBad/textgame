import tile


class Chest(tile.Tile):
	def interact(self, world, player):
		print('Opening chest...')


wall = tile.Tile('▢')
flag = tile.Tile('⚐')
air = tile.Tile(' ')
chest = Chest('=', interactable = True)
