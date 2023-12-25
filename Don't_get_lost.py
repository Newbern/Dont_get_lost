import os
from time import sleep

# Settings

level = 2
phone = False
tow = False
# Quick Clear and Wrong
cls = lambda: os.system('cls')


def wrong():
    print("Please press [1] or [2]...")
    sleep(2)
    cls()


# Main Menu
while True:
    print("Dont get lost...")
    print("[1]Continue?\n[2]New Game?")
    cho = int(input(">>>"))

    # Continue
    if cho == 1:
        print('Opening level...')
        # sleep(2)
        break

    # NEW GAME
    elif cho == 2:
        print('Making Game...')
        sleep(2)
        level = 0
        break
    # WRONG
    else:
        wrong()

# LEVEL SELECT
while True:
    # QUICK CLEAR
    cls()

    # END GAME
    if level == -1:
        break

    # START
    if level == 0:

        # START
        def Start():
            # -CHECK TIRE
            # -ASK TO USE PHONE
            print("Your driving down the road and your car stops...")
            print("Your in the middle of nowhere...")
            print("What do you do?:")
            print('[1]Check your tires?\n[2]pull your phone out?')
            cho = int(input(">>>"))
            cls()

            if cho == 1:
                level, phone = C1()
                return level, phone
            elif cho == 2:
                level, phone = C2()
                return level, phone
            else:
                wrong()
                Start()


        # C1
        def C1():
            # TIRES AERE SHREDED
            # -ASK TO USE PHONE
            # -GRAB TOOLS
            print("You step outside to check your tires...")
            print("There shreded...")
            print("What do you do?:")
            print('[1]call a tow?\n[2]grab you spare tools?')
            Cho1 = int(input(">>>"))
            cls()

            if Cho1 == 1:
                level, phone = C1a()
                return level, phone
            elif Cho1 == 2:
                level, phone = C1b()
                return level, phone
            else:
                wrong()
                C1()


        # HERE C1a
        def C1a():
            # ENTERING NEXT LEVEL
            ## NO PHONE
            ## UNDAMAGE CAR
            print("You call the tow...")
            print("There on there way... but your phone dies.")
            print("You hear something in the woods...")
            print('What do you do?:')
            print("[1]wait for the tow?\n[2]go check it out?")
            Cho1a = int(input(">>>"))
            cls()

            if Cho1a == 1:
                level, phone = Level_1()
                phone = False
                return level, phone
            elif Cho1a == 2:
                level, phone = Level_2()
                phone = False
                return level, phone
            else:
                wrong()
                C1a()


        # HERE C1b
        def C1b():
            # GRABBING TOOLS
            ## DAMAGED CAR
            ## YES PHONE
            print("You grab your spare tools and get to work...")
            print("Your tires are worse...")
            print("You broke the trunk door from slamming it...")
            print("You hear something in the woods...")
            print("What do you do?:")
            print("[1]take a break in the car?\n[2]go check it out?")
            Cho1b = int(input(">>>"))
            cls()

            if Cho1b == 1:
                level, phone = Level_1()
                phone = True
                return level, phone
            elif Cho1b == 2:
                level, phone = Level_2()
                phone = True
                return level, phone
            else:
                wrong()
                C1b()


        # HERE C2
        def C2():
            # ASK TO USE PHONE
            print("Your phone is almost dead you can only call one person...")
            print("what do you do?:")
            print("[1]call a tow?\n[2]save phone for later?")
            Cho2 = int(input(">>>"))
            cls()

            if Cho2 == 1:
                level, phone = C2a()
                return level, phone
            elif Cho2 == 2:
                level, phone = C2b()
                return level, phone
            else:
                wrong()
                C2()


        # HERE C2a
        def C2a():
            # CALLED TOW
            ## NO PHONE
            ## UNDAMAGED CAR
            print("You call the tow...")
            print("There on there way... but your phone dies.")
            print("You hear something in the woods...")
            print('What do you do?:')
            print("[1]wait for the tow?\n[2]go check it out?")
            Cho2a = int(input(">>>"))
            cls()

            if Cho2a == 1:
                level, phone = Level_1()
                phone = False
                return level, phone
            elif Cho2a == 2:
                level, phone = Level_2()
                phone = False
                return level, phone
            else:
                wrong()
                C2a()


        # HERE C2b
        def C2b():
            ## YES PHONE
            print("You power off your phone and put it up...")
            print("you hear something in the woods...")
            print("What do you do?:")
            print("[1]rest in the car?\n[2]go check it out?")
            Cho2b = int(input(">>>"))
            cls()

            if Cho2b == 1:
                level, phone = Level_1()
                phone = True
                return level, phone
            elif Cho2b == 2:
                level, phone = Level_2()
                phone = True
                return level, phone
            else:
                wrong()
                C2b()


        def Level_1():
            level = 1
            return level, phone


        def Level_2():
            level = 2
            return level, phone


        level, phone = Start()
        if phone == False:
            tow = True

    # Stay at Your car
    if level == 1:
        def Start():
            print("Your in your car")
            print("1 hour pass...")
            print("You hear scracthing against the car...")
            print("What do you do?:")
            print('[1]scream!\n[2]hide')

            cho = int(input(">>>"))
            cls()

            if cho == 1:
                level = C1()
                return level
            elif cho == 2:
                level = C2()
                return level
            else:
                wrong()
                Start()


        def C1():
            print("The car begins to shake very violently...")
            print("The roof of the car is ripped off...")
            print("You act quick before getting a look...")
            print("What do you do?:")
            print("[1]jump out of the car!?\n[2]play dead!?")
            cho1 = int(input(">>>"))
            cls()
            if cho1 == 1:
                level = C1a()
                return level
            elif cho1 == 2:
                level = C1b()
                return level
            else:
                wrong()
                C1()


        # runing
        def C1a():
            print("Your running...")
            print("You hear the best behind you...")
            print("You have a short amount of time before it catchs up to you...")
            print("What do you do:?")
            print("[1]hide in the log?\n[2]keep running?")
            cho1a = int(input(">>>"))
            cls()

            if cho1a == 1:
                level = C1a1()
                return level

            elif cho1a == 2:
                level = C1a2()
                return level
            else:
                wrong()
                C1a()


        def C1a1():
            print("You hide into the log...")
            print("The beast hits the log across to another tree...")
            print("The beast yells and runs in the distance...")
            print("You lost the beast...")
            print("What do you do?:")
            print("[1]head back to the car?")
            if phone == True:
                print("[2]call the cops")
            else:
                print("...")
            cho1a1 = int(input(">>>"))
            cls()

            # calling cop
            if phone == True:
                if cho1a1 == 2:
                    level = C1a12()
                    return level
            if cho1a1 == 1:
                level = C1a11()
                return level
            else:
                wrong()
                C1a1()


        def C1a11():
            if tow == True:
                print("Your back to the car...")
                print("You see the tow!")
                print("You see he has your car and is heading back")
                print("Your car is gone...")
                print("Your all alone with the beast...")
                print("To be continued...")
                print('[1]Play again?\n[2]Nope!')
                cho = int(input(">>>"))
                cls()

                if cho == 1:
                    Start()
                elif cho == 2:
                    level = -1
                    return level
                else:
                    wrong()
                    C1a11()
            else:
                print("Your back to your car you get in the car...")
                print("Your scared...")
                print("The beast is a few feet away...")
                print("What do you do?:")
                print("[1]except death?")
                if phone == True:
                    print('[2]call unknown number?')
                cho1a1 = int(input(">>>"))
                cls()

                if cho1a1 == 1:
                    print("You yell at the beast")
                    print("The beast tears you limb from limb...")
                    print("The beast bites your head clean off...")
                    print("with multiple stabs through the chest...")
                    print("Your Dead")
                    print('[1]Try again\n[2]Nah Bro im dead')
                    cho = int(input(">>>"))
                    cls()

                    if cho == 1:
                        Start()
                    elif cho == 2:
                        level = -1
                        return level
                    else:
                        wrong()
                        C1a1()

                if phone == True:
                    if cho1a1 == 2:
                        print("You call the number...")
                        print("the mysterious caller says:")
                        print('"Dont move we have it in our sites"')
                        print("A team of speical forces come in and kill the beast")
                        print("You are part of a special team forces set to kill monsters")
                        print("You are set on a airplane ready for your next monster hunt...")
                        print("To be continued...")
                        input()
                else:
                    if cho1a1 == 2:
                        wrong()
                        C1a1()


        def C1a12():
            print("You call the cops there on there way...")
            print("You hear the sirens in the distance...")
            print("You arive at your car the beast is shot down...")
            print("You ride back with the cops and they take you home...")
            print("You rest in bed...")
            print("You hear something at the door...")
            print("To be continued...")
            print("Your Dead")
            print('[1]Play again?\n[2]Nope!')
            cho = int(input(">>>"))
            cls()

            if cho == 1:
                Start()
            elif cho == 2:
                level = -1
                return level
            else:
                wrong()
                C1a12()


        def C1a2():
            print("You keep running...")
            print("The beast is much closer now...")
            print("It stabs you in the arm...")
            print("Your back at your car...")

            if tow == True:
                print("You see the tow man with you car...")
                print("You jump in the tow...")
                print("The beast kills the tow man...")
                print("You run into the beast with the car...")
                print("You kill the beast as it stabs into your head")
                print("Your Dead")
                print('[1]Try again\n[2]Nah Bro im dead')
                cho = int(input(">>>"))
                cls()

                if cho == 1:
                    Start()
                elif cho == 2:
                    level = -1
                    return level
                else:
                    wrong()
                    C1a2()

            else:
                print("It stabs you in the neck...")
                print("It tares you in to and bites your head off...")
                print("Your Dead")
                print('[1]Try again\n[2]Nah Bro im dead')
                cho = int(input(">>>"))
                cls()

                if cho == 1:
                    Start()
                elif cho == 2:
                    level = -1
                    return level
                else:
                    wrong()
                    C1a2()


        # hiding
        def C1b():
            print("The beast like monster stabs you in the gut...")
            print("The beast bites your head off...")
            print("Your Dead")
            print('[1]Try again\n[2]Nah Bro im dead')
            cho1b = int(input(">>>"))
            cls()
            if cho1b == 1:
                Start()
            elif cho1b == 2:
                level = -1
                return level
            else:
                wrong()
                C1b()


        def C2():
            print("The beast walks on top of the car...")
            print("The weight of the beast slowly crushes the car...")
            print("It lays down on the car...")
            print("It fell asleep on the car...")
            print("What do you do?:")
            print("[1]stay?\n[2]go out the back window?")
            cho2 = int(input(">>>"))
            cls()

            if cho2 == 1:
                C2a()
            elif cho2 == 2:
                C2b()
            else:
                wrong()
                C2()


        def C2a():
            print("You stay under neath the beast...")
            print("It crushs you alive...")
            print("as the beast hears your screams...")
            print("it begains to jump very violently on the car...")
            print("Your Dead")
            print('[1]Try again\n[2]Nah Bro im dead')
            cho = int(input(">>>"))
            cls()

            if cho == 1:
                Start()
            elif cho == 2:
                level = -1
                return level
            else:
                wrong()
                C2a()


        def C2b():
            print("You crawl out the back window...")
            print("You cut your self aginst the glass...")
            print("The beast smells you...")
            print("What do you do?:")
            print("[1]Run!\n[2]pick up broken glass?!")
            cho2b = int(input(">>>"))
            cls()

            if cho2b == 1:
                C1a()
            elif cho2b == 2:
                C2b1()
            else:
                wrong()
                C2b()


        def C2b1():
            print("You pick up the broken glass...")
            print("The beast charges at you...")
            print("You stab at it but...")
            print("Your glass crubless...")
            print("It had no effect...")
            print("The beast grabs your limbs and tears you apart...")
            print("Your Dead")
            print('[1]Try again\n[2]Nah Bro im dead')
            cho = int(input(">>>"))
            cls()

            if cho == 1:
                Start()
            elif cho == 2:
                level = -1
                return level
            else:
                wrong()
                C2b1()


        level = Start()

    # Go into the woods
    if level == 2:

        # Start
        def Start():
            print("You set out to see whats makeing that sound in the woods...")
            print("You hear bones cracking...")
            print("You see a huge beast eating on a deer...")
            print("What do you do?:")
            print("[1]yell at it?\n[2]slowly back up?")
            cho = int(input(">>>"))
            cls()

            if cho == 1:
                C1()
            elif cho == 2:
                C2()


        def C1():
            print("You yell at the beast...")
            print("It grows angry...")
            print("It jumps on top of you violently jumping...")
            print("It grabs your flesh and pulls your limps off...")
            print("eats on your bones...")
            print("Your Dead")
            print('[1]Try again\n[2]Nah Bro im dead')
            cho1b = int(input(">>>"))
            cls()
            if cho1b == 1:
                Start()
            elif cho1b == 2:
                level = -1
                return level
            else:
                wrong()
                C1()


        def C2():
            print("The beast sees you...")
            print("You run as the beast follows behind...")
            print("You find an abandon house...")
            print("You lock the door before it can enter...")
            print("Its dark in here...")
            print("What do you do?:")
            print("[1]walk in the dark?")

            if phone == True:
                print("[2]use phone flashlight?")
            else:
                print("...")

            cho2 = int(input(">>>"))
            cls()

            if cho2 == 1:
                C2a()
            if phone == True:
                if cho2 == 2:
                    C2b()
            else:
                wrong()
                C2()


        def C2a():
            print("You keep searching...")
            print("You eventually a room...")
            print("You cut the lights on...")
            print("You find a shot gun...")
            print("What do you do?:")
            print("[1]Go find the beast?\n[2]shoot yourself?")
            cho2a = int(input(">>>"))
            cls()

            if cho2a == 1:
                C2a1()
            elif cho2a == 2:
                C2a2()
            else:
                wrong()
                C2a()


        def C2a1():
            print("You step out side and you yell for the beast...")
            print("It finds you and come charging you aim your barrel..")
            print("You fire multiple shots...")
            print("The beast lays on the ground hurt...")
            print("Do you kill the beast?")
            print("[1]Yes\n[2]No")
            cho2a1 = int(input(">>>"))
            cls()

            if cho2a1 == 1:
                print("The beast is dead...")
                print("You find your way back to the road...")
                print("You see someone driving you wave them down...")
                print("They carry you back into town...")
                print("but something feels of...")
                print("You start to transform into..")
                print("The beast...")
                print("To be Continued")
                print("[1]Try again?\n[2]Nah i quit")
                cho = int(input(">>>"))
                cls()

                if cho == 1:
                    Start()
                elif cho == 2:
                    level = -1
                    return level
                else:
                    wrong()
                    C2a1()

            elif cho2a1 == 2:
                print("You let the beast live...")
                print("You return to the car...")
                if tow == True:
                    print("The tow is there ready to pick you up...")
                    print("You make it to a hospital to get checked out...")
                    print("They say your fine so you go home...")
                    print("As your rest you cant help but think of the beast...")
                    print("You set out to go kill more beast like it...")
                    print("You join a secreat black ops team disigned to kill creatures like the one you faced...")
                    print("To be Continued...")
                    print("[1]Play again?\n[2]Quit game?")
                    cho = int(input(">>>"))
                    cls()

                    if cho == 1:
                        Start()
                    elif cho == 2:
                        level = -1
                        return level
                    else:
                        wrong()
                        C2a1()

                else:
                    print("You rest...")
                    print("3 days later a couple come driving home from vacation trip...")
                    print("You flag them down and they let you hitch a ride back into town...")
                    print("They drop you off near a hospital but u just go right past into the hunting store...")
                    print("You buy gear and set out to kill more beast alike...")
                    print("You go solo into the dark woods...")
                    print("but right behind you carry the beast follows you beind becomeing your slave...")
                    print("To be Continued...")
                    print("[1]Play again?\n[2]Quit game?")
                    cho = int(input(">>>"))
                    cls()

                    if cho == 1:
                        Start()
                    elif cho == 2:
                        level = -1
                        return level
                    else:
                        wrong()
                        C2a1()


        def C2a2():
            print("You put the shotgun in your mouth you pull the trigger...")
            print("*boom*")
            print("Your dead...")
            print("[1]Restart\n[2]Quit")
            cho = int(input(">>>"))
            cls()
            if cho == 1:
                Start()
            elif cho == 2:
                level = -1
            else:
                C2a2()


        def C2b():
            print("You pull your phone out...")
            print("You see some document on the table...")
            print("You see details explaining the existance of this beast...")
            print("There are more than one beast...")
            print("They spread by turning the victiems into the same beast...")
            print("You see car keys on the table")
            print("What do you do?:")
            print("[1]leave table?\n[2]pick up the keys")
            cho2b = int(input(">>>"))
            cls()

            if cho2b == 1:
                C2ba()
            elif cho2b == 2:
                C2bb()
            else:
                C2b()


        def C2ba():
            print("A man grabs you from behind...")
            print("He stabs you twice in the gut...")
            print("You brake his grip and break your phone...")
            print("Its dark...")
            print("he grabs his axe and splits your skull in half...")
            print("Your Dead")
            print("[1]Restart\n[2]Nah bro he killed me")
            cho = int(input(">>>"))
            cls()
            if cho == 1:
                Start()
            elif cho == 2:
                level = -1
            else:
                C2ba()


        def C2bb():
            print("You grab the keys...")
            print("You get in the car outside...")
            print("as soon as it starts the beast comes running...")
            print("You drift the car and miss the beast...")
            print("You find the road and keep driving...")
            print("Your finnaly out of the horor...")
            print("You share your experience with the cops...")
            print("The throw you in a mental hosptial and lock you up...")
            print("You live scared the beast siteings are getting closer and closer...")
            print("You can do nothing...")
            print("[1]Play again?\n[2]Nope")
            cho = int(input(">>>"))
            cls()

            if cho == 1:
                Start()
            elif cho == 2:
                level = -1
            else:
                C2bb()


        Start()














