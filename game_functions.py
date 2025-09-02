import sys
from bullet import Bullet
import pygame
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """
    响应按键和鼠标事件
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings,screen, ship, bullets):
    ''' 响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_dwn = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event, ship):
    ''' 响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_dwn = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def update_screen(ai_settings, screen, ship, aliens, bullets) -> object:
    """
    更新屏幕上的图像，并切换到新屏幕
    :rtype: object
    """
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最新绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    ''' 更新子弹的位置，并删除已经消失的子弹'''
    # 更新子弹的位置
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    ''' 如果还没有到达限制，就发射一枚子弹'''
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    ''' create aliens fleet'''
    # create a single alien, and calc how many aliens could be putted in
    # distance of alien is the width of a single alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(avaliable_space_x / (2 * alien_width))

    # create first line of aliens
    for alien_number in range(number_alien_x):
        # create a alien and add it at current line
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)







