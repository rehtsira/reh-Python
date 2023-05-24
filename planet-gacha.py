import sys, time, random, math

welcomeMsg = """
=====================
       \  :  /
    `. __/ \__ .'
    _ _\     /_ _
       /_   _\\
     .'  \ /  `.
       /  :  \\
        Gacha
=====================
"""

characters = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "*** Pluto ***", "*** Eris ***", "*** Ceres *** "]
rarity = [5, 5, 5, 5, 5, 5, 5, 5, 0.5, 0.5, 0.5]

def welcome():
    print(welcomeMsg)
    time.sleep(0.5)

def initialPlayerMoney():
    print("Please play responsibly.")
    try:
        initialMoney = input("How much money would you like to add? [$10 per pull with a max of $1000]\n")
        if int(initialMoney) > int(1000):
            print("The max limit you can add is $1000")
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()
    return initialMoney

def initialPulls():
    initialMoney = initialPlayerMoney()
    pulls = math.floor(int(initialMoney)/10)
    print("You have " + str(pulls) + " total pulls.\n")
    return pulls, initialMoney

def singleWish():
    wish = str(random.choices(characters, rarity))
    time.sleep(0.5)
    print(wish)
    return wish

def multiWish(inventory):
    for i in range(0,10):
        wishes = singleWish()
        inventory.append(wishes)
    return wishes

def gacha():
    welcome()
    pulls, initialMoney = initialPulls()
    inventory = []
    try:
        while pulls > 0:
            wishType = input("Enter s for a single pull, m for a 10 pull\n" + str(pulls) + " wishes remaining.\n" )
            if wishType == 's' and pulls > 0:
                wish = singleWish()
                pulls -= 1
                inventory.append(wish)
                print("Inventory: " + str(inventory))
                balance = int(pulls) * 10
                newBalance = int(initialMoney) - int(balance)
                print("Money spent: $" + str(newBalance))
            elif pulls == 0:
                print("You have run out of pulls!")
                break
            elif wishType == 'm' and pulls < 10:
                print("Not enough wishes for a 10 pull.")
            elif wishType == 'm' and pulls > 0 and pulls >= 10:
                wishes = multiWish(inventory)
                pulls -= 10
                inventory.append(wishes)
                print("Inventory: " + str(inventory))
                balance = int(pulls) * 10
                newBalance = int(initialMoney) - int(balance)
                print("Money spent: $" + str(newBalance))
    except KeyboardInterrupt:
        sys.exit()

gacha()
