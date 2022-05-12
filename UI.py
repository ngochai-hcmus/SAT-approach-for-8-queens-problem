import pygame

class chess_game:
    def __init__(self, solver):
        pygame.init()
        self.step = 0
        self.solver = solver
        self.screen_width = 800
        self.screen_height = 900
        self.width = 100
        self.height = 100
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.flag = True
        self.smallfont = pygame.font.SysFont('Corbel',35)
        self.new_game()
    
    def update(self, queens:list):
        
        self.draw_chess_board()

        queen_black = pygame.image.load('queen_black.png')
        queen_white = pygame.image.load('queen_white.png')
        queen_black = pygame.transform.scale(queen_black, (100, 100))
        queen_white = pygame.transform.scale(queen_white, (100, 100))
        for val in queens:
            row = val[0]
            col = val[1]
            if (row + col) % 2 == 1:
                self.screen.blit(queen_white, (col * self.width, row * self.height))
            else:
                self.screen.blit(queen_black, (col * self.width, row * self.height))

    def btn_start_click(self):
        self.update(self.solver[0])
        self.step = 1
    
    def btn_next_click(self):
        if(self.step >= len(self.solver)):
            return 
        self.update(self.solver[self.step])
        self.step = self.step + 1

    def draw_chess_board(self):
        white = (255, 255, 255)
        black = (0, 0, 0)
        self.screen.fill('silver')

        for i in range(0, 8):
            for j in range(0, 8):
                square = pygame.Rect(i*self.width, j*self.height, self.width, self.height)
                if (i + j) % 2 == 1:
                    pygame.draw.rect(self.screen, white, square)
                else:
                    pygame.draw.rect(self.screen, black, square)
        
        rect = pygame.Rect(self.screen_width/2 - 200, self.screen_height-100, 190, 100)
        pygame.draw.rect(self.screen, 'aquamarine', rect)
        text = self.smallfont.render('Start' , True , 'black')
        self.screen.blit(text, (self.screen_width/2 - 130,self.screen_height-70))

        rect = pygame.Rect(self.screen_width/2+10, self.screen_height-100, 190, 100)
        pygame.draw.rect(self.screen, 'aquamarine', rect)
        text = self.smallfont.render('Next' , True , 'black')
        self.screen.blit(text, (self.screen_width/2 + 70,self.screen_height-70))

    def new_game(self):
        pygame.display.set_caption('8 queens')
        self.draw_chess_board()
        pygame.display.update()
        self.flag = True
        while self.flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.screen_width/2 - 200 <= mouse[0] <= self.screen_width/2 - 10 and self.screen_height-100 <= mouse[1] <= self.screen_height):
                        self.btn_start_click()
                    if(self.screen_width/2+10 <= mouse[0] <= self.screen_width/2 + 200 and self.screen_height-100 <= mouse[1] <= self.screen_height):
                        self.btn_next_click()


            mouse = pygame.mouse.get_pos()

            if(self.screen_width/2 - 200 <= mouse[0] <= self.screen_width/2 - 10 and self.screen_height-100 <= mouse[1] <= self.screen_height):
                rect = pygame.Rect(self.screen_width/2 - 200, self.screen_height-100, 190, 100)
                pygame.draw.rect(self.screen, 'aqua', rect)
                text = self.smallfont.render('Start' , True , 'black')
                self.screen.blit(text, (self.screen_width/2 - 130,self.screen_height-70))
            else:
                rect = pygame.Rect(self.screen_width/2 - 200, self.screen_height-100, 190, 100)
                pygame.draw.rect(self.screen, 'aquamarine', rect)
                text = self.smallfont.render('Start' , True , 'black')
                self.screen.blit(text, (self.screen_width/2 - 130,self.screen_height-70))
           
            if(self.screen_width/2+10 <= mouse[0] <= self.screen_width/2 + 200 and self.screen_height-100 <= mouse[1] <= self.screen_height):
                rect = pygame.Rect(self.screen_width/2+10, self.screen_height-100, 190, 100)
                pygame.draw.rect(self.screen, 'aqua', rect)
                text = self.smallfont.render('Next' , True , 'black')
                self.screen.blit(text, (self.screen_width/2 + 70,self.screen_height-70))
            else:
                rect = pygame.Rect(self.screen_width/2+10, self.screen_height-100, 190, 100)
                pygame.draw.rect(self.screen, 'aquamarine', rect)
                text = self.smallfont.render('Next' , True , 'black')
                self.screen.blit(text, (self.screen_width/2 + 70,self.screen_height-70))

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()