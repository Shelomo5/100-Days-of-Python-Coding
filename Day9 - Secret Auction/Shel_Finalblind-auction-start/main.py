from replit import clear
from art import logo
print(logo)
#Function finds max value in dictionary
def max_bidder(betting_dict):
    #{name: value}
    max_value = 0
    name_key =''
    #iterating through each key value (name) in dictionary
    for better_name in betting_dict:
        #storing value of dict in variable for a given key
        bid_value = betting_dict[better_name]
        #comparing max_value to values iterated to find highest value
        if bid_value > max_value:
            max_value = bid_value
            #key which is the name of highest value is the winner
            name_key = better_name
    print(f"The winner is {name_key} with a bid of {max_value}!")

print("Welcome to the secret auction program.")
bet_dict = {}
bidding = True
#while loop to keep bidding going until all values have been put in dictionary
while bidding:
    name = input("What is your name?\n ")
    bid_amount = int(input("What is your bid?\n $"))
    #bid_amount is stored in bet_dict dictionary where the name is the key
    bet_dict[name] = bid_amount
    
    more_betting = input("Are there any other bidders? yes or no\n")
    if more_betting.lower() == 'yes':
        bidding = True
        clear()
    elif more_betting.lower() == 'no':
        bidding = False
print(bet_dict)

#calling function        
max_bidder(bet_dict)      

        
    
    