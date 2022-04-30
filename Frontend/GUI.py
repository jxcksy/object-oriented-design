import pygame
import math
pygame.init()

class HostLobby():

    #Colour
    GREEN = (11, 186, 43)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (160, 160, 160)

    #Font
    FONT = pygame.font.SysFont("comicsans", 40)
    settings_header = pygame.font.Font(None, 70)
    settings_font = pygame.font.Font(None, 60)

    WIDTH, HEIGHT = 1200, 600
    FPS = 60

    def __init__(self):
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Scrabble")
        self.code = None
        self.num_players = 2

        #Text
        self.input_rect = pygame.Rect(0,125,354,80)
        self.time_hr_rect = pygame.Rect(205, 221,50,40)
        self.time_min_rect = pygame.Rect(275, 221,50,40)
        self.rect_1 = pygame.Rect(190, 304, 38, 38)
        self.rect_2 = pygame.Rect(244, 304, 38, 38)
        self.rect_3 = pygame.Rect(300, 304, 38, 38)
        self.active_hr = False
        self.active_min = False
        self.time_hr = "00"
        self.time_min = "00"
        self.colour_hr = self.GREY
        self.colour_min = self.GREY
        self.colour1 = self.GREY
        self.colour2 = self.GREY
        self.colour3 = self.GREY
        self.active1 = True
        self.active2 = False
        self.active3 = False
        self.width1 = 2
        self.width2 = 2
        self.width3 = 2

        self.player1 = "Player 1"
        self.player2 = "Player 2"
        self.player3 = "Player 3"
        self.player4 = "Player 4"
        self.active_p1 = False
        self.active_p2 = False
        self.active_p3 = False
        self.active_p4 = False
        self.colour_p1 = self.BLACK
        self.colour_p2 = self.BLACK
        self.colour_p3 = self.BLACK
        self.colour_p4 = self.BLACK

        #Set-up
        self.clock = pygame.time.Clock()
        self.run = True
        self.start = False

        #Images
        self.images = []
        self.images.append(pygame.image.load("../images/host_lobby.png"))

    def get_time(self):
        return (self.time_hr, self.time_min)

    def get_num_players(self):
        return self.num_players

    def set_code(self, code):
        self.code = code

    def start_game(self):
        self.win.fill(self.GREEN)
        start_text = self.FONT.render("Starting Game...", 1, self.BLACK)
        self.win.blit(start_text, (self.WIDTH//2 - start_text.get_width()//2, self.HEIGHT//2 - start_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)

    #Draw
    def draw(self):
        self.win.fill(self.GREEN)

        image = self.images[0]

        self.win.blit(image, (0,0))

        if self.num_players == 2:
            self.colour1 = self.BLACK
            self.width1 = 3
        else:
            self.colour1 = self.GREY
            self.width1 =2
        if self.num_players == 3:
            self.colour2 = self.BLACK
            self.width2 = 3
        else:
            self.colour2 = self.GREY
            self.width2 = 2
        if self.num_players == 4:
            self.colour3 = self.BLACK
            self.width3 = 3
        else:
            self.colour3 = self.GREY
            self.width3 = 2

        if self.active_hr:
            self.colour_hr = self.BLACK
        else:
            self.colour_hr = self.GREY
        if self.active_min:
            self.colour_min = self.BLACK
        else:
            self.colour_min = self.GREY
        if self.active_p1:
            self.colour_p1 = self.GREY
        else:
            self.colour_p1 = self.BLACK
        if self.active_p2:
            self.colour_p2 = self.GREY
        else:
            self.colour_p2 = self.BLACK
        if self.active_p3:
            self.colour_p3 = self.GREY
        else:
            self.colour_p3 = self.BLACK
        if self.active_p4:
            self.colour_p4 = self.GREY
        else:
            self.colour_p4 = self.BLACK

        pygame.draw.rect(self.win, self.BLACK, self.input_rect, 4)
        pygame.draw.rect(self.win, self.colour_hr, self.time_hr_rect, 2)
        pygame.draw.rect(self.win, self.colour_min, self.time_min_rect, 2)
        pygame.draw.rect(self.win, self.colour1, self.rect_1, self.width1)
        pygame.draw.rect(self.win, self.colour2, self.rect_2, self.width2)
        pygame.draw.rect(self.win, self.colour3, self.rect_3, self.width3)

        settings_heading = self.settings_header.render("Settings", 1, self.BLACK)
        self.win.blit(settings_heading, (self.input_rect.x + ((354 - settings_heading.get_width()) // 2), self.input_rect.y + ((80 - settings_heading.get_height()) // 2)))

        settings_time = self.settings_font.render("Time:           :", 1, self.BLACK)
        self.win.blit(settings_time, (30, 222))

        settings_time_hr = self.settings_font.render(self.time_hr, 1, self.BLACK)
        self.win.blit(settings_time_hr, (self.time_hr_rect.x + 2, self.time_hr_rect.y + 2))

        settings_time_min = self.settings_font.render(self.time_min, 1, self.BLACK)
        self.win.blit(settings_time_min, (self.time_min_rect.x + 2, self.time_min_rect.y + 2))

        settings_players = self.settings_font.render("Players:", 1, self.BLACK)
        self.win.blit(settings_players, (10, 305))

        settings_player2 = self.settings_font.render("2", 1, self.BLACK)
        self.win.blit(settings_player2, (197, 305))

        settings_player3 = self.settings_font.render("3", 1, self.BLACK)
        self.win.blit(settings_player3, (252, 305))

        settings_player4 = self.settings_font.render("4", 1, self.BLACK)
        self.win.blit(settings_player4, (307, 305))

        game_code = self.settings_font.render(self.code, 1, self.BLACK)
        self.win.blit(game_code, (590, 510))

        player1_name = self.settings_font.render(self.player1, 1, self.colour_p1)
        self.win.blit(player1_name, (725,137))

        player2_name = self.settings_font.render(self.player2, 1, self.colour_p2)
        self.win.blit(player2_name, (725,230))

        player3_name = self.settings_font.render(self.player3, 1, self.colour_p3)
        self.win.blit(player3_name, (725,315))

        player4_name = self.settings_font.render(self.player4, 1, self.colour_p4)
        self.win.blit(player4_name, (725,403))

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
                    if self.active_hr:
                        if event.key == pygame.K_BACKSPACE:
                            self.time_hr = self.time_hr[:-1]
                        else:
                            if len(self.time_hr) < 2:
                                self.time_hr += event.unicode
                    if self.active_min:
                        if event.key == pygame.K_BACKSPACE:
                            self.time_min = self.time_min[:-1]
                        else:
                            if len(self.time_min) < 2:
                                self.time_min += event.unicode

                    if self.active_p1:
                        if event.key == pygame.K_BACKSPACE:
                            self.player1 = self.player1[:-1]
                        else:
                            if len(self.player1) < 10:
                                self.player1 += event.unicode

                    if self.active_p2:
                        if event.key == pygame.K_BACKSPACE:
                            self.player2 = self.player2[:-1]
                        else:
                            if len(self.player2) < 10:
                                self.player2 += event.unicode

                    if self.active_p3:
                        if event.key == pygame.K_BACKSPACE:
                            self.player3 = self.player3[:-1]
                        else:
                            if len(self.player3) < 10:
                                self.player3 += event.unicode

                    if self.active_p4:
                        if event.key == pygame.K_BACKSPACE:
                            self.player4 = self.player4[:-1]
                        else:
                            if len(self.player4) < 10:
                                self.player4 += event.unicode
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    pos = (x, y)
                    print(pos)

                    if self.time_hr_rect.collidepoint(event.pos):
                        self.active_hr = True
                    else:
                        self.active_hr = False
                    if self.time_min_rect.collidepoint(event.pos):
                        self.active_min = True
                    else:
                        self.active_min = False
                    if self.rect_1.collidepoint(event.pos):
                        self.num_players = 2
                    if self.rect_2.collidepoint(event.pos):
                        self.num_players = 3
                    if self.rect_3.collidepoint(event.pos):
                        self.num_players = 4

                    if (x > 670 and x < 1115) and (y > 134 and y < 172):
                        self.active_p1 = True
                    else:
                        self.active_p1 = False
                    if (x > 670 and x < 1115) and (y > 225 and y < 264):
                            self.active_p2 = True
                    else:
                        self.active_p2 = False
                    if (x > 670 and x < 1115) and (y > 311 and y < 351):
                            self.active_p3 = True
                    else:
                        self.active_p3 = False
                    if (x > 670 and x < 1115) and (y > 397 and y < 437):
                            self.active_p4 = True
                    else:
                        self.active_p4 = False

                    #Start
                    if x > 961 and x < 1160:
                        if y > 503 and y < 550:
                            self.start = True

            if self.start:
                self.start_game()
                break

        pygame.display.quit()

class StartMenu():
    #pygame.init()
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

# def main():
#     sm = StartMenu()
#     sm.loop()

# if __name__ == '__main__':
#     main()

# def main():
#     hl = HostLobby()
#     hl.loop()

# if __name__ == '__main__':
#     main()
