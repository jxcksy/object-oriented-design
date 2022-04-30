class Tile():

    def __init__(self, name, value, img):
        self.name = name
        self.value = value
        self.image = img
 
    def getName(self):
        return self.name
 
    def getValue(self):
        return self.value

    def getImg(self):
        return self.image
