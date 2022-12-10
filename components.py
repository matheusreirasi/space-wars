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

        self.score = 0


        #### shot player config ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False
        self.last_shot = pygame.time.get_ticks()
        #self.player_bullet_group = pygame.sprite.Group()
        self.player_hitbox = (self.x+30, self.y+80, 85, 75)


        #### Calvo sprites ####
        self.scale_x = 100
        self.scale_y = 100

        self.walk_player_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/parado1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda7.png"), (self.scale_x, self.scale_y)),
        ]


        #### Calvo shots ####
        self.shot_player_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira7.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira8.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira9.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira10.png"), (self.scale_x, self.scale_y)),
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

        self.player_hitbox = (self.x+15, self.y+20, 65, 75) ##hitbox dentro do update serve somente para desenhar e ñ quer dizer que realmente está acertando o player
        pygame.draw.rect(window_game, glb.GAME_BACKGROUND_COLOR, self.player_hitbox, 1)


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

        self.scale_x = 100
        self.scale_y = 100

        #### Enemy sprites ####
        self.sprites = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda8.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda7.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda1.png"), (self.scale_x, self.scale_y)),
        ]
        self.rect = self.sprites[self.step_index].get_rect()
        
        self.shot_enemy_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira6.png"), (self.scale_x, self.scale_y)),
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
        self.boss_hitbox = (self.x, self.y, 64, 150)

        # Speed
        self.speed_x = random.randrange(2,4)


        #### Sprite values ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False

        self.scale_x = 145
        self.scale_y = 145


        self.sprites = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda8.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda7.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda6.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/anda1.png"), (self.scale_x, self.scale_y)),
        ]
        self.rect = self.sprites[self.step_index].get_rect()


        self.shot_boss_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/atira1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/atira2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/atira3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/atira4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/atira5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/atira6.png"), (self.scale_x, self.scale_y))
        ]
        self.rect = self.shot_boss_sprite[self.shot_index].get_rect()


        self.hit_boss_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/hit1.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/hit2.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/hit3.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/hit4.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/hit5.png"), (self.scale_x, self.scale_y)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoBoss/hit6.png"), (self.scale_x, self.scale_y))
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
        self.boss_hitbox = (self.x+40, self.y+30, 100, 120) #tamanho ideal
        pygame.draw.rect(window_game, glb.GAME_BACKGROUND_COLOR, self.boss_hitbox, 1)


        self.shot_boss(window_game)

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.player_bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/bullet-direita.png"),(20,45))
        self.rect = self.player_bullet_image.get_rect()
        #self.rect.center = [x, y]

        self.enemy_bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/enemy-bullet-direita.png"),(60,40))
        self.rect = self.enemy_bullet_image.get_rect()
        #self.rect.center = [x, y]


        self.boss_bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/boss-bullet-direita.png"),(60,40))
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
        self.life_img = pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/vida.png"), (40, 40))


    def update(self,window_game):
        window_game.blit(self.life_img, (self.x, self.y))


class BonusHeart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


        self.x = x
        self.y = y
        self.heart_speed = 7

        self.hitbox = (self.x , self.y , 64, 64)
        self.heart_img = pygame.transform.scale(pygame.image.load("Sprites/Bonus/heart.png"), (90, 70))


    def move_heart(self):
        self.x -= self.heart_speed

    def off_screen(self):
        return not (self.x >= 0)

    def update(self, window_game):
        window_game.blit(self.heart_img, (self.x , self.y))
        self.heart_hitbox = (self.x+15, self.y+15, 65, 45)
        pygame.draw.rect(window_game, glb.GAME_BACKGROUND_COLOR, self.heart_hitbox, 1)
