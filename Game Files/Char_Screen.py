import pygame

pygame.init()

size = width, height = 1360, 768
charDisplay = pygame.display.set_mode(size)
# bgcolor = (127, 255, 212)

charBackground = pygame.image.load("Char_screen.jpg")
charBackground = pygame.transform.scale(charBackground, (1360, 768))


charDisplay.blit(charBackground, (0, 0))

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
