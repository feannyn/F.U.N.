import pygame

size = width, height = 1360, 768

pygame.display.set_mode(size)

pygame.display.init()

playing = True

while playing:
    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            playing = False
            break