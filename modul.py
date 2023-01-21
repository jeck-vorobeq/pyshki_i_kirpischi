import pygame
def all_modul():
    screen=pygame.display.get_surface()

    screen_width=screen.get_width()
    screen_height=screen.get_height()
    rect=pygame.rect.Rect(80,2,screen_width-100,screen_height-70)