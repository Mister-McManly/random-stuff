import time


def endless_meow():
    meow = "meow"
    
    
    while True:

        print("The cat wants you to press enter...")

        cat_art = r"""
            /\_/\ 
           ( o.o )
            > ^ <
           /     \ 
          |       |
         /         \ 
        |   |   |   |
        (___)___(___)═-
"""
        print(cat_art)


        input(meow)
        
        meow += "ow"

if __name__ == "__main__":
    endless_meow()

