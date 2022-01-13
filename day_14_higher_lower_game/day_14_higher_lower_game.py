import art
from game_data import data
from os import system, name
import random

def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users

def get_account():
    """Pulls an account from game_data"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def compare_followers(account_a, account_b):
    """Compares the two options and returns the one with the higher follower count"""
    if account_a['follower_count'] > account_b['follower_count']:
        return account_a
    else:
        return account_b

def check_answer(guess, account_a_followers, account_b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if account_a_followers > account_b_followers:
        return guess == "a"
    else:
        return guess == "b"

def assign_guess(guess, account_a, account_b):
    if guess == 'a':
        return account_a
    else:
        return account_b

def game():
    print(art.logo)
    print("Welcome to higher or lower, guess which of the celebrities below have more instagram followers!")
    streak = 0
    game_over = False
    account_a = get_account()
    account_b = get_account()
    while not game_over:
        account_a = account_b
        account_b = get_account()

        while account_a == account_b:
            account_b = get_account()
        
        print(f"Celebrity A: {format_data(account_a)}")
        print(art.vs)
        print(f"Celebrity B: {format_data(account_b)}")
        guess = input("Who has more instagram followers? Type 'A' or 'B'\n").lower()
        account_a_followers = account_a["follower_count"]
        account_b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, account_a_followers, account_b_followers)
        clear()
        print(art.logo)
        if is_correct:
            streak += 1
            print(f"You're right! Current score: {streak}.")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {streak}")
game()
while input("Do you want to play again? Type 'y' or 'n': \n") == "y":
    clear()
    game()