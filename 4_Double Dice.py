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
first_dice = None
second_dice = None

if dices >= 1:
    random_dice = random.randrange(1,6)
    if random_dice == 1:
        print(one)
        first_dice = 1
    elif random_dice ==2:
        print(two)
        first_dice = 2
    elif random_dice ==3:
        print(three)
        first_dice = 3
    elif random_dice ==4:
        print(four)
        first_dice = 4
    elif random_dice ==5:
        print(five)
        first_dice = 5
    elif random_dice == 6:
        print(six)
        first_dice = 6
    if dices == 1:
        result = first_dice
        print("The result is {}".format(result))

if dices == 2:
    random_dice_2 = random.randrange(1,6)
    if random_dice_2 == 1:
        print(one)
        second_dice = 1
    elif random_dice_2 ==2:
        print(two)
        second_dice = 2
    elif random_dice_2 ==3:
        print(three)
        second_dice = 3
    elif random_dice_2 ==4:
        print(four)
        second_dice = 4
    elif random_dice_2 ==5:
        print(five)
        second_dice = 5
    elif random_dice_2 == 6:
        print(six)
        second_dice = 6
    result = first_dice + second_dice
    print("The result is {}".format(result))

