import pygame
import random
import constfile as const
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Game Tup")
icon = pygame.image.load("image/sniper-team.jpg")
pygame.display.set_icon(icon)

# set target image
target_img = pygame.image.load("image/zscheibe.jpg")
target_width = 100
target_height = 100

target_x = random.randint(0, const.SCREEN_WIDTH - target_width)
target_y = random.randint(0, const.SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# eof target image

running = True

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y+target_height:
                target_x = random.randint(0, const.SCREEN_WIDTH - target_width)
                target_y = random.randint(0, const.SCREEN_HEIGHT - target_height)
    screen .blit(target_img, (target_x, target_y))
    pygame.display.update()

# eof game
pygame.quit()
