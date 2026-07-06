# Hangman Game

![Hangman Demo](demo.gif)

A simple command-line Hangman game built with Python as part of my coding practice. The game randomly chooses a word from a list of words, based on the player's difficulty selection. The player guesses the secret word one letter at a time until the player either correctly guesses the word or the "hangman" figure is completed.

## About This Project
I built this project while working through the Replit 100 Days of Code challenge. After completing the challenge, I continued improving it by refactoring the code, organizing it into functions, and adding new features to strengthen my Python skills.

## Features
- ASCII hangman drawing
- Difficulty levels: Easy, Medium, Hard
- Random word select
- Input validation
- Shows wrong guesses
- Tracks correct letters
- Displays remaining lives
- Play again option
- Organized into multiple files for cleaner code

## What I Learned
This project helped me practice:
- Functions
- Loops and conditionals
- Sets for tracking guesses
- User input validation
- Separating code into multiple Python files
- refactoring existing code to make it cleaner and easier to maintain

## How to run
1. Make sure Python 3 is installed
2. Open a terminal in the project folder
3. Run:

```bash
python main.py
```

## Future Improvements
Some ideas I would like to add in future updates:
- Categories (Food, Countries, Animals, etc.)
- Load words from a text file
- Hint
- Score tracking
- High score saving
- Improve terminal interface

## Technologies Used:
- Python 3
- Standard Library (random, time, os)

## Project Structure

```text
hangman/
|---main.py
|---hangman_data.py
|---README.md
```
