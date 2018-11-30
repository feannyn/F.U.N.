import pygame

pygame.display.init()

# font declaration
pygame.font.init()
myfont = pygame.font.Font('Pokemon GB.ttf', 18)

# color declarations
white = (255, 255, 255)
black = (0, 0, 0)

# picture declarations
textBox = pygame.image.load("Character Images/textBox.jpg")
textBox = pygame.transform.scale(textBox, (520, 140))
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
Sandyfront = pygame.transform.scale(Sandyfront, (220, 220))
Sandyback = pygame.transform.scale(Sandyback, (250, 250))
# plankton
Plankfront = pygame.image.load("Character Images/PlanktonFront.png")
Plankback = pygame.image.load("Character Images/PlanktonBack.png")
Plankfront = pygame.transform.scale(Plankfront, (220, 210))
Plankback = pygame.transform.scale(Plankback, (220, 240))
# mr. krabs
Krabsfront = pygame.image.load("Character Images/KrabsFront.png")
Krabsback = pygame.image.load("Character Images/KrabsBack.png")
Krabsfront = pygame.transform.scale(Krabsfront, (220, 220))
Krabsback = pygame.transform.scale(Krabsback, (250, 250))


# text to blit to screen
SB = myfont.render('Spongebob SquarePants', False, black)

# creating the physical game screen
screen = pygame.display.set_mode((850, 600))
screen.fill(white)
screen.blit(textBox, (8, 470))
screen.blit(SB, (40, 495))
screen.blit(SBback, (25, 225))
screen.blit(Patfront, (600, 45))

pygame.display.update()


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
