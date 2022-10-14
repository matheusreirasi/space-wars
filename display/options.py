import pygame, sys

class Options(object):
    def __init__(self):
        super().__init__()
        
        self.win_width = 1140
        self.win_height = 620

        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.win.fill("white")

        pygame.display.set_caption("Options")

    def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)


    while True:
        def setting_planets(self):
            choose_planet = self.get_font(45).render("Choose Planet.", True, "Black")
            self.win.blit(choose_planet, (pygame.display.get_window_size()[0]/2 - choose_planet.get_width()/2, pygame.display.get_window_size()[1]/6))

            choose_spaceship = self.get_font(45).render("Choose Spaceship.", True, "Black")
            self.win.blit(choose_spaceship, ((pygame.display.get_window_size()[0]/2 - choose_planet.get_width()/2)-50, ((2*pygame.display.get_window_size()[1])/3)-50))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

