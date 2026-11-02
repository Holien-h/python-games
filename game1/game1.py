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
  print(f"Draw! Player {player_score}-Computer {computer_score}")
 elif computer in beats[player]:
  print(f"You win this round! Player {player_score}-Computer {computer_score}")
  player_score += 1
 else:
  print(f"You lose this round! Player {player_score}-Computer {computer_score}")
  computer_score += 1
if player_score == 3:
 print(f"Congratulations! You won the game! Player score: {player_score} | Computer score: {computer_score}")
elif computer_score == 3:
 print(f"Sorry! The computer won the game! Player score: {player_score} | Computer score: {computer_score}")