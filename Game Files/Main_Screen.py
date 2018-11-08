import pygame

pygame.init()

bgcolor = (0, 153, 153)

size = width, height = 1360, 768

gameDisplay = pygame.display.set_mode(size)
#background = pygame.Surface(gameDisplay.get_size())

#background.fill(bgcolor)

#background = background.convert()

prettyBackground = pygame.image.load("bg.jpg")
prettyBackground = pygame.transform.scale(prettyBackground, (1360, 768))

#pygame.draw.rect(prettyBackground, (255,255,255), (530,5,300,150))

gameDisplay.blit(prettyBackground, (0, 0))

play = pygame.image.load("play.png")
info = pygame.image.load("info.png")
quit = pygame.image.load("quit.png")
play = pygame.transform.scale(play, (500, 200))
info = pygame.transform.scale(info, (500, 200))
quit = pygame.transform.scale(quit, (500, 200))

gameDisplay.blit(play, (10, 10))
gameDisplay.blit(info, (10, 210))
gameDisplay.blit(quit, (10, 410))

pygame.display.set_caption('F.U.N.')

theme = pygame.mixer.Sound("themesong.wav")

theme.play(-1)

pygame.display.init()

playing = True

while playing:
    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            playing = False
            break

    pygame.display.flip()

pygame.quit()
