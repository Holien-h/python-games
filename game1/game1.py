import random
choices = ["rock", "paper", "scissors", "lizard", "spock"]
beats = {"rock": ["scissors", "lizard"], "paper": ["rock", "spock"], "scissors": ["paper", "lizard"], "lizard": ["spock", "paper"], "spock": ["scissors", "rock"]}
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
 elif computer in beats[player]:
  print("You win this round!")
  player_score += 1
 else:
  print("You lose this round!")
  computer_score += 1
if player_score == 3:
 print("Congratulations! You won the game!")
elif computer_score == 3:
 print("Sorry! The computer won the game!")