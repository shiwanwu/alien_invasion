import pygame

# 初始化 Pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 安装测试")

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill((0, 128, 255))

    # 绘制一个圆形
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()

