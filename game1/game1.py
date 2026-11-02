import random
choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3:
 player = input("rock, paper or scissors? ").lower().strip() 
 while player not in choices: 
    player = input("Please type rock, paper or scissors: ").lower().strip() 
 computer = random.choice(choices)
 print(f"You: {player} | Computer: {computer}")
 if player == computer:
  print("Draw!")
 elif beats[player] == computer:
  print("You win!")
  player_score += 1
 else:
  print("You lose!")
  computer_score += 1