import random
from replit import clear
from art import logo
print(logo)


"""function returns a random card"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_integer = random.randint(0,12)
    random_card = cards[random_integer]
    return random_card

"""Takes a list of cards as input and returns the score"""
def calculate_score(card_list):
    
    score = sum(card_list)
    #checking for 10 and 11(ace) in two cards so a total of 21
    if sum(card_list) == 21 in card_list and len(card_list) == 2:
        # 0 represents a blackjack
        return 0
    #if score over 21 change value fo ace from 11 to 1
    elif score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return score

"""Function compares user score and computer score to see who wins"""
def compare(score_user,score_computer):
    if user_score > 21 and computer_score > 21:
        return "You went over, you lose."
    elif score_user == score_computer:
        return "It's a draw!"
    elif score_computer == 0:
        return "Computer blackjack, you lose!"
    elif score_user == 0:
        return "Blackjack, you win!"
    elif score_user > 21:
        return "You busted, you lose!"
    elif score_computer > 21:
        return "Computer busted, you win :) "
    elif score_computer > score_user:
        return "You lose, computer had the better hand!"
    elif score_user > score_computer:
        return "You win, you have the higher score!"
    else:
        return "You lose!"
            
def start_game():

    print(logo)
    
    user_cards = []
    computer_cards = []
    
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    
    game_on = True
    while game_on:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards) 
        print(f"Computer's first card: {computer_cards[0]}")
        print(f"Your cards:{user_cards}, current score: {user_score}")
     
        if computer_score == 0:
            game_on = False
        elif user_score == 0:
            game_on = False
        elif user_score > 21:
            game_on = False
        else:
            draw_again = input("Would you like to draw another card? yes or no.\n")
            if draw_again.lower() == 'yes':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards) 
            else:
                game_on = False
    
        while computer_score < 17 and computer_score!= 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score,computer_score))

# Using while loop to start game
while input("Do you want to play a game of blackjack? yes or no\n").lower() == "yes":
    clear()
    start_game()  

    

                

    
    

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.      
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

