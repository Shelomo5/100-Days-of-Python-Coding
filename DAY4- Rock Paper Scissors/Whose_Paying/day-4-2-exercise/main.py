import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma then space. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = ((len(names))-1)
#Use len to get total numbers of items
index=random.randint(0, length)
payer = (names[index])
print(f"{payer} is going to buy the meal today!")