import pygame

pygame.init()

bgcolor = (0, 153, 153)

size = width, height = 1360, 768

gameDisplay = pygame.display.set_mode(size)
background = pygame.Surface(gameDisplay.get_size())

background.fill(bgcolor)

background = background.convert()
pygame.draw.rect(background, (255, 255, 255), (530, 5, 300, 150))  # Coordinate: 530 = x, 5 = y, 300 width, 150 = height
gameDisplay.blit(background, (0, 0))

pygame.display.set_caption('F.U.N.')

pygame.display.init()

playing = True

while playing:
    mouse_loc = pygame.mouse.get_pos()
    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            playing = False
            break
        if _.type == pygame.MOUSEBUTTONDOWN:
            mouse_loc = pygame.mouse.get_pos()
            if 830 > mouse_loc[0] > 530 and 155 > mouse_loc[1] > 5:
                pygame.draw.rect(background, (0, 0, 245), (20, 170, 10, 100))
                pygame.draw.rect(background, (0, 0, 245), (30, 170, 30, 10))
                pygame.draw.rect(background, (0, 0, 245), (30, 190, 30, 10))
                gameDisplay.blit(background, (0, 0))
    if 830 > mouse_loc[0] > 530 and 155 > mouse_loc[1] > 5:
        pygame.draw.rect(background, (255, 0, 0), (530, 5, 300, 150))
        gameDisplay.blit(background, (0, 0))
    else:
        pygame.draw.rect(background, (255, 255, 255), (530, 5, 300, 150))
        gameDisplay.blit(background, (0, 0))



    pygame.display.flip()

pygame.quit()
