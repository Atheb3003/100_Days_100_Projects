#In this project, there is a program that simulates the roll of two dice.
#MODELS OF EACH NUMBER ON THE DICE
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
#FUNTION THAT ROLLS THE DICE
def roll_dice(random_dice):
    if random_dice == 1:
        print(one)
        return 1
    elif random_dice == 2:
        print(two)
        return 2
    elif random_dice == 3:
        print(three)
        return 3
    elif random_dice == 4:
        print(four)
        return 4
    elif random_dice == 5:
        print(five)
        return 5
    elif random_dice == 6:
        print(six)
        return 6
    
dices = int(input("How many dices do you want to use? (You can only use 1 or 2): "))

if dices == 1:
    random_dice_1 = random.randrange(1,7)
    roll_dice(random_dice_1)
    print("Your resoult is: ", random_dice_1)
if dices == 2:
    random_dice_1 = random.randrange(1, 7)
    random_dice_2 = random.randrange(1, 7)
    roll_dice(random_dice_1)
    roll_dice(random_dice_2)
    result = random_dice_1 + random_dice_2
    print("Your resoult is: ", result)
    


