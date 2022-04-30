from TileRack import TileRack

class Player():
 
    def __init__(self, name): # String
        self.name = name # String
        self.score = 0 # int
 
    def getScore(self):
        return self.score # int
 
    def updateScore(self, wordScore): # int
        self.score += wordScore
 
    def getName(self):
        return self.name # String

    def setName(self, name):
        self.name = name