import pygame
screen = pygame.display.set_mode((900, 600))
import modul

#screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
gun1 = pygame.image.load("images\space_gun1.png")



gun1_width=gun1.get_width()
gun1_height=gun1.get_height()
gun1 = pygame.transform.scale(gun1,[gun1_width/10,gun1_height/10])
gun1 = pygame.transform.flip(gun1,True,False)
def draw():
    screen.blit(gun1,[4,2])

    pygame.draw.rect(screen, [125, 125, 125], modul.rect1)
    for a in modul.rects:
        pygame.draw.rect(screen, [125, 15, 12], a["rect"], 9)
        pygame.draw.rect(screen, [125, 15, 12], a["rect2"], 9)
        pygame.draw.rect(screen, [125, 15, 12], a["rect3"], 9)
    pygame.display.flip()
