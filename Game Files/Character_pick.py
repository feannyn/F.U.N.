import pygame

pygame.display.init()
pygame.font.init()

myfont = pygame.font.SysFont('Impact', 32)
nextfont = pygame.font.SysFont('Impact', 22)
randFont = pygame.font.SysFont('Brush Script', 24)
selectFont = pygame.font.SysFont('Rust', 32)
purple = (150, 0, 150)
white = (255, 255, 255)
black = (0, 0, 0)
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
back = pygame.image.load("Character Images/back.png")


gameDisplay = pygame.display.set_mode((850, 600))
gameDisplay.blit(background_image, (0, 0))


pygame.draw.polygon(gameDisplay, purple, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)])
pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)])
pygame.draw.polygon(gameDisplay, white, [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)])
pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)])
pygame.draw.polygon(gameDisplay, purple, [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)])
pygame.draw.polygon(gameDisplay, white, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)])
pygame.draw.polygon(gameDisplay, white, [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)])


# displaying character images on screen
sandy = pygame.transform.scale(sandy, (125, 125))
patrick = pygame.transform.scale(patrick, (120, 120))
spongebob = pygame.transform.scale(spongebob, (110, 110))
squidward = pygame.transform.scale(squidward, (115, 115))
plankton = pygame.transform.scale(plankton, (125, 125))
krabs = pygame.transform.scale(krabs, (115, 115))
random = pygame.transform.scale(random, (100, 100))
back = pygame.transform.scale(back, (30, 30))

gameDisplay.blit(sandy, (40, 390))
gameDisplay.blit(patrick, (190, 320))
gameDisplay.blit(spongebob, (195, 470))
gameDisplay.blit(squidward, (500, 320))
gameDisplay.blit(plankton, (500, 470))
gameDisplay.blit(krabs, (635, 390))
gameDisplay.blit(random, (350, 385))
gameDisplay.blit(back, (10, 10))

pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200), 1)
pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200), 1)
pygame.draw.rect(gameDisplay, black, (720, 540, 80, 40))
gameDisplay.blit(back, (10, 10))

# displaying labels
player1 = myfont.render('Player One', False, black)
player2 = myfont.render('Player Two', False, black)
randomFont = randFont.render('Random', False, black)
next = myfont.render('NEXT', False, white)
selectP1 = selectFont.render('Select Player One...', False, black)
selectP2 = selectFont.render('Now, select an opponent', False, black)


gameDisplay.blit(player1, (131, 250))
gameDisplay.blit(player2, (530, 250))
gameDisplay.blit(randomFont, (365, 475))
gameDisplay.blit(selectP1, (175, 20))
gameDisplay.blit(next, (730, 540))


def drawP1():
    drawInfoDisplay()
    gameDisplay.blit(selectP2, (390, 20))
    if Finalp1 == "squid_char":
        gameDisplay.blit(squidward, (150, 100))
    elif Finalp1 == "star_char":
        gameDisplay.blit(patrick, (150, 100))
    elif Finalp1 == "sponge_char":
        gameDisplay.blit(spongebob, (150, 100))
    elif Finalp1 == "plank_char":
        gameDisplay.blit(plankton, (150, 100))
    elif Finalp1 == "krabs_char":
        gameDisplay.blit(krabs, (150, 100))
    elif Finalp1 == "squirrel_char":
        gameDisplay.blit(sandy, (150, 100))

    pygame.display.update()




def drawInfoDisplay():
    gameDisplay.blit(background_image, (0, 0))
    squidHex = pygame.draw.polygon(gameDisplay, purple, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)])
    starHex = pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)])
    randomHex = pygame.draw.polygon(gameDisplay, white, [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)])
    spongeHex = pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)])
    planktonHex = pygame.draw.polygon(gameDisplay, purple, [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)])
    krabHex = pygame.draw.polygon(gameDisplay, white, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)])
    squirrelHex = pygame.draw.polygon(gameDisplay, white, [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)])

    # Placing Characters into the Hexagons
    gameDisplay.blit(sandy, (40, 390))
    gameDisplay.blit(patrick, (190, 320))
    gameDisplay.blit(spongebob, (195, 470))
    gameDisplay.blit(squidward, (500, 320))
    gameDisplay.blit(plankton, (500, 470))
    gameDisplay.blit(krabs, (635, 390))
    gameDisplay.blit(random, (350, 385))

    # Character image and information blocks
    go_Back = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
    character_Img = pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200), 1)
    character_Stats = pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200), 1)
    gameDisplay.blit(player1, (131, 250))
    gameDisplay.blit(player2, (530, 250))
    gameDisplay.blit(randomFont, (365, 475))
    pygame.draw.rect(gameDisplay, black, (720, 540, 80, 40))
    gameDisplay.blit(next, (730, 540))
    gameDisplay.blit(selectP1, (175, 20))
    gameDisplay.blit(back, (10, 10))


