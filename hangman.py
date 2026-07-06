import random, time, os

WORDBANK = ["dog", 'blink', 'taco', 'buffalo', 'beef', 'zebra', 'flower','computer', 'pillow']

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def main():
  word = random.choice(WORDBANK)
  guessed_letters = []
  lives = 6

  while lives > 0:
    time.sleep(3)
    clearScreen()

    print("🌟 HANGMAN 🌟\n")

    guess = input("Guess a letter: ").lower().strip()
    
    if guess in guessed_letters:
      print(f"{guess} has been guessed. \nTry Again!\n")
      continue

    guessed_letters.append(guess)

    if guess in word:
      print("Correct!")
    else:
      lives -= 1
      print(f"Nope, {guess} not in there! \n{lives} left.")

    print()

    all_letters_found = True
    for letter in word:
      if letter in guessed_letters:
        print(letter, end='')
      else:
        print('_', end='')
        all_letters_found = False

    print()

    if all_letters_found:
      print(f"You won with {lives} lives left!")
      exit()

  print(f"You Lost \nAnswer: {word}")
    
if __name__ == "__main__":
  main()
  