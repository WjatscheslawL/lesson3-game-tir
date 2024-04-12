import pygame
import random
import constfile as const
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Game Tup")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# set target image
target_img = pygame.image.load("images/zscheibe.png")
target_width = 100
target_height = 100

target_x = random.randint(0, const.SCREEN_WIDTH - target_width)
target_y = random.randint(0, const.SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# eof target image

running = True

while running:
    pass


# eof game
pygame.quit()
