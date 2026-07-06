import random, time, os
from hangman_data import HANGMAN_PICS

WORDBANK = {
  "easy": ["apple", "banana", "guitar", "pumpkin", "beach"],
  "medium": ["wizard", "jigsaw", "quartz", "blizzard", "ninja"],
  "hard": ["jazz", "sphinx", "rhythm", "fluff", "gargantuan"]
}

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def play():
  print("Select difficulty mode")
  difficulty = input("easy | medium | hard : ").lower().strip()

  if difficulty not in WORDBANK:
    print("Invalid Choice! DEFAULT MODE: EASY")
    difficulty = "easy"

  word = random.choice(WORDBANK[difficulty])
  correct_guesses = set()
  wrong_guesses = set()
  MAX_LIVES = 6
  lives = MAX_LIVES

  while lives > 0:
    time.sleep(1)
    clearScreen()

    print("🌟 HANGMAN 🌟\n")
    stage = MAX_LIVES - lives
    print(HANGMAN_PICS[stage])
    print(f"Lives: {lives}")
    print(f"Wrong Guesses: {', '.join(wrong_guesses)}\n")

    guess = input("Guess a letter: ").lower().strip()
      
    if len(guess) != 1 or not guess.isalpha():
      print("Please enter ONE letter")
      continue

    if guess in correct_guesses or guess in wrong_guesses:
      print(f"{guess} has been guessed. \nTry Again!\n")
      continue

    if guess in word:
      correct_guesses.add(guess)
      print("Correct!")
    else:
      wrong_guesses.add(guess)
      lives -= 1
      print(f"Nope, does NOT contain {guess}! \n{lives} left.")
      print(f"Correct: {', '.join(correct_guesses)}")

    all_letters_found = True
    for letter in word:
      if letter in correct_guesses:
        print(letter, end=' ')
      else:
        print('_', end=' ')
        all_letters_found = False

    print()

    if all_letters_found:
      print(f"You won with {lives} lives left!")
      return True
    
    
  print(f"You Lost \nAnswer: {word}")
  return False
      
    

def main():
  while True:
    result = play()

    again = input("\nPlay again? (y/n): ").lower().strip()
    if again != 'y':
      print("\nThanks for playing!")
      break

if __name__ == "__main__":
  main()
    