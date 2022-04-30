class Square()
    __x # int
    __y # int
    __multiplier # int
 
    def __init__(x, y, multiplier) # int, int, int
        self.x = x # int
        self.y = y # int
        self.multiplier = multiplier # int
 
    def getCord(self):
        return (self.x, self.y) # tuple
 
    def getMul(self):
        return self.multiplier # int
