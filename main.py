import pygame
import random
import constfile as const
pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Game - Tup")
icon = pygame.image.load("image/sniper-team.jpg")
pygame.display.set_icon(icon)

font = pygame.font.Font(None, 24)
text = font.render("Gesamt Treffer: ", True, "black")

# set target image
target_img = pygame.image.load("image/zscheibe.jpg")
target_width = 100
target_height = 100

# target_x = random.randint(0, const.SCREEN_WIDTH - target_width)
target_y = random.randint(0, const.SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# eof target image
clock = pygame.time.Clock()

running = True
tref = 0
speed = 5
target_x = 10

while running:

    screen.fill(color)
    target_x += speed
    if target_x > const.SCREEN_WIDTH-50:
        target_x = 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y+target_height:
                tref += 1
                text = font.render(f"К-во попаданий:  {tref}", True, "black")
                # target_x = random.randint(0, const.SCREEN_WIDTH - target_width)
                target_y = random.randint(0, const.SCREEN_HEIGHT - target_height)
<<<<<<< Updated upstream

    screen.blit(text, (20, 20))
    screen.blit(target_img, (target_x, target_y))
    clock.tick(40)

=======
    screen.blit(target_img, (target_x, target_y))
>>>>>>> Stashed changes
    pygame.display.update()

# eof game
pygame.quit()
