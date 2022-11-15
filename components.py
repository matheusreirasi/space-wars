import pygame, random

import globals as glb

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y


        #### life payer config ####
        self.number_life = 5
        self.life_array = []
        self.life_x = 50


        #### shot player config ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False
        self.last_shot = pygame.time.get_ticks()
        #self.player_bullet_group = pygame.sprite.Group()
        self.player_hitbox = (self.x+15, self.y+20, 65, 75)


        #### Calvo sprites ####
        self.escalax = 100
        self.escalay = 100

        self.walk_player_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/parado1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda2.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda3.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda4.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda5.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda6.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda7.png"), (self.escalax, self.escalay)),
        ]


        #### Calvo shots ####
        self.shot_player_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira2.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira3.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira4.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira5.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira6.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira7.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira8.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira9.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/atira10.png"), (self.escalax, self.escalay)),
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
            #self.bullet = Bullets(self.x, self.y, 1)
            #self.player_bullet_group.add(self.bullet)
            #self.bullet.update(window_game)
            self.last_shot = self.time_now

        #for bullet in self.player_bullet_group:
            #bullet.move()
            #if bullet.off_screen():
                #bullet.kill()

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
        if ((len(self.life_array) != self.number_life)):
            self.heart = Life(self.life_x)
            self.life_array.append(self.heart)
            self.life_x += 50


    def update(self, window_game):

        self.show_life_player()
        for heart in self.life_array:
            heart.update(window_game)

        self.move_player()
        self.shot_player(window_game)
        #self.player_bullet_group.update(window_game)

        self.player_hitbox = (self.x+15, self.y+20, 65, 75)
        pygame.draw.rect(window_game, glb.GAME_BACKGROUND_COLOR, self.player_hitbox, 1)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.last_shot = pygame.time.get_ticks()
        
        # Hitbox
        self.enemy_hitbox = (self.x+15, self.y+20, 85, 75)

        #### Sprite values ####
        self.step_index = 0
        self.shot_index = 0
        self.shot_value = False
        
        # Speed
        self.velx = random.randrange(2,4)

        self.escalax = 100
        self.escalay = 100

        #### Enemy sprites ####
        self.sprites = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda8.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda7.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda6.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda5.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda4.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda3.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda2.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda1.png"), (self.escalax, self.escalay)),
        ]
        self.rect = self.sprites[self.step_index].get_rect()
        
        self.shot_enemy_sprite = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira2.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira3.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira4.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira5.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/atira6.png"), (self.escalax, self.escalay)),
        ]
        self.rect = self.shot_enemy_sprite[self.shot_index].get_rect()

        #### Bullet ####
        #self.enemy_bullet_group = pygame.sprite.Group()

      
    def move_enemy(self):
        self.x -= self.velx


    def off_screen(self):
        return not(self.x >= 0)


    def update(self, window_game):
        self.enemy_hitbox = (self.x, self.y, 65, 75)
        #pygame.draw.rect(window_game, glb.GAME_BACKGROUND_COLOR, self.enemy_hitbox, 1)

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

        #self.enemy_bullet_group.update(window_game)
        
        

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.player_bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/bullet-direita.png"),(20,45))
        self.rect = self.player_bullet_image.get_rect()
        self.rect.center = [x, y]

        self.enemy_bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/enemy-bullet-direita.png"),(60,40))
        self.rect = self.enemy_bullet_image.get_rect()
        self.rect.center = [x, y]


        self.boss_bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/boss-bullet-direita.png"),(60,40))
        self.boss_bullet_rect = self.boss_bullet_image.get_rect()
        self.boss_bullet_rect.center = [x, y]

        self.x = x+8
        self.y = y+8
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