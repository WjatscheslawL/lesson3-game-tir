import pygame
import constfile as const
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Game Tup")
icon = pygame.image.load("assets")


running = True

while running:
    pass


# eof game
pygame.quit()
