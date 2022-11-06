import random
from art import logo
from replit import clear
print(logo)

def num_compare(random_num, user_num):
    if user_num > random_num:
        print(" The number guessed was too high guess something lower!!!")
    elif random_num > user_num:
        print(" The number guessed was too low guess something higher!!!")
    elif random_num == user_num:
        print(" You got the right number you're truly psychic!!!")
    else:
        print(" You did not enter a valid number between 1-100 please try again")

def start_game():
    random_number = random.randint(1,100)
    print(f"This is the right answer: {random_number}")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
    if difficulty == 'hard':
        lives = 5
    elif difficulty == 'easy':
        lives = 10
    print(f"You have been given {lives} lives")
    
    
    game_on = True    
    while game_on:
        number_entered = int(input("Please enter a number between 1-100: \n"))
        num_compare(random_number, number_entered)
        if random_number == number_entered:
            print(f"You got it, the right answer was: {random_number}")
            game_on = False
        elif random_number != number_entered:
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                game_on = False
                print("\n I'm sorry You lose!")
while input("Do you want to play the Guessing Game? 'Yes' or 'No'\n").lower() == "yes":
    clear()
    start_game()
        