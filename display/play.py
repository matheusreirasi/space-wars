import pygame, sys, random
from components import Player, Enemy

import globals as glb

class Play(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        # Load and Size Images
        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
        pygame.display.set_caption("Space Wars")
        
        self.background_image_game = pygame.transform.scale(pygame.image.load('./Sprites/Background/background.png'), (glb.GAME_WIDTH, glb.GAME_HEIGHT))

        #### create sprite groups
        self.player_group = pygame.sprite.Group()
        self.bulllet_group = pygame.sprite.Group()

        #### create player
        self.player = Player(glb.GAME_WIDTH/2, 500)
        self.player_group.add(self.player)

        #### create enemy array ####
        self.enemies_group = pygame.sprite.Group()
        self.enemy = Enemy(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-50))

        self.scroll = 0
        
    def increase_scroll(self):
        self.scroll -= 4.5
        if abs(self.scroll) > glb.GAME_WIDTH:
            self.scroll = 0

        return self.scroll


    # Draw Game
    def update(self):
        self.window_game.fill(glb.GAME_BACKGROUND_COLOR)
        self.window_game.blit(self.background_image_game, (0, 0))

        self.clock.tick()

        for i in range(0,2):
            self.window_game.blit(self.background_image_game, (i*self.background_image_game.get_width() + self.scroll, 0))

        self.player.update(self.window_game)
        self.enemy.update(self.window_game)


        if (len(self.enemies_group) < 3):
            self.enemies_group.add(self.enemy)

            for enemy in self.enemies_group:
                if  enemy.off_screen():
                    self.enemies_group.remove(enemy)
                else:
                    enemy.move_enemy()
                    


        self.increase_scroll()

        pygame.time.delay(30)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                glb.GAME_SCREEN = 1
                
                