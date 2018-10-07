class Character(object):
	def __init__(self, name, health, power, defense, moveSet):
		self.name = name
		self.health = health
		self.power = power
		self.defense = defense
		self.moveSet = moveSet
		self.status = 'Null'


class Move(object):
	def __init__(self, name, atk, acc, statEffect):
		self.name = name
		self.atk = atk
		self.acc = acc

#spongebob
moves = [Move('Patty Flip', 75, 50, 'Burn'), Move('Jelly Catch', 80, 40, 'Root'), Move('Bubbles', 100, 25, 'Blind'), Move('Inflate Arms', 0, 0, 'State Change')]
sponge = Character('Spongebob Squarepants', 300, 50, 100, moves)


#patrick
moves = [Move('Replace Brain', 0, 0, 'BuffA'), Move('Fried Oyster Skins', 75, 50, 'Sleep'), Move('Throw Rocky', 9999, 10, 'OTK')]#Patricks moves
star = Character('Patrick Star',500, 75, 25, moves)


#sandy
moves = [Move('Lassooooo', 25, 80, 'Bind'), Move('Alaskan Bull Worm', 9999, 1, 'Area'),Move('Karate Chop', 75, 50, 'N'), Move('Hibernate', 0, 0, 'State Change')]
squirrel = Character('Sandy Cheeks', 100, 150, 25, moves)

hibernatingSquirrel = 5 #input later


#mr krabs
moves = [Move('Me First Dollar', 80, 50, 'N'), Move('Robo Krabs / Chum Krabs', 0, 0, 'State Change'), Move('Withdraw', 0, 0, 'BuffD')]
crab = Character('Mr. Krabs', 150, 25, 500, moves)

#plankton
moves = [Move('Steal Formula', 0, 75, 'Steal Move'), Move('Chum Bot', 0, 0, 'State Change'), Move('Chum Blaster', 75, 50, 'N')]
plankton = Character('Sheldon Plankton', 25, 10, 500, moves)


#squidward
moves = [Move('Play Clarinet', 0, 0, 'Debuff'), Move('Throw Clarinet', 75, 50, 'N'), Move('Squilliam', 0, 0, 'State Change')]
squid = Character('Squidward Tortellini', 100, 100, 100, moves)



#larry the lobster

#gary

#doodle bob
