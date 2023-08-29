# PROJECT THAT CONSISTS OF A ROCK, PAPER, SCISSORS GAME
import random

play = str(input("Select your next play. Rock, Paper or Scissors: "))
play = play.lower()

# MAKE 2 FUNCTIONS TO AVOID REPEATING THOSE LINES SO MANY TIMES
def win(play, pc_play):
    print(" You choose: ",play,"\nThe program choose: ",pc_play,"\n win!!!")

def lose(play, pc_play):
     print("You choose: ",play,"\nThe program choose: ",pc_play,"\n You lose!!!")

if play not in ["rock", "paper", "scissors"]:
    print("ERROR! Try again")
else:
#PICKING ONE OF 3 NUMBERS (4 IS NOT INCLUDED), THAT DETERMINES THE PROGRAM'S ACTIO
    pc_play = random.randrange(1, 4)
    if pc_play == 1:
        pc_play = "rock"
    elif pc_play == 2:
        pc_play = "paper"
    else:
        pc_play = "scissors"
#THESE ARE THE CONDITIONS FOR WINNING, LOSING, OR HAVING A TIE
    if pc_play == play:
        print(" You choose: ",play,"\n The program choose: ",pc_play,"\n Is a tie!!!")
    elif play == "rock":
        if pc_play == "scissors":
            win(play, pc_play)
        elif pc_play == "paper":
            lose(play, pc_play)
    elif play == "paper":
        if pc_play == "rock":
            win(play, pc_play)
        elif pc_play == "scissors":
            lose(play, pc_play)
    else:
        if pc_play == "paper":
            win(play, pc_play)
        elif pc_play == "rock":
            lose(play, pc_play)

