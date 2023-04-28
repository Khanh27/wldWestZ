from tkinter.constants import DISABLED, NORMAL
import tkinter as tk
import storyInterface as SM
import statTest as st
import sys
import os

savedChoice1 = ""
savedChoice2 = ""
savedChoice3 = ""

savedStory = ""

userHealth = ""
userStrength=""
userIntelligence=""
userCharisma =""
userFood = ""

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.pics()
        self.create_stats_and_names()
        self.create_story_and_decisions()
        self.createButtons()
        #self.loadStory
        #self.saveGame(saveChoice1)

    def create_stats_and_names(self):
        characterStat = st.stat()
        characterStat.getHealth()

        global userHealth
        global userStrength
        global userIntelligence
        global userCharisma
        global userFood

        # name
        self.name = tk.Label(self)
        self.name["text"] = "name"
        self.name.grid(row=4, column=1, pady=2, padx=50)

        # health
        self.health = tk.Label(self)
        self.health["text"] = "Health : " + str(characterStat.getHealth())
        self.health.grid(row=1, column=3, pady=2)
        userHealth = str(characterStat.getHealth())

        # food
        self.food = tk.Label(self)
        self.food["text"] = "Food: " + str(characterStat.getFood())
        self.food.grid(row=2, column=3, pady=2)
        userFood = str(characterStat.getFood())

        # stats
        self.Intelligence = tk.Label(self)
        self.Intelligence["text"] = "Intelligence: " + str(characterStat.getIntelligence())
        self.Intelligence.grid(row=3, column=3, pady=2)
        userIntelligence = str(characterStat.getIntelligence())

        self.Strength = tk.Label(self)
        self.Strength["text"] = "Strength: " + str(characterStat.getStrength())
        self.Strength.grid(row=4, column=3, pady=2)
        userStrength = str(characterStat.getStrength())

        self.Charisma = tk.Label(self)
        self.Charisma["text"] = "Charisma: " + str(characterStat.getCharisma())
        self.Charisma.grid(row=5, column=3, pady=2)
        userCharisma = str(characterStat.getCharisma())

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
            self.decisionsPlaceholder1 = "Start"
            self.decisionsPlaceholder2 = "Start"
            self.decisionsPlaceholder3 = "Start"

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

            global savedStory

            if(self.Checkbutton1.get()):
                self.decision2.config(state=DISABLED)
                self.decision3.config(state=DISABLED)

                tempStoryText, fullDecisionText = sI.choiceSelection("a")

                savedChoice1 = fullDecisionText[0]
                savedChoice2 = fullDecisionText[1]
                savedChoice3 = fullDecisionText[2]
                #self.saveChoices(fullDecisionText[0])
                self.decision1.deselect()
                checkBox_reset()

            if(self.Checkbutton2.get()):
                self.decision1.config(state=DISABLED)
                self.decision3.config(state=DISABLED)
                tempStoryText, fullDecisionText = sI.choiceSelection("b")
                savedChoice1 = fullDecisionText[0]
                savedChoice2 = fullDecisionText[1]
                savedChoice3 = fullDecisionText[2]
                self.decision2.deselect()
                checkBox_reset()

            if(self.Checkbutton3.get()):
                self.decision1.config(state=DISABLED)
                self.decision2.config(state=DISABLED)
                tempStoryText, fullDecisionText = sI.choiceSelection("c")
                savedChoice1 = fullDecisionText[0]
                savedChoice2 = fullDecisionText[1]
                savedChoice3 = fullDecisionText[2]
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

            f = open("savefile1.txt",'r')
            lines = f.readlines()
            loadStats_and_choices = lines
            print(loadStats_and_choices[5])

            savedStory = str(loadStats_and_choices[8])
            #loadFullDecisions = sI.choiceSelection("a")
            #loadFullDecisions = 

            self.story.config(text=savedStory)
            self.decision1.config(text=str(loadStats_and_choices[5]))
            self.decision2.config(text=str(loadStats_and_choices[6]))
            self.decision3.config(text=str(loadStats_and_choices[7]))

            #return loadStats_and_choices

        global savedStory

        # story
        self.story = tk.Label(self)
        self.story["text"] = savedStory
        self.story.grid(row=10, column=1, pady=30, padx=50)


        # load game
        self.loadGame = tk.Button(self)
        self.loadGame["text"] = "Load Game"
        self.loadGame["command"] = loadGame
        self.loadGame.grid(row=2, column=0, pady=2)

        

        self.decision1 = tk.Checkbutton(
            self, text=self.decisionsPlaceholder1, variable=self.Checkbutton1, disabledforeground="gray", command=checkBox_check)
        # To check if a state is checked. Do checkDecision1.get(). If its return 1, then it's checked, otherwise it's not

        self.decision2 = tk.Checkbutton(
            self, text=self.decisionsPlaceholder2, variable=self.Checkbutton2, disabledforeground="gray", command=checkBox_check)

        self.decision3 = tk.Checkbutton(
            self, text=self.decisionsPlaceholder3, variable=self.Checkbutton3, disabledforeground="gray", command=checkBox_check)

        # Have 3 multiple choice boxes, where 1 can be selected. After it has been selected call decisionsPlaceholder()
        # tempStoryText, decisionsPlaceholder = sI.choiceSelection("a")
        self.decision1.grid(row=15, column=0, pady=1, padx=2)
        self.decision2.grid(row=16, column=0, pady=1, padx=2)
        self.decision3.grid(row=17, column=0, pady=1, padx=2)

    def createButtons(self):

        # new game
        self.newGame = tk.Button(self)
        self.newGame["text"] = "New Game"
        self.newGame["command"] = self.resetGame
        self.newGame.grid(row=1, column=0, pady=2)

        
        #saveGame
        self.saveGameButton = tk.Button(self)
        self.saveGameButton["text"] = "Save Game"
        self.saveGameButton["command"] = lambda: self.saveGame(userHealth, userFood, userStrength, userCharisma, userIntelligence, savedChoice1, savedChoice2, savedChoice3, savedStory)
        self.saveGameButton.grid(row=3, column=0, pady=2)

        # quit btton
        self.quit = tk.Button(self, text="quit application", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=4, column=0, pady=2)

    def say_new_game(self):
        print("New Game")

    def say_load_game(self):
        print("Load Game")

    def pics(self):
        self.photo = tk.PhotoImage(file="rsz_1rsz_12.png")
        self.smaller_pic = self.photo.subsample(8, 8)
        self.photoLabel = tk.Label(
            self, image=self.smaller_pic, justify="center", borderwidth=2)
        self.photoLabel.grid(row=3, column=1)

    def saveGame(self, health, food, strength, charisma, intelligence, choice1, choice2, choice3, story):
        f = open("savefile1.txt","w")

        f.write(health)
        f.write("\n")
        f.write(food)
        f.write("\n")
        f.write(strength)
        f.write("\n")
        f.write(charisma)
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
        #print("works2")
        f.close()

    def resetGame(self):  #Code is taken from this website: https://stackoverflow.com/questions/41655618/restart-program-tkinter/41655930
        python = sys.executable
        os.execl(python, python, * sys.argv)

    #def loadStory(self):
    #    global savedChoice 
    #    global savedStory 

    #    f = open("savefile1.txt",'r')
    #    lines = f.readlines()
    #    loadHealth = f.readline()[1:1]
    #    loadStrength = f.readline()[2:2]
    #    loadCharisma = f.readline()[3:3]
    #    loadIntelligence = f.readline()[4:4]
    #    loadChoice = f.readline()[5:5]
    #    loadStory = lines
    #    
    #    print(loadStory[6])
    #    return loadStory

    
root = tk.Tk()
app = Application(master=root)
app.mainloop()
