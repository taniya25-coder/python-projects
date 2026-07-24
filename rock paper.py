import random
choices = ("rock", "paper", "scissor")
tries=0
while True:
    comp = random.choice(choices)
    user = input("choose rock, paper, scissor: ")
    
    print(f"computer choose- {comp}")
    tries=tries+1
    if user == comp:
        print("No one is winner")
    elif (user == "rock" and comp == "paper") or (user == "paper" and comp == "scissor") or (user == "scissor" and comp == "rock"):
        print("Computer wins")
    elif (user == "paper" and comp == "rock") or (user == "scissor" and comp == "paper") or (user == "rock" and comp == "scissor"):
        print(f"You win after {tries}tries")
    else:
        print("Invalid choice")
 