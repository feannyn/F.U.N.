import pygame
import Info

# initializing basics
pygame.init()
curScreen = 'main_menu'

# setting up background
size = width, height = 1360, 768
gameDisplay = pygame.display.set_mode(size)
prettyBackground = pygame.image.load("Character Images/bg.jpg")
prettyBackground = pygame.transform.scale(prettyBackground, (1360, 768))
gameDisplay.blit(prettyBackground, (0, 0))

#setting up main menu
play = pygame.image.load("Character Images/play.png")
info = pygame.image.load("Character Images/info.png")
end = pygame.image.load("Character Images/quit.png")
play = pygame.transform.scale(play, (500, 200))
info = pygame.transform.scale(info, (500, 200))
end = pygame.transform.scale(end, (500, 200))
gameDisplay.blit(play, (10, 10))
gameDisplay.blit(info, (10, 210))
gameDisplay.blit(end, (10, 410))

pygame.display.set_caption('F.U.N.')

theme = pygame.mixer.Sound("Character Images/themesong.wav")

theme.play(-1)

pygame.display.init()

playing = True


# defining functions for the blitting the screen
def blitYPlay():
    global play
    global info
    global end
    play = pygame.image.load("Character Images/playyellow.png")
    info = pygame.image.load("Character Images/info.png")
    end = pygame.image.load("Character Images/quit.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    end = pygame.transform.scale(end, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(end, (10, 410))

def blitYInfo():
    global play
    global info
    global end
    play = pygame.image.load("Character Images/play.png")
    info = pygame.image.load("Character Images/infoyellow.png")
    end = pygame.image.load("Character Images/quit.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    end = pygame.transform.scale(end, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(end, (10, 410))


def blitYQuit():
    global play
    global info
    global end
    play = pygame.image.load("Character Images/play.png")
    info = pygame.image.load("Character Images/info.png")
    end = pygame.image.load("Character Images/quityellow.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    end = pygame.transform.scale(end, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(end, (10, 410))


def blitMain():
    global play
    global info
    global end
    global curScreen
    curScreen = 'main_menu'
    play = pygame.image.load("Character Images/play.png")
    info = pygame.image.load("Character Images/info.png")
    end = pygame.image.load("Character Images/quit.png")
    play = pygame.transform.scale(play, (500, 200))
    info = pygame.transform.scale(info, (500, 200))
    end = pygame.transform.scale(end, (500, 200))
    gameDisplay.blit(prettyBackground, (0, 0))
    gameDisplay.blit(play, (10, 10))
    gameDisplay.blit(info, (10, 210))
    gameDisplay.blit(end, (10, 410))


# functions for resetting the screens
def mainReset(mouseLoc):
    if 450 > mouseLoc[0] > 100 and 200 > mouseLoc[1] > 30:
        blitYPlay()
    elif 387 > mouseLoc[0] > 67 and 375 > mouseLoc[1] > 150:
        blitYInfo()
    elif 387 > mouseLoc[0] > 67 and 565 > mouseLoc[1] > 415:
        blitYQuit()
    else:
        blitMain()

def selectReset(mouseLoc):
    print(mouseLoc)

# selections on each screen
def mainOptions(mouseLoc):
    if 450 > mouseLoc[0] > 100 and 200 > mouseLoc[1] > 30:
        Info.runInfoScreen()
        return True


while playing:
    mouse_loc = pygame.mouse.get_pos()
    for _ in pygame.event.get():
        if _.type == pygame.MOUSEBUTTONDOWN:
            if curScreen == 'main_menu':
                playing = mainOptions(mouse_loc)
        elif _.type == pygame.QUIT:
            playing = False
        if playing == False:
            break
    if curScreen == 'main_menu':
        mainReset(mouse_loc)
    pygame.display.flip()

pygame.quit()
