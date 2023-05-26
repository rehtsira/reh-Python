import sys

heroes = ['Superman', 'Batman', 'Flash']

def showHeroes():
    print(heroes)

def remainingHeroes():
    print("Remaining heroes:\n" + str(heroes))

def addHeroes():
    showHeroes()
    hero = input("Who would you like to add?\n")
    heroes.append(hero)
    remainingHeroes()
    
def removeHeroes():
    showHeroes()
    hero = input("Who would you like to remove?\n")
    heroes.remove(hero)
    remainingHeroes()

def sortHeroes():
    heroes.sort()
    remainingHeroes()

#WIP sortHeroes()
