import pygame, sys, random
from components import Player, Enemy, Bullets, BonusHeart, Boss
from display import gameover

import globals as glb

class Play(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps_font = pygame.font.Font("assets/font.ttf", 20)
        self.score_font = pygame.font.Font("assets/font.ttf", 17)

        
        # Load and Size Images
        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
        pygame.display.set_caption(glb.GAME_TITLE)
        
        self.background_image_game = pygame.transform.scale(pygame.image.load('./assets/images/background.png'), (glb.GAME_WIDTH, glb.GAME_HEIGHT))
        
        self.scroll_page = 0

        self.last_shot_enemy = pygame.time.get_ticks()
        self.last_shot_boss = pygame.time.get_ticks()
        self.last_shot_player = pygame.time.get_ticks()

        #### create player ####
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player(glb.GAME_WIDTH/2, 400)
        self.player_group.add(self.player)


        #### create enemy ####
        self.enemies_group = pygame.sprite.Group()
        self.enemy = Enemy(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-200))
        self.enemies_group.add(self.enemy)


        #### create Boss ####
        self.boss_group = pygame.sprite.Group()
        self.boss = Boss(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-250))
        self.boss_group.add(self.boss)


        #### create heart ####
        self.heart_group = pygame.sprite.GroupSingle()
        self.bonus_heart = BonusHeart(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-160))
        self.heart_group.add(self.bonus_heart)


        #### create bullets ####
        self.player_bullet_group = pygame.sprite.Group()
        self.player_bullet = Bullets(self.player.x, self.player.y, 1)

        self.enemy_bullet_group = pygame.sprite.Group()
        self.enemy_bullet = Bullets(self.enemy.x , self.enemy.y , -1)

        self.boss_bullet_group = pygame.sprite.Group()
        self.boss_bullet = Bullets(self.boss.x , self.boss.y , -1.5)


        
    def increase_scroll(self):
        self.scroll_page -= 4.5
        if abs(self.scroll_page) > glb.GAME_WIDTH:
            self.scroll_page = 0

        return self.scroll_page




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
            
            bullet.update(self.window_game)


    def shot_enemy(self):
        self.time_now_enemy = pygame.time.get_ticks()

        for enemy in self.enemies_group:
            if (self.time_now_enemy - self.last_shot_enemy > glb.ENEMY_COOLDOWN ):
                self.enemy_bullet = Bullets(enemy.x, enemy.y, -1)
                self.enemy_bullet_group.add(self.enemy_bullet)
                self.enemy_bullet.update(self.window_game)
                self.last_shot_enemy = self.time_now_enemy

        for bullet in self.enemy_bullet_group:
            bullet.move()
            if bullet.off_screen():
                bullet.kill()

            bullet.update(self.window_game)


    def shot_boss(self):
        self.time_now_boss = pygame.time.get_ticks()

        for boss in self.boss_group:
            if (self.time_now_boss - self.last_shot_boss > glb.BOSS_COOLDOWN and len(self.boss_bullet_group) < 2):
                self.boss_bullet = Bullets(boss.x, boss.y, -0.7)
                self.boss_bullet_group.add(self.boss_bullet)
                self.boss_bullet.update(self.window_game)
                self.last_shot_boss = self.time_now_boss

        for bullet in self.boss_bullet_group:
            bullet.move()
            if bullet.off_screen():
                bullet.kill()

            bullet.update(self.window_game)




    def player_hit_enemy (self):
        for enemy in self.enemies_group:
            for bullet in self.player_bullet_group:
                if enemy.enemy_hitbox[0] < bullet.x < enemy.enemy_hitbox[0] + enemy.enemy_hitbox[2] and enemy.enemy_hitbox[1] < bullet.y < enemy.enemy_hitbox[1] + enemy.enemy_hitbox[3]:
                    self.player.score += 33
                    bullet.kill()
                    enemy.kill()
                    self.enemies_group.remove(enemy)


    def player_hit_boss(self):
        for boss in self.boss_group:
            for bullet in self.player_bullet_group:
                if boss.boss_hitbox[0] < bullet.x < boss.boss_hitbox[0] + boss.boss_hitbox[2] and boss.boss_hitbox[1] < bullet.y < boss.boss_hitbox[1] + boss.boss_hitbox[3]:
                    self.player.score += 55
                    self.boss.boss_life -= 1
                    bullet.kill()

                    if (self.boss.boss_life == 0):
                        self.boss.kill()


    def player_hit_heart(self):
        for heart in self.heart_group:
            for bullet in self.player_bullet_group:
                if heart.heart_hitbox[0] < bullet.x < heart.heart_hitbox[0] + heart.heart_hitbox[2] and heart.heart_hitbox[1] < bullet.y < heart.heart_hitbox[1] + heart.heart_hitbox[3]:
                    self.player.score += 5
                    self.player.player_life += 1
                    self.player.life_x += 50
                    self.player.life_array.append(heart)
                    bullet.kill()
                    self.heart_group.remove(heart)
                    self.bonus_heart.kill()
                    heart.update(self.window_game)
                
                


    def enemy_hit_player(self):
        for enemy_bullet in self.enemy_bullet_group:
            if self.player.player_hitbox[0] < enemy_bullet.x < self.player.player_hitbox[0] + self.player.player_hitbox[2] and self.player.player_hitbox[1] < enemy_bullet.y+30 < self.player.player_hitbox[1] + self.player.player_hitbox[3]:
                self.enemy_bullet_group.remove(enemy_bullet)
                self.player.player_life -= 1
                self.player.life_x -= 50
                self.player.life_array.pop()

                if (self.player.player_life <= 0):
                    gameover.GameOver()
                    glb.GAME_SCREEN = 5

    def boss_hit_player(self):
        for boss_bullet in self.boss_bullet_group:
            if self.player.player_hitbox[0] < boss_bullet.x < self.player.player_hitbox[0] + self.player.player_hitbox[2] and self.player.player_hitbox[1] < boss_bullet.y < self.player.player_hitbox[1] + self.player.player_hitbox[3]:
                self.boss_bullet_group.remove(boss_bullet)
                self.player.player_life -= 3
                self.player.life_x -= 150
                self.player.life_array.pop()
                self.player.life_array.pop()
                self.player.life_array.pop()


                if (self.player.player_life == 0):
                    gameover.GameOver()
                    glb.GAME_SCREEN = 5

    def create_new_enemy(self):
        for enemy in self.enemies_group:
            if (len(self.enemies_group) <= 3 and len(self.enemies_group) > 0):
                self.enemy = Enemy(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+300), random.randrange(10, glb.GAME_HEIGHT-100))
                self.enemies_group.add(self.enemy)
            if (enemy.off_screen()):
                self.player.player_life -= 1
                self.player.life_x -= 50
                self.player.life_array.pop()
                enemy.kill()
                self.enemies_group.remove(enemy)
            else:
                enemy.move_enemy()


    def create_new_boss(self):
        if(random.randrange(1, 200) == 5 and len(self.boss_group) < 1):
            self.boss = Boss(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-160))
            self.boss_group.add(self.boss)
        for boss in self.boss_group:
            if (boss.off_screen()):
                self.player.player_life -= 1
                self.player.life_x -= 50
                self.player.life_array.pop()
                boss.kill()
                self.boss_group.remove(boss)
            else:
                boss.move_boss()


    def create_new_heart(self):
        if(random.randrange(1, 300) == 5 and len(self.heart_group) < 1):
            self.bonus_heart = BonusHeart(random.randrange(glb.GAME_WIDTH, glb.GAME_WIDTH+100), random.randrange(10, glb.GAME_HEIGHT-160))
            self.heart_group.add(self.bonus_heart)
        for heart in self.heart_group:
            if (heart.off_screen()):
                self.heart_group.remove(heart)
            else:
                heart.move_heart()
            

        
    # Draw Game
    def update(self):
        self.window_game.fill(glb.GAME_BACKGROUND_COLOR)
        print(self.player.player_life)

        for i in range(0,2):
            self.window_game.blit(self.background_image_game, (i*self.background_image_game.get_width() + self.scroll_page, 0))

        self.increase_scroll()


        self.create_new_heart()
        self.create_new_enemy()
        self.create_new_boss()

        self.enemies_group.update(self.window_game)
        self.boss_group.update(self.window_game)
        self.heart_group.update(self.window_game)
        
        self.player.update(self.window_game)

        self.player_hit_enemy()
        self.player_hit_boss()
        self.player_hit_heart()

        self.boss_hit_player()
        self.enemy_hit_player()
        
        self.shot_player()
        self.shot_enemy()
        self.shot_boss()

    
        pygame.time.delay(30)

        self.clock.tick(60)
        self.fps = self.clock.get_fps()


        self.fps_text = self.fps_font.render("FPS: " + str(self.fps), True, "white")
        self.window_game.blit(self.fps_text, (glb.GAME_WIDTH-180, 60))

        self.score_text = self.score_font.render("Score: " + str(self.player.score), True, "white")
        self.window_game.blit(self.score_text, (50, 100))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                glb.GAME_SCREEN = 1