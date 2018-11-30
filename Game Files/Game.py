import pygame

pygame.display.init()

# color declarations
white = (255, 255, 255)

# creating the physical game screen
screen = pygame.display.set_mode((850, 600))
screen.fill(white)

pygame.display.update()


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
