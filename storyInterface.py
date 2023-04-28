import characterStat as CS


class storyInterface:
    def __init__(self, current_decision_Identifier="", storage_decision_Identifier=[]):
        # What level are we progressing twoard
        self.current_decision_Identifier = current_decision_Identifier
        # List of each decison made in order
        self.storage_decision_Identifier = storage_decision_Identifier

    # sets a var for the most recenlty selected value from user in order of levels

    def set_current_decision_Identifier(self, new_current_decision_Identifier):
        self.current_decision_Identifier += new_current_decision_Identifier

    # saves each order of selected values one by one in a list for Exporting later
    def set_storage_decision_Identifier(self, decision_selected):
        self.storage_decision_Identifier.append(decision_selected)
        print(self.storage_decision_Identifier)

    def get_storage_decision_Identifier(self):
        return self.storage_decision_Identifier

    # Call upon by GUI to prosss which option the user selected
    def choiceSelection(self, decision_selected):
        if (decision_selected == "a"):
            self.set_current_decision_Identifier("a")
            self.set_storage_decision_Identifier(
                self.current_decision_Identifier)
            return self.getStoryText(self.current_decision_Identifier)

        elif (decision_selected == "b"):
            self.set_current_decision_Identifier("b")
            self.set_storage_decision_Identifier(
                self.current_decision_Identifier)
            return self.getStoryText(self.current_decision_Identifier)

        elif (decision_selected == "c"):
            self.set_current_decision_Identifier("c")
            self.set_storage_decision_Identifier(
                self.current_decision_Identifier)
            return self.getStoryText(self.current_decision_Identifier)
        else:
            print("Error in storyInterface")
        print(self.current_decision_Identifier)

    def choiceSelectionTest(self, decision_selected):

        self.set_current_decision_Identifier(decision_selected)
        self.set_storage_decision_Identifier(
            self.current_decision_Identifier)
        return self.getStoryText(self.current_decision_Identifier)

    # enter a,b,c for value the user selected, will return next StoryText and next DecisionText
    def getStoryText(self, storyKey):
        print(storyKey)