pygame.display.update()

#Screen options
playing = True
p1, p2 = False, False

while playing:
    for _ in pygame.event.get():
        mouse_loc = pygame.mouse.get_pos()
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 500 < mouse_loc[0] < 600 and 300 < mouse_loc[1] < 450:
                print("button 4!")
                if p1 == True:  # player one chosen already
                    drawP1()
                    gameDisplay.blit(squidward, (535, 100))
                    char2 = "squid_char"
                    pygame.display.update()
                else:
                    drawInfoDisplay()
                    gameDisplay.blit(squidward, (150, 100))
                    character = "squid_char"
                    pygame.display.update()

            elif 200 < mouse_loc[0] < 299 and 300 < mouse_loc[1] < 450:
                print("button 2!")
                if p1 == True:
                    drawP1()
                    gameDisplay.blit(patrick, (535, 100))
                    char2 = "star_char"
                    pygame.display.update()
                else:
                    drawInfoDisplay()
                    gameDisplay.blit(patrick, (150, 100))
                    character = "star_char"
                    pygame.display.update()
            elif 350 < mouse_loc[0] < 450 and 375 < mouse_loc[1] < 525:
                print("button 7!")

            elif 200 < mouse_loc[0] < 300 and 450 < mouse_loc[1] < 600:
                print("button 3!")
                if p1 == True:
                    drawP1()
                    gameDisplay.blit(spongebob, (535, 100))
                    char2 = "sponge_char"
                    pygame.display.update()
                else:
                    drawInfoDisplay()
                    gameDisplay.blit(spongebob, (150, 100))
                    character = "sponge_char"
                    pygame.display.update()
            elif 500 < mouse_loc[0] < 600 and 450 < mouse_loc[1] < 600:
                print("button 5!")
                if p1 == True:
                    drawP1()
                    gameDisplay.blit(plankton, (535, 100))
                    char2 = "plank_char"
                    pygame.display.update()
                else:
                    drawInfoDisplay()
                    gameDisplay.blit(plankton, (150, 100))
                    character = "plank_char"
                    pygame.display.update()
            elif 50 < mouse_loc[0] < 150 and 375 < mouse_loc[1] < 525:
                print("button 1!")
                if p1 == True:
                    drawP1()
                    gameDisplay.blit(sandy, (535, 100))
                    char2 = "squirrel_char"
                    pygame.display.update()
                else:
                    drawInfoDisplay()
                    gameDisplay.blit(sandy, (150, 100))
                    character = "squirrel_char"
                    pygame.display.update()
            elif 650 < mouse_loc[0] < 750 and 375 < mouse_loc[1] < 525:
                print("button 6!")
                if p1 == True:
                    drawP1()
                    gameDisplay.blit(krabs, (530, 100))
                    char2 = "krabs_char"
                    pygame.display.update()
                else:
                    drawInfoDisplay()
                    gameDisplay.blit(krabs, (150, 100))
                    character = "krabs_char"
                    pygame.display.update()
            elif 720 < mouse_loc[0] < 800 and 540 < mouse_loc[1] < 580:     # clicked next button
                if p1 == False:
                    Finalp1 = str(character)
                    print("player 1 = ", Finalp1)
                    p1 = True
                    drawP1()
                else:   # p1 is True
                    Finalp2 = str(char2)
                    print("player 2 = ", Finalp2)
                    p2 = True

        if _.type == pygame.QUIT:
            playing = False