import pygame
from Characters import Character

curPlayer = 10
attack1 = 10
attack2 = 10
attack3 = 10
attack4 = 10
pOneHp = 10
pTwoHp = 10
topDamage = 0
bottomDamage = 0
winner = 0
playOne = 10
playTwo = 10

# font declaration
def runGameScreen(choiceOne, choiceTwo):
    global curPlayer, attack2, attack1, attack3, attack4, pOneHp, pTwoHp, playOne, playTwo
    pygame.font.init()
    myfont = pygame.font.Font('Pokemon GB.ttf', 19)
    smallerFont = pygame.font.Font('Pokemon GB.ttf', 18)
    #playOne = 10
   # playTwo = 10

    # color declarations
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (124, 252, 0)
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    # character declarations
    spongebob = Character("Spongebob", 100, ("Fry", 15), ("Drive", 40),("Breathe", 5), ("The Lid", 10), "Character Images/SpongeBobFront.png", "Character Images/SpongebobBack.png")
    patrick = Character("Patrick", 100, ("Firmly Grasp It", 10), ("Mayonnaise", 15), ("Yellow", 5), ("Wombo", 40), "Character Images/PatrickFront.png", "Character Images/PatrickBack.png")
    squidward = Character("Squidward", 100, ("Snowball", 15), ("Clarinet", 10), ("Canned Bread", 5), ("Seabear", 40), "Character Images/SquidwardFront.png", "Character Images/SquidwardBack.png")
    sandy = Character("Sandy", 100, ("Lassoh", 5), ("Hibernation", 10), ("Karate", 15), ("Alaskian Bull Worm", 40), "Character Images/SandyFront.png", "Character Images/SandyBack.png")
    mrKrabs = Character("Mr. Krabs", 100, ("String Coin", 5), ("Secret Formula", 15), ("Kraby Patty", 10), ("Pearl", 40), "Character Images/PlanktonFront.png", "Character Images/PlanktonBack.png")
    plankton = Character("Plankton", 100, ("Robot Slam", 40), ("Chum Bucket", 10), ("Steal", 15), ("Karen", 5), "Character Images/KrabsFront.png", "Character Images/KrabsBack.png")

    print(choiceOne)
    print(choiceTwo)
    if choiceOne == "squid_char":
        playOne = squidward
    elif choiceOne == "star_char":
        playOne = patrick
    elif choiceOne == "sponge_char":
        playOne = spongebob
    elif choiceOne == "plank_char":
        playOne = plankton
    elif choiceOne == "krabs_char":
        playOne = mrKrabs
    elif choiceOne == "squirrel_char":
        playOne = sandy

    if choiceTwo == "squid_char":
        playTwo = squidward
    elif choiceTwo == "star_char":
        playTwo = patrick
    elif choiceTwo == "sponge_char":
        playTwo = spongebob
    elif choiceTwo == "plank_char":
        playTwo = plankton
    elif choiceTwo == "krabs_char":
        playTwo = mrKrabs
    elif choiceTwo == "squirrel_char":
        playTwo = sandy

    # picture declarations
    textBox = pygame.image.load("Character Images/textBox.jpg")
    textBox = pygame.transform.scale(textBox, (1320, 200))
    bottomHealthBar = pygame.image.load("Character Images/bottom char bar.jpg")
    topHealthBar = pygame.image.load("Character Images/top char bar.jpg")

    # spongebob
    SBfront = pygame.image.load(spongebob.imgFront)
    SBback = pygame.image.load(spongebob.imgBack)
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
    nameOne = myfont.render('Patrick', False, black)
    nameTwo = myfont.render('Sandy', False, black)
    attack1 = myfont.render('Attack 1', False, black)
    attack2 = myfont.render('Attack 2', False, black)
    attack3 = myfont.render('Attack 3', False, black)
    attack4 = myfont.render('Attack 4', False, black)
    if playOne == patrick:
        nameOne = myfont.render('Patrick', False, black)
    elif playOne == sandy:
        nameOne = myfont.render('Sandy', False, black)
    elif playOne == squidward:
        nameOne = myfont.render('Squidward', False, black)
    elif playOne == mrKrabs:
        nameOne = myfont.render('Mr. Krabs', False, black)
    elif playOne == spongebob:
        nameOne = myfont.render('Spongebob', False, black)
    elif playOne == plankton:
        nameOne = myfont.render('Plankton', False, black)

    if playTwo == patrick:
        nameTwo = myfont.render('Patrick', False, black)
    elif playTwo == sandy:
        nameTwo = myfont.render('Sandy', False, black)
    elif playTwo == squidward:
        nameTwo = myfont.render('Squidward', False, black)
    elif playTwo == mrKrabs:
        nameTwo = myfont.render('Mr. Krabs', False, black)
    elif playTwo == spongebob:
        nameTwo = myfont.render('Spongebob', False, black)
    elif playTwo == plankton:
        nameTwo = myfont.render('Plankton', False, black)

    attack1 = myfont.render(playOne.attack1[0], False, black)
    attack2 = myfont.render(playOne.attack2[0], False, black)
    attack3 = myfont.render(playOne.attack3[0], False, black)
    attack4 = myfont.render(playOne.attack4[0], False, black)
    fightTXT = myfont.render('FIGHT', False, black)
    runTXT = myfont.render('RUN', False, black)
    topDamage = 0
    bottomDamage = 0
    pOneHp = smallerFont.render(str(playOne.health - bottomDamage), False, black)
    pTwoHp = smallerFont.render(str(playTwo.health - topDamage), False, black)
    hp = smallerFont.render('HP:', False, black)
    totalHealth = myfont.render('/100', False, black)
    curPlayer = playOne





    # creating the physical game screen
    screen = pygame.display.set_mode((1360, 768))
    def blitGameScreen():
        global topDamage, bottomDamage, pOneHp, pTwoHp
        pOneHp = smallerFont.render(str(playOne.health - bottomDamage), False, black)
        pTwoHp = smallerFont.render(str(playTwo.health - topDamage), False, black)
        screen.fill(white)
        screen.blit(topHealthBar, (185, 60))
        screen.blit(bottomHealthBar, (980, 485))
        screen.blit(pTwoHp, (275, 100))
        screen.blit(hp, (215, 80))
        pygame.draw.line(screen, green, [280, 85], [480 - topDamage * 2, 85], 10)
        screen.blit(pOneHp, (1070, 520))
        screen.blit(hp, (1010, 502))
        pygame.draw.line(screen, green, [1070, 505], [1270 - bottomDamage * 2, 505], 10)
        screen.blit(totalHealth, (330, 100))
        screen.blit(totalHealth, (1135, 520))
        screen.blit(textBox, (60, 570))
        screen.blit(nameTwo, (215, 45))
        screen.blit(nameOne, (1120, 450))
        if playOne == patrick:
            screen.blit(Patback, (90, 325))
        elif playOne == sandy:
            screen.blit(Sandyback, (90, 325))
        elif playOne == squidward:
            screen.blit(Squidback, (90, 325))
        elif playOne == mrKrabs:
            screen.blit(Krabsback, (90, 325))
        elif playOne == spongebob:
            screen.blit(SBback, (90, 325))
        elif playOne == plankton:
            screen.blit(Plankback, (90, 325))

        if playTwo == patrick:
            screen.blit(Patfront, (1000, 25))
        elif playTwo == sandy:
            screen.blit(Sandyfront, (1000, 25))
        elif playTwo == squidward:
            screen.blit(Squidfront, (1000, 25))
        elif playTwo == mrKrabs:
            screen.blit(Krabsfront, (1000, 25))
        elif playTwo == spongebob:
            screen.blit(SBfront, (1000, 25))
        elif playTwo == plankton:
            screen.blit(Plankfront, (1000, 25))
        screen.blit(fightTXT, (1030, 620))
        screen.blit(runTXT, (1030, 690))
        screen.blit(attack1, (150, 620))
        screen.blit(attack2, (150, 690))
        screen.blit(attack3, (450, 620))
        screen.blit(attack4, (450, 690))
        pygame.display.update()

    def swapTurn(attNum):
        global curPlayer, attack1, attack2, attack3, attack4, topDamage, bottomDamage, winner
        if curPlayer == playOne:
            if attNum == 1:
                topDamage = topDamage + curPlayer.attack1[1]
            elif attNum == 2:
                topDamage = topDamage + curPlayer.attack2[1]
            elif attNum == 3:
                topDamage = topDamage + curPlayer.attack3[1]
            elif attNum == 4:
                topDamage = topDamage + curPlayer.attack4[1]
            curPlayer = playTwo
        else:
            if attNum == 1:
                bottomDamage = bottomDamage + curPlayer.attack1[1]
            elif attNum == 2:
                bottomDamage = bottomDamage + curPlayer.attack2[1]
            elif attNum == 3:
                bottomDamage = bottomDamage + curPlayer.attack3[1]
            elif attNum == 4:
                bottomDamage = bottomDamage + curPlayer.attack4[1]
            curPlayer = playOne
        attack1 = myfont.render(curPlayer.attack1[0], False, black)
        attack2 = myfont.render(curPlayer.attack2[0], False, black)
        attack3 = myfont.render(curPlayer.attack3[0], False, black)
        attack4 = myfont.render(curPlayer.attack4[0], False, black)
        blitGameScreen()
        if topDamage >= 100:
            print("Player One Won")
            return False
            winner = 0
        elif bottomDamage >= 100:
            print("Player Two Won")
            winner = 1
            return False
        else:
            return True

    def blitGameOverScreen():
        global winner, playOne, playTwo
        bigfont = pygame.font.Font('Pokemon GB.ttf', 40)

        if winner == 0:
            spongebobVictory = pygame.image.load("Character Images/spongebobVictory.png")
            spongebobVictory = pygame.transform.scale(spongebobVictory, (1360, 768))
            screen.blit(spongebobVictory, (0, 0))
            winnerTXT = bigfont.render('Player 1 Wins!', False, black)
            screen.blit(winnerTXT, (420, 354))
        else:
            spongebobVictory = pygame.image.load("Character Images/spongebobVictory.png")
            spongebobVictory = pygame.transform.scale(spongebobVictory, (1360, 768))
            screen.blit(spongebobVictory, (0, 0))
            winnerTXT = bigfont.render('Player 2 Wins!', False, black)
            screen.blit(winnerTXT, (420, 354))

        gameOverTXT = bigfont.render('Game over!', False, black)
        screen.blit(gameOverTXT, (450, 304))

        pygame.display.update()

    blitGameScreen()

    playing = True
    while playing:
        for _ in pygame.event.get():
            mouse_loc = pygame.mouse.get_pos()
            if _.type == pygame.MOUSEBUTTONDOWN:
                if 130 < mouse_loc[0] < 295 and 605 < mouse_loc[1] < 640:
                    print("attack 1!")
                    playing = swapTurn(1)
                if 130 < mouse_loc[0] < 305 and 680 < mouse_loc[1] < 705:
                    print("attack 2!")
                    playing = swapTurn(2)
                if 440 < mouse_loc[0] < 605 and 615 < mouse_loc[1] < 645:
                    print("attack 3!")
                    playing = swapTurn(3)
                if 440 < mouse_loc[0] < 605 and 680 < mouse_loc[1] < 710:
                    print("attack4!")
                    playing = swapTurn(4)
                if 1020 < mouse_loc[0] < 1120 and 615 < mouse_loc[1] < 645:
                    print("fight button!")
                if 1020 < mouse_loc[0] < 1100 and 680 < mouse_loc[1] < 710:
                    print("run button!")
            if _.type == pygame.QUIT:
                playing = False
    print("game over!")

    blitGameOverScreen()



