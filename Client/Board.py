class Board():
 
    def __init__(self):
        self.squares = [[()]]
        self.playedTiles = {}
 
    def getSquares(self):
        return self.squares # dict
 
    def getPlayedTiles(self):
        return self.playedTiles # dict
 
    def updatePlayedTiles(self, x, y, tile): # int, int, Tile()
        pass

    def updateSquares(self, x, y, squares): # int, int, []  
        pass
        
    def buildBoard():

        grid = [] 

        for i in range (15):
            grid.append([])

            for j in range(15):
                grid[i].append((None, None))
                
        return grid # list of lists of tuples
