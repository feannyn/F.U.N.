import pygame

pygame.display.init()
pygame.font.init()

myfont = pygame.font.SysFont('Impact', 32)
purple = (150, 0, 150)
white = (255, 255, 255)
background_image = pygame.image.load("Character Images/charScreenBG.jpg")
background_image = pygame.transform.scale(background_image, (850, 600))

# character pick images
sandy = pygame.image.load("Character Images/SandyFront.png")
patrick = pygame.image.load("Character Images/PatrickFront.png")
spongebob = pygame.image.load("Character Images/SpongebobFront.png")
sqidward = pygame.image.load("Character Images/SquidwardFront.png")
# plakton = pygame.image.load("Character Image/PlanktonFront.png")
# krabs = pygame.image.load("Character Image/KrabsFront.png")

gameDisplay = pygame.display.set_mode((850, 600))
gameDisplay.blit(background_image, (0, 0))


pygame.draw.polygon(gameDisplay, white, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)])
pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)])
pygame.draw.polygon(gameDisplay, (15, 139, 141), [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)])
pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)])
pygame.draw.polygon(gameDisplay, white , [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)])
pygame.draw.polygon(gameDisplay, purple, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)])
pygame.draw.polygon(gameDisplay, (15,139,141), [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)])


# displaying character images on screen
sandy = pygame.transform.scale(sandy, (125, 125))
patrick = pygame.transform.scale(patrick, (120, 120))
spongebob = pygame.transform.scale(spongebob, (110, 110))
# sqidward = pygame.

gameDisplay.blit(sandy, (40, 390))
gameDisplay.blit(patrick, (190, 320))
gameDisplay.blit(spongebob, (195, 470))

pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200))
pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200))

# displaying player one and player two labels
player1 = myfont.render('Player One', False, (0, 0, 0))
player2 = myfont.render('Player Two', False, (0, 0, 0))
gameDisplay.blit(player1, (131, 211))
gameDisplay.blit(player2, (530, 211))


pygame.display.update()

#Screen options
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False


def createHexagon(points):
    pygame.draw.polygon(gameDisplay, purple, points)