import random

input("Press ENTER to flip the coin")
flip = random.randint(0, 1)

if flip == 1:
    print("Heads")
else:
    print("Tails")