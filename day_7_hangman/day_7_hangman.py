import random
import art
import word_list
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users

def game():
    chosen_word = random.choice(word_list.word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    print(art.logo)

    display = []
    already_guessed = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter:").lower()
        clear()
        if guess in already_guessed:
            print(f"You have already guessed {guess}, please try another letter. \n")
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

            if guess not in chosen_word:
                lives -= 1
                print(f"\n'{guess}' is not in the word, you have {lives} lives remaining.\n")
                if lives == 0:
                    print(f"You lose. The word was {chosen_word}")
                    end_of_game = True
            already_guessed.append(guess)
     

        print(f"\n{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")
        print(art.stages[lives])
        print(f"Guessed letters: {already_guessed}")
game()
while input("\nDo you want to play another game? Type 'y' or 'n': \n") == "y":
    clear()
    game()