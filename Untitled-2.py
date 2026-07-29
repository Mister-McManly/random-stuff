import random

question = input("Please ask the magic 8-ball a question! ")
answer = random.randint(1, 15)
if answer == 1:
    print("It is certain.")
elif answer == 2:
    print("Without a doubt.")
elif answer == 3:
    print("Yes, definitley.")
elif answer == 4:
    print("Most likely.")
elif answer == 5:
    print("Outlook good.")
elif answer == 6:
    print("Signs point to yes.")
elif answer == 7:
    print("Reply hazy, try again.")
elif answer == 8:
    print("Ask again later.")
elif answer == 9:
    print("Better not tell you now.")
elif answer == 10:
    print("Cannot predict now.")
elif answer == 11:
    print("Concentrate and ask again.")
elif answer == 12:
    print("Don't count on it.")
elif answer == 13:
    print("My reply is no.")
elif answer == 14:
    print("Outlook not so good.")
else:
    print("Very doubtful")

magic_8_ball = r"""
          .-----------.
       .-'             `-.
     .'                   `.
    /       .-------.       \
   /       /         \       \
  |       |           |       |
  |       |           |       |
  |       |    (O)    |       |
  |       |    (O)    |       |
  |       |           |       |
   \       \         /       /
    \       `-------'       /
     `.                   .'
       `-.             .-'
          `-----------'
"""

print(magic_8_ball)