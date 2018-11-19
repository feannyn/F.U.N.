import pygame

pygame.display.init()

purple = (150, 0, 150)
white = (0, 0, 0)


#photo variables and modifications
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
gameDisplay = pygame.display.set_mode((850, 600))
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
    gameDisplay.blit(squirrelIMG, (40, 390))
    gameDisplay.blit(starIMG, (190, 320))
    gameDisplay.blit(spongeIMG, (195, 470))
    gameDisplay.blit(squidIMG, (500, 320))
    gameDisplay.blit(planktonIMG, (500, 470))
    gameDisplay.blit(krabIMG, (635, 390))
    gameDisplay.blit(randomIMG, (350, 385))

    # Character image and information blocks
    go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
    character_Img = pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200), 1)
    character_Stats = pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200), 1)

#Character image and information blocks
go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
character_Img = pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200), 1)
character_Stats = pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200), 1)
pygame.display.update()

#Screen options
playing = True


#MAIN PROGRAM
while playing == True:
    mouse_loc = pygame.mouse.get_pos()
    for _ in pygame.event.get():
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 500 < mouse_loc[0] < 600 and 300 < mouse_loc[1] < 450:
                print("button 4!")
                drawInfoDisplay()
                gameDisplay.blit(squidIMG, (150, 100))
                pygame.display.update()

                # random button image
                pass
            elif 200 < mouse_loc[0] < 300 and 300 < mouse_loc[1] < 450:
                print("button 2!")
                drawInfoDisplay()
                gameDisplay.blit(starIMG, (150, 100))
                pygame.display.update()
                pass
            elif 350 < mouse_loc[0] < 450 and 375 < mouse_loc[1] < 525:
                print("button 7!")

                pass
            elif 200 < mouse_loc[0] < 300 and 450 < mouse_loc[1] < 600:
                print("button 3!")
                drawInfoDisplay()
                gameDisplay.blit(spongeIMG, (150, 100))
                pygame.display.update()

                pass
            elif 500 < mouse_loc[0] < 600 and 450 < mouse_loc[1] < 600:
                print("button 5!")
                drawInfoDisplay()
                gameDisplay.blit(planktonIMG, (150, 100))
                pygame.display.update()
                pass
            elif 50 < mouse_loc[0] < 150 and 375 < mouse_loc[1] < 525:
                print("button 1!")
                drawInfoDisplay()
                gameDisplay.blit(squirrelIMG, (150, 100))
                pygame.display.update()
                pass
            elif 650 < mouse_loc[0] < 750 and 375 < mouse_loc[1] < 525:
                print("button 6!")
                drawInfoDisplay()
                gameDisplay.blit(krabIMG, (150, 100))
                pygame.display.update()

        if _.type == pygame.QUIT:
            playing = False
