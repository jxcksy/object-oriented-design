import pygame

class StartMenu():
    pygame.init()
    #Colour
    GREEN = (11, 186, 43)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (160, 160, 160)
    WIDTH, HEIGHT = 1200, 600
    #Font
    FONT = pygame.font.SysFont("comicsans", 40)
    FPS = 60

    def __init__(self):
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Scrabble")
        self.status = None
        self.code = None

        #Initialisation

        #Text
        self.input_rect1 = pygame.Rect(539,298,20,30)
        self.input_rect2 = pygame.Rect(561,298,20,30)
        self.input_rect3 = pygame.Rect(583,298,20,30)
        self.input_rect4 = pygame.Rect(605,298,20,30)
        self.input_rect5 = pygame.Rect(627,298,20,30)
        self.active1 = False
        self.active2 = False
        self.active3 = False
        self.active4 = False
        self.active5 = False
        self.user_text1 = ""
        self.user_text2 = ""
        self.user_text3 = ""
        self.user_text4 = ""
        self.user_text5 = ""
        self.colour1 = self.GREY
        self.colour2 = self.GREY
        self.colour3 = self.GREY
        self.colour4 = self.GREY
        self.colour5 = self.GREY

        #Set-up
        self.clock = pygame.time.Clock()
        self.run = True
        self.join = False

        #Images
        self.images = []
        self.images.append(pygame.image.load("../images/start_menu.png"))

    #Join game
    def join_game(self, code):
        self.status = "Client"
        self.code = code
        self.win.fill(self.GREEN)
        join_text = self.FONT.render(f"Joining Lobby: {code}", 1, self.BLACK)
        self.win.blit(join_text, (self.WIDTH//2 - join_text.get_width()//2, self.HEIGHT//2 - join_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)

    def getCode(self):
        return self.code

    def getStatus(self):
        if self.status == "Client":
            return self.status
        elif self.status == "Host":
            print("Host")
            return self.status
        else:
            return None

    #Draw buttons
    def draw(self):
        self.win.fill(self.GREEN)

        image = self.images[0]

        self.win.blit(image, (0,0))

        if self.active1:
            self.colour1 = self.BLACK
        else:
            self.colour1 = self.GREY
        if self.active2:
            self.colour2 = self.BLACK
        else:
            self.colour2 = self.GREY
        if self.active3:
            self.colour3 = self.BLACK
        else:
            self.colour3 = self.GREY
        if self.active4:
            self.colour4 = self.BLACK
        else:
            self.colour4 = self.GREY
        if self.active5:
            self.colour5 = self.BLACK
        else:
            self.colour5 = self.GREY

        pygame.draw.rect(self.win, self.colour1, self.input_rect1, 2)
        pygame.draw.rect(self.win, self.colour2, self.input_rect2, 2)
        pygame.draw.rect(self.win, self.colour3, self.input_rect3, 2)
        pygame.draw.rect(self.win, self.colour4, self.input_rect4, 2)
        pygame.draw.rect(self.win, self.colour5, self.input_rect5, 2)

        text_surface1 = self.FONT.render(self.user_text1, True, self.BLACK)
        self.win.blit(text_surface1, (self.input_rect1.x + 2, self.input_rect1.y + 2))

        text_surface2 = self.FONT.render(self.user_text2, True, self.BLACK)
        self.win.blit(text_surface2, (self.input_rect2.x + 2, self.input_rect2.y + 2))

        text_surface3 = self.FONT.render(self.user_text3, True, self.BLACK)
        self.win.blit(text_surface3, (self.input_rect3.x + 2, self.input_rect3.y + 2))

        text_surface4 = self.FONT.render(self.user_text4, True, self.BLACK)
        self.win.blit(text_surface4, (self.input_rect4.x + 2, self.input_rect4.y + 2))

        text_surface5 = self.FONT.render(self.user_text5, True, self.BLACK)
        self.win.blit(text_surface5, (self.input_rect5.x + 2, self.input_rect5.y + 2))

        pygame.display.update()

#Game Loop
    def loop(self):
        while self.run:
            self.clock.tick(self.FPS)

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if self.active1:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text1 = ""
                        else:
                            self.user_text1 = event.unicode
                    if self.active2:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text2 = ""
                        else:
                            self.user_text2 = event.unicode
                    if self.active3:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text3 = ""
                        else:
                            self.user_text3 = event.unicode
                    if self.active4:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text4 = ""
                        else:
                            self.user_text4 = event.unicode
                    if self.active5:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text5 = ""
                        else:
                            self.user_text5 = event.unicode
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    pos = (x, y)
                    print(pos)

                    if self.input_rect1.collidepoint(event.pos):
                        self.active1 = True
                    else:
                        self.active1 = False

                    if self.input_rect2.collidepoint(event.pos):
                        self.active2 = True
                    else:
                        self.active2 = False

                    if self.input_rect3.collidepoint(event.pos):
                        self.active3 = True
                    else:
                        self.active3 = False

                    if self.input_rect4.collidepoint(event.pos):
                        self.active4 = True
                    else:
                        self.active4 = False

                    if self.input_rect5.collidepoint(event.pos):
                        self.active5 = True
                    else:
                        self.active5 = False

                    #Join
                    if x > 778 and x < 836:
                        if y > 293 and y < 336:
                            if len(self.user_text1 + self.user_text2 + self.user_text3 + self.user_text4 + self.user_text5) == 5:
                                code = self.user_text1 + self.user_text2 + self.user_text3 + self.user_text4 + self.user_text5
                                self.join = True

                    #Host
                    if x > 403 and x < 736:
                        if y > 356 and y < 403:
                            self.status = "Host"
                            self.run = False

                    #Quit
                    if x > 508 and x < 635:
                        if y > 428 and y < 474:
                            self.run = False

            if self.join:
                self.join_game(code)
                break


        pygame.display.quit()

def main():
    sm = StartMenu()
    sm.loop()

if __name__ == '__main__':
    main()
