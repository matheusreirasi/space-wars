import pygame, random


import globals as glb

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y


        #### life payer config ####
        self.player_life = 5
        self.life_array = []
        self.life_x = 50

        if (self.player_life <= 0):
            glb.GAME_SCREEN = 5

        self.score = 0


        #### shot player config ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False
        self.last_shot = pygame.time.get_ticks()
        self.player_hitbox = (self.x+15, self.y+25, 65, 70)


        #### Calvo sprites ####
        self.scale_x = 135
        self.scale_y = 135

        self.walk_player_sprite = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/parado1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/anda7.png"), (self.scale_x, self.scale_y)),
        ]


        #### Calvo shots ####
        self.shot_player_sprite = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira7.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira8.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira9.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/atira10.png"), (self.scale_x, self.scale_y)),
        ]


    def move_player(self):
        self.userInput = pygame.key.get_pressed()

        if self.userInput[pygame.K_d] and self.walk_player_sprite[self.step_index].get_width() + self.x < glb.GAME_WIDTH:
            self.x += glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_a] and self.x > 0:
            self.x -= glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_w] and self.y > 0:
            self.y -= glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_s] and self.walk_player_sprite[self.step_index].get_width() + self.y < glb.GAME_HEIGHT:
            self.y += glb.SPACESHIP_SPEED


    def shot_player(self, window_game):
        self.time_now = pygame.time.get_ticks()

        if (self.userInput[pygame.K_SPACE] and self.time_now - self.last_shot > glb.PLAYER_COOLDOWN):
            self.shot_value = True
            self.last_shot = self.time_now


        if (self.shot_value == False):
            if (self.step_index >= 7):
                self.step_index = 0
            window_game.blit(self.walk_player_sprite[self.step_index], (self.x, self.y))
            self.step_index += 1
        else:
            if (self.shot_index < 10):
                window_game.blit(self.shot_player_sprite[self.shot_index], (self.x, self.y))       
                self.shot_index += 1
            else:
                self.shot_index = 0
                self.shot_value = False
        

    def off_screen(self):
        return not(self.x >= 0 and self.x <= glb.GAME_WIDTH)

    
    def show_life_player(self):
        if ((len(self.life_array) != self.player_life)):
            self.heart = Life(self.life_x)
            self.life_array.append(self.heart)
            self.life_x += 50


    def update(self, window_game):

        self.show_life_player()
        for heart in self.life_array:
            heart.update(window_game)

        self.move_player()
        self.shot_player(window_game)

        self.player_hitbox = (self.x+15, self.y+25, 65, 70) ##hitbox dentro do update serve somente para desenhar e ñ quer dizer que realmente está acertando o player


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        
        # Hitbox
        self.enemy_hitbox = (self.x+15, self.y+20, 85, 75)

        # Speed
        self.speed_x = random.randrange(2,4)

        #### Sprite values ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False
        self.last_shot_enemy = pygame.time.get_ticks()

        self.scale_x = 135
        self.scale_y = 135

        #### Enemy sprites ####
        self.sprites = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda8.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda7.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/anda1.png"), (self.scale_x, self.scale_y)),
        ]
        self.rect = self.sprites[self.step_index].get_rect()
        
        self.shot_enemy_sprite = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/atira1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/atira2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/atira3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/atira4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/atira5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoenemy/atira6.png"), (self.scale_x, self.scale_y)),
        ]
        self.rect = self.shot_enemy_sprite[self.shot_index].get_rect()


      
    def move_enemy(self):
        self.x -= self.speed_x


    def shot_enemy(self, window_game):
        self.time_now_enemy = pygame.time.get_ticks()

        if (self.time_now_enemy - self.last_shot_enemy > glb.ENEMY_COOLDOWN):
            self.shot_value = True
            self.last_shot_enemy = self.time_now_enemy

        if (self.shot_value == False):
            if (self.step_index >= 7):
                self.step_index = 0
            window_game.blit(self.sprites[self.step_index], (self.x, self.y))
            self.step_index += 1
        else:
            if (self.shot_index < 5):
                window_game.blit(self.shot_enemy_sprite[self.shot_index], (self.x, self.y))       
                self.shot_index += 1
            else:
                self.shot_index = 0
                self.shot_value = False


    def off_screen(self):
        return not(self.x >= 0)


    def update(self, window_game):
        self.enemy_hitbox = (self.x, self.y, 65, 75)

        self.shot_enemy(window_game)

        """
        if (self.shot_value == False):
            if self.step_index >= 8:
                self.step_index = 0
            window_game.blit(self.sprites[self.step_index], (self.x, self.y))
            self.step_index += 1
        else:
            if self.shot_index < 6:
                window_game.blit(self.shot_enemy_sprite[self.shot_index], (self.x, self.y))
                self.shot_index += 1
            else:
                self.shot_index = 0
                self.shot_value = False
        """

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.last_shot_boss = pygame.time.get_ticks()

        self.boss_life = 3

        # Hitbox
        self.boss_hitbox = (self.x+40, self.y+15, 100, 120)

        # Speed
        self.speed_x = random.randrange(2,4)


        #### Sprite values ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False

        self.scale_x = 165
        self.scale_y = 165


        self.sprites = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda8.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda7.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/anda1.png"), (self.scale_x, self.scale_y)),
        ]
        self.rect = self.sprites[self.step_index].get_rect()


        self.shot_boss_sprite = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/atira1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/atira2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/atira3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/atira4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/atira5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/atira6.png"), (self.scale_x, self.scale_y))
        ]
        self.rect = self.shot_boss_sprite[self.shot_index].get_rect()


        self.hit_boss_sprite = [
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/hit1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/hit2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/hit3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/hit4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/hit5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("assets/sprites/calvoboss/hit6.png"), (self.scale_x, self.scale_y))
        ]


    def move_boss(self):
        self.x -= self.speed_x

    
    def shot_boss(self, window_game):
        self.time_now_boss = pygame.time.get_ticks()

        if (self.time_now_boss - self.last_shot_boss > glb.BOSS_COOLDOWN):
            self.shot_value = True
            self.last_shot_boss = self.time_now_boss

        if (self.shot_value == False):
            if (self.step_index >= 7):
                self.step_index = 0
            window_game.blit(self.sprites[self.step_index], (self.x, self.y))
            self.step_index += 1
        else:
            if (self.shot_index < 5):
                window_game.blit(self.shot_boss_sprite[self.shot_index], (self.x, self.y))       
                self.shot_index += 1
            else:
                self.shot_index = 0
                self.shot_value = False


    def off_screen(self):
        return not(self.x >= 0)


    def update(self, window_game):
        self.boss_hitbox = (self.x+40, self.y+15, 100, 120)


        self.shot_boss(window_game)

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.player_bullet_image = pygame.transform.scale(pygame.image.load("./assets/sprites/bullet/bullet-direita.png"),(30,55))
        self.rect = self.player_bullet_image.get_rect()
        #self.rect.center = [x, y]

        self.enemy_bullet_image = pygame.transform.scale(pygame.image.load("./assets/sprites/bullet/enemy-bullet-direita.png"),(70,50))
        self.rect = self.enemy_bullet_image.get_rect()
        #self.rect.center = [x, y]


        self.boss_bullet_image = pygame.transform.scale(pygame.image.load("./assets/sprites/bullet/boss-bullet-direita.png"),(70,50))
        self.boss_bullet_rect = self.boss_bullet_image.get_rect()
        #self.boss_bullet_rect.center = [x, y]

        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        self.x += 15 *self.direction

    
    def off_screen(self):
        return not (self.x >= 0 and self.x <= glb.GAME_WIDTH)


    def update(self, window_game):
        self.hitbox = (self.x+10, self.y+10, 40, 20) ##hitbox dentro do update serve somente para desenhar e ñ quer dizer que realmente está acertando o player

        if self.direction == 1:
            window_game.blit(self.player_bullet_image, (self.x, self.y))
        elif self.direction == -1:
            window_game.blit(self.enemy_bullet_image, (self.x, self.y))
        else:
            window_game.blit(self.boss_bullet_image, (self.x, self.y))

class Life(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = 45
        self.life_img = pygame.transform.scale(pygame.image.load("assets/sprites/calvohero/vida.png"), (40, 40))


    def update(self,window_game):
        window_game.blit(self.life_img, (self.x, self.y))


class BonusHeart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


        self.x = x
        self.y = y
        self.heart_speed = 7

        self.heart_hitbox = (self.x+15 , self.y , 30, 30)
        self.heart_img = pygame.transform.scale(pygame.image.load("assets/sprites/bonus/heart.png"), (90, 70))


    def move_heart(self):
        self.x -= self.heart_speed

    def off_screen(self):
        return not (self.x >= 0)

    def update(self, window_game):
        window_game.blit(self.heart_img, (self.x , self.y))
        self.heart_hitbox = (self.x, self.y-5 , 65, 30)
