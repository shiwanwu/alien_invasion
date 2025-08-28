import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        '''
        Initialize the ship and set its starting position.
        Args:
            screen: The game screen surface where the ship will be displayed.
        '''
        self.screen = screen  # Store the screen surface
        self.ai_settings = ai_settings
        #self.image = pygame.image.load('images/airplan.png')  # Load the ship image
        #self.image = pygame.image.load('images/monkey.bmp')  # Load the ship image
        self.image = pygame.image.load('images/monkey_resized.bmp')  # Load the ship image
        self.rect = self.image.get_rect()  # Get the rectangular area of the ship image
        self.screen_rect = screen.get_rect()  # Get the rectangular area of the screen
        # Position the ship at the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx  # Set the ship's center x-coordinate to match screen's center
        self.rect.centery = self.screen_rect.centery  # Set the ship's center y-coordinate to match screen's center
        self.rect.bottom = self.screen_rect.bottom  # Set the ship's bottom edge to match screen's bottom edge
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #移动标志
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_dwn   = False

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)


    def update(self):
        '''
        根据移动标志调整飞船位置
        :return:
        '''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_dwn and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        # 根据self.center 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery








