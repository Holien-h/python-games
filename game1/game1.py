import random
choices = ["rock", "paper", "scissors"]
player = input("rock, paper or scissors? ") # NEW
computer = random.choice(choices)
print(f"You chose: {player}") # NEW
print(f"The computer chose: {computer}")
print(f"You: {player} | Computer: {computer}")
if player == computer: # NEW
 print("Draw!") # NEW
elif beats[player] == computer: # NEW
 print("You win!") # NEW
else: # NEW
 print("You lose!") # NEW