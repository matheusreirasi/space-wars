import pygame, sys
from button import Button
from components import Spaceship_1

pygame.init()


#### main config ####
win_width = 1140
win_height = 620

win = pygame.display.set_mode((win_width, win_height))

background_image_menu = pygame.transform.scale(pygame.image.load("assets/background-image-menu.png"),(win_width, win_height))



def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

    

def play():

    pygame.display.set_caption("Space Wars")


    # Load and Size Images
    background_image_game = pygame.transform.scale(pygame.image.load('assets/background.png'), (win_width, win_height))
    player = Spaceship_1(win_width/2, 500)
            
    # Draw Game
    def draw_game():
        win.fill((0, 0, 0))
        win.blit(background_image_game, (0, 0))
        player.update(win)
        pygame.time.delay(30)
        pygame.display.update()



    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main_menu()

        #### Player configs ####
        userInput = pygame.key.get_pressed()

        player.move_spaceship(userInput)

        #### Players collided ####
        
        draw_game()


        pygame.display.update()



def options():
    while True:
        pygame.display.set_caption("Options")

        win.fill("white")

        choose_planet = get_font(45).render("Choose Planet.", True, "Black")
        win.blit(choose_planet, (pygame.display.get_window_size()[0]/2 - choose_planet.get_width()/2, pygame.display.get_window_size()[1]/6))

        choose_spaceship = get_font(45).render("Choose Spaceship.", True, "Black")
        win.blit(choose_spaceship, ((pygame.display.get_window_size()[0]/2 - choose_planet.get_width()/2)-50, ((2*pygame.display.get_window_size()[1])/3)-50))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main_menu()

        pygame.display.update()



def main_menu():
    while True:
        win.blit(background_image_menu, (0, 0))
        

        pygame.display.set_caption("Menu")

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Space Wars", True, "#8e6fb1")
        menu_rectangle = menu_text.get_rect(center=(win.get_width()/2, 100))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(win.get_width()/2, 250), text_input="PLAY", font=get_font(75), base_color="#82e1aa", hovering_color="White")

        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(win.get_width()/2, 400), text_input="OPTIONS", font=get_font(75), base_color="#82e1aa", hovering_color="White")

        exit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(win.get_width()/2, 550), text_input="EXIT", font=get_font(75), base_color="#82e1aa", hovering_color="White")

        win.blit(menu_text, menu_rectangle)

        for button in [play_button, options_button, exit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if exit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



main_menu()


## Para a imagem ficar bem enquadrada, o tamanho da tela padrão deve ser 1140x620
## Quando eu uso o scroll também muda o menu, o scroll é considerado um click do mouse