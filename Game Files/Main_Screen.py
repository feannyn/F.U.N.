import pygame

pygame.init()

bgcolor = (0, 153, 153)

size = width, height = 1360, 768

gameDisplay = pygame.display.set_mode(size)
background = pygame.Surface(gameDisplay.get_size())

background.fill(bgcolor)

background = background.convert()

gameDisplay.blit(background, (0, 0))

pygame.display.set_caption('F.U.N.')

pygame.display.init()

playing = True

while playing:
    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            playing = False
            break

    pygame.display.flip()

pygame.quit()
