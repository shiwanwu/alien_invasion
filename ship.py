import pygame

class Ship():
    def __init__(self, screen):
        '''
        Initialize the ship and set its starting position.
        Args:
            screen: The game screen surface where the ship will be displayed.
        '''
        self.screen = screen  # Store the screen surface
        #self.image = pygame.image.load('images/airplan.png')  # Load the ship image
        #self.image = pygame.image.load('images/monkey.bmp')  # Load the ship image
        self.image = pygame.image.load('images/monkey_resized.bmp')  # Load the ship image
        self.rect = self.image.get_rect()  # Get the rectangular area of the ship image
        self.screen_rect = screen.get_rect()  # Get the rectangular area of the screen
    # Position the ship at the center bottom of the screen
        self.rect.centerx = self.screen_rect.centerx  # Set the ship's center x-coordinate to match screen's center
        self.rect.bottom = self.screen_rect.bottom  # Set the ship's bottom edge to match screen's bottom edge

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)












