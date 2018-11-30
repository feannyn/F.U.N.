import pygame

pygame.display.init()
pygame.font.init()

myFont = pygame.font.SysFont('Rust', 35)
purple = (150, 0, 150)
white = (255, 255, 255)
black = (0, 0, 0)

display_text = myFont.render('Select a character for more information', False, black)

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
gameDisplay = pygame.display.set_mode((850, 600))
background_image = pygame.transform.scale(background_image, (850, 600))
gameDisplay.blit(background_image, (0, 0))
gameDisplay.blit(display_text, (200, 20))

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


def drawInfoDisplay():
    gameDisplay.blit(background_image, (0, 0))
    gameDisplay.blit(display_text, (200, 20))
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
    gameDisplay.blit(backIMG, (10, 10))

# Character image and information blocks
gameDisplay.blit(backIMG, (10, 10))

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
                pygame.draw.rect(gameDisplay, black, (246, 71, 207, 208), 4)
                gameDisplay.blit(squid2, (250, 75))
                pygame.display.update()
            elif 200 < mouse_loc[0] < 299 and 300 < mouse_loc[1] < 450:
                print("button 2!")
                drawInfoDisplay()
                pygame.draw.rect(gameDisplay, black, (246, 71, 207, 208), 4)
                gameDisplay.blit(pat2, (250, 75))
                pygame.display.update()
            elif 350 < mouse_loc[0] < 450 and 375 < mouse_loc[1] < 525:
                print("button 7!")
            elif 200 < mouse_loc[0] < 300 and 450 < mouse_loc[1] < 600:
                print("button 3!")
                drawInfoDisplay()
                pygame.draw.rect(gameDisplay, black, (246, 71, 207, 208), 4)
                gameDisplay.blit(sponge2, (250, 75))
                pygame.display.update()
            elif 500 < mouse_loc[0] < 600 and 450 < mouse_loc[1] < 600:
                print("button 5!")
                drawInfoDisplay()
                pygame.draw.rect(gameDisplay, black, (246, 71, 207, 208), 4)
                gameDisplay.blit(plank2, (250, 75))
                pygame.display.update()
            elif 50 < mouse_loc[0] < 150 and 375 < mouse_loc[1] < 525:
                print("button 1!")
                drawInfoDisplay()
                pygame.draw.rect(gameDisplay, black, (246, 71, 207, 208), 4)
                gameDisplay.blit(sandy2, (250, 75))
                pygame.display.update()
            elif 650 < mouse_loc[0] < 750 and 375 < mouse_loc[1] < 525:
                print("button 6!")
                drawInfoDisplay()
                pygame.draw.rect(gameDisplay, black, (246, 71, 207, 208), 4)
                gameDisplay.blit(krabs2, (250, 75))
                pygame.display.update()
            elif 8 < mouse_loc[0] < 40 and 8 < mouse_loc[1] < 40:
                print("back button!")
        if _.type == pygame.QUIT:
            playing = False
