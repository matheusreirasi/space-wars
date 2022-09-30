import pygame
from pygame.locals import *
from sys import exit
pygame.init()

# Window Settings
win_width = 1140 ## esses são as melhores valores pra imagem de fundo
win_height = 620
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Space Wars')

# Load and Size Images
background = pygame.transform.scale(pygame.image.load('background.png'), (win_width, win_height))
spaceshipImg = pygame.transform.scale(pygame.image.load('spaceship.png'), (30, 40))

# Classes
class Spaceship:
    def __init__(self, x, y):
        # Move
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 10
    def move_spaceship(self, userInput): ## limitei a movimentação da nave até o tamanho da tela do jogo
            if userInput[pygame.K_RIGHT] and spaceshipImg.get_width() + self.x < pygame.display.get_window_size()[0]:
                self.x += self.velx
            if userInput[pygame.K_LEFT] and self.x > 0:
                self.x -= self.velx
            if userInput[pygame.K_UP] and self.y > 0:
                self.y -= self.vely
            if userInput[pygame.K_DOWN] and spaceshipImg.get_height() + self.y < pygame.display.get_window_size()[1]:
                self.y += self.vely
    def draw(self, win):
        win.blit(spaceshipImg, (self.x, self.y))
        
# Draw Game
def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    player.draw(win)
    pygame.time.delay(30)
    pygame.display.update()

player = Spaceship(win_width/2, 500)

# Mainloop
while True:
    for event in pygame.event.get():

        # Quit Game
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Input
    userInput = pygame.key.get_pressed()

    # Movement
    player.move_spaceship(userInput)

    # Draw Game in Window   
    draw_game()


