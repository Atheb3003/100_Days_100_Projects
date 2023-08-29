#In this project, I'm going to create a loop that will continue until you enter the word "break," at which point it will end.

n = None
while n != "BREAK":
    print("Writte 'break' to end the loop")
    n = input("> ")
    n = n.upper()
    
