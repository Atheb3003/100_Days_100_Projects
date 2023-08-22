"""In this project im going to make a dice. This proyect is usefull to start knowning how to use the librery called random'"""

import random


random_dice = random.randrange(1, 6)


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
elif random_dice ==6:
    print(six)
    print("Your number is 6")
