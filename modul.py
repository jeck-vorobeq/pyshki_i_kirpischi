import pygame,random
def all_modul():
    global rect,rect2,rect3,rect4
    screen=pygame.display.get_surface()

    screen_width=screen.get_width()
    screen_height=screen.get_height()
    offset_left=80
    offset_top=2
    rect=pygame.rect.Rect(offset_left,offset_top,screen_width-100,screen_height-70)


    rect2=pygame.rect.Rect(offset_left,offset_top,screen_width-100,screen_height-500)
    rect3 = pygame.rect.Rect(offset_left, offset_top+100, screen_width - 100, screen_height - 500)
    rect4 = pygame.rect.Rect(offset_left, offset_top+200, screen_width - 100, screen_height - 500)