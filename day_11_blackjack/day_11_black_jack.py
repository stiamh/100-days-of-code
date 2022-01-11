import art
import random
from os import system, name, times_result

def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users

def deal_card():
    """Returns a random card from the list of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the sum of all the cards in a list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the users scores"""
    if user_score > 21 and computer_score > 21:
        return "You have busted,\nyou lose.\n"
    if user_score == computer_score:
        return "It's a draw!\n"
    elif computer_score == 0:
        return "The dealer has blackjack,\nyou lose.\n"
    elif user_score == 0:
        return "You have blackjack,\nyou win!\n"
    elif user_score > 21:
        return "You have busted,\nyou lose.\n"
    elif computer_score > 21:
        return "The dealer has busted,\nyou win!\n"
    elif user_score > computer_score:
        return f"You scored {user_score}, dealer scored {computer_score}.\nYou win!\n"
    elif user_score < computer_score:
        return f"You scored {user_score}, dealer scored {computer_score}.\nYou lose.\n"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Dealer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            go_again = input("Type 'y' if you would like to draw another card, type 'n' if you would like to pass:\n").lower()
            if go_again == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True 
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, current score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n") == "y":
    clear()
    play_game()