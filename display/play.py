import pygame, sys
from components import Spaceship

import globals as glb

class Play(object):
    def __init__(self):
        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
        
        pygame.display.set_caption("Space Wars")

        # Load and Size Images
        self.background_image_game = pygame.transform.scale(pygame.image.load('assets/background.png'), (glb.GAME_WIDTH, glb.GAME_HEIGHT))

        #### create sprite groups
        self.player_group = pygame.sprite.Group()
        self.bulllet_group = pygame.sprite.Group()

        #### create player
        self.player = Spaceship(glb.GAME_WIDTH/2, 500)
        self.player_group.add(self.player)
        

        # Draw Game
    def update(self):
        self.window_game.fill(glb.GAME_BACKGROUND_COLOR)
        self.window_game.blit(self.background_image_game, (0, 0))

        self.player.update(self.window_game)
        
        pygame.time.delay(30)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                glb.GAME_SCREEN = 1
                
                
        pygame.display.update()