from game_data import data
import random
from art import logo, vs
from replit import clear

"""Compares followers for each name and returns the name with the most followers between the options"""
def compare(name_count, name_count2):
    if name_count > name_count2:
        return name_count
    elif name_count2 > name_count:
        return name_count2
print(logo)
current_score = 0
round = True
#picks random item from list for each name option the user gets to pick
name1 = random.choice(data)
name2 = random.choice(data)
while round:
    #Shfting name B become name A for next question
    name1 = name2
    name2 = random.choice(data)

    while name1 == name2:
      name2 = random.choice(data)
    

    name_number1 = name1['follower_count']
    print(
        f"Compare A: {name1['name']}, from {name1['description']}, {name1['country']}"
    )
  
    print(vs)

    name_number2 = name2['follower_count']
    print(
        f"Compare B: {name2['name']}, from {name2['description']},{name2['country']}"
    )
  
    higher_count = compare(name_number1, name_number2)

    player_selection = input("Who has more followers? Type 'A' or 'B'\n").lower()
    
    
    clear()
    print(logo)
    if player_selection == 'a' and higher_count == name_number1:
        current_score += 1
        
        print(f"you're right! Current score: {current_score}")
    elif player_selection == 'b' and higher_count == name_number2:
        current_score += 1
        print(f"you're right! Current score: {current_score}")
    else:
        print(f"Sorry you're wrong, Final score:{current_score}!")
        round = False
