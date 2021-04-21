import random
from enum import Enum


def findApproximateValue(value, percentRange):
    lowestValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowestValue, highestValue)


Event = Enum("Event", ["Chest", "Empty"])

eventDictionary = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}

eventList = list(eventDictionary.keys())
eventProbability = list(eventDictionary.values())

Colours = Enum("Colours", {"Green": "zielony",
                           "Orange": "pomarańczowy",
                           "Purple": "fiolet",
                           "Gold": "złoty"
                           }
               )

chestColoursDictionary = {
    Colours.Green: 0.75,
    Colours.Purple: 0.04,
    Colours.Orange: 0.2,
    Colours.Gold: 0.01
}

chestColourList = tuple(chestColoursDictionary.keys())
chestColoursProbability = tuple(chestColoursDictionary.values())

# rewardsForChest = Enum("rewardsForChest", {"Sword": "Two-Handed Sword",
#                                            "Gold": "1000 Gold",
#                                            "Boots": "leather boots",
#                                            "Crystal": "White Crystal"
#                                            }
#                        )

rewardsForChest = {chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                   for reward in range(len(chestColourList))
                   }

gameLength = 5
goldAcquired = 0

print("Welcome in my game called Dungeon")
print("You have only 5 steps to make, see yourself how much gold you gonna get till the end!")

while gameLength > 0:
    gameAnswer = input("Do you want to move forward?")
    if gameAnswer == "Yes":
        print("Great, lets see what you got...")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        if drawnEvent == Event.Chest:
            print("Great you won a CHEST!")
            drawnChest = random.choices(chestColourList, chestColoursProbability)[0]
            print("the chest color is...", drawnChest)
            gamerReward = findApproximateValue(rewardsForChest[drawnChest], 10)
            goldAcquired = gamerReward + goldAcquired
        elif drawnEvent == Event.Empty:
            print("Sorry you got nothing!")
        print(drawnEvent)
    else:
        print("You can go just straight man, nothing else, this game is simple")
        continue
    gameLength = gameLength - 1

print("Congrats!! You have won: ", goldAcquired, "gold")

if __name__ == '__main__':
    pass
