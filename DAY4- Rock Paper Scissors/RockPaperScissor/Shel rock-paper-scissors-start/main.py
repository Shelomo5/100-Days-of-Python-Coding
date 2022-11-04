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

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice > 2:
  print("you typed an invalid number,you lose!")
  
print(game_images[player_choice])

computer_choice = random.randint(0,2)
print("Computer picks:")
print(game_images[computer_choice])

if player_choice == 0:
  if computer_choice == 0:
    print("it's a draw")
  elif computer_choice == 1:
    print("computer wins")
  else:
    print("player wins")
elif player_choice == 1:
  if computer_choice == 0:
    print("computer wins")
  elif computer_choice == 1:
    print("it's a draw")
  else:
    print("computer win")
elif player_choice == 2:
  if computer_choice == 0:
    print("computer wins")
  elif computer_choice == 1:
    print("player wins")
  else:
    print("it's a draw")
else:
  print("you typed an invalid number,you lose!")
