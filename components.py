import pygame

import globals as glb

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


        self.spaceship_image = pygame.transform.scale(pygame.image.load('./assets/Spaceships/01/Spaceship_01_BLUE.png'), (50, 60))
        self.rect = self.spaceship_image.get_rect()
        self.x = x
        self.y = y

        self.bullet_group = pygame.sprite.Group()        
        self.last_shot = pygame.time.get_ticks()

    def move_spaceship(self):
        self.userInput = pygame.key.get_pressed()

        if self.userInput[pygame.K_d] and self.spaceship_image.get_width() + self.x < pygame.display.get_window_size()[0]:
            self.x += glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_a] and self.x > 0:
            self.x -= glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_w] and self.y > 0:
            self.y -= glb.SPACESHIP_SPEED
        if self.userInput[pygame.K_s] and self.spaceship_image.get_height() + self.y < pygame.display.get_window_size()[1]:
            self.y += glb.SPACESHIP_SPEED
    

    def shot_player(self, window_game):
        self.time_now = pygame.time.get_ticks()
        if (self.userInput[pygame.K_SPACE] and self.time_now - self.last_shot > self.cooldown):
            bullet = Bullets(self.x+15, self.y-35)
            self.bullet_group.add(bullet)
            bullet.update(window_game)
            self.last_shot = self.time_now
            print("shoot")


    def update(self, window_game):
        self.cooldown = 500 #milissegundos
        self.move_spaceship()
        self.shot_player(window_game)
        window_game.blit(self.spaceship_image, (self.x, self.y))
        self.bullet_group.update(window_game)
        

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = pygame.transform.scale(pygame.image.load("./assets/bullet.png"),(20,45))
        self.rect = self.bullet_image.get_rect()  
        self.x = x
        self.y = y

    def update(self, window_game):
        self.y -= glb.BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()
        window_game.blit(self.bullet_image, (self.x, self.y))
