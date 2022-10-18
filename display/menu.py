import pygame, sys
from button import Button


import globals as glb

class Menu (object):
    def __init__(self):
        self.window_game = pygame.display.set_mode((glb.GAME_WIDTH, glb.GAME_HEIGHT))
        self.background_image_menu = pygame.transform.scale(pygame.image.load("assets/background-image-menu.png"),(glb.GAME_WIDTH, glb.GAME_HEIGHT))

        self.window_game.blit(self.background_image_menu,(0,0))
        pygame.display.set_caption("Menu")

        def get_font(size):
            return pygame.font.Font("assets/font.ttf", size)


        self.menu_text = get_font(100).render("Calvo Wars", True, "#8e6fb1")
        self.menu_rectangle = self.menu_text.get_rect(center=(glb.GAME_WIDTH/2, 100))

        self.play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(glb.GAME_WIDTH/2, 250), text_input="PLAY", font=get_font(75), base_color="#82e1aa", hovering_color="White")

        self.options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(glb.GAME_WIDTH/2, 400), text_input="OPTIONS", font=get_font(75), base_color="#82e1aa", hovering_color="White")
        
        self.exit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(glb.GAME_WIDTH/2, 550), text_input="EXIT", font=get_font(75), base_color="#82e1aa", hovering_color="White")



        pass


    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        
        self.window_game.blit(self.background_image_menu,(0,0))
        self.menu_text.get_rect()
        self.window_game.blit(self.menu_text,(glb.GAME_WIDTH/2 - self.menu_text.get_width()/2, 60))
        
        for button in [self.play_button, self.options_button, self.exit_button]:
            button.changeColor(self.mouse_pos)
            button.update(self.window_game)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.checkForInput(self.mouse_pos):
                    glb.GAME_SCREEN = 2
                #if self.options_button.checkForInput(self.mouse_pos):
                    #glb.GAME_SCREEN = 3
                if self.exit_button.checkForInput(self.mouse_pos):
                    glb.GAME_SCREEN = 4
                    pygame.quit()
                    sys.exit()

        pass