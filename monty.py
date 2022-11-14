import random
import time

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
    totalIterations = 10
    changeWins = 0
    stayWins = 0

    for i in range(5):
        totalIterations *= 10

        for i in range(totalIterations):
            # Generate a list of 3 doors with a prize randomly hidden behind one of them
            doors = doorGenerator()
    
            # Contestant randomly chooses 1 of the 3 doors
            playerChoiceValue = doors[random.randint(0, 2)]
            
            # Check the choices 
            if (playerChoiceValue == 1):
                stayWins += 1
            else:
                changeWins += 1
        
        # Print the statistics
        print("Iterations {}".format(totalIterations))
        print("\tstayWins   = {}".format(stayWins))
        print("\tchangeWins = {}".format(changeWins))
        

if __name__ == '__main__':
    main()