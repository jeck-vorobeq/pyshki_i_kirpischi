import pygame

screen = pygame.display.set_mode((900, 600))
gun1 = pygame.image.load("images\space_gun1.png")
gun1_width=gun1.get_width()
gun1_height=gun1.get_height()
gun1 = pygame.transform.scale(gun1,[gun1_width/7,gun1_height/7])
gun1 = pygame.transform.flip(gun1,True,False)
def draw():
    screen.blit(gun1,[4,2])
    pygame.display.flip()
