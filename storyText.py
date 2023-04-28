# gets story string for selcted value / contains the story
fullStoryText = {
    "a": "You search the office. Amongst scattered papers you find an article: “Virus Released Upon the World; Hail Mary Cure World’s Only Hope.” You also uncover a loaded revolver. Handy. Your noisy search draws zombies banging on the office door.",
    "b": "You open the office door. Why did you open the office door? The zombies notice you immediately, and you have nowhere to hide. You barely last 30 seconds.",
    "c": "You break the window. It shatters in a hail of glass and one flying office chair. The sheer 13-floor drop looms in front of you, hundreds of zombies wandering the streets below. The window’s balcony stretches to the left and to the right. Across the office, zombies start banging at the office door",
    "aa": "You break the window. It shatters in a hail of glass, a flying office chair, and... your brand new revolver. Dang! You dropped it off the building. The sheer 13-floor drop looms in front of you, hundreds of zombies wandering the streets below. The window’s balcony stretches to the left and to the right. Across the office, zombies start banging at the office door.",
    "ab": "You shoot the zombies outside the office door. Nice aim! But one of the zombies is less dead than you thought. It bites your ankle as you make your way to the stairs. In the stairwell you face a door opposite you, and you can hear groans coming from below.",
    "ac": "You make a break for the elevators. Unfortunately for you, the elevators are behind a wall of ravenous zombies, and you find yourself playing the highest stakes game of Red Rover the world’s ever seen. You lose",
    "aab": "You slide along the balcony to the left. The air rushes around you, carrying the noise of hundreds of zombie groans. You slide along the balcony until you hit the building’s fire escape.",
    "aaba": "You climb to the ground. The fire escape leads to a dingy alley, but at least it's free of zombies. To the east you spot the edge of a lush forest. To the west is town, and you see the Hail Mary Laboratory, rumored to have developed the cure to the virus, just a block away.",
    "aabaa": "You head towards the forest. To to north lays a lush bit dim path. To the south you see a few wandering zombies. To the east you spy a flash of color.",
    "aabaaa": "You head north. Wandering along the dim forest path, you hear fewer and fewer zombie groans. The more you walk, the more the potential for a cure fades in your mind. You survive and live the rest of your life alone and zombie-free in the forest."
}

# gets Decisions string for each  story / contains the Decisions for the story that is being loaded
fullDecisionText = {
    "a": ["Break the window", "Shoot the zombies outside the office door", "Make a break for the elevators"],
    "aa": ["Jump for it", "Slide along the balcony to the left", "Slide along the balcony to the right"],
    "aab": ["Climb to the ground", "Climb to the roof", "You take your chances inside"],
    "aaba": ["Forget the cure, head towards the forest", "The cure! Head towards Hail Mary", "Forget the cure and the forest, make camp in the alley"],
    "aabaa": ["Head north", "Head south", "Head east"],
    "aabaaa": ["New Game", "New Game", "New Game"],
}

decisionStats = {
    "a": [100, 90, 0, 1, 0],
    "aa": [100, 80, 1, 1, 0],
    "aab": [100, 80, 1, 1, 1],
    "aaba": [100, 70, 1, 1, 1],
    "aabaa": [100, 60, 2, 1, 1],
    "aabaaa": [100, 50, 2, 2, 1],
}
