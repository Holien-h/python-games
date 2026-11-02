word = "python"
guessed = []
lives = 6

while True:
 display = ""
 for letter in word:
  if letter in guessed:
   display = display + letter + " "
  else:
   display = display + "_ "
 print(display)
 print(f"You have {lives} lives left.")
 if "_" not in display:
  print("Congratulations! You guessed the word!")
  break
 lives = lives - 1
 if lives == 0:
  print("Game over! You ran out of lives.")
  break
 guess = input("Guess a letter: ").lower()
 guessed.append(guess)
 if guess in word:
  print(f"Good guess! {guess} is in the word.")
 else:
  print(f"Sorry, {guess} is not in the word. You lose a life. {lives} lives left.")