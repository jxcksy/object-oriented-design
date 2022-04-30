import pygame
import math

class inGame():
    pygame.init()

    #Colour
    TILE = (251,235,165)
    GREEN = (27, 161, 83)
    BACKGROUND_GREEN = (27, 161, 83)
    DARK_GREEN = (0, 117, 31)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    LIGHT_RED = (235, 120, 120)
    RED = (255, 54, 54)
    LIGHT_BLUE = (184, 211, 255)
    BLUE = (15, 4, 222)
    WIDTH, HEIGHT = 1200, 600
    FPS = 60



    def __init__(self):
        #Initialisation
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.win.fill(self.BACKGROUND_GREEN)
        pygame.display.set_caption("MyScrabble")
        self.changes = False
        self.clock = pygame.time.Clock()

        self.tileRack = pygame.image.load("../images/TileRack.png")
        self.tileRack = pygame.transform.scale(self.tileRack, (600, 80))
        self.tileRackLeft = pygame.transform.scale(self.tileRack, (390, 60))
        self.tileRackTop = pygame.transform.scale(self.tileRack, (390, 60))
        self.tileRackRight = pygame.transform.scale(self.tileRack, (390, 60))

        self.font = pygame.font.Font('freesansbold.ttf', 22)
        self.settings_header = pygame.font.Font(None, 70)
        self.settings_font = pygame.font.Font(None, 60)
        self.run = True
        self.text = self.font.render('    ', True, self.BLACK, self.WHITE)
        self.grid = [[0 for x in range(15)] for y in range(15)]
        self.multipliers = [(0,0,1), (0,7,1), (0,1,14), (14,0,1), (0,7,1),
                       (0,3,2), (0,11,2), (2,6,2), (2,8,2), (3,0,2), (3,7,2), (3,14,2),(6,2,2), (6,6,2), (6,8,2), (6,12,2),
                       (5,1,3), (9,1,3), (1,5,3), (5,5,3), (9,5,3), (13,5,3),
                       (1,1,4), (13,1,4), (2,2,4), (12,2,4), (3,3,4), (11,3,4), (4,4,4), (10,4,4)]
        self.makeGrid()
        self.currentTiles = []
        self.playedTiles = []
        self.blocked = []
        self.history = []

        self.player1 = ("Player1", "player1")
        self.player2 = ("Player2", "player2")
        self.player3 = ("Player3", "player3")
        self.player4 = ("Player4", "player4")
        self.player2Score = 0
        self.player3Score = 0
        self.player4Score = 0

    def updateTiles(self, tiles):
        self.currentTiles = []
        for tile in tiles:
            self.currentTiles.append(tile)

    # make a grid and set the multiples
    def makeGrid(self):
        for square in self.multipliers:
            x = square[0]
            y = square[1]
            typeSqr = square[2]
            self.grid[x][y] = typeSqr
            self.grid[14-x][14-y] = typeSqr

    def redrawGameWindow(self): 
        # add tile racks to screen
        self.win.blit(self.tileRack, (302,510))
        self.win.blit(self.tileRackLeft, (0,270))
        self.win.blit(self.tileRackTop, (405,25))
        self.win.blit(self.tileRackRight, (810,270))
        pygame.draw.circle(self.win, self.DARK_GREEN, (190, 375), 30, 2)
        pygame.draw.circle(self.win, self.DARK_GREEN, (800, 50), 30, 2)
        pygame.draw.circle(self.win, self.DARK_GREEN, (1015, 375), 30, 2)
        pygame.draw.circle(self.win, self.DARK_GREEN, (325, 550), 30, 2)
        pygame.draw.rect(self.win, self.TILE, pygame.Rect(1000, 550, 110, 30))
        confirm = self.font.render("Confirm", 1, self.BLACK)
        self.win.blit(confirm, (1012,555))

        # multiple tiles added to gameboard
        for row in range(15):
            for column in range(15):
                font = pygame.font.Font('freesansbold.ttf', 22)
                text = font.render('    ', True, self.BLACK, self.WHITE)
                if self.grid[row][column] == 1:
                    font = pygame.font.Font('freesansbold.ttf', 19)
                    text = font.render('3W', True, self.WHITE, self.RED)

                if self.grid[row][column] == 2:
                    font = pygame.font.Font('freesansbold.ttf', 19)
                    text = font.render('2L', True, self.WHITE, self.LIGHT_BLUE)

                if self.grid[row][column] == 3:
                    font = pygame.font.Font('freesansbold.ttf', 19)
                    text = font.render('3L', True, self.WHITE, self.BLUE)

                if self.grid[row][column] == 4:
                    font = pygame.font.Font('freesansbold.ttf', 19)
                    text = font.render('2W', True, self.WHITE, self.LIGHT_RED)

                if self.grid[row][column] == 5:
                    font = pygame.font.Font('freesansbold.ttf', 22)
                    text = font.render('    ', True, self.GREEN, self.GREEN)

                self.win.blit(text, [(27) * column + 400, (27) * row + 100,27, 27])

        # players names added to game screen
        if self.player2[0] != "":
            player2_name = self.settings_font.render(self.player2[0] + " : " + str(self.player2Score), 1, self.BLACK)
            self.win.blit(player2_name, (80,280))

        if self.player3[0] != "":
            player3_name = self.settings_font.render(self.player3[0] + " : " + str(self.player3Score), 1, self.BLACK)
            self.win.blit(player3_name, (490,35))

        if self.player4[0] != "":
            player4_name = self.settings_font.render(self.player4[0] + " : " + str(self.player4Score), 1, self.BLACK)
            self.win.blit(player4_name, (890,280))

        # display the players tiles on the tile rack
        firstTile = 400
        for tile in self.currentTiles:
            tileImg = pygame.transform.scale(pygame.image.load(tile.getImg()), (55, 55))
            self.win.blit(tileImg, (firstTile,510))
            firstTile += 57

        # display the tiles played by all players
        for playedTile in self.playedTiles:
            tileImg = pygame.transform.scale(pygame.image.load(playedTile[0].getImg()), (30, 30))
            self.win.blit(tileImg, playedTile[1])

        pygame.display.update()
        pygame.draw.rect(self.win, self.BLACK, pygame.Rect(395, 95, 412, 410))


    def loop(self):
        prevGridVal = -1
        x, y = None, None
        self.win.fill(self.BACKGROUND_GREEN)
        while self.run:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # handle a click on the grid
                    if pos[0] >= 400 and pos[0] <= 800 and pos[1] >= 50 and pos[1] <= 500:
                        column = (pos[0] // (27)) - 15
                        row = (pos[1] // (27)) - 4

                        # check to see if a tile has been played on that grid
                        if (str(row) + str(column)) not in self.blocked:
                            #if not then highlight it
                            if prevGridVal == -1:
                                prevGridVal = self.grid[row][column]
                                x = row 
                                y = column
                                self.grid[row][column] = 5
                            # if highlighted the unhighlight
                            elif x == row and y == column:
                                self.grid[row][column] = prevGridVal
                                prevGridVal = -1
                    # if grid highlighted and player clicks tile in tile rack then add that tile to the gameboard where highlighted
                    if prevGridVal != -1 and pos[0] >= 400 and pos[0] <= 400 + (57 * len(self.currentTiles)) and pos[1] >= 510 and pos[1] <= 565:
                        self.playedTiles.append((self.currentTiles[(pos[0] - 400)//57], ((y*27) + 395, (x*27) + 95)))
                        self.grid[row][column] = prevGridVal
                        self.blocked.append(str(row) + str(column))
                        self.history.append(self.currentTiles.pop((pos[0] - 400)//57))
                        prevGridVal = -1

                    # commit play and indicate that changes are to be pushed to other players
                    if pos[0] >= 1000 and pos[0] <= 1110 and pos[1] >= 550 and pos[1] <= 580:
                        print("sending changes")
                        self.changes = True
            self.redrawGameWindow()

        pygame.display.quit()

def main():
    inG = inGame()
    inG.loop()

if __name__ == '__main__':
    main()