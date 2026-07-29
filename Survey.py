import time
import random
import threading

sanity = 0

name = input("What is your name? ")
if name == "APACHE-MALE-SUPER-ROMAN-GUY-NOPEY":
    sanity += 5
elif name == "SUPER-APACHE-ROMAN":
    sanity += 3
elif name == "ROMAN-GUY":
    sanity += 1
print("Alright ")
gender = input("What is your gender (e.g. apache helicopter.) ")
print("Alright ")
input("Why do you want this job? ")
print("Ok. ")
input("What is the average rainfall of the Amazon Rainforest divided by the number of grains of sand that have been walked on in the Sahara Desert? ")
if random.random() < 0.30:
    print("Hey, what is that airplane doing, WAIT ITS COMING RIGHT FOR US IT GONNA- (explosion sound) ")
    if name == "ERROR!418":
        print("I'm a teapot.")
    elif name == "ERROR!254":
        print("ERROR! COULD NOT VALIDATE SOURCE CODE.")
    elif name == "0x0000000000000000":
        print("panic(cpu 2 caller 0x0000000000000000: \"Possible memory corruption: pmap_pv_remove(...): empty hash, priors: 0\"")
    elif random.random() < 0.80:
        print("YOU DIED!")
    else:
         print("YOU... survived by instead flying the plane seat out not the plane just the plane seat... it somehow worked though. But the job died")
else:
    print("Hmmmmmmm")
    input("Are you homosexual? ")
    print("I'm sure thats true... ")
    answer = input("Can you speak demon (e.g. I̸̤̊͗̏̋̚'̸͓̦͇̝͇̯͇͌̀͐m̸̱̹͔̓́͜͠ ̴̠̘̔̎c̴̟̈́̑͋͝ǒ̸̧̨̮̯̞̰͑̊̾m̴̡̏̓͐̉̉̎̕i̸̢̡̬͓̣͑̉͘͘n̸̦͓̜̖͙̠̮̂g̶̨͉͔̒̓̂̄͝ ̷̺̙͔̹̼͍͒̒̀͊̄̉ͅf̸̘̿͂͐̔͗͆õ̸̡̟̺̳̙̦̿͛̿̍̍́r̸̳̈̒͑ ̴̲̠͍̩̒́̃͒y̷̨̠͎̩͖̤̓͐̚͜͝o̶͚̓̄̑̂̈͝.̸͇̂̀̔͒͐͠) ")
    if answer == "yes":
        sanity += 2
    input("Are you okay of having to suffer through no breaks, 120 degree weather, and nearly unlivable circumstances? ")
    print("Alright. ")
    chaos = random.randint(0,5)
    if chaos == 1:
        print("The chair becomes an elephant and stares at you looking disappointed.")
    elif chaos == 2:
        sanity += 1
        print("You fall up through the ceiling and the interview continues from where you were with different people.")
        sanity += 2
    elif chaos == 3:
        print("A stately raven flies in through the window lands on a bust and, then the bird said \"nevermore.\" ")
        sanity += 50
    elif chaos == 4:
        print("WAIT, NO NO NO NO NO!!!")
        time.sleep(5)
        print("THERE'S A... SINGLE TYPO HIDDEN IN THIS INTERVIEW SOMEWHERE!!!")
    else:
        print("The entire room turns into a big candle for a few seconds, no one but you seemed to notice.")
        sanity += 2
    input("Would you die for this job? ")
    print("Ok. ")
    input("Are you as smart as the average person? ")
    print("Hmm I'm not so sure. ")
    if random.random() < 0.50:
        print("Here take this ouija board and use it.")
        input("AWAITING QUESTION. ")
        sanity += 1

        ouija_words = [
            ("Yes", True),
            ("No", True),
            ("John", False),
            ("Isabella", False),
            ("Elias", False),
            ("Sophia", False),
            ("Jasper", False),
            ("Alyce", False),
        ]

        picked = None
        for word, needs_helicopter_check in ouija_words:
            if random.random() < 0.10 and (not needs_helicopter_check or name != "APACHE HELICOPTEr"):
                picked = word
                break

        if picked is not None:
            print(picked)
            print("Thank you for using that, now lets keep the questions going.")
            input("Have you ever swallowed demons whole? ")
            print("Alright ")
            input("If I was to give you all 12 elephants that are in my fridge do you think you could eat them all? ")
            print("OK,", name + " i'll talk to the others to see if you are suitable. ")


            start = time.time()
            stop_listening = threading.Event()

            def listen_for_enter():
                while not stop_listening.is_set():
                    input()
                    if not stop_listening.is_set():
                        print("SHUT UP!!!")

            listener = threading.Thread(target=listen_for_enter, daemon=True)
            listener.start()

            while time.time() - start < 15:
                time.sleep(0.05)

            stop_listening.set()

            while time.time() - start < 30:
                print("...")
                time.sleep(1) 

            if random.random() < 0.50:
                if gender == "APACHE HELICOPTEr":
                    print("You are denfinitly qualified for this job Mr.", name + "!")
                    print("*Hands you a rotor*")
                else:
                    if random.random() < 0.01:
                       print("We have decided,", name + " that you actualy are suitable for this job.")
                    else:
                        print("After no consideration,", name + " we have decided that you are not suitable for this job.")
            else:
                print ("H-Hey whats that airplane doing?!?!?! It's coming right for us! ")
                if random.random() < 0.7999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    print("YOU DIED!")
                else:
                    print("YOU... survived? Somehow the airplane didn't crash, but in the panic the office manager threw the papers into a fire that the owner of the company made. You might die now though because it is right near the main gas pipe...")
                    time.sleep(20)
                    print("BOOM")
        else:
            print("Goodnight")
            time.sleep(10)
            print("boo")
            time.sleep(2)
            print("YOU DIED OF SHOCK!")
    else:
        input("Have you ever swallowed demons whole? ")
        print("Alright ")
        eatsy = input("If I was to give you all 12 elephants that are in my fridge do you think you could eat them all? ")
        if eatsy == "yes":
            sanity += 1
        print("OK,", name + " i'll talk to the others to see if you are suitable. ")

        start = time.time()
        print("...")
        while time.time() - start < 30:
            input(" ")
            print("SHUT UP!")

        if random.random() < 0.50:
            if gender == "APACHE HELICOPTEr":
                print("You are denfinitly qualified for this job Mr.", name + "!")
                time.sleep(3)
                print("*Hands you a rotor*")
            else:
                if random.random() < 0.01:
                   print("We have decided,", name + " that you actualy are suitable for this job.")
                else:
                    print("After no consideration,", name + " we have decided that you are not suitable for this job.")
        else:
            print ("H-Hey whats that airplane doing?!?!?! It's coming right for us! ")
            if random.random() < 0.7999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                print("YOU DIED!")
            else:
                print("YOU... survived? Somehow the airplane didn't crash, but in the panic the office manager threw the papers into a fire that the owner of the company made. You might die now though because it is right near the main gas pipe...")
                time.sleep(20)
                print("BOOM")
print("-INSANITY LEVEL-")
time.sleep(5)
if sanity <= 0:
    print("You are a perfectly normal person... THATS BAD!!!")
elif 0 < sanity <= 5:
     print("Hmmmm only slightly? your an amatuer.")
elif 5 < sanity <= 15:
    print("Ok you're pretty good")
elif 15 < sanity <= 30:
    print("Wow you're good!")
else:
    print("You're mental instituite level!")