import pygame

pygame.font.init()

# pygame.display.init()
charChoice = "na"


def runInfoScreen():
    myFont = pygame.font.SysFont('Rust', 35)
    purple = (150, 0, 150)
    white = (255, 255, 255)
    black = (0, 0, 0)
    display_text = myFont.render('Select a character for more information', False, black)

    # photo variables and modifications
    spongeIMG = pygame.image.load("Character Images/SpongeBobFront.png")
    spongeIMG = pygame.transform.scale(spongeIMG, (125, 125))
    spongeinfo = pygame.image.load("Character Images/spongeinfo.png")

    starIMG = pygame.image.load("Character Images/PatrickFront.png")
    starIMG = pygame.transform.scale(starIMG, (125, 125))
    patrickinfo = pygame.image.load("Character Images/patrickinfo.png")

    squirrelIMG = pygame.image.load("Character Images/SandyFront.png")
    squirrelIMG = pygame.transform.scale(squirrelIMG, (125, 125))
    sandyinfo = pygame.image.load("Character Images/sandyinfo.png")

    squidIMG = pygame.image.load("Character Images/SquidwardFront.png")
    squidIMG = pygame.transform.scale(squidIMG, (125, 125))
    squidwardinfo = pygame.image.load("Character Images/squidwardinfo.png")

    krabIMG = pygame.image.load("Character Images/KrabsFront.png")
    krabIMG = pygame.transform.scale(krabIMG, (125, 125))
    krabsinfo = pygame.image.load("Character Images/krabsinfo.png")

    planktonIMG = pygame.image.load("Character Images/PlanktonFront.png")
    planktonIMG = pygame.transform.scale(planktonIMG, (125, 125))
    plankinfo = pygame.image.load("Character Images/planktoninfo.png")

    backIMG = pygame.image.load("Character Images/back.png")
    backIMG = pygame.transform.scale(backIMG, (30, 30))

    sponge2 = pygame.image.load("Character Images/sponge2.jpg")
    sponge2 = pygame.transform.scale(sponge2, (200, 200))

    pat2 = pygame.image.load("Character Images/pat2.jpg")
    pat2 = pygame.transform.scale(pat2, (200, 200))

    krabs2 = pygame.image.load("Character Images/krabs2.jpg")
    krabs2 = pygame.transform.scale(krabs2, (200, 200))

    plank2 = pygame.image.load("Character Images/plankton2.jpg")
    plank2 = pygame.transform.scale(plank2, (200, 200))

    sandy2 = pygame.image.load("Character Images/sandy2.jpg")
    sandy2 = pygame.transform.scale(sandy2, (200, 200))

    squid2 = pygame.image.load("Character Images/squid2.jpg")
    squid2 = pygame.transform.scale(squid2, (200, 200))

    # Screen set up
    background_image = pygame.image.load("Character Images/info_BG.jpg")
    background_image = pygame.transform.scale(background_image, (1360, 768))
    gameDisplay = pygame.display.set_mode((1360, 768))
    gameDisplay.blit(background_image, (0, 0))
    gameDisplay.blit(display_text, (200, 20))

    spongeHex = pygame.draw.polygon(gameDisplay, white,
                                    [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)], 3)
    starHex = pygame.draw.polygon(gameDisplay, purple,
                                  [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)], 3)
    squirrelHex = pygame.draw.polygon(gameDisplay, white,
                                      [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)], 3)
    randomHex = pygame.draw.polygon(gameDisplay, purple,
                                    [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)], 3)
    squidHex = pygame.draw.polygon(gameDisplay, white,
                                   [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)], 3)
    krabHex = pygame.draw.polygon(gameDisplay, purple,
                                  [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)], 3)
    planktonHex = pygame.draw.polygon(gameDisplay, (15, 139, 141),
                                      [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)], 3)

    # Placing Characters into the Hexagons
    gameDisplay.blit(squirrelIMG, (40, 390))
    gameDisplay.blit(starIMG, (190, 320))
    gameDisplay.blit(spongeIMG, (195, 470))
    gameDisplay.blit(squidIMG, (500, 320))
    gameDisplay.blit(planktonIMG, (500, 470))
    gameDisplay.blit(krabIMG, (635, 390))

    # +250
    def drawInfoDisplay():
        global spongeHex, starHex, squirrelHex, randomHex, squidHex, krabHex, planktonHex, go_Back, character_Img
        global character_Stats, charChoice
        gameDisplay.blit(background_image, (0, 0))
        gameDisplay.blit(display_text, (450, 20))
        spongeHex = pygame.draw.polygon(gameDisplay, white,
                                        [(700, 375), (750, 450), (850, 450), (900, 375), (850, 300), (750, 300)], 3)
        starHex = pygame.draw.polygon(gameDisplay, purple,
                                      [(400, 375), (450, 450), (550, 450), (600, 375), (550, 300), (450, 300)], 3)
        squirrelHex = pygame.draw.polygon(gameDisplay, white,
                                          [(550, 450), (600, 525), (700, 525), (750, 450), (700, 375), (600, 375)], 3)
        randomHex = pygame.draw.polygon(gameDisplay, purple,
                                        [(400, 525), (450, 600), (550, 600), (600, 525), (550, 450), (450, 450)], 3)
        squidHex = pygame.draw.polygon(gameDisplay, white,
                                       [(700, 525), (750, 600), (850, 600), (900, 525), (850, 450), (750, 450)], 3)
        krabHex = pygame.draw.polygon(gameDisplay, purple,
                                      [(850, 450), (900, 525), (1000, 525), (1045, 450), (1000, 375), (900, 375)], 3)
        planktonHex = pygame.draw.polygon(gameDisplay, (15, 139, 141),
                                          [(255, 450), (300, 525), (400, 525), (450, 450), (400, 375), (300, 375)], 3)

        # Placing Characters into the Hexagons
        gameDisplay.blit(squirrelIMG, (290, 390))
        gameDisplay.blit(starIMG, (440, 320))
        gameDisplay.blit(spongeIMG, (445, 470))
        gameDisplay.blit(squidIMG, (750, 320))
        gameDisplay.blit(planktonIMG, (750, 470))
        gameDisplay.blit(krabIMG, (885, 390))

        # Character image and information blocks
        gameDisplay.blit(backIMG, (10, 10))

        if charChoice == "SQUID":
            pygame.draw.rect(gameDisplay, black, (435, 80, 207, 208), 4)
            gameDisplay.blit(squid2, (439, 84))
        elif charChoice == "ST":
            pygame.draw.rect(gameDisplay, black, (435, 80, 207, 208), 4)
            gameDisplay.blit(pat2, (439, 84))
        elif charChoice == "SP":
            pygame.draw.rect(gameDisplay, black, (435, 80, 207, 208), 4)
            gameDisplay.blit(sponge2, (439, 84))
        elif charChoice == "SQUIRREL":
            pygame.draw.rect(gameDisplay, black, (435, 80, 207, 208), 4)
            gameDisplay.blit(sandy2, (439, 84))
        elif charChoice == "PL":
            pygame.draw.rect(gameDisplay, black, (435, 80, 207, 208), 4)
            gameDisplay.blit(plank2, (439, 84))
        elif charChoice == "KR":
            pygame.draw.rect(gameDisplay, black, (435, 80, 207, 208), 4)
            gameDisplay.blit(krabs2, (439, 84))
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

    # MAIN PROGRAM
    while playing == True:
        mouse_loc = pygame.mouse.get_pos()
        for _ in pygame.event.get():
            if _.type == pygame.MOUSEBUTTONDOWN and 10 < mouse_loc[0] < 40 and 10 < mouse_loc[1] < 40:
                charChoice = "na"
                playing = False
            elif _.type == pygame.MOUSEBUTTONDOWN:
                pickChar(mouse_loc)
            if _.type == pygame.QUIT:
                playing = False
        if playing:
            drawInfoDisplay()
