import pygame, sys
import globals as glb

from display import play
from components import Player

class GameOver(object):
    def __init__(self):
        self.scroll_page = 0

        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
        self.gameover_image = pygame.transform.scale(pygame.image.load('./assets/images/gameover.png'), (glb.GAME_WIDTH, glb.GAME_HEIGHT))

        self.calvou_font = pygame.font.Font("assets/font.ttf", 150)
        self.score_font = pygame.font.Font("assets/font.ttf", 30)


        self.score = play.Player(0,0).score
        #self.score = play.Play().player.score
        #self.score = Player(0,0).score



    def increase_scroll(self):
        self.scroll_page -= 3.5
        if abs(self.scroll_page) > glb.GAME_WIDTH:
            self.scroll_page = 0

        return self.scroll_page

    
    def update(self):


        for i in range(0,2):
            self.window_game.blit(self.gameover_image, (i*self.gameover_image.get_width() + self.scroll_page, 0))

        self.increase_scroll()


        self.calvou_text = self.calvou_font.render("CALVOU", True, "white")
        self.window_game.blit(self.calvou_text, (glb.GAME_WIDTH/2 - self.calvou_text.get_width()/2, glb.GAME_HEIGHT/5))

        self.score_text = self.score_font.render("Score: " + str(self.score), True, "white")
        self.window_game.blit(self.score_text, (glb.GAME_WIDTH/2 - self.score_text.get_width()/2, 2*glb.GAME_HEIGHT/3))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                glb.GAME_SCREEN = 1