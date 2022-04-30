class TileRack():

    def __init__(self):
        self.tiles = []
        self.numTiles = 0
 
    def getAllTiles(self):
        return self.tiles
 
    def getNumTiles(self):
        return self.numTiles
 
    def addTile(self, tile):
        self.tiles.append(tile)
        self.numTiles += 1

    def removeTile(self, tile):
        self.tiles.remove(tile)
        self.numTiles -= 1

