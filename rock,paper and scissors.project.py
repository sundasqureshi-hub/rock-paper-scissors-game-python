import random
options= ("rock" ,"paper", "scissors")

player = input("enter a choice (rock ,paper, scissors: )")
while player not in options:
    print ("invalid choice,please try again")
computer =random.choice(options)

print (f"player:{player}")
print(f"computer:{computer}")
if player == computer:
    print("it's a Tie!")
elif player == "rock" and computer == "scissors":
    print("rock smashes scissors, you win!")
elif player == "paper" and computer == "scissors":
    print("scissors cut papers!,you loss!")
elif player == "scissors" and computer == "rock":
    print("rock smashes scissors,you loss!")
elif player == "rock" and computer == "paper":
    print("papers cover rock,you loss!")
elif player == "paper" and computer == "rock":
    print("paper covers rock,you win")














