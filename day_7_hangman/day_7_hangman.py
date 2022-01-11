import random
import art
import word_list
from os import system, name
chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users

print(art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
already_guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    clear()
    if guess in already_guessed:
        print(f"You have already guessed {guess}, please try another letter. \n")
        print(art.stages[lives])
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"\n'{guess}' is not in the word, you have {lives} lives remaining.\n")
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"\n{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        already_guessed.append(guess)
        print(art.stages[lives])
        print(f"Guessed letters: {already_guessed}")