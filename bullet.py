import pygame
from   pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self, ai_settings, screen, ship):
        ''' create a bullet at ship position'''
        super(Bullet,self).__init__()
        self.screen = screen

        # create a rectangle of bullet, than set right position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # use float number indicate position of bullet
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


