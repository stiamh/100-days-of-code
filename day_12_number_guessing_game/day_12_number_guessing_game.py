import art
import random
from os import system, name

EASY_LIVES = 10
HARD_LIVES = 5

def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users

def check_answer(guess, answer, lives):
    """Checks the users guess vs the answer and subtracts a life if they are wrong."""
    if guess > answer:
        print("Too high")
        return lives - 1
    elif guess < answer:
        print("Too low")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}") 

 

def set_difficulty():
    """Sets the difficulty for the game"""
    difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': \n").lower()
    if difficulty == "easy":
        return  EASY_LIVES
    elif difficulty == "hard":
        return HARD_LIVES

def game():
    print(art.logo)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    lives = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, answer, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
game()
while input("Do you want to play another game? Type 'y' or 'n': \n") == "y":
    clear()
    game()