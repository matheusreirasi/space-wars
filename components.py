import pygame, random

import globals as glb

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


        self.spaceship_image = pygame.transform.scale(pygame.image.load('./assets/Spaceships/01/Spaceship_01_BLUE.png'), (50, 60))
        self.rect = self.spaceship_image.get_rect()
        self.x = x
        self.y = y

        self.stepIndex = 0
        self.shotIndex = 0

        self.bullet_player_group = pygame.sprite.Group()
        self.last_shot = pygame.time.get_ticks()
        self.hitbox = (self.x, self.y, 100, 100)

        #### Calvo sprites ####
        self.escalax = 100
        self.escalay = 100

        self.anda = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/parado1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda2.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda3.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda4.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda5.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda6.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoHero/anda7.png"), (self.escalax, self.escalay)),
        ]

        #### Calvo atira ####

        self.atira = [
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

        self.enemies = []

        self.anda_enemy = [None]*9
        for picIndex in range(1, 9):
            self.anda_enemy[picIndex-1] = pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda" + str(picIndex) + ".png"), (self.escalax, self.escalay))


    def move_player(self):
        self.userInput = pygame.key.get_pressed()

        if self.userInput[pygame.K_d] and self.anda[self.stepIndex].get_width() + self.x < pygame.display.get_window_size()[0]:
            self.x += glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_a] and self.x > 0:
            self.x -= glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_w] and self.y > 0:
            self.y -= glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_s] and self.anda[self.stepIndex].get_width() + self.y < pygame.display.get_window_size()[1]:
            self.y += glb.SPACESHIP_SPEED
    

    def shot_player(self, window_game):
        self.time_now = pygame.time.get_ticks()

        if (self.userInput[pygame.K_SPACE] and self.time_now - self.last_shot > self.cooldown):
            bullet = Bullets(self.x, self.y)
            self.bullet_player_group.add(bullet)
            bullet.update(window_game)
            self.last_shot = self.time_now
            print("shoot")


    def hit (self):
        for enemy in self.enemies:
            for bullet in self.bullet_player_group:
                if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                    self.enemies.remove(enemy)
                    self.bullet_player_group.remove(bullet)


    def update(self, window_game):
        self.cooldown = 500 #milissegundos
        self.move_player()
        self.shot_player(window_game)
        window_game.blit(self.anda[self.stepIndex], (self.x, self.y))
        self.bullet_player_group.update(window_game)
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.escalax = 100
        self.escalay = 100

        self.anda_enemy = [
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda1.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda2.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda3.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda4.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda5.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda6.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda7.png"), (self.escalax, self.escalay)),
            pygame.transform.scale(pygame.image.load("Sprites/CalvoEnemy/anda8.png"), (self.escalax, self.escalay)),
        ]

        # Speed
        self.velx = random.randrange(3, 7)

        # Bullet
        self.bullet_enemy_group = []
        self.cool_down_count = 0

        # Hitbox
        self.hitbox = (self.x, self.y, 100, 100)

        # Sprite
        self.stepIndex = 0

        
    def move_enemy(self):
        self.x -= self.velx


    def off_screen(self):
        return not(self.x >= 0)


    def update(self, window_game):
        if self.stepIndex >= 8:
            self.stepIndex = 0
        window_game.blit(self.anda_enemy[self.stepIndex], (self.x, self.y))
        self.stepIndex+=1
        self.hitbox = (self.x, self.y, 100, 100)



class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.transform.scale(pygame.image.load("./Sprites/Bullet/bullet-direita.png"),(20,45))
        self.rect = self.bullet_image.get_rect()  
        self.x = x+8
        self.y = y+8

    def update(self, window_game):
        self.x += glb.BULLET_SPEED
        if self.rect.right < 0:
            self.kill()
        window_game.blit(self.bullet_image, (self.x, self.y))
