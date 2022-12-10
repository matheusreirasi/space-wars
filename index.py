import pygame
from display import menu, play, gameover

import globals as glb

pygame.init()

window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
pygame.display.set_caption(glb.GAME_TITLE)

menu_page = menu.Menu()
play_page = play.Play()
#options_page = options.Options(window_game)
gameover_page = gameover.GameOver()

user_input = pygame.key.get_pressed()
current_game = 0##por padrão nada será mostrado na tela

while (glb.GAME_SCREEN > 0 and glb.GAME_SCREEN < 5):##será quase sempre verdadeiro
    window_game.fill(glb.GAME_BACKGROUND_COLOR)



    if (glb.GAME_SCREEN == 1):
        menu_page.update()

    if (glb.GAME_SCREEN == 2):
        play_page.update()
    
    #if (glb.GAME_SCREEN == 3):
        #options_page.update()

    if (glb.GAME_SCREEN == 5):
        gameover_page.update()
        
    if (user_input[pygame.K_ESCAPE]):
        glb.GAME_SCREEN = 1

    #print(glb.GAME_SCREEN)

    pygame.display.update()