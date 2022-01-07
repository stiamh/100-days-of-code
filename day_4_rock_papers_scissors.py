import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock, paper, scissors]
print("Lets play rock, paper scissors!")
user_input = int(input("Please type 0 for rock, 1 for paper, or 2 for scissors.\n"))

if user_input >= 3 or user_input < 0:
    print("ERROR: You have typed an invalid number/character")
else:
    print("You have chosen: ")
    print(hand[user_input])

    computer_input = random.randint(0,2)
    print("computer has chosen: ")
    print(hand[computer_input])


    if user_input == 0 and computer_input == 2:
        print("You win!")
    elif computer_input == 0 and user_input == 2:
        print("You lose.")
    elif user_input == computer_input:
        print("It's a draw!")
    elif computer_input > user_input:
        print("You lose.")
    elif user_input > computer_input:
        print("You Win!")
    elif user_input >= 3 or user_input < 0:
        print("ERROR: You have typed an invalid number/character")