# Iterator Pattern
# gets story string for selcted value / contains the story
        fullStoryText = {
            # 1 a, a, b, a, a, a, a
            "a": "You search the office. Amongst scattered papers you find an article: \n“Virus Released Upon the World; Hail Mary Cure World’s Only Hope.” \nYou also uncover a loaded revolver. Handy. Your noisy search draws zombies banging on the office door.",
            "b": "You open the office door. Why did you open the office door? \nThe zombies notice you immediately, and you have nowhere to hide. You barely last 30 seconds.",
            "aa": "You break the window. It shatters in a hail of glass, a flying office chair, \nand... your brand new revolver. Dang! You dropped it off \nthe building. The sheer 13-floor drop looms in front of you, hundreds of \nzombies wandering the streets below. The window’s balcony stretches to the left and to the right. Across the office, zombies start banging at the office door.",
            "ab": "You shoot the zombies outside the office door. Nice aim! \nBut one of the zombies is less dead than you thought. It bites your ankle as\n you make your way to the stairs. In the stairwell you face a door opposite you, and you can hear groans coming from below.",
            "ac": "You make a break for the elevators. Unfortunately for you,\n the elevators are behind a wall of ravenous zombies, and you find yourself \nplaying the highest stakes game of Red Rover the world’s ever seen. You lose",
            "aab": "You slide along the balcony to the left. The air rushes around you, \ncarrying the noise of hundreds of zombie groans. You slide along \nthe balcony until you hit the building’s fire escape.",
            "aaba": "You climb to the ground. The fire escape leads to a dingy alley, \nbut at least it's free of zombies. To the east you spot the edge of\n a lush forest. To the west is town, and you see the Hail Mary Laboratory, rumored to have developed the cure to the virus, just a block away.",
            "aabaa": "You head towards the forest. To to north lays a lush bit dim path. \nTo the south you see a few wandering zombies. To the east you \nspy a flash of color.",
            "aabaaa": "You head north. Wandering along the dim forest path, you hear fewer\n and fewer zombie groans. The more you walk, the more the\n potential for a cure fades in your mind. You survive and live the rest of your life alone and zombie-free in the forest.",

            # 2 c, c, b, c, a, a
            "c": "You break the window. It shatters in a hail of glass and one flying \noffice chair. The sheer 13-floor drop looms in front of you, \nhundreds of zombies wandering the streets below. The window’s balcony stretches to the left and to the right. \nAcross the office, zombies start banging at the office door",
            "cc": "You slide along the balcony to the right. The air rushes around you, \ncarrying the noise of hundreds of zombie groans. You slide along \nthe balcony until you hit the building’s fire escape.",
            "ccb": "You climb to the roof. Here you get a 360 view of the city. To the east, \nyou spot a building labeled \"Hail Mary Laboratories\". To the \nwest, a lush forest. On the roof is a locked supply shed.",
            "ccbc": "You head towards Hail Mary. You take the stairs down the building\n two at a time, and reach the street unhindered. You sprint to Hail \nMary Laboratories, the cure in mind, when you are greeted by a hoard of zombies guarding the entrance.",
            "ccbca": "You turn back towards the forest. A hoard of zombies?\n No, thank you. In the forest it's a little quieter. To to north lays a lush bit \ndim path. To the south you see a few wandering zombies. To the east you spy a flash of color.",
            "ccbcaa": "You head north. Wandering along the dim forest path,\n you hear fewer and fewer zombie groans. The more you walk, the more the \npotential for a cure fades in your mind. You survive and live the rest of your life alone and zombie-free in the forest.",

        }

        # gets Decisions string for each  story / contains the Decisions for the story that is being loaded
        fullDecisionText = {
            # 1 a, a, b, a, a, a, a
            "a": ["Break the window", "Shoot the zombies outside the office door", "Make a break for the elevators"],
            "aa": ["Jump for it", "Slide along the balcony to the left", "Slide along the balcony to the right"],
            "aab": ["Climb to the ground", "Climb to the roof", "You take your chances inside"],
            "aaba": ["Forget the cure, head towards the forest", "The cure! Head towards Hail Mary", "Forget the cure and the forest, make camp in the alley"],
            "aabaa": ["Head north", "Head south", "Head east"],
            "aabaaa": ["Game Over", "Game Over", "Game Over"],

            # 2 c, c, b, c, a, a
            "c": ["Jump for it", "Slide along the balcony to the left", "Slide along the balcony to the right"],
            "cc": ["Climb to the ground", "Climb to the roof", "Take your chances inside"],
            "ccb": ["Jump into the trees", "Investigate the shed", "Head towards Hail Mary"],
            "ccbc": ["Turn back towards the forest", "Make a break for the door", "Search for a weapon"],
            "ccbca": ["Head north", "Head south", "Head east"],
            "ccbcaa": ["Game Over", "Game Over", "Game Over"],
        }

        decisionStats = {
            # 1 a, a, b, a, a, a, a
            "a": [100, 90, 0, 1, 0],
            "aa": [100, 80, 1, 1, 0],
            "aab": [100, 80, 1, 1, 1],
            "aaba": [100, 70, 1, 1, 1],
            "aabaa": [100, 60, 2, 1, 1],
            "aabaaa": [100, 50, 2, 2, 1],

            # 2 c, c, b, c, a, a
            "c": [100, 90, 1, 0, 0],
            "cc": [100, 90, 1, 0, 1],
            "ccb": [100, 80, 2, 0, 1],
            "ccbc": [100, 70, 2, 1, 1],
            "ccbca": [100, 60, 1, 2, 1],
            "ccbcaa": [100, 50, 2, 3, 1],
        }

        return fullStoryText[storyKey], fullDecisionText[storyKey], decisionStats[storyKey]
