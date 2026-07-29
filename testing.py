import random

input("Press ENTER to roll the dice")
roll = random.randint(1, 6)

if roll == 1:
    print("One")
elif roll == 2:
    print("Two")
elif roll == 3:
    print("Three")
elif roll == 4:
    print("Four")
elif roll == 5:
    print("Five")
else:
    print("Six")