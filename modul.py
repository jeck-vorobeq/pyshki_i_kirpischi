import pygame
screen=pygame.display.get_surface()
rects=[]
offset_left=80
offset_top=2
screen_width=screen.get_width()
screen_height=screen.get_height()
rect2=pygame.rect.Rect(offset_left,offset_top,screen_width-100,screen_height-500)
rect3 = pygame.rect.Rect(offset_left, offset_top+100, screen_width - 100, screen_height - 500)
rect4 = pygame.rect.Rect(offset_left, offset_top+200, screen_width - 100, screen_height - 500)
rect = {"rect":rect2,"rect2":rect3,"rect3":rect4}
rect1=pygame.rect.Rect(offset_left,offset_top,screen_width-100,screen_height-70)
rects.append(rect)
def all_modul():
    pass


