import random

"""
Game consists of 3 doors, 1 is the prize, 2 are not
1. Player chooses door from 3 doors
2. Host reveals an unselected door without prize
3. Player can choose to change selection to the remaining door
    3a. Player switches
    3b. Player does not switch
4. Prize is revealed
"""

def doorGenerator():
    doors = [0, 0, 0]  # create an empty list of doors
    randomIndex = random.randint(0, 2)
    doors[randomIndex] = 1  # create a prize door with value 1
    return doors

def main():
    print(doorGenerator())

main()