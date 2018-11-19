import pygame

pygame.display.init()
pygame.font.init()

myfont = pygame.font.SysFont('Impact', 32)
randFont = pygame.font.SysFont('Brush Script', 24)
purple = (150, 0, 150)
white = (255, 255, 255)
background_image = pygame.image.load("Character Images/charScreenBG.jpg")
background_image = pygame.transform.scale(background_image, (850, 600))

# character pick images
sandy = pygame.image.load("Character Images/SandyFront.png")
patrick = pygame.image.load("Character Images/PatrickFront.png")
spongebob = pygame.image.load("Character Images/SpongebobFront.png")
squidward = pygame.image.load("Character Images/SquidwardFront.png")
plankton = pygame.image.load("Character Images/PlanktonFront.png")
krabs = pygame.image.load("Character Images/KrabsFront.png")
random = pygame.image.load("Character Images/random.png")

gameDisplay = pygame.display.set_mode((850, 600))
gameDisplay.blit(background_image, (0, 0))


pygame.draw.polygon(gameDisplay, white, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)], 3)
pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)], 3)
pygame.draw.polygon(gameDisplay, (15, 139, 141), [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)], 3)
pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)], 3)
pygame.draw.polygon(gameDisplay, white, [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)], 3)
pygame.draw.polygon(gameDisplay, purple, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)], 3)
pygame.draw.polygon(gameDisplay, (15,139,141), [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)], 3)


# displaying character images on screen
sandy = pygame.transform.scale(sandy, (125, 125))
patrick = pygame.transform.scale(patrick, (120, 120))
spongebob = pygame.transform.scale(spongebob, (110, 110))
squidward = pygame.transform.scale(squidward, (115, 115))
plankton = pygame.transform.scale(plankton, (125, 125))
krabs = pygame.transform.scale(krabs, (115, 115))
random = pygame.transform.scale(random, (100, 100))

gameDisplay.blit(sandy, (40, 390))
gameDisplay.blit(patrick, (190, 320))
gameDisplay.blit(spongebob, (195, 470))
gameDisplay.blit(squidward, (500, 320))
gameDisplay.blit(plankton, (500, 470))
gameDisplay.blit(krabs, (635, 390))
gameDisplay.blit(random, (350, 385))

pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30), 1)
pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200), 1)
pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200), 1)

# displaying player one and player two labels
player1 = myfont.render('Player One', False, (0, 0, 0))
player2 = myfont.render('Player Two', False, (0, 0, 0))
randomFont = randFont.render('Random', False, (0, 0, 0))
gameDisplay.blit(player1, (131, 211))
gameDisplay.blit(player2, (530, 211))
gameDisplay.blit(randomFont, (365, 475))


def drawInfoDisplay():
    gameDisplay.blit(background_image, (0, 0))
    spongeHex = pygame.draw.polygon(gameDisplay, white, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)], 3)
    starHex = pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)], 3)
    squirrelHex = pygame.draw.polygon(gameDisplay, white, [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)], 3)
    randomHex = pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)], 3)
    squidHex = pygame.draw.polygon(gameDisplay, white, [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)], 3)
    krabHex = pygame.draw.polygon(gameDisplay, purple, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)], 3)
    planktonHex = pygame.draw.polygon(gameDisplay, (15, 139, 141), [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)], 3)

    # Placing Characters into the Hexagons
    gameDisplay.blit(sandy, (40, 390))
    gameDisplay.blit(patrick, (190, 320))
    gameDisplay.blit(spongebob, (195, 470))
    gameDisplay.blit(squidward, (500, 320))
    gameDisplay.blit(plankton, (500, 470))
    gameDisplay.blit(krabs, (635, 390))
    gameDisplay.blit(random, (350, 385))

    # Character image and information blocks
    go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30), 1)
    character_Img = pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200), 1)
    character_Stats = pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200), 1)



pygame.display.update()

#Screen options
playing = True

while playing:
    for _ in pygame.event.get():
        mouse_loc = pygame.mouse.get_pos()
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 500 < mouse_loc[0] < 600 and 300 < mouse_loc[1] < 450:
                print("button 4!")
                drawInfoDisplay()
                gameDisplay.blit(squidward, (150, 100))
                pygame.display.update()
            elif 200 < mouse_loc[0] < 300 and 300 < mouse_loc[1] < 450:
                print("button 2!")
                drawInfoDisplay()
                gameDisplay.blit(patrick, (150, 100))
                pygame.display.update()
            elif 350 < mouse_loc[0] < 450 and 375 < mouse_loc[1] < 525:
                print("button 7!")
            elif 200 < mouse_loc[0] < 300 and 450 < mouse_loc[1] < 600:
                print("button 3!")
                drawInfoDisplay()
                gameDisplay.blit(spongebob, (150, 100))
                pygame.display.update()
            elif 500 < mouse_loc[0] < 600 and 450 < mouse_loc[1] < 600:
                print("button 5!")
                drawInfoDisplay()
                gameDisplay.blit(plankton, (150, 100))
                pygame.display.update()
                pass
            elif 50 < mouse_loc[0] < 150 and 375 < mouse_loc[1] < 525:
                print("button 1!")
                drawInfoDisplay()
                gameDisplay.blit(sandy, (150, 100))
                pygame.display.update()
            elif 650 < mouse_loc[0] < 750 and 375 < mouse_loc[1] < 525:
                print("button 6!")
                drawInfoDisplay()
                gameDisplay.blit(krabs, (150, 100))
                pygame.display.update()
        if _.type == pygame.QUIT:
            playing = False