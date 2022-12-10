import pygame, sys
import globals as glb

from display import play

class GameOver(object):
    def __init__(self):
        self.scroll_page = 0
        cooldown = 0
        cooldown_limit = 0

        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))

        self.calvou_font = pygame.font.Font("assets/font.ttf", 200)
        self.score_font = pygame.font.Font("assets/font.ttf", 30)

        self.gameover_image = pygame.transform.scale(pygame.image.load('./Sprites/Background/gameover.png'), (glb.GAME_WIDTH, glb.GAME_HEIGHT))

        self.score = play.Player(0,0).score


    def increase_scroll(self):
        self.scroll_page -= 4.5
        if abs(self.scroll_page) > glb.GAME_WIDTH:
            self.scroll_page = 0

        return self.scroll_page

    
    def update(self):
        self.window_game.fill(glb.GAME_BACKGROUND_COLOR)


        for i in range(0,2):
            self.window_game.blit(self.gameover_image, (i*self.gameover_image.get_width() + self.scroll_page, 0))

        self.increase_scroll()


        self.calvou_text = self.calvou_font.render("CALVOU", True, "white")
        self.window_game.blit(self.calvou_text, (glb.GAME_WIDTH/2, glb.GAME_HEIGHT/4))

        self.score_text = self.score_font.render("Score: " + str(self.score), True, "white")
        self.window_game.blit(self.score_text, (glb.GAME_WIDTH/2, glb.GAME_HEIGHT/3))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                glb.GAME_SCREEN = 1