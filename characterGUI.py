
from tkinter.constants import DISABLED, NORMAL
import tkinter as tk
import storyInterface as SM
import sys
import os
import characterStat as CS


stClass = CS.characterStat()

savedChoice1 = ""
savedChoice2 = ""
savedChoice3 = ""

savedStory = "You wake at dusk. \n The sun’s red glow stings your eyes and silhouettes the city skyline through the 13th floor office windows. \n Outside the office door, zombies roam and groan. You need to escape."

userHealth = ""
userStrength = ""
userIntelligence = ""
userBravery = ""
userFood = ""
decision_array = []
answer = ""
answer2 = ""
answerKey = ""


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.pics()
        self.create_stats_and_names()
        self.create_story_and_decisions()
        self.createButtons()

    def create_stats_and_names(self):
        characterStat = CS.characterStat()
        characterStat.getHealth()

        global userHealth
        global userStrength
        global userIntelligence
        global userBravery
        global userFood

        # name
        self.name = tk.Label(self)
        self.name["text"] = "name"
        self.name.grid(row=4, column=1, pady=2, padx=50)

        # health
        self.health = tk.Label(self)
        self.health["text"] = "Health : " + str(characterStat.getHealth())
        self.health.grid(row=4, column=3, pady=2)
        userHealth = str(characterStat.getHealth())

        # food
        self.food = tk.Label(self)
        self.food["text"] = "Food: " + str(characterStat.getFood())
        self.food.grid(row=5, column=3, pady=2)
        userFood = str(characterStat.getFood())

        # stats
        self.Intelligence = tk.Label(self)
        self.Intelligence["text"] = "Intelligence: " + \
            str(characterStat.getIntelligence())
        self.Intelligence.grid(row=6, column=3, pady=2)
        userIntelligence = str(characterStat.getIntelligence())

        self.Strength = tk.Label(self)
        self.Strength["text"] = "Strength: " + str(characterStat.getStrength())
        self.Strength.grid(row=7, column=3, pady=2)
        userStrength = str(characterStat.getStrength())

        self.Bravery = tk.Label(self)
        self.Bravery["text"] = "Bravery: " + str(characterStat.getBravery())
        self.Bravery.grid(row=8, column=3, pady=2)
        userBravery = str(characterStat.getBravery())

    def create_story_and_decisions(self):

        # Create story class
        sI = SM.storyInterface()
        tempStoryText = ""
        self.decisionsPlaceholder1 = ""
        self.decisionsPlaceholder2 = ""
        self.decisionsPlaceholder3 = ""

        self.Checkbutton1 = tk.BooleanVar()
        self.Checkbutton2 = tk.BooleanVar()
        self.Checkbutton3 = tk.BooleanVar()
        self.checkLoad = tk.BooleanVar()

        if (sI.current_decision_Identifier == ""):
            tempStoryText = "Intro Text"
            self.decisionsPlaceholder1 = "Search the office"
            self.decisionsPlaceholder2 = "Open the office door"
            self.decisionsPlaceholder3 = "Beak the window"

        # Resets greyed boxes back to nomal color
        def checkBox_reset():
            if(self.Checkbutton1.get() == False):
                self.decision2.config(state=NORMAL)
                self.decision3.config(state=NORMAL)

            if(self.Checkbutton2.get() == False):
                self.decision1.config(state=NORMAL)
                self.decision3.config(state=NORMAL)

            if(self.Checkbutton3.get() == False):
                self.decision1.config(state=NORMAL)
                self.decision2.config(state=NORMAL)

        # function for making the checkbox grey out after picking one decision
        def checkBox_check():
            global savedChoice1
            global savedChoice2
            global savedChoice3
            global answer
            global answer2
            global answerKey

            global savedStory
            global decision_array

            if(self.Checkbutton1.get()):
                self.decision2.config(state=DISABLED)
                self.decision3.config(state=DISABLED)

                tempStoryText, fullDecisionText, decisionStats = sI.choiceSelection(
                    "a")

                savedChoice1 = fullDecisionText[0]

                sI.set_storage_decision_Identifier(
                    savedChoice1)  # store decision here
                answer = sI.get_storage_decision_Identifier()
                answerKey = answer[-2]

                print(answerKey)

                stClass.setHealth(decisionStats[0])
                stClass.setFood(decisionStats[1])
                stClass.setStrength(decisionStats[2])
                stClass.setIntelligence(decisionStats[3])
                stClass.setBravery(decisionStats[4])

                self.health.config(
                    text=("Health : " + str(stClass.getHealth())))

                self.food.config(text=("Food: " + str(stClass.getFood())))

                self.Intelligence.config(text="Intelligence: " +
                                         str(stClass.getIntelligence()))

                self.Strength.config(text="Strength: " +
                                     str(stClass.getStrength()))

                self.Bravery.config(text="Bravery: " +
                                    str(stClass.getBravery()))

                self.decision1.deselect()
                checkBox_reset()

            if(self.Checkbutton2.get()):
                self.decision1.config(state=DISABLED)
                self.decision3.config(state=DISABLED)
                tempStoryText, fullDecisionText, decisionStats = sI.choiceSelection(
                    "b")
                sI.set_storage_decision_Identifier(fullDecisionText[0])
                sI.set_storage_decision_Identifier(fullDecisionText[1])
                sI.set_storage_decision_Identifier(fullDecisionText[2])

                stClass.setHealth(decisionStats[0])
                stClass.setFood(decisionStats[1])
                stClass.setStrength(decisionStats[2])
                stClass.setIntelligence(decisionStats[3])
                stClass.setBravery(decisionStats[4])

                self.health.config(
                    text=("Health : " + str(stClass.getHealth())))

                self.food.config(text=("Food: " + str(stClass.getFood())))

                self.Intelligence.config(text="Intelligence: " +
                                         str(stClass.getIntelligence()))

                self.Strength.config(text="Strength: " +
                                     str(stClass.getStrength()))

                self.Bravery.config(text="Bravery: " +
                                    str(stClass.getBravery()))

                self.decision2.deselect()
                checkBox_reset()

            if(self.Checkbutton3.get()):
                self.decision1.config(state=DISABLED)
                self.decision2.config(state=DISABLED)
                tempStoryText, fullDecisionText, decisionStats = sI.choiceSelection(
                    "c")
                sI.set_storage_decision_Identifier(fullDecisionText[0])
                sI.set_storage_decision_Identifier(fullDecisionText[1])
                sI.set_storage_decision_Identifier(fullDecisionText[2])

                stClass.setHealth(decisionStats[0])
                stClass.setFood(decisionStats[1])
                stClass.setStrength(decisionStats[2])
                stClass.setIntelligence(decisionStats[3])
                stClass.setBravery(decisionStats[4])

                self.health.config(
                    text=("Health : " + str(stClass.getHealth())))

                self.food.config(text=("Food: " + str(stClass.getFood())))

                self.Intelligence.config(text="Intelligence: " +
                                         str(stClass.getIntelligence()))

                self.Strength.config(text="Strength: " +
                                     str(stClass.getStrength()))

                self.Bravery.config(text="Bravery: " +
                                    str(stClass.getBravery()))

                self.decision3.deselect()
                checkBox_reset()

            self.decision1.config(text=str(fullDecisionText[0]))
            self.decision2.config(text=str(fullDecisionText[1]))
            self.decision3.config(text=str(fullDecisionText[2]))

            savedStory = tempStoryText
            self.story.config(text=savedStory)

        def loadGame():
            global savedStory
            global savedChoice1
            global savedChoice2
            global savedChoice3

            f = open("savefile1.txt", 'r')
            lines = f.readlines()
            loadStats_and_choices = lines

            pseudoKey = loadStats_and_choices[5].split()
            storyKey = pseudoKey[0]

            savedStory, savedDecisions, savedStat = sI.getStoryText(storyKey)

            print(savedStory)

            self.story.config(text=savedStory)
            self.decision1.config(text=savedDecisions[0])
            self.decision2.config(text=savedDecisions[1])
            self.decision3.config(text=savedDecisions[2])

            self.health.config(
                text=("Health : " + str(savedStat[0])))

            self.food.config(text=("Food: " + str(savedStat[1])))

            self.Intelligence.config(text="Intelligence: " +
                                     str(savedStat[2]))

            self.Strength.config(text="Strength: " +
                                 str(savedStat[3]))

            self.Bravery.config(text="Bravery: " +
                                str(savedStat[4]))

        global savedStory
        # story
        self.story = tk.Label(self)
        self.story["text"] = savedStory
        self.story.grid(row=10, column=1, pady=30, padx=50)

        # load game
        self.loadGame = tk.Button(self)
        self.loadGame["text"] = "Load Game"
        self.loadGame["command"] = loadGame
        self.loadGame.grid(row=5, column=0, pady=2)

        self.decision1 = tk.Checkbutton(
            self, text=self.decisionsPlaceholder1, variable=self.Checkbutton1, disabledforeground="gray", command=checkBox_check)
        # To check if a state is checked. Do checkDecision1.get(). If its return 1, then it's checked, otherwise it's not
        self.decision2 = tk.Checkbutton(
            self, text=self.decisionsPlaceholder2, variable=self.Checkbutton2, disabledforeground="gray", command=checkBox_check)

        self.decision3 = tk.Checkbutton(
            self, text=self.decisionsPlaceholder3, variable=self.Checkbutton3, disabledforeground="gray", command=checkBox_check)

        # Have 3 multiple choice boxes, where 1 can be selected. After it has been selected call decisionsPlaceholder()
        self.decision1.grid(row=15, column=0, pady=1, padx=2)
        self.decision2.grid(row=16, column=0, pady=1, padx=2)
        self.decision3.grid(row=17, column=0, pady=1, padx=2)

    def createButtons(self):
        sI = SM.storyInterface()
        global decision_array

        # new game
        self.newGame = tk.Button(self)
        self.newGame["text"] = "New Game"
        self.newGame["command"] = self.resetGame
        self.newGame.grid(row=4, column=0, pady=2)

        # saveGame
        self.saveGameButton = tk.Button(self)
        self.saveGameButton["text"] = "Save Game"
        self.saveGameButton["command"] = lambda: self.saveGame(
            userHealth, userFood, userStrength, userBravery, userIntelligence, answerKey, savedChoice2, savedChoice3, savedStory)
        #self.saveGameButton["command"] = self.getStuffs
        self.saveGameButton.grid(row=6, column=0, pady=2)

        # quit btton
        self.quit = tk.Button(self, text="quit application", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=7, column=0, pady=2)

    def pics(self):
        self.photo = tk.PhotoImage(file="1.png")
        self.smaller_pic = self.photo.subsample(4, 4)
        self.photoLabel = tk.Label(
            self, image=self.smaller_pic, justify="center", borderwidth=2)
        self.photoLabel.grid(row=3, column=1)

    def saveGame(self, health, food, strength, Bravery, intelligence, choice1, choice2, choice3, story):
        f = open("savefile1.txt", "w", encoding="utf-8")

        f.write(health)
        f.write("\n")
        f.write(food)
        f.write("\n")
        f.write(strength)
        f.write("\n")
        f.write(Bravery)
        f.write("\n")
        f.write(intelligence)
        f.write("\n")
        f.write(choice1)
        f.write("\n")
        f.write(choice2)
        f.write("\n")
        f.write(choice3)
        f.write("\n")
        f.write(story)
        f.write("\n")
        f.close()

    def resetGame(self):  # Code is taken from this website: https://stackoverflow.com/questions/41655618/restart-program-tkinter/41655930
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def getStuffs(self, array):  # gets global decision array and try to read it
        sI = SM.storyInterface()
        var = sI.get_storage_decision_Identifier(array)
        print(var)


root = tk.Tk()
root.title("Choose-Your-Own-Adventure Zombie World")

app = Application(master=root)
app.mainloop()
