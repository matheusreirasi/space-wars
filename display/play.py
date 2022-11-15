import pygame, sys, random
from components import Player, Enemy, Bullets, Life

import globals as glb

class Play(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        # Load and Size Images
        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
        pygame.display.set_caption(glb.GAME_TITLE)
        
        self.background_image_game = pygame.transform.scale(pygame.image.load('./Sprites/Background/background.png'), (glb.GAME_WIDTH, glb.GAME_HEIGHT))
        
        self.scroll = 0

        self.last_shot_enemy = pygame.time.get_ticks()
        self.last_shot_player = pygame.time.get_ticks()

        #### create player ####
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player(glb.GAME_WIDTH/2, 500)
        self.player_group.add(self.player)
        self.player_hitbox = (self.player.x, self.player.y, 60, 80)


        #### create enemy ####
        self.enemies_group = pygame.sprite.Group()
        self.enemy = Enemy(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-100))
        self.enemies_group.add(self.enemy)
        self.enemy_hitbox = (self.enemy.x, self.enemy.y, 65, 75)


        #### create bullets ####
        self.player_bullet_group = pygame.sprite.Group()
        self.player_bullet = Bullets(self.player.x, self.player.y, 1)

        self.enemy_bullet_group = pygame.sprite.Group()
        self.enemy_bullet = Bullets(self.enemy.x, self.enemy.y, -1)
        self.enemy_bullet_group.add(self.enemy_bullet)

        
    def increase_scroll(self):
        self.scroll -= 4.5
        if abs(self.scroll) > glb.GAME_WIDTH:
            self.scroll = 0

        return self.scroll


    def shot_player(self):
        self.time_now_player = pygame.time.get_ticks()
        self.userInput = pygame.key.get_pressed()

        if (self.userInput[pygame.K_SPACE] and self.time_now_player - self.last_shot_player > glb.PLAYER_COOLDOWN):
            self.player_bullet = Bullets(self.player.x, self.player.y, 1)
            self.player_bullet_group.add(self.player_bullet)
            self.player_bullet.update(self.window_game)
            self.last_shot_player = self.time_now_player

        for bullet in self.player_bullet_group:
            bullet.move()
            if bullet.off_screen():
                bullet.kill()
                print("player bullet off screen")
            
            bullet.update(self.window_game)


    def shot_enemy(self):
        self.time_now_enemy = pygame.time.get_ticks()

        for enemy in self.enemies_group:
            if (self.time_now_enemy - self.last_shot_enemy > self.enemy_cooldown and len(self.enemy_bullet_group) < 2):
                self.enemy_bullet = Bullets(enemy.x, enemy.y, -1)
                self.enemy_bullet_group.add(self.enemy_bullet)
                self.enemy_bullet.update(self.window_game)
                self.last_shot_enemy = self.time_now_enemy

        for bullet in self.enemy_bullet_group:
            bullet.move()
            if bullet.off_screen():
                bullet.kill()
                print("enemy bullet off screen")

            bullet.update(self.window_game)

    def shot_enemy2 (self):
        self.time_now_enemy = pygame.time.get_ticks()

        for enemy in self.enemies_group:
            self.bullet = Bullets(enemy.x , enemy.y, -1)
            self.enemy_bullet_group.add(self.bullet)
            self.last_shot_enemy = self.time_now_enemy

            if (self.time_now_enemy - self.last_shot_enemy > self.enemy_cooldown and len(self.enemy_bullet_group) < 2):

                for bullet in self.enemy_bullet_group:
                
                    bullet.move()
                    if bullet.off_screen():
                        bullet.kill()
                        print("enemy bullet off screen")
                    
            self.enemy_bullet_group.update(self.window_game)
                        



    def player_hit_enemy (self):
        for enemy in self.enemies_group:
            if enemy.enemy_hitbox[0] < self.player_bullet.x < enemy.enemy_hitbox[0] + enemy.enemy_hitbox[2] and enemy.enemy_hitbox[1] < self.player_bullet.y < enemy.enemy_hitbox[1] + enemy.enemy_hitbox[3]:
                #self.enemy.kill()
                self.player_bullet.kill()
                enemy.kill()
                self.enemies_group.remove(enemy)


    def create_new_enemy(self):
        for enemy in self.enemies_group:
            if (len(self.enemies_group) <= 3 and len(self.enemies_group) > 0):
                self.enemy = Enemy(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+300), random.randrange(10, glb.GAME_HEIGHT-100))
                self.enemies_group.add(self.enemy)
            if (enemy.off_screen()):
                enemy.kill()
                self.enemies_group.remove(enemy)
                print("enemy off screen")
            else:
                enemy.move_enemy()
                

        

    # Draw Game
    def update(self):
        self.clock.tick(glb.FPS)

        self.window_game.fill(glb.GAME_BACKGROUND_COLOR)

        self.enemy_cooldown = random.randrange(2000,9000)

        #self.player_hitbox = (self.player.x+15, self.player.y+20, 60, 80)
        #pygame.draw.rect(self.window_game, glb.GAME_BACKGROUND_COLOR, self.player_hitbox, 1)

        #self.enemy_hitbox = (self.enemy.x+15, self.enemy.y+20, 65, 75)#width,height
        #pygame.draw.rect(self.window_game, glb.GAME_BACKGROUND_COLOR, self.enemy_hitbox, 1)

        for i in range(0,2):
            self.window_game.blit(self.background_image_game, (i*self.background_image_game.get_width() + self.scroll, 0))

        
        self.create_new_enemy()

        self.enemies_group.update(self.window_game)
        #self.player_group.update(self.window_game)
        
        self.player.update(self.window_game)
        self.enemy.update(self.window_game)

        self.player_hit_enemy()

        self.shot_player()
        self.shot_enemy2()

    
        #self.player_bullet.update(self.window_game)
        #self.enemy_bullet.update(self.window_game)

        self.increase_scroll()

        pygame.time.delay(30)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                glb.GAME_SCREEN = 1