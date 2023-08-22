"""In this project there is a progam that simulate the throw of two dices"""

import random
one =  """
┌─────────┐
│         │
│    ●    │
│         │
└─────────┘
"""
two = """
┌─────────┐
│  ●      │
│         │
│      ●  │
└─────────┘
"""
three = """
┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘
"""
four ="""
┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘
"""
five = """
┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘
"""
six = """
┌─────────┐
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
└─────────┘
"""

dices = int(input("How many dices do you want to use? (You can only use 1 or 2): "))

opt = None

if dices == 1:
    random_dice = random.randrange(1,6)
    if random_dice == 1:
        print(one)
        print("Your number is 1")
    elif random_dice ==2:
        print(two)
        print("Your number is 2")
    elif random_dice ==3:
        print(three)
        print("Your number is 3")
    elif random_dice ==4:
        print(four)
        print("Your number is 4")
    elif random_dice ==5:
        print(five)
        print("Your number is 5")
    else:
        print(six)
        print("Your number is 6")

elif dices == 2:
    random_dice = random.randrange(2, 12)
    if random_dice == 2:
        print(one, one)
        print("Your number is 2")

    elif random_dice == 3:
        opt = random.randrange(1,4)
        if opt == 1:
            print(one, two)
        else:
            print(two, one)
        print("Your number is 3")

    elif random_dice == 4:
        opt = random.randrange(1,3)
        if opt == 1:
            print(one, three)
        elif opt == 2:
            print(two, two)
        else:
            print(three, one)
        print("Your number is 4")

    elif random_dice == 5:
        opt = random.randrange(1,4)
        if opt == 1:
            print(one, four)
        elif opt == 2:
            print(two, three)
        elif opt == 3:
            print(three, two)
        else:
            print(four, one)
        print("Your number is 5")

    elif random_dice == 6:
        opt = random.randrange(1,5)
        if opt == 1:
            print(one, five)
        elif opt == 2:
            print(two, four)
        elif opt == 3:
            print(three, three)
        elif opt == 4:
            print(four, two)
        else:
            print(five, one)
        print("Your number is 6")

    elif random_dice == 7:
        opt = random.randrange(1,6)
        if opt == 1:
            print(one, six)
        elif opt == 2:
            print(two, five)
        elif opt == 3:
            print(three, four)
        elif opt == 4:
            print(four, three)
        elif opt == 5:
            print(five, two)
        else:
            print(six, one)
        print("Your number is 7")

    elif random_dice == 8:
        opt = random.randrange(1,5)
        if opt == 1:
           print(two, six)
        elif opt == 2:
            print(three, five)
        elif opt == 3:
            print(four, four)
        elif opt == 4:
            print(five, three)
        else:
            print(six, two)
        print("Your number is 8")

    elif random_dice == 9:
        opt = random.randrange(1,4)
        if opt == 1:
            print(three, six)
        elif opt == 2:
            print(four, five)
        elif opt == 3:
            print(five, four)
        else:
            print(six, three)
        print("Your number is 9")

    elif random_dice == 10:
        opt = random.randrange(1,3)
        if opt == 1:
            print(four, six)
        elif opt == 2:
            print(five, five)
        else:
            print(six, four)
        print("Your number is 10")
    
    elif random_dice == 11:
        opt = random.randrange(1,2)
        if opt == 1:
            print(five, six)
        else:
            print(six, five)
        print("Your number is 11")
    
    else:
        print(six, six)
        print("Your number is 12")