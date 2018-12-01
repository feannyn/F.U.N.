import pygame
from random import randint

pygame.display.init()
pygame.font.init()
playing = True
p1, p2 = False, False

def runCharSelectionScreen():
    global p1, p2, playing
    myfont = pygame.font.SysFont('Impact', 32)
    # nextfont = pygame.font.SysFont('Impact', 22)
    randFont = pygame.font.SysFont('Brush Script', 24)
    selectFont = pygame.font.SysFont('Rust', 32)
    purple = (150, 0, 150)
    white = (255, 255, 255)
    black = (0, 0, 0)
    background_image = pygame.image.load("Character Images/charScreenBG.jpg")
    background_image = pygame.transform.scale(background_image, (1360, 760))

    # character pick images
    sandy = pygame.image.load("Character Images/SandyFront.png")
    patrick = pygame.image.load("Character Images/PatrickFront.png")
    spongebob = pygame.image.load("Character Images/SpongebobFront.png")
    squidward = pygame.image.load("Character Images/SquidwardFront.png")
    plankton = pygame.image.load("Character Images/PlanktonFront.png")
    krabs = pygame.image.load("Character Images/KrabsFront.png")
    random = pygame.image.load("Character Images/random.png")
    back = pygame.image.load("Character Images/back.png")


    gameDisplay = pygame.display.set_mode((1360, 760))
    gameDisplay.blit(background_image, (0, 0))


    pygame.draw.polygon(gameDisplay, purple, [(700, 375), (750, 450), (850, 450), (900, 375), (850, 300), (750, 300)])
    pygame.draw.polygon(gameDisplay, purple, [(400, 375), (450, 450), (550, 450), (600, 375), (550, 300), (450, 300)])
    pygame.draw.polygon(gameDisplay, white, [(550, 450), (600, 525), (700, 525), (750, 450), (700, 375), (600, 375)])
    pygame.draw.polygon(gameDisplay, purple, [(400, 525), (450, 600), (550, 600), (600, 525), (550, 450), (450, 450)])
    pygame.draw.polygon(gameDisplay, purple, [(700, 525), (750, 600), (850, 600), (900, 525), (850, 450), (750, 450)])
    pygame.draw.polygon(gameDisplay, white, [(850, 450), (900, 525), (1000, 525), (1045, 450), (1000, 375), (900, 375)])
    pygame.draw.polygon(gameDisplay, white, [(255, 450), (300, 525), (400, 525), (450, 450), (400, 375), (300, 375)])


    # displaying character images on screen
    sandy = pygame.transform.scale(sandy, (125, 125))
    patrick = pygame.transform.scale(patrick, (120, 120))
    spongebob = pygame.transform.scale(spongebob, (110, 110))
    squidward = pygame.transform.scale(squidward, (115, 115))
    plankton = pygame.transform.scale(plankton, (125, 125))
    krabs = pygame.transform.scale(krabs, (115, 115))
    random = pygame.transform.scale(random, (100, 100))
    back = pygame.transform.scale(back, (30, 30))

    charImages = [sandy, patrick, spongebob, squidward, plankton, krabs]
    charNames = ["squirrel_char", "star_char", "sponge_char", "squid_char", "plank_char", "krabs_char"]

    gameDisplay.blit(sandy, (290, 390))
    gameDisplay.blit(patrick, (440, 320))
    gameDisplay.blit(spongebob, (445, 470))
    gameDisplay.blit(squidward, (750, 320))
    gameDisplay.blit(plankton, (750, 470))
    gameDisplay.blit(krabs, (890, 390))
    gameDisplay.blit(random, (600, 385))
    gameDisplay.blit(back, (10, 10))

    pygame.draw.rect(gameDisplay, white, (300, 50, 300, 200), 1)
    pygame.draw.rect(gameDisplay, white, (700, 50, 300, 200), 1)
    pygame.draw.rect(gameDisplay, black, (970, 540, 80, 40))
    gameDisplay.blit(back, (10, 10))

    # displaying labels
    player1 = myfont.render('Player One', False, black)
    player2 = myfont.render('Player Two', False, black)
    randomFont = randFont.render('Random', False, black)
    next = myfont.render('NEXT', False, white)
    play = myfont.render('PLAY', False, white)
    selectP1 = selectFont.render('Select Player One...', False, black)
    selectP2 = selectFont.render('Now, select an opponent', False, black)


    gameDisplay.blit(player1, (381, 250))
    gameDisplay.blit(player2, (780, 250))
    gameDisplay.blit(randomFont, (615, 475))
    gameDisplay.blit(selectP1, (425, 20))
    gameDisplay.blit(next, (980, 540))


    def drawP1():
        drawInfoDisplay()
        gameDisplay.blit(selectP2, (640, 20))
        if Finalp1 == "squid_char":
            gameDisplay.blit(squidward, (400, 100))
        elif Finalp1 == "star_char":
            gameDisplay.blit(patrick, (400, 100))
        elif Finalp1 == "sponge_char":
            gameDisplay.blit(spongebob, (400, 100))
        elif Finalp1 == "plank_char":
            gameDisplay.blit(plankton, (400, 100))
        elif Finalp1 == "krabs_char":
            gameDisplay.blit(krabs, (400, 100))
        elif Finalp1 == "squirrel_char":
            gameDisplay.blit(sandy, (400, 100))

        pygame.display.update()




    def drawInfoDisplay():
        global squidHex, starHex, randomHex, planktonHex, spongeHex
        global krabHex, squirrelHex, go_Back, character_Stats, character_Img
        gameDisplay.blit(background_image, (0, 0))
        pygame.draw.polygon(gameDisplay, purple, [(700, 375), (750, 450), (850, 450), (900, 375), (850, 300), (750, 300)])
        pygame.draw.polygon(gameDisplay, purple, [(400, 375), (450, 450), (550, 450), (600, 375), (550, 300), (450, 300)])
        pygame.draw.polygon(gameDisplay, white, [(550, 450), (600, 525), (700, 525), (750, 450), (700, 375), (600, 375)])
        pygame.draw.polygon(gameDisplay, purple, [(400, 525), (450, 600), (550, 600), (600, 525), (550, 450), (450, 450)])
        pygame.draw.polygon(gameDisplay, purple, [(700, 525), (750, 600), (850, 600), (900, 525), (850, 450), (750, 450)])
        pygame.draw.polygon(gameDisplay, white, [(850, 450), (900, 525), (1000, 525), (1045, 450), (1000, 375), (900, 375)])
        pygame.draw.polygon(gameDisplay, white, [(255, 450), (300, 525), (400, 525), (450, 450), (400, 375), (300, 375)])

        # Placing Characters into the Hexagons
        gameDisplay.blit(sandy, (290, 390))
        gameDisplay.blit(patrick, (440, 320))
        gameDisplay.blit(spongebob, (445, 470))
        gameDisplay.blit(squidward, (750, 320))
        gameDisplay.blit(plankton, (750, 470))
        gameDisplay.blit(krabs, (890, 390))
        gameDisplay.blit(random, (600, 385))
        gameDisplay.blit(back, (10, 10))

        # Character image and information blocks
        go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
        character_Img = pygame.draw.rect(gameDisplay, white, (300, 50, 300, 200), 1)
        character_Stats = pygame.draw.rect(gameDisplay, white, (700, 50, 300, 200), 1)
        gameDisplay.blit(player1, (381, 250))
        gameDisplay.blit(player2, (780, 250))
        gameDisplay.blit(randomFont, (615, 475))
        pygame.draw.rect(gameDisplay, black, (970, 540, 80, 40))
        if p1 == True:
            gameDisplay.blit(play, (980, 540))
        else:
            gameDisplay.blit(next, (980, 540))
        gameDisplay.blit(selectP1, (425, 20))
        gameDisplay.blit(back, (10, 10))
        pygame.display.update()


    pygame.display.update()


    def pickChar(mouseLoc):
        global character, char2, p1, playing, p2, Finalp1, Finalp2
        if 750 < mouseLoc[0] < 850 and 300 < mouseLoc[1] < 450:
            if p1 == True:  # player one chosen already
                drawP1()
                gameDisplay.blit(squidward, (785, 100))
                char2 = "squid_char"
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(squidward, (400, 100))
                character = "squid_char"
                pygame.display.update()
        elif 450 < mouseLoc[0] < 549 and 300 < mouseLoc[1] < 450:
            print("button 2!")
            if p1 == True:
                drawP1()
                gameDisplay.blit(patrick, (785, 100))
                char2 = "star_char"
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(patrick, (400, 100))
                character = "star_char"
                pygame.display.update()
        elif 600 < mouseLoc[0] < 700 and 375 < mouseLoc[1] < 525:
            randChar = randint(0, 5)
            if p1 == True:
                drawP1()
                gameDisplay.blit(charImages[randChar], (785, 100))
                char2 = charNames[randChar]
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(charImages[randChar], (400, 100))
                character = charNames[randChar]
                pygame.display.update()
        elif 450 < mouseLoc[0] < 550 and 450 < mouseLoc[1] < 600:
            print("button 3!")
            if p1 == True:
                drawP1()
                gameDisplay.blit(spongebob, (785, 100))
                char2 = "sponge_char"
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(spongebob, (400, 100))
                character = "sponge_char"
                pygame.display.update()
        elif 750 < mouseLoc[0] < 850 and 450 < mouseLoc[1] < 600:
            print("button 5!")
            if p1 == True:
                drawP1()
                gameDisplay.blit(plankton, (785, 100))
                char2 = "plank_char"
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(plankton, (400, 100))
                character = "plank_char"
                pygame.display.update()
        elif 300 < mouseLoc[0] < 400 and 375 < mouseLoc[1] < 525:
            print("button 1!")
            if p1 == True:
                drawP1()
                gameDisplay.blit(sandy, (785, 100))
                char2 = "squirrel_char"
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(sandy, (400, 100))
                character = "squirrel_char"
                pygame.display.update()
        elif 900 < mouseLoc[0] < 1000 and 375 < mouseLoc[1] < 525:
            print("button 6!")
            if p1 == True:
                drawP1()
                gameDisplay.blit(krabs, (785, 100))
                char2 = "krabs_char"
                pygame.display.update()
            else:
                drawInfoDisplay()
                gameDisplay.blit(krabs, (400, 100))
                character = "krabs_char"
                pygame.display.update()
        elif 970 < mouseLoc[0] < 1050 and 540 < mouseLoc[1] < 580:  # clicked next button
            if p1 == False:
                Finalp1 = str(character)
                print("player 1 = ", Finalp1)
                p1 = True
                drawP1()
            else:  # p1 is True
                Finalp2 = str(char2)
                print("player 2 = ", Finalp2)
                p2 = True
        elif 8 < mouseLoc[0] < 40 and 8 < mouseLoc[1] < 40:
            print("back button!")
            playing = False

    # Screen options

    while playing:
        for _ in pygame.event.get():
            mouse_loc = pygame.mouse.get_pos()
            if _.type == pygame.MOUSEBUTTONDOWN:
                pickChar(mouse_loc)
            if _.type == pygame.QUIT:
                playing = False

