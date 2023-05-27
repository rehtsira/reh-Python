#Playing with lists
import sys, copy

heroes = ['Superman', 'Batman', 'Flash']

def showHeroes():
    print(str(len(heroes)) + " current heroes: " + str(heroes))

def remainingHeroes():
    print(str(len(heroes)) + " remaining heroes:\n" + str(heroes))

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

def backupHeroes():
    showHeroes()
    backupList = copy.copy(heroes)
    print("Hero list backed up.")
    print(backupList)

def heroFunc():
    try:
        while True:
            heroInput = input("Enter 'l' to show list of heroes. 'a' to add a hero. 'r' to remove a hero. 's' to sort heroes. 'b' to backup the hero list, or 'x' to exit.\n")
            if heroInput == 'l':
                showHeroes()
            elif heroInput == 'a':
                addHeroes()
            elif heroInput == 'r':
                removeHeroes()
            elif heroInput == 's':
                sortHeroes()
            elif heroInput == 'b':
                backupHeroes()
            elif heroInput == 'x':
                sys.exit()
            else:
                print("Please enter l, a, r, s, or b")
    except KeyboardInterrupt:
        sys.exit()

heroFunc()
