import pygame,modul

#screen = pygame.display.set_mode((900, 600))
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
gun1 = pygame.image.load("images\space_gun1.png")


pygame.draw.rect(screen,[125,125,125],modul.all_modul.rect)
gun1_width=gun1.get_width()
gun1_height=gun1.get_height()
gun1 = pygame.transform.scale(gun1,[gun1_width/10,gun1_height/10])
gun1 = pygame.transform.flip(gun1,True,False)
def draw():
    screen.blit(gun1,[4,2])
    pygame.display.flip()
