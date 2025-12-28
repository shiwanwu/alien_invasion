import  pygame
from    pygame.sprite import Sprite

class Alien(Sprite):
    ''' indicate a single alien'''
    def __init__(self, ai_settings, screen):
        ''' initialize alien and set it's initial position'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # laod alien images and set it's rect property
        self.image = pygame.image.load('images/alien_resized.bmp')
        self.rect = self.image.get_rect()

        # every alien present at left top corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store precise position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        ''' draw alien at specified position'''
        self.screen.blit(self.image, self.rect)






