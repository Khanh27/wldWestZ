class characterStat:
    def __init__(self, name="", intelligence=0, strength=0, bravery=0, health=100, food=100):
        self._characterName = name
        self._characterIntelligence = intelligence
        self._characterStrength = strength
        self._characterBravery = bravery
        self.characterHealth = health
        self.characterFood = food
        self.gameStatus = False

    # getters
    def getName(self):
        return self._characterName

    def getIntelligence(self):
        return self._characterIntelligence

    def getStrength(self):
        return self._characterStrength

    def getBravery(self):
        return self._characterBravery

    def getHealth(self):
        return self.characterHealth

    def getGameStatus(self):
        return self.gameStatus

    def getFood(self):
        return self.characterFood

    # setters
    def setGameStatus(self, x):
        self.gameStatus = x

    def setIntelligence(self, x):
        self._characterIntelligence = x

    def setBravery(self, x):
        self._characterBravery = x

    def setStrength(self, x):
        self._characterStrength = x

    def setName(self, name):
        self._characterName = name

    def setHealth(self, x):
        self.characterHealth = x


##### Child class is down here ############

class userStat(characterStat):
    # def __init__(self, name, weapon, intelligence, strength, Bravery, health, food, ammoAmmount):
    #    super().__init__(name, weapon , intelligence, strength, Bravery, health, food, ammoAmmount)

    def statUpdaterBravery(self):  # increment stat after each choices
        newBravery = self.getBravery()+1
        return newBravery

    def statUpdaterStrength(self):  # increment stat after each choices
        newStrenght = self.getStrength()+1
        return newStrenght

    def statUpdaterIntelligence(self):  # increment stat after each choices
        newIntelligence = self.getIntelligence() + 1
        return newIntelligence

    def totalStat(self, strength, intelligence, bravery):
        return strength + intelligence + bravery

    pass


# ########### TEST ############
# dog = userStat()

# dog.setName("I'm doggo")

# dog.setBravery(10)
# dog.setIntelligence(10)
# dog.setStrength(10)

# userBravery = dog.getBravery()
# userStrength = dog.getStrength()
# userIntelligence = dog.getIntelligence()

# userBravery = dog.statUpdaterBravery()
# userStrength = dog.statUpdaterStrength()
# userIntelligence = dog.statUpdaterIntelligence()

# print(dog.getName())
# print(dog.getBravery())
# print(dog.getIntelligence())
# print(dog.getStrength())
# print(dog.totalStat(userStrength, userBravery, userIntelligence))
# # print(dog.statUpdaterBravery())
