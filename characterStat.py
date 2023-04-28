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

    def setFood(self, x):
        self.characterFood = x


##### Child class is down here ############
class userStat(characterStat):
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
