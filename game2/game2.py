import random

words = ["python", "java", "javascript", "laptop", "computer", "programming", "algorithm", "function", "variable", "loop", "php", "html", "css", "database", "software", "hardware", "network", "security", "debugging", "testing"]
word = random.choice(words)
guessed = []
lives = 6

print("Welcome to Hangman!")
while True:
 display = ""
 for letter in word:
  if letter in guessed:
   display = display + letter + " "
  else:
   display = display + "_ "
 print(display)
 print(f"Lives: {'<3 ' * lives}")
 print("Tried letters: " + (", ".join(guessed) if guessed else "None"))
 print(f"You have {lives} lives left.")
 if "_" not in display:
  print(f"You found it with {lives} lives left.")
  print("Congratulations! You guessed the word!")
  print(f"The word was: {word}")
  break
 guess = input("Guess a letter: ").lower()
 if len(guess) != 1 or not guess.isalpha():
  print("Please enter a single letter.")
  continue
 if guess in guessed: ` `
  print("You already guessed that letter.")
  continue
 guessed.append(guess)
 if guess in word:
  print(f"Good guess! {guess} is in the word.")
 else:
  lives = lives - 1
  print(f"Sorry, {guess} is not in the word. You lose a life. {lives} lives left.")
  if lives == 0:
   print("Game over! You ran out of lives.")
   print(f"The word was: {word}")
   break