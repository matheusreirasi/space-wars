#importar as bibliotecas necessarias
import pygame
from pygame.locals import *
from sys import exit

#inicializar as funcoes do pygame
pygame.init()

#configuracoes da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space Wars')

#criacao do loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


