import pygame

pygame.display.init()

# font declaration
pygame.font.init()
myfont = pygame.font.Font('Pokemon GB.ttf', 19)
smallerFont = pygame.font.Font('Pokemon GB.ttf', 18)


# color declarations
white = (255, 255, 255)
black = (0, 0, 0)
green = (124, 252, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

# picture declarations
textBox = pygame.image.load("Character Images/textBox.jpg")
textBox = pygame.transform.scale(textBox, (1320, 200))
bottomHealthBar = pygame.image.load("Character Images/bottom char bar.jpg")
topHealthBar = pygame.image.load("Character Images/top char bar.jpg")

# spongebob
SBfront = pygame.image.load("Character Images/SpongebobFront.png")
SBback = pygame.image.load("Character Images/SpongebobBack.png")
SBfront = pygame.transform.scale(SBfront, (210, 210))
SBback = pygame.transform.scale(SBback, (250, 250))
# patrick
Patfront = pygame.image.load("Character Images/PatrickFront.png")
Patback = pygame.image.load("Character Images/PatrickBack.png")
Patfront = pygame.transform.scale(Patfront, (220, 220))
Patback = pygame.transform.scale(Patback, (250, 250))
# squidward
Squidfront = pygame.image.load("Character Images/SquidwardFront.png")
Squidback = pygame.image.load("Character Images/SquidwardBack.png")
Squidfront = pygame.transform.scale(Squidfront, (220, 220))
Squidback = pygame.transform.scale(Squidback, (245, 245))
# sandy
Sandyfront = pygame.image.load("Character Images/SandyFront.png")
Sandyback = pygame.image.load("Character Images/SandyBack.png")
Sandyfront = pygame.transform.scale(Sandyfront, (250, 250))
Sandyback = pygame.transform.scale(Sandyback, (250, 250))
# plankton
Plankfront = pygame.image.load("Character Images/PlanktonFront.png")
Plankback = pygame.image.load("Character Images/PlanktonBack.png")
Plankfront = pygame.transform.scale(Plankfront, (230, 220))
Plankback = pygame.transform.scale(Plankback, (220, 240))
# mr. krabs
Krabsfront = pygame.image.load("Character Images/KrabsFront.png")
Krabsback = pygame.image.load("Character Images/KrabsBack.png")
Krabsfront = pygame.transform.scale(Krabsfront, (220, 220))
Krabsback = pygame.transform.scale(Krabsback, (250, 250))


# text to blit to screen
PAT = myfont.render('Patrick', False, black)
SANDY = myfont.render('Sandy', False, black)
fightTXT = myfont.render('FIGHT', False, black)
runTXT = myfont.render('RUN', False, black)
attack1 = myfont.render('Attack 1', False, black)
attack2 = myfont.render('Attack 2', False, black)
attack3 = myfont.render('Attack 3', False, black)
attack4 = myfont.render('Attack 4', False, black)
hp = smallerFont.render('HP:', False, black)
totalHealth = myfont.render('/100', False, black)


# creating the physical game screen
screen = pygame.display.set_mode((1360, 768))
screen.fill(white)
screen.blit(topHealthBar, (185, 60))
screen.blit(bottomHealthBar, (980, 485))
screen.blit(hp, (215, 80))
pygame.draw.line(screen, green, [280, 85], [480, 85], 10)
screen.blit(hp, (1010, 502))
pygame.draw.line(screen, green, [1070, 505], [1270, 505], 10)
screen.blit(totalHealth, (330, 100))
screen.blit(totalHealth, (1135, 520))
screen.blit(textBox, (60, 570))
screen.blit(SANDY, (215, 45))
screen.blit(PAT, (1120, 450))
screen.blit(Plankback, (90, 325))
screen.blit(Plankfront, (1000, 25))
screen.blit(fightTXT, (1030, 620))
screen.blit(runTXT, (1030, 690))
screen.blit(attack1, (150, 620))
screen.blit(attack2, (150, 690))
screen.blit(attack3, (450, 620))
screen.blit(attack4, (450, 690))



pygame.display.update()

playing = True
while playing:
    for _ in pygame.event.get():
        mouse_loc = pygame.mouse.get_pos()
        if _.type == pygame.MOUSEBUTTONDOWN:
            if 130 < mouse_loc[0] < 295 and 605 < mouse_loc[1] < 640:
                print("attack 1!")
            if 130 < mouse_loc[0] < 305 and 680 < mouse_loc[1] < 705:
                print("attack 2!")
            if 440 < mouse_loc[0] < 605 and 615 < mouse_loc[1] < 645:
                print("attack 3!")
            if 440 < mouse_loc[0] < 605 and 680 < mouse_loc[1] < 710:
                print("attack4!")
            if 1020 < mouse_loc[0] < 1120 and 615 < mouse_loc[1] < 645:
                print("fight button!")
            if 1020 < mouse_loc[0] < 1100 and 680 < mouse_loc[1] < 710:
                print("run button!")