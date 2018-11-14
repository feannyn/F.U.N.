import pygame

pygame.display.init()

purple = (150, 0, 150)
white = (255, 255, 255)
background_image = pygame.image.load('/Users/nicholasfeanny/Documents/Python/group_Project/F.U.N./Character Images/saltySpitoon.jpg')

gameDisplay = pygame.display.set_mode((800, 600))
#gameDisplay.fill(white);
gameDisplay.blit(background_image, (0, 0))


#pygame.draw.polygon(gameDisplay, purple, [(100, 100), (150, 150), (250, 150), (300, 100), (250, 50), (150, 50)])
pygame.draw.polygon(gameDisplay, purple, [(400, 300), (450, 375), (550, 375), (600, 300), (550, 225), (450, 225)])
pygame.draw.polygon(gameDisplay, (15,139,141), [(100, 300), (150, 375), (250, 375), (300, 300), (250, 225), (150, 225)])
pygame.draw.polygon(gameDisplay, (236,154,41), [(250, 375), (300, 450), (400, 450), (450, 375), (400, 300), (300, 300)])
pygame.draw.polygon(gameDisplay, (168,32,26), [(550, 375), (600, 450), (700, 450), (750, 375), (700, 300), (600, 300)])
pygame.draw.polygon(gameDisplay, (168,32,26), [(250, 225), (300, 300), (400, 300), (450, 225), (400, 150), (300, 150)])
pygame.draw.polygon(gameDisplay, (15,139,141), [(550, 225), (600, 300), (700, 300), (750, 225), (700, 150), (600, 150)])
pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))




pygame.display.update()

#Screen options
playing = True

while playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

def createHexagon(points):
    pygame.draw.polygon(gameDisplay, purple, points)