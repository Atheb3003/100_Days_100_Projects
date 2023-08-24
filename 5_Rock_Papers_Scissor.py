#IN THIS PROJECT IM GOING TO MAKE A SIMPLE GAME OF ROCK, PAPERS, SCISSORS.\
import random

play = str(input("What do you choose? Rock, Paper or Scissor: "))

if play not in "rockRockROCKpaperPaperPAPERscissorScissorSCISSOR" or len(play) < 4:
    print("ERROR, TRY AGAIN")
else:
    if play in "rockRockROCK":
        play = "rock"
    elif play in "paperPaperPAPER":
        play = "paper"
    elif play in "scissorScissorSCISSOR":
        play = "scissor"
    random_play = random.randrange(1,3)
    if random_play == 1:
        pc_play = "rock"
        print("Program choose: {}".format(pc_play))
        if pc_play == play:
            print("IT IS A TIE")
        elif play == "scissor":
            print("YOU LOOSE")
        else:
            print("YOU WIN")
    elif random_play == 2:
        pc_play = "paper"
        print("Program choose: {}".format(pc_play))
        if pc_play == play:
            print("IT IS A TIE")
        elif play == "rock":
            print("YOU LOOSE")
        else:
            print("YOU WIN")
    else:
        pc_play = "scissor"
        print("Program choose: {}".format(pc_play))
        if pc_play == play:
            print("IT IS A TIE")
        elif play == "paper":
            print("YOU LOOSE")
        else:
            print("YOU WIN")
        
