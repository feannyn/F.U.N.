import pygame

# pygame.display.init()
charChoice = "na"
def runInfoScreen():
    purple = (150, 0, 150)
    white = (0, 0, 0)


    # photo variables and modifications
    spongeIMG = pygame.image.load("Character Images/SpongeBobFront.png")
    spongeIMG = pygame.transform.scale(spongeIMG, (125, 125))

    starIMG = pygame.image.load("Character Images/PatrickFront.png")
    starIMG = pygame.transform.scale(starIMG, (125, 125))

    squirrelIMG = pygame.image.load("Character Images/SandyFront.png")
    squirrelIMG = pygame.transform.scale(squirrelIMG, (125, 125))

    squidIMG = pygame.image.load("Character Images/SquidwardFront.png")
    squidIMG = pygame.transform.scale(squidIMG, (125, 125))

    krabIMG = pygame.image.load("Character Images/KrabsFront.png")
    krabIMG = pygame.transform.scale(krabIMG, (125, 125))

    planktonIMG = pygame.image.load("Character Images/PlanktonFront.png")
    planktonIMG = pygame.transform.scale(planktonIMG, (125, 125))

    randomIMG = pygame.image.load("Character Images/random.png")
    randomIMG = pygame.transform.scale(randomIMG, (125, 125))

    #Screen set up
    background_image = pygame.image.load("Character Images/saltySpitoon.jpg")
    background_image = pygame.transform.scale(background_image, (1360, 768))
    gameDisplay = pygame.display.set_mode((1360, 768))
    gameDisplay.blit(background_image, (0, 0))

    spongeHex = pygame.draw.polygon(gameDisplay, white, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)], 3)
    starHex= pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)], 3)
    squirrelHex = pygame.draw.polygon(gameDisplay, white, [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)], 3)
    randomHex = pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)], 3)
    squidHex = pygame.draw.polygon(gameDisplay, white , [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)], 3)
    krabHex = pygame.draw.polygon(gameDisplay, purple, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)], 3)
    planktonHex = pygame.draw.polygon(gameDisplay, (15,139,141), [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)], 3)

    #Placing Characters into the Hexagons
    gameDisplay.blit(squirrelIMG, (40, 390))
    gameDisplay.blit(starIMG, (190, 320))
    gameDisplay.blit(spongeIMG, (195, 470))
    gameDisplay.blit(squidIMG, (500, 320))
    gameDisplay.blit(planktonIMG, (500, 470))
    gameDisplay.blit(krabIMG, (635, 390))
    gameDisplay.blit(randomIMG, (350, 385))

    #Character image and information blocks
    go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
    character_Img = pygame.draw.rect(gameDisplay, white, (320, 50, 300, 200), 1)
    character_Stats = pygame.draw.rect(gameDisplay, white, (720, 50, 300, 200), 1)
    pygame.display.update()

    # +250
    def drawInfoDisplay():
        global spongeHex, starHex, squirrelHex, randomHex, squidHex, krabHex, planktonHex, go_Back, character_Img
        global character_Stats, charChoice
        gameDisplay.blit(background_image, (0, 0))
        spongeHex = pygame.draw.polygon(gameDisplay, white, [(700, 375), (750, 450), (850, 450), (900, 375), (850, 300), (750, 300)], 3)
        starHex = pygame.draw.polygon(gameDisplay, purple, [(400, 375), (450, 450), (550, 450), (600, 375), (550, 300), (450, 300)], 3)
        squirrelHex = pygame.draw.polygon(gameDisplay, white, [(550, 450), (600, 525), (700, 525), (750, 450), (700, 375), (600, 375)], 3)
        randomHex = pygame.draw.polygon(gameDisplay, purple, [(400, 525), (450, 600), (550, 600), (600, 525), (550, 450), (450, 450)], 3)
        squidHex = pygame.draw.polygon(gameDisplay, white, [(700, 525), (750, 600), (850, 600), (900, 525), (850, 450), (750, 450)], 3)
        krabHex = pygame.draw.polygon(gameDisplay, purple, [(850, 450), (900, 525), (1000, 525), (1045, 450), (1000, 375), (900, 375)], 3)
        planktonHex = pygame.draw.polygon(gameDisplay, (15, 139, 141), [(255, 450), (300, 525), (400, 525), (450, 450), (400, 375), (300, 375)], 3)

        # Placing Characters into the Hexagons
        gameDisplay.blit(squirrelIMG, (290, 390))
        gameDisplay.blit(starIMG, (440, 320))
        gameDisplay.blit(spongeIMG, (445, 470))
        gameDisplay.blit(squidIMG, (750, 320))
        gameDisplay.blit(planktonIMG, (750, 470))
        gameDisplay.blit(krabIMG, (885, 390))
        gameDisplay.blit(randomIMG, (600, 385))

        # Character image and information blocks
        go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
        character_Img = pygame.draw.rect(gameDisplay, white, (320, 50, 300, 200), 1)
        character_Stats = pygame.draw.rect(gameDisplay, white, (720, 50, 300, 200), 1)

        if charChoice == "SQUID":
            gameDisplay.blit(squidIMG, (425, 100))
        elif charChoice == "ST":
            gameDisplay.blit(starIMG, (425, 100))
        elif charChoice == "SP":
            gameDisplay.blit(spongeIMG, (425, 100))
        elif charChoice == "SQUIRREL":
            gameDisplay.blit(squirrelIMG, (425, 100))
        elif charChoice == "PL":
            gameDisplay.blit(planktonIMG, (425, 100))
        elif charChoice == "KR":
            gameDisplay.blit(krabIMG, (425, 100))
        pygame.display.update()


    def pickChar(mouseLoc):
        global charChoice
        if 750 < mouseLoc[0] < 850 and 300 < mouseLoc[1] < 450:
            charChoice = "SQUID"
            pass
        elif 450 < mouseLoc[0] < 550 and 300 < mouseLoc[1] < 450:
            charChoice = "ST"
            pass
        elif 600 < mouseLoc[0] < 700 and 375 < mouseLoc[1] < 525:
            print("button 7!")
            pass
        elif 450 < mouseLoc[0] < 550 and 450 < mouseLoc[1] < 600:
            charChoice = "SP"
            pass
        elif 750 < mouseLoc[0] < 850 and 450 < mouseLoc[1] < 600:
            charChoice = "PL"
            pass
        elif 300 < mouseLoc[0] < 400 and 375 < mouseLoc[1] < 525:
            charChoice = "SQUIRREL"
            pass
        elif 900 < mouseLoc[0] < 1000 and 375 < mouseLoc[1] < 525:
            charChoice = "KR"


    drawInfoDisplay()
    pygame.display.update()

    # Screen options
    playing = True


    #MAIN PROGRAM
    while playing == True:
        mouse_loc = pygame.mouse.get_pos()
        for _ in pygame.event.get():
            if _.type == pygame.MOUSEBUTTONDOWN and 10 < mouse_loc[0] < 40 and 10 < mouse_loc[1] < 40:
                playing = False
            elif _.type == pygame.MOUSEBUTTONDOWN:
                pickChar(mouse_loc)
            if _.type == pygame.QUIT:
                playing = False
        if playing:
            drawInfoDisplay()
