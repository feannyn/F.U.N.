import pygame

# initializing basics
pygame.init()
curScreen = 'main_menu'

# setting up background
size = width, height = 1360, 768
gameDisplay = pygame.display.set_mode(size)
prettyBackground = pygame.image.load("bg.jpg")
prettyBackground = pygame.transform.scale(prettyBackground, (1360, 768))
gameDisplay.blit(prettyBackground, (0, 0))

#setting up main menu
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


# defining functions to use during playing loop
def blitYPlay():
    play = pygame.image.load("playyellow.png")
    info = pygame.image.load("info.png")
    quit = pygame.image.load("quit.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    quit = pygame.transform.scale(quit, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(quit, (10, 410))

def blitYInfo():
    play = pygame.image.load("play.png")
    info = pygame.image.load("infoyellow.png")
    quit = pygame.image.load("quit.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    quit = pygame.transform.scale(quit, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(quit, (10, 410))


def blitYQuit():
    play = pygame.image.load("play.png")
    info = pygame.image.load("info.png")
    quit = pygame.image.load("quityellow.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    quit = pygame.transform.scale(quit, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(quit, (10, 410))


def blitMain():
    curScreen = 'main_menu'
    play = pygame.image.load("play.png")
    info = pygame.image.load("info.png")
    quit = pygame.image.load("quit.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    quit = pygame.transform.scale(quit, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(quit, (10, 410))


def checkMain(mouseLoc):
    if 450 > mouseLoc[0] > 100 and 200 > mouseLoc[1] > 30:
        blitYPlay()
    elif 387 > mouseLoc[0] > 67 and  375 > mouse_loc[1] > 150:
        blitYInfo()
    elif 387 > mouseLoc[0] > 67 and  565 > mouseLoc[1] > 415:
        blitYQuit()
    else:
        blitMain()

while playing:
    mouse_loc = pygame.mouse.get_pos()
    for _ in pygame.event.get():
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 450 > mouse_loc[0] > 100 and 200 > mouse_loc[1] > 30:
                curScreen = 'character_select'
        elif _.type == pygame.QUIT:
            playing = False
            break
    if 450 > mouse_loc[0] > 100 and 200 > mouse_loc[1] > 30 and curScreen == 'main_menu':
        blitYPlay()
    elif 387 > mouse_loc[0] > 67 and  375 > mouse_loc[1] > 150 and curScreen == 'main_menu':
        blitYInfo()
    elif 387 > mouse_loc[0] > 67 and  565 > mouse_loc[1] > 415 and curScreen == 'main_menu':
        blitYQuit()
    else:
        blitMain()

#67 225 320 150
#67 415 320 150

    pygame.display.flip()

pygame.quit()
