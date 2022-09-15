import pygame
from pygame.locals import *
from sys import exit
pygame.init()

# Window Settings
win_width = 800
win_height = 600
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
    def move_spaceship(self, userInput):
        if userInput[pygame.K_RIGHT]:
            self.x += self.velx
        if userInput[pygame.K_LEFT]:
            self.x -= self.velx
        if userInput[pygame.K_UP]:
            self.y -= self.vely
        if userInput[pygame.K_DOWN]:
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

player = Spaceship(250, 500)

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


