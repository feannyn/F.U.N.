import pygame

pygame.display.init()

purple = (150, 0, 150)
white = (255, 255, 255)
background_image = pygame.image.load("Character Images/saltySpitoon.jpg")

gameDisplay = pygame.display.set_mode((850, 600))
gameDisplay.blit(background_image, (0, 0))

hex1 = pygame.draw.polygon(gameDisplay, white, [(450, 375), (500, 450), (600, 450), (650, 375), (600, 300), (500, 300)])
hex2 = pygame.draw.polygon(gameDisplay, purple, [(150, 375), (200, 450), (300, 450), (350, 375), (300, 300), (200, 300)])
hex3 = pygame.draw.polygon(gameDisplay, white, [(300, 450), (350, 525), (450, 525), (500, 450), (450, 375), (350, 375)])
hex4 = pygame.draw.polygon(gameDisplay, purple, [(150, 525), (200, 600), (300, 600), (350, 525), (300, 450), (200, 450)])
hex5 = pygame.draw.polygon(gameDisplay, white , [(450, 525), (500, 600), (600, 600), (650, 525), (600, 450), (500, 450)])
hex6 = pygame.draw.polygon(gameDisplay, purple, [(600, 450), (650, 525), (750, 525), (795, 450), (750, 375), (650, 375)])
hex7 = pygame.draw.polygon(gameDisplay, (15,139,141), [(5, 450), (50, 525), (150, 525), (200, 450), (150, 375), (50, 375)])


character_Img = pygame.draw.rect(gameDisplay, purple, (10, 10, 30, 30))
Character_Stats = pygame.draw.rect(gameDisplay, white, (50, 50, 300, 200))
go_Back = pygame.draw.rect(gameDisplay, white, (450, 50, 300, 200))



pygame.display.update()

#Screen options
playing = True

while playing == True:
    mouse_loc = pygame.mouse.get_pos()
    for _ in pygame.event.get():
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 500 < mouse_loc[0] < 600 and 300 < mouse_loc[1] < 450:

                pass
            elif 200 < mouse_loc[0] < 300 and 300 < mouse_loc[1] < 450:
                pass
            elif 350 < mouse_loc[0] < 450 and 375 < mouse_loc[1] < 525:
                pass
            elif 200 < mouse_loc[0] < 300 and 450 < mouse_loc[1] < 600:
                pass
            elif 500 < mouse_loc[0] < 600 and 450 < mouse_loc[1] < 600:
                pass
            elif 50 < mouse_loc[0] < 150 and 375 < mouse_loc[1] < 525:
                pass

        if _.type == pygame.QUIT:
            playing = False

def createHexagon(points):
    pygame.draw.polygon(gameDisplay, purple, points)


    #Button code
    '''
    while playing:
    mouse_loc = pygame.mouse.get_pos()
    for _ in pygame.event.get():
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 450 > mouse_loc[0] > 100 and 200 > mouse_loc[1] > 30:
                curScreen = 'character_select'
            elif 387 > mouse_loc[0] > 67 and 565 > mouse_loc[1] > 415:
                playing = False
                break
        elif _.type == pygame.QUIT:
            playing = False
            break
    if 450 > mouse_loc[0] > 100 and 200 > mouse_loc[1] > 30 and curScreen == 'main_menu':
        blitYPlay()
    elif 387 > mouse_loc[0] > 67 and  375 > mouse_loc[1] > 150 and curScreen == 'main_menu':
        blitYInfo()
    elif 387 > mouse_loc[0] > 67 and  565 > mouse_loc[1] > 415 and curScreen == 'main_menu':
        blitYQuit()
    else:
        blitMain()
    '''