import pygame

class Spaceship_1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.transform.scale(pygame.image.load('spaceship.png'), (30, 40))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10

    def move_spaceship(self, userInput):
        if userInput[pygame.K_d] and self.image.get_width() + self.x < pygame.display.get_window_size()[0]:
            self.x += self.vel_x
        if userInput[pygame.K_a] and self.x > 0:
            self.x -= self.vel_x
        if userInput[pygame.K_w] and self.y > 0:
            self.y -= self.vel_y
        if userInput[pygame.K_s] and self.image.get_height() + self.y < pygame.display.get_window_size()[1]:
            self.y += self.vel_y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Spaceship_2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.transform.scale(pygame.image.load('assets/Graphics-Asset/PNG/Spaceships/01/Spaceship_01_BLUE.png'), (60, 70))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10

    def move_spaceship(self, userInput):
        if userInput[pygame.K_RIGHT] and self.image.get_width() + self.x < pygame.display.get_window_size()[0]:
            self.x += self.vel_x
        if userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel_x
        if userInput[pygame.K_UP] and self.y > 0:
            self.y -= self.vel_y
        if userInput[pygame.K_DOWN] and self.image.get_height() + self.y < pygame.display.get_window_size()[1]:
            self.y += self.vel_y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))