import  sys
import pygame
from   settings import Settings
from   ship import Ship
import game_functions as gf

# Define a function to run the game
def run_game():
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship= Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
run_game()


















