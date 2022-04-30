import random
from Tile import Tile

class TileBag():

    def __init__(self):
        self.count = 255
        self.tiles = {"A": {"Value": 1,
                            "NoOfTiles": 9,
                            "imageName": "../images/a.png"},
                      "B": {"Value": 3,
                            "NoOfTiles": 2,
                            "imageName": "../images/b.png"},
                      "C": {"Value": 3,
                            "NoOfTiles": 2,
                            "imageName": "../images/c.png"},
                      "D": {"Value": 2,
                            "NoOfTiles": 4,
                            "imageName": "../images/d.png"},
                      "E": {"Value": 1,
                            "NoOfTiles": 12,
                            "imageName": "../images/e.png"},
                      "F": {"Value": 4,
                            "NoOfTiles": 2,
                            "imageName": "../images/f.png"},
                      "G": {"Value": 2,
                            "NoOfTiles": 3,
                            "imageName": "../images/g.png"},
                      "H": {"Value": 4,
                            "NoOfTiles": 2,
                            "imageName": "../images/h.png"},
                      "I": {"Value": 1,
                            "NoOfTiles": 9,
                            "imageName": "../images/i.png"},
                      "J": {"Value": 8,
                            "NoOfTiles": 1,
                            "imageName": "../images/j.png"},
                      "K": {"Value": 5,
                            "NoOfTiles": 1,
                            "imageName": "../images/k.png"},
                      "L": {"Value": 1,
                            "NoOfTiles": 4,
                            "imageName": "../images/l.png"},
                      "M": {"Value": 3,
                            "NoOfTiles": 2,
                            "imageName": "../images/m.png"},
                      "N": {"Value": 1,
                            "NoOfTiles": 6,
                            "imageName": "../images/n.png"},
                      "O": {"Value": 1,
                            "NoOfTiles": 8,
                            "imageName": "../images/o.png"},
                      "P": {"Value": 3,
                            "NoOfTiles": 2,
                            "imageName": "../images/p.png"},
                      "Q": {"Value": 10,
                            "NoOfTiles": 1,
                            "imageName": "../images/q.png"},
                      "R": {"Value": 1,
                            "NoOfTiles": 6,
                            "imageName": "../images/r.png"},
                      "S": {"Value": 1,
                            "NoOfTiles": 4,
                            "imageName": "../images/s.png"},
                      "T": {"Value": 1,
                            "NoOfTiles": 6,
                            "imageName": "../images/t.png"},
                      "U": {"Value": 1,
                            "NoOfTiles": 4,
                            "imageName": "../images/u.png"},
                      "V": {"Value": 4,
                            "NoOfTiles": 2,
                            "imageName": "../images/v.png"},
                      "W": {"Value": 4,
                            "NoOfTiles": 2,
                            "imageName": "../images/w.png"},
                      "X": {"Value": 8,
                            "NoOfTiles": 1,
                            "imageName": "../images/x.png"},
                      "Y": {"Value": 4,
                            "NoOfTiles": 2,
                            "imageName": "../images/y.png"},
                      "Z": {"Value": 10,
                            "NoOfTiles": 1,
                            "imageName": "../images/z.png"},
                      " ": {"Value": 0,
                            "NoOfTiles": 2,
                            "imageName": "../images/a.png"},}

    def getCount(self):
        return self.count
 
    def getRandomTile(self):
        assert self.count >= 1
        self.count -= 1
        # randomly get a key from the dictionary
        key = random.choice(list(self.tiles))
        self.tiles[key]["NoOfTiles"] -= 1
        # delete the key if no more remain
        tile = (key, self.tiles[key]["Value"], self.tiles[key]["imageName"])
        if self.tiles[key]["NoOfTiles"] == 0:
            del self.tiles[key]
        return tile 

def main():
    tile = TileBag()
    print(tile.getRandomTile())

if __name__ == '__main__':
    main()
    