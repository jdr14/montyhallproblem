import random

select = 0
changeWins = 0
stayWins = 0

for i in range(10):
    doors = ["prize", "nothin1", "nothin2"]

    random.shuffle(doors)
    #print(doors)

    select = 0
    #print(doors[select])

    if doors[select] == "nothin1" or "prize":
        doors.remove("nothin2")
    else:
        doors.remove("nothin1")
    #print(doors)

    select = 1
    print(doors[select])



#Change Strategy
for i in range(100000):
    doors = ["prize", "nothin1", "nothin2"]
    random.shuffle(doors)

    select = 0

    if doors[select] == "nothin1" or "prize":
        doors.remove("nothin2")
    else:
        doors.remove("nothin1")

    select = 1

    if doors[select] == "prize":
        changeWins += 1

    

#Stay Strategy
for i in range(100000):
    doors = ["prize", 1, 2]
    random.shuffle(doors)

    if doors[select] == 1 or "prize":
        doors.remove(2)
    elif doors[select] == 2:
        doors.remove(1)

    if doors[select] == "prize":
        stayWins += 1

#print("Changed Door Strategy: ", changeWins)
#print("Staying Door Strategy: ", stayWins)


winsStay = 0
winsChange = 0

for i in range(100000):
    doors = [0, 1, 2]
    prize = random.choice(doors)
    select = random.choice(doors)
    open = list(set(doors) - set([prize, select]))[0]
    other = list(set([prize, select]) - set([select, open]))[0]
    if select == prize:
        winsStay += 1
    elif other == prize:
        winsChange += 1

print("Changed Door Strategy: ", winsChange)
print("Staying Door Strategy: ", winsStay)
        

